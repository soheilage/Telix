#!/usr/bin/env python3
"""Generate synthetic Telix workshop sample data (CSV + TXT + SVG pie chart)."""
import csv
import math
import os
import sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Clinical trial sites
# ---------------------------------------------------------------------------
STUDIES = {
    "TLX-PRO-01": ("PSMA-targeted PET imaging in biochemically recurrent prostate cancer", "Prostate cancer", "Phase 3"),
    "TLX-REN-02": ("Carbonic anhydrase IX PET imaging of indeterminate renal masses", "Renal cell carcinoma", "Phase 2"),
    "TLX-GLI-03": ("Targeted radioligand therapy in recurrent high-grade glioma", "Glioblastoma", "Phase 1/2"),
}

sites = [
    # SiteID, Study, SiteName, City, Country, PI, CRA, Activation, Status, Target, Actual, Screened, LastMV, Notes
    ("S101", "TLX-PRO-01", "Royal Harbour Hospital", "Melbourne", "Australia", "Dr Amelia Hartigan", "J. Okafor", "2026-01-12", "Enrolling", 20, 17, 24, "2026-03-20", "Top recruiter; requesting additional investigational product (IP) slots"),
    ("S102", "TLX-PRO-01", "Pacific Coast Cancer Institute", "San Diego", "USA", "Dr Marcus Feld", "L. Nguyen", "2026-01-19", "Enrolling", 20, 12, 18, "2026-03-18", "Camera downtime in February delayed 3 scans"),
    ("S103", "TLX-PRO-01", "Klinikum Nordstadt", "Hannover", "Germany", "Prof. Ingrid Vossberg", "M. Dubois", "2026-02-02", "Enrolling", 15, 9, 13, "2026-03-25", "Radiopharmacy delivery window too tight for Monday scans"),
    ("S104", "TLX-PRO-01", "Hôpital Sainte-Claire", "Lyon", "France", "Dr Étienne Marchal", "M. Dubois", "2026-02-09", "Enrolling", 15, 6, 11, "2026-03-11", "Ethics amendment approved 2026-03-02"),
    ("S105", "TLX-PRO-01", "Thames Valley NHS Trust", "Reading", "UK", "Dr Priya Raman", "S. Whitcombe", "2026-02-16", "Enrolling", 15, 5, 9, "2026-03-27", "Slow start; awaiting second nuclear medicine physician"),
    ("S106", "TLX-PRO-01", "Lakeside University Medical Center", "Toronto", "Canada", "Dr Daniel Oyelaran", "L. Nguyen", "2026-03-02", "Enrolling", 10, 2, 4, "2026-03-30", "Activated late due to contract negotiation"),
    ("S107", "TLX-PRO-01", "Kanto Nuclear Medicine Centre", "Yokohama", "Japan", "Dr Haruki Sato", "A. Tanaka", "2026-03-16", "Activated - not yet enrolling", 10, 0, 0, "N/A", "Site initiation visit completed 2026-03-16"),
    ("S201", "TLX-REN-02", "Royal Harbour Hospital", "Melbourne", "Australia", "Dr Amelia Hartigan", "J. Okafor", "2026-01-26", "Enrolling", 12, 10, 14, "2026-03-20", "Shares nuclear medicine suite with TLX-PRO-01"),
    ("S202", "TLX-REN-02", "Midwest Urology Research Partners", "Cleveland", "USA", "Dr Sofia Castellano", "L. Nguyen", "2026-02-09", "Enrolling", 12, 7, 12, "2026-03-19", "High screen-fail rate: lesion size criterion"),
    ("S203", "TLX-REN-02", "Universitätsklinik Westfalen", "Münster", "Germany", "Prof. Lukas Brennecke", "M. Dubois", "2026-02-23", "Enrolling", 10, 4, 6, "2026-03-24", "Requested protocol clarification on imaging timepoint"),
    ("S204", "TLX-REN-02", "St Brendan's Hospital", "Dublin", "Ireland", "Dr Niamh Kearney", "S. Whitcombe", "2026-03-09", "Enrolling", 8, 1, 2, "2026-03-31", "First patient dosed 2026-03-23"),
    ("S301", "TLX-GLI-03", "Harbour Neuro-Oncology Centre", "Sydney", "Australia", "Prof. Callum Reyes", "J. Okafor", "2026-01-05", "Enrolling", 8, 6, 9, "2026-03-17", "Dose level 2 cohort open"),
    ("S302", "TLX-GLI-03", "Bayview Brain Tumour Institute", "Boston", "USA", "Dr Hannah Lindqvist", "R. Alvarez", "2026-01-19", "Enrolling", 8, 5, 8, "2026-03-26", "One dose-limiting toxicity review completed - no DLT"),
    ("S303", "TLX-GLI-03", "Centre Hospitalier du Léman", "Geneva", "Switzerland", "Dr Olivier Bastien", "M. Dubois", "2026-02-16", "Enrolling", 6, 2, 3, "2026-03-12", "Awaiting cohort 2 safety review before next enrolment"),
    ("S304", "TLX-GLI-03", "Seoul Metropolitan Cancer Hospital", "Seoul", "South Korea", "Dr Ji-woo Park", "A. Tanaka", "2026-03-23", "Activated - not yet enrolling", 6, 0, 0, "N/A", "Import licence for therapeutic IP pending"),
]

