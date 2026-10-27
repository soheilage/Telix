variable "project_id" {
  description = "Shared GCP project (already created by the admin) that hosts the workshop."
  type        = string
}

variable "location" {
  description = "Gemini Enterprise multi-region. Keep `global` to match the lab."
  type        = string
  default     = "global"
}

variable "bucket_name" {
  description = "Cloud Storage bucket for sample data. Defaults to the project ID, like the lab."
  type        = string
  default     = null
}

variable "bucket_location" {
  description = "Location of the sample-data bucket."
  type        = string
  default     = "US"
}

variable "app_id" {
  description = "Engine (app) ID of the Gemini Enterprise application."
  type        = string
  default     = "cymbal-foods-gemini-enterprise"
}

variable "app_display_name" {
  description = "Display name shown in the Gemini Enterprise console and web app."
  type        = string
  default     = "Cymbal Foods - Gemini Enterprise"
}

variable "company_name" {
  description = "Company name used for branding / LLM grounding."
  type        = string
  default     = "Cymbal Foods"
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
    Project role granted to participants.
    - `roles/discoveryengine.editor` (default): participants can use the web app AND
      see/modify the app in the Cloud console (Module 2.1 verification, or adding the
      Drive/Calendar data stores themselves if you delegate that to a volunteer).
    - `roles/discoveryengine.user`: web-app access only; the facilitator adds the
      connectors and participants skip the console parts of Modules 1-2.
  EOT
  type        = string
  default     = "roles/discoveryengine.editor"
}

variable "run_preflight" {
  description = "Run the one-time access preflight check before creating resources. Set to false after it has passed once."
  type        = bool
  default     = true
}
