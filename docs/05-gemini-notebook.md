# Module 5 — Analyse enterprise documents with Gemini Notebook (20 min)

So far you used Gemini Enterprise as a broad platform over *all* connected data.
**Gemini Notebook** (NotebookLM for the enterprise) is the opposite: a focused research
assistant grounded **only** in the sources you add to a notebook — ideal for an in-depth
review of a few operational reports and feedback trends before drafting a proposal.

## 5.1 Create a notebook and add sources

1. In the Gemini Enterprise navigation menu click **Gemini Notebook**.
2. On **Welcome to Gemini Notebook** click **+ Create new notebook**. A new notebook opens
   with the **Add sources** dialog.

   ![Add sources dialog](../assets/notebook-add-sources.png)

3. Download the three text files from the `notebooklm-drive/` folder of the bucket
   (**<BUCKET_CONSOLE_URL>** → `notebooklm-drive/` → select → **Download**):

   ```text
   CLINICAL_TRIAL_SITES.txt
   MEDICAL_INFO_ENQUIRIES.txt
   investigator_feedback.txt
   ```

4. Drag them into **Upload sources** (or click **Upload sources** and pick them).
5. After a few seconds the three sources appear, and the notebook gets an automatic title
   (e.g. *Telix Trials: Sites, Enquiries, Feedback*) and summary.

   ![Notebook overview](../assets/notebook-overview.png)

<details>
<summary>Alternative: add the files from Google Drive</summary>

If your facilitator also placed the `.txt` files in the **Telix Gemini Enterprise Drive
Assets** folder, choose **Google Drive** in the Add sources dialog and select them there.
Gemini Notebook also accepts PDF, Markdown, Word, PowerPoint, Excel, audio, images,
Google Docs/Slides and pasted text.
</details>

## 5.2 Query the sources

Gemini Notebook answers **only** from the documents in this notebook and cites the exact
passages. Try each prompt and click a citation number to jump to the source text.

```text
Which sites in CLINICAL_TRIAL_SITES.txt are furthest behind their enrolment target, and what reasons are noted?
```

```text
Summarize the key themes in investigator_feedback.txt for the sites that have medical information enquiries logged in MEDICAL_INFO_ENQUIRIES.txt.
```

```text
Are there enquiries in MEDICAL_INFO_ENQUIRIES.txt that correspond to concerns raised in the investigator feedback or to enrolment problems in the site tracker? Give examples with IDs.
```

```text
What are the top 3 most frequently mentioned positive aspects in investigator_feedback.txt?
```

Expected highlights: Reading (`S105`, 5/15) and Toronto (`S106`, 2/10) lag with staffing
and contract reasons; the Hannover delivery-window complaint echoes the similar UK request
in enquiry `MI-2026-004`, and the Boston customs-delay feedback matches `MI-2026-015`;
positives centre on responsive medical information / MSL support, the clear imaging
protocol and the discharge leaflet.

Compare this with Module 3: enterprise search queries *everything* you can access; a
custom agent follows *its* instructions; a notebook studies a *curated* collection.
Use **Save to note** on any answer to build up a structured set of notes.

## 5.3 Studio: Audio Overview, Infographic, Slide Deck

The **Studio** panel (right-hand column) synthesises your sources into other formats:
Audio Overview, Slide Deck, Video Overview, Mind Map, Reports, Flashcards, Quiz,
Infographic.

1. In **Studio** click **Audio Overview**, then **Infographic**, then **Slide Deck**.
   They generate in the background (a few minutes each).

   ![Studio panel](../assets/notebook-studio.png)

2. Open each generated artefact. How faithfully do they capture the main themes of the
   Telix documents? Would the Slide Deck be a reasonable first draft for the Clinical
   Operations Review?

## ✅ Checkpoint

- [ ] Notebook contains three sources with an auto-generated title.
- [ ] All four queries returned cited answers.
- [ ] At least one Studio artefact (e.g. Audio Overview) was generated and reviewed.

Don't forget to go back to [Module 4](04-deep-research.md) and read your Deep Research
report.

**Next:** [Module 6 — Explore further](06-explore-further.md)
