variable "project_id" {
  description = "Shared GCP project (already created by the admin) that hosts the workshop."
  type        = string
}

variable "location" {
  description = <<-EOT
    Gemini Enterprise (Discovery Engine) multi-region. The Telix workshop runs in the
    EU multi-region (`eu`) for data residency; the app, the Cloud Storage data store and
    the Drive/Calendar connectors added in Module 2 must all use the same location.
  EOT
  type        = string
  default     = "eu"

  validation {
    condition     = contains(["eu", "us", "global"], var.location)
    error_message = "location must be one of: eu, us, global."
  }
}

variable "bucket_name" {
  description = "Cloud Storage bucket for sample data. Defaults to the project ID, like the lab."
  type        = string
  default     = null
}

variable "bucket_location" {
  description = "Location of the sample-data bucket. Kept in the EU multi-region to match `location`."
  type        = string
  default     = "EU"
}

variable "app_id" {
  description = "Engine (app) ID of the Gemini Enterprise application."
  type        = string
  default     = "telix-gemini-enterprise"
}

variable "app_display_name" {
  description = "Display name shown in the Gemini Enterprise console and web app."
  type        = string
  default     = "Telix - Gemini Enterprise"
}

variable "company_name" {
  description = "Company name used for branding / LLM grounding."
  type        = string
  default     = "Telix Pharmaceuticals"
}

variable "data_store_id" {
  description = "ID of the pre-connected Cloud Storage data store."
  type        = string
  default     = "cloud-storage-ds"
}

variable "participants" {
  description = <<-EOT
    IAM principals that get end-user access to the app, e.g.
    ["group:ge-workshop@telix.com"] or ["user:jane@telix.com", "user:john@telix.com"].
    Prefer a single Google Group managed by the admin.
  EOT
  type        = list(string)
  default     = []
}

variable "participant_role" {
  description = <<-EOT
    Role granted to participants. `roles/discoveryengine.editor` is needed so they can
    add the Google Drive / Calendar data stores themselves (Task 2) and create agents
    and skills. Use `roles/discoveryengine.user` if the facilitator pre-connects
    Drive/Calendar and participants should only consume the app.
  EOT
  type        = string
  default     = "roles/discoveryengine.editor"
}

variable "run_preflight" {
  description = "Run the one-time access preflight check before creating resources. Set to false after it has passed once."
  type        = bool
  default     = true
}
