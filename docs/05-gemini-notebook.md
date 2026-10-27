# Module 5 — Analyse enterprise documents with Gemini Notebook (20 min)

So far you used Gemini Enterprise as a broad platform over *all* connected data.
**Gemini Notebook** (NotebookLM for the enterprise) is the opposite: a focused research
assistant grounded **only** in the sources you add to a notebook — ideal for an in-depth
review of a few sales reports and feedback trends before drafting a proposal.

## 5.1 Create a notebook and add sources

1. In the Gemini Enterprise navigation menu click **Gemini Notebook**.
2. On **Welcome to Gemini Notebook** click **+ Create new notebook**. A new notebook opens
   with the **Add sources** dialog.

   ![Add sources dialog](../assets/notebook-add-sources.png)

3. Under **Link** click **Website**.
4. In **Paste URLs** paste these three text files (public copies of the files in the
   `notebooklm-drive/` folder):

   ```text
   https://storage.googleapis.com/spls/gemini-enterprise/SALES_data.txt
   https://storage.googleapis.com/spls/gemini-enterprise/customer_feedback.txt
   https://storage.googleapis.com/spls/gemini-enterprise/MARKETING_data.txt
   ```

5. Click **Insert**. After a few seconds the three sources appear, and the notebook gets an
   automatic title (e.g. *Sweet Treats: Campaigns, Sales, Feedback*) and summary.

   ![Notebook overview](../assets/notebook-overview.png)

<details>
<summary>Alternative: upload the files yourself</summary>

Download the three `.txt` files from this repo's
[`data/`](../data) folder (or from `<BUCKET_NAME>/notebooklm-drive/`) and drag them into
**Upload sources**. Gemini Notebook also accepts PDF, Markdown, Word, PowerPoint, Excel,
audio, images, Google Docs/Slides and pasted text.
</details>

## 5.2 Query the sources

Gemini Notebook answers **only** from the documents in this notebook and cites the exact
passages. Try each prompt and click a citation number to jump to the source text.

```text
What audience did the Spring Cookie Promotion target?
```

```text
Summarize the key themes from the customer_feedback.txt regarding products that had sales figures reported in Q1 2026 in the SALES_data.txt.
```

```text
Are there any marketing campaigns in MARKETING_data.txt that correspond to products with significant customer feedback or notable sales trends from the other documents?
```

```text
What are the top 3 most frequently mentioned positive aspects in the customer_feedback.txt?
```

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
   Cymbal Foods documents?

## ✅ Checkpoint

- [ ] Notebook contains three sources with an auto-generated title.
- [ ] All four queries returned cited answers.
- [ ] At least one Studio artefact (e.g. Audio Overview) was generated and reviewed.

Don't forget to go back to [Module 4](04-deep-research.md) and read your Deep Research
report.

**Next:** [Module 6 — Explore further](06-explore-further.md)
