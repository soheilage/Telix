# Terraform — workshop environment

Provisions the shared Gemini Enterprise environment in a project the admin already created.
See [../FACILITATOR.md](../FACILITATOR.md) for the full procedure.

```bash
cp terraform.tfvars.example terraform.tfvars   # set project_id, participants
terraform init
terraform apply          # preflight access check runs once, then creates resources
terraform output         # URLs to paste into docs/
terraform destroy        # teardown after the workshop
```

| File | Purpose |
|------|---------|
| `versions.tf` | Provider pins (`hashicorp/google >= 7.7`, needed for `app_type = APP_TYPE_INTRANET`) |
| `variables.tf` | Inputs; only `project_id` and `participants` are required in practice. `location` defaults to `eu` and `bucket_location` to `EU` (Telix data residency) |
| `main.tf` | Preflight → APIs → bucket + data → data store + import → app → IAM |
| `outputs.tf` | Console URLs and bucket name |

Requires `terraform >= 1.6`, `gcloud`, `curl`. State is local by default; add a GCS backend
if several facilitators share the environment.
