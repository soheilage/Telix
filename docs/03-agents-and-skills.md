# Module 3 — Interact with your Gemini Enterprise agents (30 min)

Now the Telix app is connected to your data. In this module you experience it first-hand:
search and summarise documents, ask multimodal questions, check your agenda, then build
your own **custom agent** and a reusable **skill**.

Concepts in one line each:

- **Chat / Search** – ask questions across every connected data store; answers are grounded and cited.
- **Agent** – a specialised persona with its own instructions, model and data-source bindings, built visually in **Agent Designer** (a.k.a. *Workflow Builder*).
- **Skill** – a lightweight, reusable instruction package (`SKILL.md`) invoked on demand with `/slash` (or `@mention`) in any chat.

> [!NOTE]
> Because everyone shares one app, name your agent and skill with your initials
> (e.g. *Medical Affairs Assistant – SK*) so you can find them in the shared gallery.

> [!IMPORTANT]
> All figures below come from the **synthetic** workshop data. Studies, sites,
> investigators and enquiries are fictional.

## 3.1 Search across your data

1. In the web app click **New chat**.
2. Enter:

   ```text
   Give me an update on enrolment across our clinical trial sites.
   ```

   Expect a table of overall performance (15 sites, **86 of 175** patients enrolled ≈ 49 %
   of target, 133 screened, 47 screen failures ≈ 35 %) with a per-study breakdown —
   `TLX-PRO-01` 51/105, `TLX-REN-02` 22/42, `TLX-GLI-03` 13/28 — and an
   **Export to Sheets** button. Two sites (Yokohama, Seoul) are activated but not yet enrolling.

   ![Enrolment update](../assets/chat-enrolment-update.png)

   > If you get no response, refresh and resubmit — the Drive connector may still be indexing.

3. Follow up in the same chat:

   ```text
   Which sites have the highest screen-fail rate, and what reasons are recorded?
   ```

   Expect the small, newly activated sites (Toronto `S106`, Dublin `S204`) at 50 % on tiny
   numbers, then Lyon, Reading and Cleveland in the 40–45 % range — with Cleveland (`S202`,
   5 of 12 screened) the only one with a recorded reason: the lesion-size eligibility criterion.

## 3.2 Multimodal: ask about an image

1. **New chat**.
2. In the search bar click **Tools** → **Search company data**.
3. Enter:

   ```text
   Summarize the medical information enquiry categories pie chart.
   ```

   The answer compares *perceived* vs *actual* category split (e.g. Dosing 35 % perceived
   vs 16 % actual, Preparation & QC 15 % vs 24 %, Imaging Protocol 25 % vs 28 %) and links
   to `pie_chart_enquiry_categories.png`. Note the insight: the team over-estimates dosing
   questions and under-estimates radiopharmacy preparation / QC questions.

   ![Pie chart summary](../assets/chat-pie-chart.png)

   > Re-run the query if it doesn't find the image on the first try.

## 3.3 Calendar awareness

1. **New chat**, then:

   ```text
   What meetings are on my agenda today? What do I need to have prepped for them?
   ```

   Because the Calendar connector is authorised, it sees your *Telix - Clinical Operations
   Review* and suggests preparation based on the site enrolment tracker, the enquiry log
   and the investigator feedback.

## 3.4 Build a custom agent with Agent Designer

1. Click the **Telix** (or Gemini Enterprise) logo to return home.
2. In the navigation menu click **+ New agent** → **Chat agent**.
3. In **What do you want your agent to do?** enter and press ENTER:

   ```text
   Create a Medical Affairs Assistant agent that analyzes medical information enquiry trends and investigator feedback, and highlights issues that need follow-up.
   ```

4. When *Your agent 'Medical Affairs Assistant' is ready* appears, review the preview
   panel with its **Flow**, **Schedule** and **Preview** tabs.

   ![Agent Designer](../assets/agent-designer.png)

5. Select the **Flow** tab and click the **Medical Affairs Assistant** node to open
   **Details**. Inspect (and feel free to tweak) **Name** (add your initials),
   **Description**, **Instructions** (the generated *Role* section tells it to use Google
   Drive / Cloud Storage), **Model** (e.g. Gemini 3.5 Flash) and **Connectors** (Cloud
   Storage, Drive, Google Search).

   > [!TIP]
   > Add one line to the instructions: *"Never make efficacy or safety claims; report only
   > what the documents say and flag anything that may need pharmacovigilance review."*
   > This is how you encode medical-affairs guardrails into an agent.

   ![Agent details](../assets/agent-details.png)

6. Click **Create** in the toolbar to publish. In **Agent Created Successfully** click
   **Chat with Agent**.
7. Test it:

   ```text
   Summarize the key themes from our Q1 2026 medical information enquiries and the investigator feedback. Which items are still open or need follow-up?
   ```

   Expect: 25 enquiries, most about **Imaging Protocol** (7) and **Preparation & QC** (6);
   `TLX-PRO-01` generates the most (12); 22 closed with an average response time of
   ~9 hours; 3 still open / in progress (`MI-2026-021`, `-022`, `-025`); recurring feedback
   themes such as delivery windows, customs delays, screen-fail criteria and slow monitoring
   reports.

8. Inspect the analysis, then return home → **Agents** and confirm your agent is listed
   under **Your agents**.

> [!TIP]
> Invoke any published agent inside a normal chat by typing `@Medical Affairs Assistant`.

## 3.5 Create a reusable skill

1. In the navigation menu click **Skills**.
2. On **Add your first skill** click **Create skill with Gemini**.
3. In **Describe your skill** enter and press ENTER:

   ```text
   Create a Telix Medical Writing Style skill that formats clinical and medical-affairs summaries in a formal, balanced, referenced scientific tone, avoids promotional language, states data sources, and ends with three recommended actions.
   ```

4. Gemini drafts the **Name** (`telix-medical-style`), **Description**, **Trigger**
   (`/telix-medical-style`) and step-by-step **Instructions**. Add your initials to the
   name/trigger, then click **Save**; wait for *Skill created successfully*.
5. **New chat** → type `/` and pick your skill from the **Skills** menu, then enter:

   ```text
   Draft an internal update for the Clinical Operations Review summarizing the Q1 2026 medical information enquiry trends.
   ```

6. Notice the **Skill used** badge: Gemini loaded your style guide, searched the
   connected stores for `MEDICAL_INFO_ENQUIRIES` data, wrote in a neutral scientific tone,
   and ended with three recommended actions (e.g. publish a radiopharmacy QC FAQ, review
   courier windows, close the open enquiries).

## ✅ Checkpoint

- [ ] The enrolment-update query returned a site/study performance table.
- [ ] The pie-chart query produced a perceived-vs-actual comparison.
- [ ] Your **Medical Affairs Assistant** agent appears under **Your agents** and answered the Q1 question.
- [ ] Your medical-writing skill ran and showed the **Skill used** badge.

**Next:** [Module 4 — Deep Research](04-deep-research.md)
