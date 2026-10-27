# Module 3 — Interact with your Gemini Enterprise agents (30 min)

Now the Cymbal Foods app is connected to your data. In this module you experience it
first-hand: search and summarise documents, ask multimodal questions, check your agenda,
then build your own **custom agent** and a reusable **skill**.

Concepts in one line each:

- **Chat / Search** – ask questions across every connected data store; answers are grounded and cited.
- **Agent** – a specialised persona with its own instructions, model and data-source bindings, built visually in **Agent Designer** (a.k.a. *Workflow Builder*).
- **Skill** – a lightweight, reusable instruction package (`SKILL.md`) invoked on demand with `/slash` (or `@mention`) in any chat.

> [!NOTE]
> Because everyone shares one app, name your agent and skill with your initials
> (e.g. *Sales Assistant – SK*) so you can find them in the shared gallery.

## 3.1 Search across your data

1. In the web app click **New chat**.
2. Enter:

   ```text
   Give me an update on our latest marketing data.
   ```

   Expect a table of overall performance (Total Budget \$3,000.00, Total Spend \$2,121.75,
   Impressions 164,500, Clicks 11,100, Conversions 625, CTR 6.75 %, Conversion Rate 5.63 %,
   Cost per Conversion \$3.39) with an **Export to Sheets** button.

   > If you get no response, refresh and resubmit — the Drive connector may still be indexing.

3. Follow up in the same chat:

   ```text
   What products were in the March newsletter?
   ```

## 3.2 Multimodal: ask about an image

1. **New chat**.
2. In the search bar click **Tools** → **Search company data**.
3. Enter:

   ```text
   Summarize the customer sentiment pie chart.
   ```

   The answer compares *perceived* vs *actual* sentiment (e.g. Positive 52.2 % vs 42.1 %,
   Negative 13.0 % vs 31.6 %) and links to `pie_chart_customer_sentiment-png.png`.

   > Re-run the query if it doesn't find the image on the first try.

## 3.3 Calendar awareness

1. **New chat**, then:

   ```text
   What meetings are on my agenda today? What do I need to have prepped for them?
   ```

   Because the Calendar connector is authorised, it sees your *Cymbal Foods - Marketing
   Strategy Meeting* and suggests preparation based on the marketing data.

## 3.4 Build a custom agent with Agent Designer

1. Click the **Cymbal Foods** (or Gemini Enterprise) logo to return home.
2. In the navigation menu click **+ New agent** → **Chat agent**.
3. In **What do you want your agent to do?** enter and press ENTER:

   ```text
   Create a Sales Assistant agent that analyzes quarterly transaction data and customer feedback.
   ```

4. When *Your agent 'Sales Assistant' is ready* appears, review the preview panel with
   its **Flow**, **Schedule** and **Preview** tabs.

5. Select the **Flow** tab and click the **Sales Assistant** node to open **Details**.
   Inspect (and feel free to tweak) **Name** (add your initials), **Description**,
   **Instructions** (the generated *Role* section tells it to use Google Drive / Cloud
   Storage), **Model** (e.g. Gemini 3.5 Flash) and **Connectors** (Cloud Storage, Drive,
   Google Search).

6. Click **Create** in the toolbar to publish. In **Agent Created Successfully** click
   **Chat with Agent**.
7. Test it:

   ```text
   Summarize the key takeaways from our Q1 2026 sales records.
   ```

8. Inspect the analysis, then return home → **Agents** and confirm your agent is listed
   under **Your agents**.

> [!TIP]
> Invoke any published agent inside a normal chat by typing `@Sales Assistant`.

## 3.5 Create a reusable skill

1. In the navigation menu click **Skills**.
2. On **Add your first skill** click **Create skill with Gemini**.
3. In **Describe your skill** enter and press ENTER:

   ```text
   Create a Cymbal Brand Voice skill that formats marketing and product summaries into Cymbal Foods' friendly, sustainability-focused executive tone and ends with a three-bullet action plan.
   ```

4. Gemini drafts the **Name** (`cymbal-brand-voice`), **Description**, **Trigger**
   (`/cymbal-brand-voice`) and step-by-step **Instructions**. Add your initials to the
   name/trigger, then click **Save**; wait for *Skill created successfully*.
5. **New chat** → type `/` and pick your skill from the **Skills** menu, then enter:

   ```text
   Draft an internal announcement summarizing our Spring Cookie Promotion results.
   ```

6. Notice the **Skill used** badge: Gemini loaded your brand guidelines, searched the
   connected stores for campaign `SPRING25` metrics, and ended with a three-bullet action
   plan.

## ✅ Checkpoint

- [ ] The marketing-update query returned a performance table.
- [ ] The pie-chart query produced a sentiment comparison.
- [ ] Your **Sales Assistant** agent appears under **Your agents** and answered the Q1 question.
- [ ] Your brand-voice skill ran and showed the **Skill used** badge.

**Next:** [Module 4 — Deep Research](04-deep-research.md)
