# Facilitator guide

Goal: participants open one URL and spend the whole session on Gemini Enterprise features.
Everything else is done by **the admin** (once, before you) and **you** (Terraform, the day
before).

## 1. Responsibilities

| Who | What | When |
|-----|------|------|
| **Customer admin** (Telix) | Create the shared GCP project with billing; enable Gemini Enterprise subscription and assign licences to participants' Workspace users; set **Gemini Enterprise → Settings → Identity = Google Identity**; create a Google Group for participants (e.g. `ge-workshop@telix.com`); grant **you** `roles/editor` + `roles/discoveryengine.admin` + `roles/resourcemanager.projectIamAdmin` on the project; make sure Workspace allows the Drive and Calendar connectors | ≥ 1 week before |
| **Facilitator** (you) | Run preflight once, `terraform apply`, share the Drive folder, fill the doc placeholders, dry-run | 1 day before |
| **Participants** | Modules 0–6 with a browser | Workshop day |

## 2. Provision (day before)

```bash
git clone <this-repo> && cd telix-gemini-enterprise-workshop

gcloud auth login
gcloud auth application-default login
gcloud config set project <PROJECT_ID>

cd terraform
cp terraform.tfvars.example terraform.tfvars   # edit project_id and participants
terraform init
terraform apply                                 # runs scripts/preflight.sh first
```

`preflight.sh` is the **one-time access check**: it validates auth, project visibility,
billing, and the exact IAM permissions `apply` needs, and prints the admin-only
prerequisites it cannot verify. If it fails, nothing is created — forward the printed
list to the admin. After it has passed once you can skip it:
`terraform apply -var run_preflight=false`.

What `apply` creates (see [terraform/main.tf](terraform/main.tf)):

1. Enables `discoveryengine`, `storage`, `drive`, `calendar-json` APIs (no-op if already on).
2. Bucket `<PROJECT_ID>` in the **EU** multi-region with `gemini-enterprise-drive/`,
   `notebooklm-drive/`, `gemini-enterprise-cloud-storage/` populated from [`data/`](data).
3. Data store `cloud-storage-ds` + a document import from `gemini-enterprise-cloud-storage/`.
4. Gemini Enterprise app `telix-gemini-enterprise` (location `eu`, `APP_TYPE_INTRANET`,
   Enterprise tier + LLM add-on, agent sharing enabled, company name *Telix Pharmaceuticals*).
5. IAM for `participants`: `roles/discoveryengine.editor` + `roles/viewer` on the
   project, `objectViewer` on the bucket.

Indexing of the Cloud Storage data store takes 5–10 minutes.

> [!IMPORTANT]
> **EU region.** Telix's Gemini Enterprise is provisioned in the **`eu` multi-region**
> (`location = "eu"`, bucket in `EU`). Everything created later must match:
> - Drive and Calendar connectors (Module 2) must be created with multi-region **eu**;
>   a `global`/`us` connector cannot be attached to an `eu` app.
> - The console URLs from `terraform output` and the document-import script already use
>   the regional endpoint (`eu-discoveryengine.googleapis.com`).
> - Some Gemini Enterprise capabilities roll out to `eu` after `global`/`us`. During the
>   dry run confirm that Agent Designer, Skills, Deep Research and Gemini Notebook are all
>   available in the EU app, and check Workspace admin settings allow EU data-region
>   processing for Gemini. If a feature is missing, drop that section from the run of show
>   rather than switching regions.

> [!NOTE]
> Terraform cannot (yet) set Workspace identity or upload the app logo. Identity is the
> admin's prerequisite above; optional branding can be set in the console under the app's
> **Configurations → UI**.

## 3. Stage Google Workspace content (approach A — one shared Drive folder)

1. With your workshop account, create a Drive folder named **Telix Gemini Enterprise Drive Assets**.
2. Upload the four files from `data/`: `CLINICAL_TRIAL_SITES.csv`, `MEDICAL_INFO_ENQUIRIES.csv`,
   `investigator_feedback.csv`, `pie_chart_enquiry_categories.png`.
   Optionally also upload the three `.txt` files so participants can add them to Gemini
   Notebook straight from Drive in Module 5 (the default path downloads them from the bucket).
