# Module 2 — Connect Google Workspace (10 min)

In a typical deployment an administrator provisions the Gemini Enterprise app, configures
identity, enables agentic features and attaches foundational repositories (here: the
**Cloud Storage** data store), and then connects collaboration tools such as Google Drive
and Google Calendar. Terraform has already done the first part. In this module the app
gets its Drive and Calendar connectors.

> [!IMPORTANT]
> **Everyone shares one app**, so the connectors are added **once**. Your facilitator
> does steps 2.2 and 2.3 live on screen (or asks one volunteer to). Everyone follows
> along, then **everyone** completes 2.4 to authorise their *own* Drive and Calendar.

## 2.1 Verify the pre-provisioned app (everyone)

1. Open **<DATA_STORES_CONSOLE_URL>** (Cloud console → search bar → **Gemini Enterprise**
   → **Apps** → **Cymbal Foods - Gemini Enterprise** → **Connected data stores**).
2. Verify the app is listed in location **global** and that the **Cloud Storage** data
   store (`cloud-storage-ds`) is already connected, importing unstructured documents from
   the `gemini-enterprise-cloud-storage/` folder of `<BUCKET_NAME>`.

## 2.2 Create a Google Drive data store (facilitator / volunteer)

1. On the **Connected data stores** page click **+ New data store**.
2. In **Select a data source** type `Google Drive` and on the **Google Drive** card click
   **Add data source**.
3. On **Specify the Google Drive authentication parameters** click **Continue**.
4. Under **Select Google Drive actions to enable** choose **Select all actions** →
   **Continue**.

   > [!NOTE]
   > Gemini Enterprise never grants extra access: users only find documents they can
   > already open in Drive, and others only see what you share with them.

5. Configure the connector (leave everything else at defaults):

   | Setting | Value |
   |---------|-------|
   | Multi-region (Location of your data connector) | **global** (pre-selected to match the app) |
   | Data connector name | `Google Drive` |

6. Click **Create**.

## 2.3 Create a Google Calendar data store (facilitator / volunteer)

1. **Connected data stores** → **+ New data store**.
2. Search `Google Calendar` → **Add data source**.
3. Authentication parameters page → **Continue**.
4. **Select all actions** → **Continue**.
5. Multi-region **global**, data connector name `Google Calendar` → **Create**.
6. Confirm the panel now lists three data stores:

   | Name | Type | Status |
   |------|------|--------|
   | Cloud Storage | Unstructured data | – |
   | Google Calendar | Calendar | Active |
   | Google Drive | Drive | Active |

   ![Connected data stores](../assets/connected-data-stores.png)

Behind the scenes Gemini Enterprise links all three stores to the
`cymbal-foods-gemini-enterprise` engine and enforces **per-user ACLs** through Google
Identity — which is why each of you now authorises your own account.

## 2.4 Authorise your own Drive and Calendar (everyone)

1. Go back to the Gemini Enterprise web app (**<GEMINI_ENTERPRISE_APP_URL>**).
2. In the chat box click **Connectors** (the puzzle-piece icon).
3. Next to **Drive** click **Authorize** and accept the consent screen.
4. Next to **Calendar** click **Authorize** and accept.

> [!NOTE]
> Newly added connectors can take **5–10 minutes** to index. If Drive results don't show
> up yet in the next module, carry on and retry later.

## ✅ Checkpoint

- [ ] Three data stores (Cloud Storage, Google Drive, Google Calendar) are listed for the app.
- [ ] In the web app's **Connectors** panel, Drive and Calendar show as authorised for you.

**Next:** [Module 3 — Agents & skills](03-agents-and-skills.md)