site_header = ["SiteID", "StudyID", "StudyTitle", "Indication", "Phase", "SiteName", "City", "Country",
               "PrincipalInvestigator", "CRA", "ActivationDate", "SiteStatus", "EnrolmentTarget",
               "EnrolmentActual", "PercentOfTarget", "PatientsScreened", "ScreenFailures", "ScreenFailRate",
               "LastMonitoringVisit", "Notes"]
site_rows = []
for s in sites:
    sid, study, name, city, country, pi, cra, act, status, target, actual, screened, lmv, notes = s
    title, ind, phase = STUDIES[study]
    sf = screened - actual
    sfr = f"{sf / screened:.3f}" if screened else "0.000"
    pct = f"{actual / target:.3f}"
    site_rows.append([sid, study, title, ind, phase, name, city, country, pi, cra, act, status, target, actual, pct,
                      screened, sf, sfr, lmv, notes])

# ---------------------------------------------------------------------------
# 2. Medical information enquiries
# ---------------------------------------------------------------------------
enq_header = ["EnquiryID", "DateReceived", "RequesterType", "Country", "Programme", "Category", "Channel",
              "Summary", "Priority", "Status", "ResponseTimeHours", "FollowUpRequired", "AssignedTo", "Notes"]
enquiries = [
    ("MI-2026-001", "2026-01-06 09:15", "Nuclear medicine physician", "Australia", "TLX-PRO-01", "Imaging Protocol", "Email", "Optimal uptake time between injection and PET acquisition for patients with low PSA.", "Medium", "Closed", 6, "No", "Medical Science Liaison - ANZ", "Referred to imaging manual section 4.2"),
    ("MI-2026-002", "2026-01-08 14:40", "Radiopharmacist", "USA", "TLX-PRO-01", "Preparation & QC", "Phone", "Radiochemical purity result 94% - acceptable release threshold?", "High", "Closed", 2, "Yes", "Medical Information - Americas", "Below release limit; batch not released. Deviation logged by site."),
    ("MI-2026-003", "2026-01-12 11:05", "Oncologist", "Germany", "TLX-GLI-03", "Dosing", "Email", "Dose adjustment guidance for patient with estimated GFR of 48 mL/min.", "High", "Closed", 10, "Yes", "Medical Information - EMEA", "Escalated to study medical monitor"),
    ("MI-2026-004", "2026-01-15 16:20", "Study coordinator", "UK", "TLX-PRO-01", "Supply & Logistics", "Web form", "Can delivery be moved to 07:00 to accommodate first scan slot?", "Medium", "Closed", 24, "No", "Clinical Supply", "Courier window updated"),
    ("MI-2026-005", "2026-01-20 10:30", "Nuclear medicine physician", "USA", "TLX-REN-02", "Imaging Protocol", "Email", "Is a diagnostic CT required alongside the low-dose attenuation CT?", "Low", "Closed", 8, "No", "Medical Science Liaison - US", ""),
    ("MI-2026-006", "2026-01-22 13:10", "Hospital pharmacist", "France", "TLX-PRO-01", "Preparation & QC", "Phone", "Kit stored at 30 °C for 3 hours during transport - still usable?", "High", "Closed", 3, "Yes", "Medical Information - EMEA", "Excursion within stability data; usable. Site to file temperature log."),
    ("MI-2026-007", "2026-01-27 09:50", "Oncologist", "Australia", "TLX-GLI-03", "Adverse Event", "Phone", "Grade 2 fatigue and transient thrombocytopenia 10 days post dose - reporting requirements?", "High", "Closed", 1, "Yes", "Pharmacovigilance", "SAE assessment not met; AE recorded in eCRF within 24 h"),
    ("MI-2026-008", "2026-02-02 15:45", "Nuclear medicine technologist", "Canada", "TLX-PRO-01", "Imaging Protocol", "Web form", "Recommended reconstruction parameters for digital PET/CT systems.", "Medium", "Closed", 12, "No", "Imaging Core Lab", "Shared vendor-specific parameter sheet"),
    ("MI-2026-009", "2026-02-04 08:30", "Study coordinator", "Germany", "TLX-REN-02", "Supply & Logistics", "Email", "Short-dated vial received - minimum shelf life at delivery?", "Medium", "Closed", 20, "Yes", "Clinical Supply", "Replacement vial shipped"),
    ("MI-2026-010", "2026-02-06 12:00", "Nuclear medicine physician", "Japan", "TLX-PRO-01", "Clinical Data", "Email", "Request for published detection-rate data stratified by PSA level.", "Low", "Closed", 30, "No", "Medical Science Liaison - APAC", "Provided peer-reviewed references"),
    ("MI-2026-011", "2026-02-10 10:15", "Radiopharmacist", "USA", "TLX-PRO-01", "Preparation & QC", "Phone", "Generator eluate volume differs from label - adjust labelling procedure?", "Medium", "Closed", 4, "No", "Medical Information - Americas", ""),
    ("MI-2026-012", "2026-02-12 14:25", "Oncologist", "UK", "TLX-PRO-01", "Dosing", "Email", "Can the agent be administered on the same day as a bone scan?", "Medium", "Closed", 9, "No", "Medical Information - EMEA", "Recommended 24 h separation"),
    ("MI-2026-013", "2026-02-17 09:00", "Nuclear medicine physician", "Australia", "TLX-REN-02", "Imaging Protocol", "Phone", "Patient unable to lie still for full acquisition - acceptable shortened protocol?", "Medium", "Closed", 5, "Yes", "Imaging Core Lab", "Protocol deviation form provided"),
    ("MI-2026-014", "2026-02-19 16:10", "Hospital pharmacist", "Ireland", "TLX-REN-02", "Preparation & QC", "Web form", "Compatibility of the agent with the site's standard saline flush volume.", "Low", "Closed", 18, "No", "Medical Information - EMEA", ""),
    ("MI-2026-015", "2026-02-24 11:40", "Study coordinator", "USA", "TLX-GLI-03", "Supply & Logistics", "Email", "Therapeutic dose shipment delayed at customs - patient scheduled tomorrow.", "High", "Closed", 2, "Yes", "Clinical Supply", "Dose arrived 4 h late; patient treated same day"),
    ("MI-2026-016", "2026-02-26 13:30", "Oncologist", "Switzerland", "TLX-GLI-03", "Dosing", "Phone", "Radiation safety instructions for patient discharge after therapeutic dose.", "High", "Closed", 3, "No", "Medical Information - EMEA", "Discharge leaflet (v2.1) shared"),
    ("MI-2026-017", "2026-03-02 09:20", "Nuclear medicine technologist", "Germany", "TLX-PRO-01", "Imaging Protocol", "Email", "Bladder activity obscuring prostate bed - voiding or diuretic recommended?", "Medium", "Closed", 7, "No", "Imaging Core Lab", "Added to FAQ v3"),
    ("MI-2026-018", "2026-03-04 15:05", "Radiopharmacist", "Australia", "TLX-REN-02", "Preparation & QC", "Phone", "pH test strip reading at the edge of the specified range.", "Medium", "Closed", 2, "No", "Medical Information - ANZ", "Within specification; confirmed by QP"),
    ("MI-2026-019", "2026-03-09 10:50", "Oncologist", "USA", "TLX-GLI-03", "Adverse Event", "Email", "Grade 1 nausea on day of infusion - prophylactic antiemetic allowed?", "Medium", "Closed", 6, "No", "Pharmacovigilance", "Permitted per protocol section 6.4"),
    ("MI-2026-020", "2026-03-11 08:45", "Nuclear medicine physician", "France", "TLX-PRO-01", "Imaging Protocol", "Web form", "Interpretation guidance for equivocal rib uptake.", "Medium", "Closed", 14, "Yes", "Imaging Core Lab", "Central read requested"),
    ("MI-2026-021", "2026-03-16 12:35", "Hospital pharmacist", "Canada", "TLX-PRO-01", "Supply & Logistics", "Email", "Ordering lead time for additional kits after enrolment increase.", "Low", "In progress", 0, "Yes", "Clinical Supply", "Awaiting forecast from site"),
    ("MI-2026-022", "2026-03-18 14:15", "Oncologist", "Australia", "TLX-GLI-03", "Clinical Data", "Email", "Interim safety summary for dose level 1 cohort for ethics committee.", "Medium", "In progress", 0, "Yes", "Medical Science Liaison - ANZ", "Data cut scheduled 2026-04-01"),
    ("MI-2026-023", "2026-03-23 09:10", "Nuclear medicine physician", "South Korea", "TLX-GLI-03", "Dosing", "Phone", "Body-weight cap for dose calculation in patients over 120 kg.", "Medium", "Closed", 5, "No", "Medical Science Liaison - APAC", ""),
    ("MI-2026-024", "2026-03-25 16:40", "Study coordinator", "UK", "TLX-PRO-01", "Imaging Protocol", "Email", "Can scan be rescheduled if patient arrives 90 minutes late?", "Medium", "Closed", 3, "No", "Imaging Core Lab", "Within acceptable window"),
    ("MI-2026-025", "2026-03-30 11:25", "Radiopharmacist", "USA", "TLX-REN-02", "Preparation & QC", "Web form", "Clarification on filter integrity test frequency.", "Low", "Open", 0, "No", "Medical Information - Americas", "Received end of quarter"),
]
enq_rows = [list(e) for e in enquiries]

