# Sample data — Telix Clinical & Medical Affairs scenario

> [!IMPORTANT]
> **All files in this folder are synthetic and created solely for this workshop.**
> Study codes (`TLX-PRO-01`, `TLX-REN-02`, `TLX-GLI-03`), sites, investigators, enquiries,
> figures and feedback are fictional. They do not describe any real Telix programme,
> product, patient, trial result or safety profile, and must not be quoted as such.

| File | Rows | Description | Used by |
|------|------|-------------|---------|
| `CLINICAL_TRIAL_SITES.csv` / `.txt` | 15 sites | Site-level enrolment tracker for three fictional studies: target vs actual enrolment, screen-fail rate, activation date, CRA, monitoring visit, notes | Modules 3 & 5 |
| `MEDICAL_INFO_ENQUIRIES.csv` / `.txt` | 25 enquiries | Q1 2026 medical-information log: requester type, country, programme, category (Imaging Protocol, Preparation & QC, Dosing, Supply & Logistics, Adverse Event, Clinical Data), channel, priority, status, response time | Modules 3 & 5 |
| `investigator_feedback.csv` / `.txt` | 20 comments | Free-text feedback from investigators, pharmacists and study coordinators | Modules 3 & 5 |
| `pie_chart_enquiry_categories.png` | — | *Perceived* (Medical Affairs survey) vs *actual* (Q1 log) split of enquiry categories | Module 3 (multimodal) |

The `.txt` files are byte-identical copies of the CSVs; they are used where the product
expects plain-text sources (Gemini Notebook, Cloud Storage data store).

Headline figures (handy for checking answers during the workshop):

- Enrolment: **86 / 175** patients (49.1 % of target) across 15 sites; 133 screened, 47
  screen failures (35.3 %). By study: `TLX-PRO-01` 51/105, `TLX-REN-02` 22/42, `TLX-GLI-03` 13/28.
- Enquiries: 25 total — Imaging Protocol 7, Preparation & QC 6, Dosing 4, Supply & Logistics 4,
  Adverse Event 2, Clinical Data 2. 22 closed, 2 in progress, 1 open; average response time
  for closed enquiries 8.8 h; 6 high priority.

To regenerate the files, edit [`scripts/generate-sample-data.py`](../scripts/generate-sample-data.py) and run:

```bash
python3 scripts/generate-sample-data.py data
convert -density 96 data/pie_chart_enquiry_categories.svg data/pie_chart_enquiry_categories.png
rm data/pie_chart_enquiry_categories.svg
```
