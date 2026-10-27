output "project_number" {
  value = data.google_project.project.number
}

output "bucket_name" {
  description = "Bucket participants open in Task 1."
  value       = google_storage_bucket.data.name
}

output "bucket_console_url" {
  value = "https://console.cloud.google.com/storage/browser/${google_storage_bucket.data.name}?project=${var.project_id}"
}

output "app_console_url" {
  description = "Gemini Enterprise > Apps > Overview page. Copy the 'Your Gemini Enterprise webapp is ready' link from here into docs/00-getting-started.md."
  value       = "https://console.cloud.google.com/gen-app-builder/locations/${var.location}/engines/${google_discovery_engine_search_engine.app.engine_id}/overview?project=${var.project_id}"
}

output "data_stores_console_url" {
  description = "Connected data stores page used in Task 2."
  value       = "https://console.cloud.google.com/gen-app-builder/locations/${var.location}/engines/${google_discovery_engine_search_engine.app.engine_id}/data?project=${var.project_id}"
}

output "participants" {
  value = var.participants
}
