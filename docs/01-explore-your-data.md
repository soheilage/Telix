# Module 1 — Explore your data (10 min)

Gemini Enterprise is only as useful as the data it can reach. In this module you look at
the Cymbal Foods sample data that lives in three places — Cloud Storage, Google Drive and
Google Calendar — so you know what to expect when you query it later.

## 1.1 Sample documents in Cloud Storage

1. Open the bucket in the Cloud console: **<BUCKET_CONSOLE_URL>**
   (Navigation menu ☰ → **Cloud Storage** → **Buckets** → `<BUCKET_NAME>`).

   > [!NOTE]
   > You may also see a system-generated *Discovery Engine import staging* bucket.
   > Ignore it and open `<BUCKET_NAME>`.

2. Browse the three folders:

   | Folder | Contents | Used by |
   |--------|----------|---------|
   | `gemini-enterprise-drive/` | `MARKETING_data.csv`, `SALES_data.csv`, `customer_feedback.csv`, `pie_chart_customer_sentiment-png.png` | Copies of the files in your Drive folder; used by the app and custom agents |
   | `notebooklm-drive/` | `.txt` versions of the key data files | Gemini Notebook (Module 5) |
   | `gemini-enterprise-cloud-storage/` | Enterprise operations text files | Already connected and indexed via the **Cloud Storage** data store |

3. Click `gemini-enterprise-drive/MARKETING_data.csv` → **Download** (or **Preview**) and
   skim it. Notice campaign IDs such as `SPRING25` (Spring Cookie Promotion) and
   `EMAIL0325` (March Newsletter). You will ask about these later.

## 1.2 Pre-staged files in Google Drive

1. Open [Google Drive](https://drive.google.com) in a new tab (same account).
2. Go to **Shared with me** and open **Gemini Enterprise Drive Assets**.
   Tip: right-click → **Add shortcut to Drive** so it also appears under *My Drive*.
3. Verify it contains these four files:

   - `MARKETING_data.csv`
   - `SALES_data.csv`
   - `customer_feedback.csv`
   - `pie_chart_customer_sentiment-png.png`

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
   - **Title:** `Cymbal Foods - Marketing Strategy Meeting`
   - **Start:** at least one hour from now (adjust if you like)
   - **Description:** agenda referencing the Q1 2026 campaigns
2. Confirm the profile icon shows your workshop account, then click **Save**.

<details>
<summary>Manual alternative</summary>

In Google Calendar click **Create → Event**, set the title to
`Cymbal Foods - Marketing Strategy Meeting`, choose a start time at least one hour
from now, click **Save**.
</details>

## ✅ Checkpoint

- [ ] You can open `<BUCKET_NAME>` and see the three folders.
- [ ] **Gemini Enterprise Drive Assets** shows four files.
- [ ] *Cymbal Foods - Marketing Strategy Meeting* appears in your calendar today.

**Next:** [Module 2 — Connect Google Workspace](02-connect-workspace.md)
