# Module 1 — Explore your data (10 min)

Gemini Enterprise is only as useful as the data it can reach. In this module you look at
the Telix sample data that lives in three places — Cloud Storage, Google Drive and
Google Calendar — so you know what to expect when you query it later.

The (fictional) scenario: you support three recruiting studies — `TLX-PRO-01` (Phase 3,
PSMA-targeted PET in prostate cancer), `TLX-REN-02` (Phase 2, renal mass PET) and
`TLX-GLI-03` (Phase 1/2, radioligand therapy in glioma). Your team tracks **site
enrolment**, answers **medical-information enquiries** from HCPs and pharmacists, and
collects **investigator feedback**.

## 1.1 Sample documents in Cloud Storage

1. Open the bucket in the Cloud console: **<BUCKET_CONSOLE_URL>**
   (Navigation menu ☰ → **Cloud Storage** → **Buckets** → `<BUCKET_NAME>`).

   > [!NOTE]
   > You may also see a system-generated *Discovery Engine import staging* bucket.
   > Ignore it and open `<BUCKET_NAME>`.

2. Browse the three folders:

   | Folder | Contents | Used by |
   |--------|----------|---------|
   | `gemini-enterprise-drive/` | `CLINICAL_TRIAL_SITES.csv`, `MEDICAL_INFO_ENQUIRIES.csv`, `investigator_feedback.csv`, `pie_chart_enquiry_categories.png` | Copies of the files in your Drive folder; used by the app and custom agents |
   | `notebooklm-drive/` | `.txt` versions of the three data files | Gemini Notebook (Module 5) |
   | `gemini-enterprise-cloud-storage/` | The same `.txt` files | Already connected and indexed via the **Cloud Storage** data store |

   | File | What it contains |
   |------|------------------|
   | `CLINICAL_TRIAL_SITES` | 15 sites across the three studies: enrolment target vs actual, patients screened, screen-fail rate, activation date, CRA, last monitoring visit, notes |
   | `MEDICAL_INFO_ENQUIRIES` | 25 enquiries received in Q1 2026: requester type, country, programme, category (Imaging Protocol, Preparation & QC, Dosing, Supply & Logistics, Adverse Event, Clinical Data), priority, status, response time |
   | `investigator_feedback` | 20 free-text comments from investigators, pharmacists and study coordinators |
   | `pie_chart_enquiry_categories.png` | *Perceived* vs *actual* split of enquiry categories |

3. Click `gemini-enterprise-drive/CLINICAL_TRIAL_SITES.csv` → **Download** (or **Preview**)
   and skim it. Notice site IDs such as `S101` (Royal Harbour Hospital, Melbourne — the top
   recruiter) and `S202` (Cleveland — a high screen-fail rate). You will ask about these later.

## 1.2 Pre-staged files in Google Drive

1. Open [Google Drive](https://drive.google.com) in a new tab (same account).
2. Go to **Shared with me** and open **Telix Gemini Enterprise Drive Assets**.
   Tip: right-click → **Add shortcut to Drive** so it also appears under *My Drive*.
3. Verify it contains these four files:

   - `CLINICAL_TRIAL_SITES.csv`
   - `MEDICAL_INFO_ENQUIRIES.csv`
   - `investigator_feedback.csv`
   - `pie_chart_enquiry_categories.png`

   ![Drive assets folder](../assets/drive-assets.png)

   > [!NOTE]
   > In a real deployment each employee's own Drive content is searchable, subject to
   > their existing Drive permissions. For the workshop a single shared folder is used so
   > nobody has to upload anything.

## 1.3 Add a meeting to Google Calendar (one click)

Gemini Enterprise can reason over your calendar once the Calendar connector is added
(next module). Create one relevant event now:

1. Click this pre-filled link: **<CALENDAR_TEMPLATE_LINK>**
   It opens Google Calendar with:
   - **Title:** `Telix - Clinical Operations Review`
   - **Start:** at least one hour from now (adjust if you like)
   - **Description:** agenda referencing Q1 2026 site enrolment, enquiry trends and investigator feedback
2. Confirm the profile icon shows your workshop account, then click **Save**.

<details>
<summary>Manual alternative</summary>

In Google Calendar click **Create → Event**, set the title to
`Telix - Clinical Operations Review`, choose a start time at least one hour
from now, click **Save**.
</details>

## ✅ Checkpoint

- [ ] You can open `<BUCKET_NAME>` and see the three folders.
- [ ] **Telix Gemini Enterprise Drive Assets** shows four files.
- [ ] *Telix - Clinical Operations Review* appears in your calendar today.

**Next:** [Module 2 — Connect Google Workspace](02-connect-workspace.md)