3. Share the folder with the participant group as **Viewer**.
4. Generate the one-click Calendar link (participants create their own event
   *Telix - Clinical Operations Review* in Module 1):

   ```bash
   ./scripts/calendar-link.sh                       # next full hour + 1h
   ./scripts/calendar-link.sh 20261105T100000Z 20261105T103000Z   # or explicit UTC times
   ```

## 4. Connect Drive & Calendar (your choice)

Module 2 is written so that **you** add the Drive and Calendar data stores live
(10 minutes of demo), and every participant then authorises their own account in the
app. If you'd rather save the time, add both connectors the day before and tell
participants to skip to section 2.4.

## 5. Fill in the placeholders

Run `terraform output` and replace these tokens across `docs/` (`sed -i` or your editor):

| Placeholder | Source |
|-------------|--------|
| `<PROJECT_ID>` | your tfvars |
| `<BUCKET_NAME>`, `<BUCKET_CONSOLE_URL>` | `terraform output bucket_name` / `bucket_console_url` |
| `<APP_CONSOLE_URL>`, `<DATA_STORES_CONSOLE_URL>` | `terraform output` |
| `<GEMINI_ENTERPRISE_APP_URL>` | Open `app_console_url` → **Overview** → copy the link under *Your Gemini Enterprise webapp is ready* |
| `<CALENDAR_TEMPLATE_LINK>` | `scripts/calendar-link.sh` |

Example:

```bash
cd terraform
PROJECT_ID=$(grep -E '^project_id' terraform.tfvars | cut -d'"' -f2)
BUCKET=$(terraform output -raw bucket_name)
sed -i "s|<PROJECT_ID>|${PROJECT_ID}|g; s|<BUCKET_NAME>|${BUCKET}|g" ../docs/*.md
```

Then do a **full dry run** with a non-admin test user from the participant group.

## 6. Run of show (≈ 90–100 min)

| Time | Segment | Notes |
|------|---------|-------|
| 0:00 | Welcome, what Gemini Enterprise is, architecture slide | Show the Mermaid diagram in README |
| 0:10 | Module 0–1 | Everyone opens the app, Drive folder, clicks the Calendar link |
| 0:20 | Module 2 (live demo) | You add Drive + Calendar connectors; everyone authorises |
| 0:30 | Module 3 | Longest block; circulate. Encourage initials on agent/skill names |
| 1:00 | Module 4 | Start Deep Research, move on immediately |
| 1:05 | Module 5 | Notebook; Studio artefacts generate in background |
| 1:25 | Back to Module 4 results, Module 6 discussion prompts | |
| 1:35 | Wrap-up, next steps | |

### Common pitfalls

- Participants signed in with a personal Gmail → 403. Ask them to use a dedicated Chrome profile.
- Connector created in the wrong multi-region (`global` instead of `eu`) → it won't appear under the app; delete and recreate it in `eu`.
- Drive/Calendar connector indexing lag → start Module 2 early; have Cloud Storage-only prompts ready.
- Many people creating "Medical Affairs Assistant" in the shared app → initials in names.
- Deep Research quota at scale → fine for ~20 users; for larger groups stagger starts.
- Participants asking whether the figures are real → point to the disclaimer in
  [data/README.md](data/README.md); everything is synthetic and must not be quoted externally.

## 7. Teardown

```bash
cd terraform
terraform destroy      # removes app, data store, bucket (force_destroy), IAM bindings
```

Agents and skills participants created live inside the app and are removed with it.
Delete the shared Drive folder manually. The APIs stay enabled (`disable_on_destroy = false`).

## 8. Updating the content

- Sample data lives in `data/` and is generated by `scripts/generate-sample-data.py`
  (see [data/README.md](data/README.md)); Terraform re-uploads on change and re-triggers
  the import. If you change the data, update the expected figures quoted in
  `docs/03-agents-and-skills.md` and `docs/05-gemini-notebook.md`.
- Keep all data synthetic: no real Telix programme codes, patient data or product claims.
- Screenshots go in `assets/` with the file names referenced in the docs.
- Keep each module to: goal → concepts → numbered steps → checkpoint.
