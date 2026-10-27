# Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| <a id="no-access"></a>App URL says *You don't have access* / 403 | Wrong Google account, or not in the workshop group | Check the profile icon; sign out of personal accounts or use a Chrome profile for your work account. Ask the facilitator to confirm you are in the access group. |
| Console shows *There are no apps yet* (facilitator) | Console location selector is on **global** but the app was deployed to another multi-region (e.g. `eu`) | Click **Edit** next to *Current location* and select the location from `terraform output location`. |
| *Gemini Enterprise licence required* | No licence assigned | Workspace admin must assign a Gemini Enterprise licence to your user. |
| No Drive / Calendar results, or files "not found" | Connectors still indexing (5–10 min), or you skipped **Authorize** in the Connectors panel | Wait, then retry. Open the puzzle-piece **Connectors** icon and authorise Drive and Calendar. |
| Pie-chart question doesn't find the image | Image not yet indexed | Re-run the query; make sure **Tools → Search company data** is selected. |
| Chat shows no response at all | Transient | Refresh the page and resubmit. |
| Calendar question doesn't see your meeting | Event created in a different account/calendar, or Calendar connector not authorised | Verify the event is on your primary calendar of the workshop account; authorise Calendar. |
| **+ New data store** fails with permission error (Module 2) | Participants were granted `roles/discoveryengine.user` (read-only) | Expected — connectors are added once per app by the facilitator. |
| Agent Designer "Create" button disabled | Required Details fields empty | Make sure Name and Instructions are filled; try **Preview** first. |
| Skill doesn't show when typing `/` | Not saved, or browser cache | Open **Skills** and confirm it is listed; start a **New chat**. |
| **Deep Research** (or another feature) missing from the menu | App deployed in `eu`/`us`; some agentic features ship to `global` first | Check the feature list for your region; skip the module or demo it from a `global` app. |
| Deep Research never finishes | Long-running or quota | It can take >10 min at peak; it keeps running if you navigate away. Check back from **Library**. |
| Notebook: `.txt` files not visible in the Drive picker | Folder not shared with you, or Drive connector not authorised | Check **Shared with me** in Drive; otherwise download the `.txt` files from `data/` and use **Upload sources**. |
| Studio artefacts missing | Still generating | They build in the background; check again after a few minutes. |

Still stuck? Ask your facilitator — they can check the app in the Cloud console
(**Gemini Enterprise → Apps → Cymbal Foods → Connected data stores / Activity**).