# ---------------------------------------------------------------------------
# 3. Investigator / site feedback
# ---------------------------------------------------------------------------
feedback = [
    "The imaging protocol for TLX-PRO-01 is clear and our technologists found the acquisition straightforward. However, the radiopharmacy delivery window in Hannover is too tight for our Monday morning slots.",
    "a.hartigan@royalharbour.example The medical information team responded to our dosing question within two hours. Excellent support from the ANZ MSL.",
    "Enrolment in TLX-REN-02 is slower than expected in Cleveland because the lesion-size eligibility criterion excludes many otherwise suitable patients.",
    "The electronic CRF for TLX-GLI-03 is intuitive, but the adverse event module requires too many mandatory fields for grade 1 events.",
    "Our pharmacists in Lyon appreciated the stability data shared after the temperature excursion - it avoided an unnecessary batch rejection.",
    "p.raman@thamesvalley.example We need a second trained nuclear medicine physician before we can increase our enrolment rate in Reading.",
    "The investigator meeting in January was well organised and the imaging interpretation workshop was genuinely useful.",
    "Customs clearance for therapeutic doses in Boston remains unpredictable. Two shipments have arrived with less than four hours to spare.",
    "Our coordinators in Melbourne would like the monitoring visit reports to be shared sooner; the last one took three weeks to arrive.",
    "The patient discharge leaflet for TLX-GLI-03 is excellent - clear radiation safety instructions in plain language.",
    "s.castellano@midwesturology.example Screening failures are frustrating for patients. Could the protocol team consider an amendment to the lesion-size threshold?",
    "Reconstruction parameters for our digital PET/CT were not in the imaging manual. Thanks to the core lab for sending them quickly.",
    "Site initiation in Yokohama went smoothly, although translated patient materials arrived only two days before the visit.",
    "Toronto contract negotiation took almost three months, which delayed activation well past the planned date.",
    "The study drug accountability log for TLX-REN-02 is duplicated between the paper binder and the IRT system - please streamline.",
    "h.lindqvist@bayview.example Safety review turnaround for cohort 2 was fast and the medical monitor was very accessible.",
    "Bladder activity obscured the prostate bed in two of our TLX-PRO-01 scans; the new FAQ guidance on voiding should help.",
    "We would welcome a central read option for equivocal findings; our Lyon readers do not want to delay patient management.",
    "The CRA for the German sites is extremely responsive and well prepared for monitoring visits.",
    "Overall the Telix study team is supportive, but communication about protocol amendments could be more proactive across all three studies.",
]
fb_rows = [[f] for f in feedback]

