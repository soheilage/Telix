locals {
  bucket_name = coalesce(var.bucket_name, var.project_id)
  data_dir    = "${path.module}/../data"

  # Mirrors the three folders the Qwiklabs startup script creates, populated with
  # synthetic Telix clinical / medical-affairs sample data (see data/README.md).
  folders = {
    "gemini-enterprise-drive"         = ["CLINICAL_TRIAL_SITES.csv", "MEDICAL_INFO_ENQUIRIES.csv", "investigator_feedback.csv", "pie_chart_enquiry_categories.png"]
    "notebooklm-drive"                = ["CLINICAL_TRIAL_SITES.txt", "MEDICAL_INFO_ENQUIRIES.txt", "investigator_feedback.txt"]
    "gemini-enterprise-cloud-storage" = ["CLINICAL_TRIAL_SITES.txt", "MEDICAL_INFO_ENQUIRIES.txt", "investigator_feedback.txt"]
  }

  objects = merge([
    for folder, files in local.folders : {
      for f in files : "${folder}/${f}" => f
    }
  ]...)

  content_types = {
    csv = "text/csv"
    txt = "text/plain"
    png = "image/png"
  }
}

data "google_project" "project" {
  project_id = var.project_id
}

# -----------------------------------------------------------------------------
# 0. One-time access preflight (admin is expected to have granted access already)
# -----------------------------------------------------------------------------
resource "terraform_data" "preflight" {
  count = var.run_preflight ? 1 : 0

  provisioner "local-exec" {
    command     = "${path.module}/../scripts/preflight.sh"
    environment = { PROJECT_ID = var.project_id }
  }
}

# -----------------------------------------------------------------------------
# 1. Required APIs (no-op if the admin already enabled them)
# -----------------------------------------------------------------------------
resource "google_project_service" "apis" {
  for_each = toset([
    "discoveryengine.googleapis.com",
    "storage.googleapis.com",
    "drive.googleapis.com",
    "calendar-json.googleapis.com",
  ])

  project            = var.project_id
  service            = each.key
  disable_on_destroy = false

  depends_on = [terraform_data.preflight]
}

# -----------------------------------------------------------------------------
# 2. Sample data bucket + the three lab folders
# -----------------------------------------------------------------------------
resource "google_storage_bucket" "data" {
  name                        = local.bucket_name
  project                     = var.project_id
  location                    = var.bucket_location
  uniform_bucket_level_access = true
  force_destroy               = true

  depends_on = [google_project_service.apis]
}

resource "google_storage_bucket_object" "files" {
  for_each = local.objects

  bucket       = google_storage_bucket.data.name
  name         = each.key
  source       = "${local.data_dir}/${each.value}"
  content_type = lookup(local.content_types, element(split(".", each.value), length(split(".", each.value)) - 1), "application/octet-stream")
}

# Discovery Engine service agent must be able to read the bucket for import.
resource "google_storage_bucket_iam_member" "discoveryengine_reader" {
  bucket = google_storage_bucket.data.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:service-${data.google_project.project.number}@gcp-sa-discoveryengine.iam.gserviceaccount.com"
}

# Participants can browse the bucket in Task 1.
resource "google_storage_bucket_iam_member" "participants_reader" {
  for_each = toset(var.participants)

  bucket = google_storage_bucket.data.name
  role   = "roles/storage.objectViewer"
  member = each.key
}

# -----------------------------------------------------------------------------
# 3. Pre-connected Cloud Storage data store (cloud-storage-ds)
# -----------------------------------------------------------------------------
resource "google_discovery_engine_data_store" "cloud_storage" {
  project                     = var.project_id
  location                    = var.location
  data_store_id               = var.data_store_id
  display_name                = "Cloud Storage"
  industry_vertical           = "GENERIC"
  content_config              = "CONTENT_REQUIRED"
  solution_types              = ["SOLUTION_TYPE_SEARCH"]
  create_advanced_site_search = false

  depends_on = [google_project_service.apis]
}

# Import the clinical / medical-affairs text files. The provider has no import
# resource yet, so call the Discovery Engine API once.
resource "terraform_data" "import_documents" {
  triggers_replace = [
    google_discovery_engine_data_store.cloud_storage.name,
    join(",", sort([for k, _ in local.objects : k if startswith(k, "gemini-enterprise-cloud-storage/")])),
  ]

  provisioner "local-exec" {
    command = "${path.module}/../scripts/import-gcs-documents.sh"
    environment = {
      PROJECT_ID    = var.project_id
      LOCATION      = var.location
      DATA_STORE_ID = google_discovery_engine_data_store.cloud_storage.data_store_id
      GCS_URI       = "gs://${google_storage_bucket.data.name}/gemini-enterprise-cloud-storage/*"
    }
  }

  depends_on = [
    google_storage_bucket_object.files,
    google_storage_bucket_iam_member.discoveryengine_reader,
  ]
}

# -----------------------------------------------------------------------------
# 4. Gemini Enterprise application (Agentspace / APP_TYPE_INTRANET)
# -----------------------------------------------------------------------------
resource "google_discovery_engine_search_engine" "app" {
  project           = var.project_id
  engine_id         = var.app_id
  collection_id     = "default_collection"
  location          = google_discovery_engine_data_store.cloud_storage.location
  display_name      = var.app_display_name
  industry_vertical = "GENERIC"
  app_type          = "APP_TYPE_INTRANET"
  data_store_ids    = [google_discovery_engine_data_store.cloud_storage.data_store_id]

  common_config {
    company_name = var.company_name
  }

  search_engine_config {
    search_tier                = "SEARCH_TIER_ENTERPRISE"
    required_subscription_tier = "SUBSCRIPTION_TIER_ENTERPRISE"
    search_add_ons             = ["SEARCH_ADD_ON_LLM"]
  }

  # Agentic features used in Tasks 3-5 (custom agents, sharing).
  features = {
    "agent-sharing-without-admin-approval" = "FEATURE_STATE_ON"
    "disable-agent-sharing"                = "FEATURE_STATE_OFF"
    "enable-end-user-sharing-with-groups"  = "FEATURE_STATE_ON"
  }
}

# -----------------------------------------------------------------------------
# 5. Participant access (one shared project, one shared app)
# -----------------------------------------------------------------------------
resource "google_project_iam_member" "participants" {
  for_each = toset(var.participants)

  project = var.project_id
  role    = var.participant_role
  member  = each.key
}

resource "google_project_iam_member" "participants_viewer" {
  for_each = toset(var.participants)

  project = var.project_id
  role    = "roles/viewer"
  member  = each.key
}
