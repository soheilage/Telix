# Module 0 — Getting started (5 min)

Everything you need has been set up by your facilitator. In this module you simply open
the application and confirm you can see it.

## What is already provisioned for you

| Item | Value |
|------|-------|
| GCP project | `<PROJECT_ID>` |
| Gemini Enterprise app | **Telix - Gemini Enterprise** (`telix-gemini-enterprise`, location **`eu`** — EU multi-region) |
| Pre-connected data store | **Cloud Storage** (`cloud-storage-ds`) — clinical trial site, medical-information enquiry and investigator feedback text files, already indexed |
| Cloud Storage bucket | `<BUCKET_NAME>` (EU multi-region) with three folders of sample data |
| Shared Drive folder | **Telix Gemini Enterprise Drive Assets** (shared with you) |

> [!NOTE]
> Placeholders in `<ANGLE_BRACKETS>` are filled in by your facilitator before the
> workshop. If you still see them, ask.

> [!IMPORTANT]
> The scenario uses **synthetic data**: studies `TLX-PRO-01`, `TLX-REN-02` and `TLX-GLI-03`,
> their sites, investigators, enquiries and figures are fictional. Nothing in this
> workshop describes a real Telix programme, product, patient or trial result.

## Steps

1. In Chrome, make sure you are signed in with your **Telix Workspace account**
   (the one your admin assigned a Gemini Enterprise licence to). Check the profile
   icon in the top-right of any Google page.

2. Open the Gemini Enterprise web app:

   **<GEMINI_ENTERPRISE_APP_URL>**

   If you see a **Welcome to Gemini Enterprise!** dialog, click **Get started**.

3. Your home page should look like this: a chat box ("Let's get some work done!") and a
   navigation menu with **New chat**, **Search**, **Library**, **Agents**,
   **Gemini Notebook**, **Deep Research**, and **+ New agent**.

   ![Gemini Enterprise home page](../assets/ge-home.png)

4. (Optional) Open the Google Cloud console view of the same app to see how an admin
   sees it: **<APP_CONSOLE_URL>** → the **Overview** tab shows
   *Your Gemini Enterprise webapp is ready* with the link you just used.

## ✅ Checkpoint

- [ ] The Gemini Enterprise home page loads and shows **Telix** branding.
- [ ] Clicking **Agents** in the navigation menu opens the agent gallery.

If the page says you don't have access, see [troubleshooting](troubleshooting.md#no-access).

**Next:** [Module 1 — Explore your data](01-explore-your-data.md)