# ---------------------------------------------------------------------------
# Write CSV + TXT (TXT is an identical CSV-formatted copy, like the lab)
# ---------------------------------------------------------------------------
def write(name, header, rows):
    for ext in ("csv", "txt"):
        with open(os.path.join(OUT, f"{name}.{ext}"), "w", newline="") as fh:
            w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
            w.writerow(header)
            w.writerows(rows)

write("CLINICAL_TRIAL_SITES", site_header, site_rows)
write("MEDICAL_INFO_ENQUIRIES", enq_header, enq_rows)
write("investigator_feedback", ["Feedback"], fb_rows)

# ---------------------------------------------------------------------------
# 4. Pie charts: perceived vs actual enquiry categories (SVG -> PNG via convert)
# ---------------------------------------------------------------------------
from collections import Counter
actual = Counter(e[5] for e in enquiries)
perceived = {"Dosing": 35, "Imaging Protocol": 25, "Preparation & QC": 15,
             "Supply & Logistics": 10, "Adverse Event": 10, "Clinical Data": 5}
order = ["Imaging Protocol", "Preparation & QC", "Dosing", "Supply & Logistics", "Adverse Event", "Clinical Data"]
colors = {"Imaging Protocol": "#1f77b4", "Preparation & QC": "#ff7f0e", "Dosing": "#2ca02c",
          "Supply & Logistics": "#d62728", "Adverse Event": "#9467bd", "Clinical Data": "#8c564b"}

