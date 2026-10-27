# Facilitator guide

Goal: participants open one URL and spend the whole session on Gemini Enterprise features.
Everything else is done by **the admin** (once, before you) and **you** (Terraform, the day
before).

## 1. Responsibilities

| Who | What | When |
|-----|------|------|
| **Customer admin** (Telix) | Create the shared GCP project with billing; enable Gemini Enterprise subscription and assign licences to participants' Workspace users; set **Gemini Enterprise → Settings → Identity = Google Identity**; grant **you** `roles/editor` + `roles/discoveryengine.admin` + `roles/resourcemanager.projectIamAdmin` on the project; make sure Workspace allows the Drive and Calendar connectors | ≥ 1 week before |
| **Facilitator** (you) | Create the participant group (§1b), `terraform apply`, share the Drive folder, fill the doc placeholders, dry-run | 1 day before |
| **Participants** | Modules 0–6 with a browser | Workshop day |

## 1b. Create the participant group

Access is granted to one Google Group. Create it with Cloud Identity (you need the
Groups Admin role in Workspace, or ask the admin to run this):

```bash
gcloud services enable cloudresourcemanager.googleapis.com cloudidentity.googleapis.com --project <PROJECT_ID>

gcloud identity groups create ge-workshop@<DOMAIN> \
  --organization=<DOMAIN> --display-name="Gemini Enterprise Workshop" \
  --labels=cloudidentity.googleapis.com/groups.discussion_forum

# The creator is automatically OWNER + MEMBER. Add participants one by one
# (only ONE --roles value per call):
gcloud identity groups memberships add --group-email=ge-workshop@<DOMAIN> \
  --member-email=jane@<DOMAIN> --roles=MEMBER

gcloud identity groups memberships list --group-email=ge-workshop@<DOMAIN>
```

Put `group:ge-workshop@<DOMAIN>` in `participants` in `terraform.tfvars`.

## 2. Provision (day before)

```bash
git clone https://github.com/soheilage/Telix.git && cd Telix

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

1. Enables `cloudresourcemanager`, `serviceusage`, `iam`, `cloudidentity`, `discoveryengine`, `storage`, `drive`, `calendar-json` APIs (no-op if already on).
2. Bucket `<PROJECT_ID>` with `gemini-enterprise-drive/`, `notebooklm-drive/`,
   `gemini-enterprise-cloud-storage/` populated from [`data/`](data).
3. Data store `cloud-storage-ds` + a document import from `gemini-enterprise-cloud-storage/`.
4. Gemini Enterprise app `cymbal-foods-gemini-enterprise` (global, `APP_TYPE_INTRANET`,
   Enterprise tier + LLM add-on, agent sharing enabled, company name *Cymbal Foods*).
5. IAM for `participants`: `roles/discoveryengine.editor` + `roles/viewer` on the
   project, `objectViewer` on the bucket.

Indexing of the Cloud Storage data store takes 5–10 minutes.

> [!TIP]
> On a brand-new project the google provider itself needs the Cloud Resource Manager
> API. If `terraform plan` fails with `SERVICE_DISABLED`, run
> `gcloud services enable cloudresourcemanager.googleapis.com --project <PROJECT_ID>` once.

### 2.1 Deploying to `eu` (or `us`) instead of `global`

Set **both** `location = "eu"` and `bucket_location = "EU"` in `terraform.tfvars`.
Everything (app, data stores, Drive/Calendar connectors, Gemini Notebook) must stay in
the same multi-region. Be aware of:

- **Console location selector** – the Gemini Enterprise console opens on *global* and
  will show *There are no apps yet*. Click **Edit** next to *Current location* and pick
  `eu`. `terraform output app_console_url` already includes the right location.
- **Feature lag** – Deep Research and newer models/Studio formats reach `global` first.
  Check the app menu during your dry run; drop Module 4 if Deep Research is absent.
- **Licences** – Gemini Notebook licences are purchased per multi-region.
- **Org policy** – if `gcp.resourceLocations` is enforced it must allow the `eu`
  multi-region value, not only `europe-west*` regions.

> [!NOTE]
> Terraform cannot (yet) set Workspace identity or upload the app logo. Identity is the
> admin's prerequisite above; optional branding can be set in the console under the app's
> **Configurations → UI**.

## 3. Stage Google Workspace content (approach A — one shared Drive folder)

1. With your workshop account, create a Drive folder named **Gemini Enterprise Drive Assets**.
2. Upload the four files from `data/`: `MARKETING_data.csv`, `SALES_data.csv`,
   `customer_feedback.csv`, `pie_chart_customer_sentiment-png.png`.
3. Share the folder with the participant group as **Viewer**.
4. Generate the one-click Calendar link (participants create their own event in Module 1):

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

Two values are not known to Terraform: the web-app URL and the calendar link.

1. Open `terraform output app_console_url` → **Overview** → copy the link under
   *Your Gemini Enterprise webapp is ready*.
2. Run, from the repo root:

   ```bash
   ./scripts/fill-placeholders.sh "https://vertexaisearch.cloud.google.com/home/cid/..."
   ```

   It replaces `<PROJECT_ID>`, `<LOCATION>`, `<BUCKET_NAME>`, `<BUCKET_CONSOLE_URL>`,
   `<APP_CONSOLE_URL>`, `<DATA_STORES_CONSOLE_URL>`, `<GEMINI_ENTERPRISE_APP_URL>` and
   `<CALENDAR_TEMPLATE_LINK>` (generated via `scripts/calendar-link.sh` unless passed as
   the second argument) across `docs/`, and warns about anything left unresolved.

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
- Drive/Calendar connector indexing lag → start Module 2 early; have Cloud Storage-only prompts ready.
- Many people creating "Sales Assistant" in the shared app → initials in names.
- Deep Research quota at scale → fine for ~20 users; for larger groups stagger starts.

## 7. Teardown

```bash
cd terraform
terraform destroy      # removes app, data store, bucket (force_destroy), IAM bindings
```

Agents and skills participants created live inside the app and are removed with it.
Delete the shared Drive folder manually. The APIs stay enabled (`disable_on_destroy = false`).

## 8. Updating the content

- Sample data lives in `data/`; Terraform re-uploads on change and re-triggers the import.
- Keep each module to: goal → concepts → numbered steps → checkpoint.
