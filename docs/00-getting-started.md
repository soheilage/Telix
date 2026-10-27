# Module 0 — Getting started (5 min)

Everything you need has been set up by your facilitator. In this module you simply open
the application and confirm you can see it.

## What is already provisioned for you

| Item | Value |
|------|-------|
| GCP project | `<PROJECT_ID>` |
| Gemini Enterprise app | **Cymbal Foods - Gemini Enterprise** (`cymbal-foods-gemini-enterprise`, location `<LOCATION>`) |
| Pre-connected data store | **Cloud Storage** (`cloud-storage-ds`) — enterprise operations text files, already indexed |
| Cloud Storage bucket | `<BUCKET_NAME>` with three folders of sample data |
| Shared Drive folder | **Gemini Enterprise Drive Assets** (shared with you) |

> [!NOTE]
> Placeholders in `<ANGLE_BRACKETS>` are filled in by your facilitator before the
> workshop. If you still see them, ask.

## Steps

1. In Chrome, make sure you are signed in with your **company Workspace account**
   (the one your admin assigned a Gemini Enterprise licence to). Check the profile
   icon in the top-right of any Google page.

2. Open the Gemini Enterprise web app:

   **<GEMINI_ENTERPRISE_APP_URL>**

   If you see a **Welcome to Gemini Enterprise!** dialog, click **Get started**.

3. Your home page should look like this: a chat box ("Let's get some work done!") and a
   navigation menu with **New chat**, **Search**, **Library**, **Agents**,
   **Gemini Notebook**, **Deep Research**, and **+ New agent**.

4. (Optional) Open the Google Cloud console view of the same app to see how an admin
   sees it: **<APP_CONSOLE_URL>** → the **Overview** tab shows
   *Your Gemini Enterprise webapp is ready* with the link you just used.

   > [!NOTE]
   > The Gemini Enterprise console defaults to location **global**. This workshop's app
   > lives in **`<LOCATION>`** — if you see *There are no apps yet*, click **Edit** next
   > to *Current location* and pick `<LOCATION>`.

## ✅ Checkpoint

- [ ] The Gemini Enterprise home page loads and shows **Cymbal Foods** branding.
- [ ] Clicking **Agents** in the navigation menu opens the agent gallery.

If the page says you don't have access, see [troubleshooting](troubleshooting.md#no-access).

**Next:** [Module 1 — Explore your data](01-explore-your-data.md)