def pie(cx, cy, r, data, title):
    total = sum(data.values())
    out = [f'<text x="{cx}" y="{cy - r - 30}" text-anchor="middle" font-size="22" font-weight="bold">{title}</text>']
    a0 = -math.pi / 2
    for k in order:
        v = data.get(k, 0)
        if not v:
            continue
        frac = v / total
        a1 = a0 + 2 * math.pi * frac
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        large = 1 if frac > 0.5 else 0
        out.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large},1 {x1:.1f},{y1:.1f} Z" fill="{colors[k]}" stroke="white" stroke-width="2"/>')
        am = (a0 + a1) / 2
        lx, ly = cx + 0.65 * r * math.cos(am), cy + 0.65 * r * math.sin(am)
        out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="16" fill="white" font-weight="bold">{frac*100:.1f}%</text>')
        a0 = a1
    return "\n".join(out)

W, H = 1200, 640
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif">',
       '<rect width="100%" height="100%" fill="white"/>',
       f'<text x="{W/2}" y="40" text-anchor="middle" font-size="26" font-weight="bold">Medical Information Enquiries by Category - Q1 2026 (fictional workshop data)</text>',
       pie(300, 340, 200, perceived, "Perceived (Medical Affairs survey)"),
       pie(760, 340, 200, actual, "Actual (Q1 2026 enquiry log, n=25)")]
ly = 160
for k in order:
    svg.append(f'<rect x="1000" y="{ly}" width="22" height="22" fill="{colors[k]}"/>')
    svg.append(f'<text x="1032" y="{ly + 17}" font-size="17">{k.replace("&", "&amp;")}</text>')
    ly += 36
svg.append("</svg>")
with open(os.path.join(OUT, "pie_chart_enquiry_categories.svg"), "w") as fh:
    fh.write("\n".join(svg))

# Print stats for the docs
print("Sites:", len(site_rows))
tot_t = sum(r[12] for r in site_rows); tot_a = sum(r[13] for r in site_rows)
tot_s = sum(r[15] for r in site_rows); tot_sf = sum(r[16] for r in site_rows)
print(f"Target {tot_t}, Actual {tot_a} ({tot_a/tot_t:.1%}), Screened {tot_s}, ScreenFail {tot_sf} ({tot_sf/tot_s:.1%})")
for st in STUDIES:
    rs = [r for r in site_rows if r[1] == st]
    print(f"  {st}: sites {len(rs)}, target {sum(r[12] for r in rs)}, actual {sum(r[13] for r in rs)}")
print("Enquiries:", len(enq_rows))
for k in order:
    print(f"  {k}: actual {actual[k]} ({actual[k]/25:.1%}) vs perceived {perceived[k]}%")
closed = [e for e in enquiries if e[9] == "Closed"]
print(f"  Status: {Counter(e[9] for e in enquiries)}; avg response (closed) {sum(e[10] for e in closed)/len(closed):.1f} h; high priority {sum(1 for e in enquiries if e[8]=='High')}")
print("  By programme:", Counter(e[4] for e in enquiries))
print("  By requester:", Counter(e[2] for e in enquiries))
print("Feedback:", len(fb_rows))
