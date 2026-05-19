#!/usr/bin/env python3
"""Generate invention_analysis.html from analysis_checkpoint.jsonl."""
import json, re

# ── Load and prepare data ────────────────────────────────────────────────────
with open("analysis_checkpoint.jsonl", "r") as f:
    raw = [json.loads(l) for l in f]

def parse_ep(ep):
    if not ep or ep == "Flag": return None
    m = re.search(r"(\d{3,4})", ep)
    return int(m.group(1)) if m else None

records = []
for e in raw:
    ep_year = parse_ep(e.get("earliest_plausible", ""))
    actual = e.get("year")
    gap = (int(actual) - ep_year) if (actual and ep_year) else None
    records.append({
        "invention": e["invention"],
        "year": actual,
        "inventor": e.get("inventor", ""),
        "category": e.get("category", "") or "Other",
        "earliest_plausible": e.get("earliest_plausible", ""),
        "earliest_straightforward": e.get("earliest_straightforward", ""),
        "ep_year": ep_year,
        "gap": gap,
        "actual_location": e.get("actual_location", ""),
        "possible_locations": e.get("possible_locations", ""),
        "geographic_flag": e.get("geographic_flag", ""),
        "geographic_note": e.get("geographic_note", ""),
        "confidence": e.get("confidence", ""),
        "full_text": e.get("full_text", ""),
    })

js_data = json.dumps(records, ensure_ascii=False)

# ── Aggregates ───────────────────────────────────────────────────────────────
cats = {}
for r in records:
    c = r["category"]
    if c not in cats:
        cats[c] = {"ALIGNED": 0, "MISMATCH": 0, "Flag": 0}
    gf = r["geographic_flag"]
    if gf in cats[c]:
        cats[c][gf] += 1

gap_buckets = {"0–10": 0, "11–25": 0, "26–50": 0, "51–100": 0, "101–250": 0, "251–500": 0, "500+": 0}
for r in records:
    g = r["gap"]
    if g is None: continue
    if   g <= 10:  gap_buckets["0–10"]    += 1
    elif g <= 25:  gap_buckets["11–25"]   += 1
    elif g <= 50:  gap_buckets["26–50"]   += 1
    elif g <= 100: gap_buckets["51–100"]  += 1
    elif g <= 250: gap_buckets["101–250"] += 1
    elif g <= 500: gap_buckets["251–500"] += 1
    else:          gap_buckets["500+"]    += 1

cats_json    = json.dumps(cats)
gap_json     = json.dumps(gap_buckets)
n_aligned    = sum(1 for r in records if r["geographic_flag"] == "ALIGNED")
n_mismatch   = sum(1 for r in records if r["geographic_flag"] == "MISMATCH")
n_flag       = sum(1 for r in records if r["geographic_flag"] == "Flag")
n_total      = len(records)
mismatches   = [r for r in records if r["geographic_flag"] == "MISMATCH"]

# ── MISMATCH categories for "Factors" tab ───────────────────────────────────
# Each case assigned a factor category with a brief driving explanation.
MISMATCH_FACTORS = {
    "General anaesthetic":
        ("Independent tradition",
         "Seishu Hanaoka synthesized a plant-based anaesthetic from Japanese/Chinese herbal pharmacology — an entirely independent path from Western ether chemistry. The knowledge base was different, not just the location."),
    "Commercial steamboat":
        ("Local demand pull",
         "The Hudson River offered a uniquely profitable route with no road alternative. The US's geography of long navigable rivers and scarce roads made the commercial case more urgent than in Britain or France, where canals already existed."),
    "Stethoscope":
        ("Specialised institution",
         "The Paris Clinical School concentrated an unprecedented density of hospital beds and systematic pathological anatomy, giving Laennec both the patients and the culture of close physical examination needed to recognise the device's value. No equivalent institutional context existed at the formally 'plausible' ancient medical centres."),
    "Pattern-tracing lathe":
        ("State/military commissioning",
         "The US Army's specific mandate to achieve interchangeable-parts manufacture at Springfield Armory — and Thomas Blanchard's employment there — concentrated demand for a copying mechanism that European craftsmen had no institutional reason to pursue at the same moment."),
    "Braile Tactile alphabet":
        ("Specialised institution",
         "Louis Braille was a student and later teacher at the Paris Institution Nationale des Jeunes Aveugles — a pioneering specialised school whose existence (a product of Enlightenment social policy) created both the user community and the motivated inventor in one place."),
    "Morse Code":
        ("Chronological mismatch",
         "Any literate civilisation with a standardised alphabet could have produced a dot-dash substitution cipher. The actual 1837 US invention reflects when someone happened to pursue it, not a binding technical constraint; a motivated scholar in Han China or Renaissance Europe could equally have done it."),
    "Wood-pulp paper":
        ("Chronological mismatch",
         "Song China (1100–1300) had water-powered mills, abrasive grindstones, and papermaking expertise simultaneously — all prerequisites. The 1844 German/Canadian realisations are independent industrial-era re-discoveries of a solution that history had already reached, then lost."),
    "Hypodermic needle":
        ("Peripheral genius",
         "Dr. Francis Rynd in Dublin had the clinical problem (administering morphine to a neuralgia patient) and the practical dexterity to fashion a hollow trocar, but Dublin was secondary to London, Paris, and Amsterdam as an instrument-making centre. His specific clinical need drove a solution the major hubs had not yet bothered to pursue."),
    "Pin-tumbler cylinder lock":
        ("American invention culture",
         "Linus Yale Jr. worked in a US patent culture that incentivised incremental mechanical refinement. European clockmakers and locksmiths had the precision metalworking capability earlier but lacked the same economic pressure to commoditise domestic security hardware."),
    "Safety pin":
        ("American invention culture",
         "Walter Hunt invented the safety pin in New York in a single afternoon, driven partly by the need to pay off a $15 debt by selling the patent. The device's components (spring wire, catch) were standard European metalwork for decades; the US patent economy created a specific incentive to reduce and commercialise."),
    "Vapour-compression ice machine":
        ("Local demand pull",
         "James Harrison in Geelong, Australia faced acute demand for mechanical refrigeration in a hot climate with no natural ice supply — a much sharper need than in temperate industrial Britain, which still had ice-houses and winter ice harvesting. The extremity of the local problem motivated the solution."),
    "Barbed wire":
        ("Local demand pull",
         "The American prairie presented millions of acres of unfenced farmland with no timber for rails and no stone for walls. The specific combination of iron wire availability (from the East) and vast unenclosed land (of the Midwest) created an invention context with no European equivalent at the time."),
    "Electric tram":
        ("Peripheral genius",
         "Fyodor Pirottsky was a Russian military engineer with a specific interest in electric traction, operating in Saint Petersburg where an academic electrical culture (Jacobi, Lenz) had taken root independently of Western industry. He had the theoretical background but lacked the machine-shop infrastructure of Berlin or Birmingham."),
    "Phonograph":
        ("American invention culture",
         "Edison's Menlo Park embodied a new institutional form — the industrial research laboratory — that had no precise European equivalent yet. The phonograph emerged not despite being in New Jersey rather than Paris, but because Edison's factory-of-invention model could iterate on tinfoil-cylinder mechanics faster than any European atelier."),
    "Ballpoint pen":
        ("Chronological mismatch",
         "A precise metal ball seated in a viscous-ink reservoir is well within Renaissance Italian or German clockmaking capability. John Loud's 1888 US patent reflects a period when patent activity was high and mechanical tinkering was rewarded, not a binding technical breakthrough unavailable to Nuremberg artisans three centuries earlier."),
    "Zipper":
        ("American invention culture",
         "Whitcomb Judson's 1891 Chicago patent reflects the US patent system's reward for mechanical combination, not a technical capability gap. Swiss watch-part makers or German Saxony weavers had the requisite fine metalworking — the invention required an institutional context that valued locking-clasp novelty as patentable."),
    "Electric oven":
        ("Peripheral genius",
         "Thomas Ahearn in Ottawa was an electrical entrepreneur who had personally built Ottawa's streetcar and lighting systems, giving him both access to the grid and a practical motive to showcase electric heating. The major European and US cities had grid power first, but Ahearn had unique local opportunity and ownership of the supply."),
    "First self-sustaining gas turbine":
        ("Peripheral genius",
         "Ægidius Elling in Norway was an independent inventor who had studied engineering in Berlin and returned to Christiania to work alone. His success reflected sustained personal obsession rather than institutional backing; the UK, Germany, and France had better-resourced teams who paradoxically produced less because they were less willing to iterate on unproven designs."),
    "Yagi-Uda directional antenna":
        ("Peripheral genius",
         "Hidetsugu Yagi and Shintaro Uda at Tohoku University worked in a world-class academic engineering department that Japan had built through deliberate Meiji-era investment in technical education. They had full access to Hertzian electromagnetics but sat outside the dense RF-experimentation networks of Marconi's Europe, giving them an independent perspective on directional arrays."),
    "Phase-contrast microscopy":
        ("Peripheral genius",
         "Frits Zernike at Groningen was studying diffraction gratings for metrology when he recognised that the same phase-shift mathematics applied to transparent specimens in a microscope. The Zeiss Jena optical industry — the expected location — had both the manufacturing capability and the user base but had not made the conceptual link. Zernike's peripheral position meant he encountered the problem with fresh eyes."),
    "Defibrilator":
        ("State/military commissioning",
         "N.L. Gurvich conducted sustained state-funded research at the All-Union Institute of Experimental Medicine in Moscow, motivated by Soviet interest in resuscitation physiology. The Western prerequisite literature (Prevost-Batelli 1899, Einthoven ECG 1903) was fully available, but no comparable directed programme existed in the West until later."),
    "Bertie the Brain (interactive electronic game)":
        ("Peripheral genius",
         "Josef Kates built Bertie as a showpiece for the 1950 Canadian National Exhibition in Toronto. His engineering background (University of Vienna, then wartime radar work in Canada) gave him the relay-logic skills; the CNE context gave him the unusual institutional motivation to build an interactive public game. No equivalent public-demonstration culture existed in the UK or US relay-computing world at that moment."),
}

FACTOR_COLORS = {
    "Peripheral genius":          "#8e44ad",
    "Local demand pull":          "#2980b9",
    "Specialised institution":    "#16a085",
    "State/military commissioning":"#c0392b",
    "American invention culture": "#e67e22",
    "Independent tradition":      "#27ae60",
    "Chronological mismatch":     "#7f8c8d",
}

# ── Build mismatch card HTML for geo tab ────────────────────────────────────
def mismatch_card(r, show_factor=False):
    note   = r["geographic_note"].replace("<","&lt;").replace(">","&gt;")
    loc    = r["actual_location"].replace("<","&lt;").replace(">","&gt;")
    pl     = r["possible_locations"].replace("<","&lt;").replace(">","&gt;")
    factor_html = ""
    if show_factor:
        fc, _ = MISMATCH_FACTORS.get(r["invention"], ("", ""))
        col   = FACTOR_COLORS.get(fc, "#aaa")
        factor_html = f'<div class="mcard-factor" style="background:{col}20;color:{col};border-color:{col}40">{fc}</div>'
    return f"""
      <div class="mcard">
        <div class="mcard-year">{r['year']}</div>
        <div class="mcard-name">{r['invention']}</div>
        {factor_html}
        <div class="mcard-row"><span class="label-actual">Actual</span><span>{loc}</span></div>
        <div class="mcard-row"><span class="label-possible">Plausible</span><span>{pl}</span></div>
        <div class="mcard-note">{note}</div>
      </div>"""

mismatch_cards_geo   = "".join(mismatch_card(r, show_factor=False) for r in mismatches)

# ── Factor counts for chart ──────────────────────────────────────────────────
factor_counts = {}
for inv, (fc, _) in MISMATCH_FACTORS.items():
    factor_counts[fc] = factor_counts.get(fc, 0) + 1
fc_labels  = json.dumps(list(factor_counts.keys()))
fc_values  = json.dumps(list(factor_counts.values()))
fc_colors  = json.dumps([FACTOR_COLORS.get(k,"#aaa") for k in factor_counts.keys()])

# ── Build factor section cards ───────────────────────────────────────────────
# Group MISMATCH cases by factor
from collections import defaultdict
factor_groups = defaultdict(list)
for r in mismatches:
    fc, explanation = MISMATCH_FACTORS.get(r["invention"], ("Other",""))
    factor_groups[fc].append((r, explanation))

def factor_section(fc, cases):
    col   = FACTOR_COLORS.get(fc, "#aaa")
    cards = ""
    for r, explanation in cases:
        inv  = r["invention"].replace("<","&lt;").replace(">","&gt;")
        yr   = r["year"]
        loc  = r["actual_location"].replace("<","&lt;").replace(">","&gt;")
        expl = explanation.replace("<","&lt;").replace(">","&gt;")
        cards += f"""<div class="fc-case">
          <div class="fc-case-title"><span class="fc-year">{yr}</span> {inv}</div>
          <div class="fc-case-loc">{loc}</div>
          <div class="fc-case-expl">{expl}</div>
        </div>"""
    return f"""<div class="factor-block" style="--fc:{col}">
      <div class="factor-header">
        <span class="factor-dot" style="background:{col}"></span>
        <span class="factor-name">{fc}</span>
        <span class="factor-count">{len(cases)}</span>
      </div>
      <div class="fc-cases">{cards}</div>
    </div>"""

divergence_sections = "".join(
    factor_section(fc, cases)
    for fc, cases in sorted(factor_groups.items(), key=lambda x: -len(x[1]))
)

# ── ALIGNED factor examples (curated) ────────────────────────────────────────
CONCENTRATION_FACTORS = [
    {
        "name": "Industrial ecosystem effects",
        "color": "#2980b9",
        "icon": "⚙",
        "body": """When a region accumulated the prerequisite supply chains, skilled workers, and tacit knowledge for one generation of technology, follow-on inventions arose there almost automatically. Birmingham's metalworking ecosystem produced a cascade of mechanical inventions: the steam engine, precision screws, and standardised fasteners all reinforced each other. Germany's Liebig school of organic chemistry made that country the natural birthplace of aspirin, synthetic dyes, and early plastics. The San Francisco Bay Area's accumulation of silicon crystal growers, vacuum deposition specialists, and photolithography expertise after the transistor made it the only plausible location for the integrated circuit and MOSFET within a decade of the transistor itself.""",
        "examples": ["Bessemer process (Sheffield)", "Aspirin, Sulfa drugs (Germany — Liebig school)", "Integrated circuit, MOSFET (Bell Labs / Silicon Valley ecosystem)"]
    },
    {
        "name": "Institutional concentration",
        "color": "#8e44ad",
        "icon": "🏛",
        "body": """Corporate research laboratories and elite universities concentrated expertise, equipment, and institutional culture in ways that made them disproportionate generators of invention. Bell Labs produced the transistor (1947), the solar photovoltaic cell (1954), the MOSFET (1959), and the theoretical laser proposal (1958) — all in roughly the same building and the same decade — because it had co-located the right physicists, chemists, and engineers with unlimited access to precision fabrication. Germany's Technische Hochschulen and research universities similarly dominated 19th-century chemistry. Institutional concentration meant that once one invention succeeded, the people most likely to recognise and exploit its implications were already present.""",
        "examples": ["Transistor, Solar PV, MOSFET (Bell Labs)", "Aspirin, Novocaine, Buna-S synthetic rubber (German university labs)", "Logic Theorist, early AI (CMU / Princeton IAS)"]
    },
    {
        "name": "Prior invention advantage",
        "color": "#16a085",
        "icon": "🔗",
        "body": """The inventors of one generation's technology best understood its implications and the specific obstacles in the next step. The Peenemünde V-2 team — captured by both the US and USSR in 1945 — was the most natural origin of orbital rocketry because they had already solved the hardest turbopump and guidance problems. Charles Townes' maser team at Columbia was the most likely group to build a laser because they had already internalised stimulated emission engineering. The Bell Labs team that developed thermal SiO₂ passivation in 1957 was the same team that immediately recognised its application to the MOSFET. This 'adjacent possible' effect strongly favoured geographic continuity.""",
        "examples": ["Sputnik (from captured V-2 expertise in USSR and USA)", "First laser (from Townes' maser group, Columbia / Hughes)", "MOSFET (from Frosch-Derick SiO₂ team at Bell Labs)"]
    },
    {
        "name": "State and military demand",
        "color": "#c0392b",
        "icon": "🏛",
        "body": """Government procurement concentrated inventions in locations with strong state-industrial relationships. The US and UK defence establishments effectively created entire new technology sectors by commissioning research at specific institutions. Radar emerged primarily at the UK's Telecommunications Research Establishment and MIT Rad Lab because government contracts concentrated the relevant RF engineers there. Early digital computing clustered at Penn (ENIAC), MIT (Whirlwind), and the IAS (von Neumann architecture) because of military funding. The effect was not just to accelerate invention but to determine where it happened: institutions with government contracts attracted talent and equipment that made them the obvious locus for follow-on work.""",
        "examples": ["Radar (UK TRE, MIT Rad Lab)", "ENIAC, early computing (Penn, MIT — US military funding)", "Atomic bomb → nuclear physics cluster at Los Alamos / Livermore"]
    },
    {
        "name": "Commercial network proximity",
        "color": "#e67e22",
        "icon": "📦",
        "body": """Inventions tied to specific industries tended to occur near those industries' customers, suppliers, and capital. The shipping container was invented in the United States because it had the world's largest domestic freight market and the most acute intermodal bottleneck. Float glass emerged from Pilkington's existing glass manufacturing infrastructure in the UK — proximity to the production problem drove the solution. The hard disk drive was developed at IBM's San Jose laboratory because San Jose was adjacent to the manufacturing and commercial operations that needed high-capacity storage. Market proximity meant inventors had both the feedback and the funding to iterate efficiently.""",
        "examples": ["Shipping container (USA — dominant freight market)", "Float glass (UK Pilkington — existing glass manufacturing)", "Hard disk drive (IBM San Jose — co-located with commercial need)"]
    },
]

concentration_html = ""
for f in CONCENTRATION_FACTORS:
    examples_html = "".join(f"<li>{e}</li>" for e in f["examples"])
    concentration_html += f"""<div class="cf-block" style="--cf:{f['color']}">
      <div class="cf-name"><span class="cf-icon">{f['icon']}</span>{f['name']}</div>
      <div class="cf-body">{f['body']}</div>
      <div class="cf-examples"><strong>Examples from the dataset:</strong><ul>{examples_html}</ul></div>
    </div>"""

# ── Write HTML ───────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>When Could It Have Been? — 190 Invention Analysis</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
<style>
  :root {{
    --aligned: #27ae60;
    --mismatch: #e74c3c;
    --flagged: #95a5a6;
    --bg: #f5f6fa;
    --card: #ffffff;
    --text: #2c3e50;
    --subtext: #7f8c8d;
    --border: #dde1e7;
    --accent: #2980b9;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);font-size:14px;line-height:1.5}}

  /* ── layout ── */
  header{{background:#1a2638;color:#fff;padding:28px 36px 0}}
  header h1{{font-size:1.8rem;font-weight:700;margin-bottom:4px}}
  header p{{opacity:.7;font-size:.95rem;max-width:640px;margin-bottom:18px}}
  .tabs{{display:flex;gap:0}}
  .tab{{padding:10px 20px;cursor:pointer;border-radius:6px 6px 0 0;font-size:.82rem;font-weight:600;opacity:.6;transition:.15s;border:none;background:none;color:#fff}}
  .tab.active{{background:var(--bg);color:var(--text);opacity:1}}
  .tab:hover:not(.active){{opacity:.9}}
  main{{padding:28px 36px;max-width:1320px;margin:0 auto}}
  section{{display:none}}
  section.visible{{display:block}}

  /* ── stat cards ── */
  .stat-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:28px}}
  .stat{{background:var(--card);border-radius:10px;padding:20px 22px;border:1px solid var(--border)}}
  .stat .num{{font-size:2.4rem;font-weight:700;line-height:1}}
  .stat .lbl{{font-size:.8rem;color:var(--subtext);margin-top:4px;text-transform:uppercase;letter-spacing:.05em}}
  .stat.aligned .num{{color:var(--aligned)}}
  .stat.mismatch .num{{color:var(--mismatch)}}
  .stat.flagged  .num{{color:var(--flagged)}}

  /* ── chart grids ── */
  .chart-row{{display:grid;gap:16px;margin-bottom:28px}}
  .chart-row.two{{grid-template-columns:1fr 1fr}}
  .chart-box{{background:var(--card);border-radius:10px;padding:20px;border:1px solid var(--border)}}
  .chart-box h3{{font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--subtext);margin-bottom:14px}}
  .chart-box canvas{{max-height:300px}}

  /* ── geo + mismatch cards ── */
  .geo-intro,.gap-intro,.factors-intro{{background:var(--card);border-radius:10px;padding:20px 24px;border:1px solid var(--border);margin-bottom:24px;line-height:1.75}}
  .geo-intro strong{{color:var(--mismatch)}}
  .section-h2{{font-size:.9rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--subtext);margin:28px 0 12px}}

  .mismatch-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;margin-top:4px}}
  .mcard{{background:var(--card);border-radius:10px;border:2px solid #f5b7b1;padding:16px 18px}}
  .mcard-year{{font-size:.72rem;font-weight:700;color:var(--subtext);margin-bottom:2px}}
  .mcard-name{{font-size:.95rem;font-weight:700;color:var(--text);margin-bottom:8px}}
  .mcard-factor{{display:inline-block;font-size:.72rem;font-weight:700;padding:2px 9px;border-radius:12px;border:1px solid;margin-bottom:8px}}
  .mcard-row{{display:flex;gap:8px;align-items:baseline;margin-bottom:5px;font-size:.8rem}}
  .label-actual{{background:#fdecea;color:var(--mismatch);padding:1px 7px;border-radius:4px;font-weight:600;white-space:nowrap;flex-shrink:0;font-size:.72rem}}
  .label-possible{{background:#eaf4fb;color:var(--accent);padding:1px 7px;border-radius:4px;font-weight:600;white-space:nowrap;flex-shrink:0;font-size:.72rem}}
  .mcard-note{{font-size:.77rem;color:var(--subtext);margin-top:8px;padding-top:8px;border-top:1px solid var(--border);line-height:1.5}}

  /* ── concentration factors ── */
  .cf-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px}}
  .cf-block{{background:var(--card);border-radius:10px;border:1px solid var(--border);border-left:4px solid var(--cf);padding:20px 22px}}
  .cf-name{{font-size:1rem;font-weight:700;margin-bottom:10px;display:flex;align-items:center;gap:8px}}
  .cf-icon{{font-size:1.2rem}}
  .cf-body{{font-size:.85rem;line-height:1.7;color:#444;margin-bottom:12px}}
  .cf-examples{{font-size:.8rem;color:var(--subtext)}}
  .cf-examples ul{{margin-top:4px;padding-left:18px}}
  .cf-examples li{{margin-bottom:2px}}

  /* ── divergence / factor blocks ── */
  .factor-grid{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
  .factor-block{{background:var(--card);border-radius:10px;border:1px solid var(--border);border-left:4px solid var(--fc);padding:18px 20px}}
  .factor-header{{display:flex;align-items:center;gap:10px;margin-bottom:14px}}
  .factor-dot{{width:10px;height:10px;border-radius:50%;flex-shrink:0}}
  .factor-name{{font-size:.9rem;font-weight:700;flex:1}}
  .factor-count{{background:var(--bg);border:1px solid var(--border);border-radius:12px;padding:1px 10px;font-size:.78rem;font-weight:600;color:var(--subtext)}}
  .fc-cases{{display:flex;flex-direction:column;gap:10px}}
  .fc-case{{background:#f9fafb;border-radius:7px;padding:10px 12px;border:1px solid var(--border)}}
  .fc-case-title{{font-size:.85rem;font-weight:600;margin-bottom:2px}}
  .fc-year{{font-size:.75rem;font-weight:700;color:var(--subtext);margin-right:6px}}
  .fc-case-loc{{font-size:.75rem;color:var(--subtext);margin-bottom:5px}}
  .fc-case-expl{{font-size:.8rem;color:#555;line-height:1.55}}

  /* ── gap scatter ── */
  #scatterWrap canvas{{max-height:500px}}

  /* ── table ── */
  .table-controls{{display:flex;gap:12px;margin-bottom:14px;flex-wrap:wrap;align-items:center}}
  .table-controls input{{flex:1;min-width:180px;padding:8px 12px;border:1px solid var(--border);border-radius:8px;font-size:.85rem;outline:none}}
  .table-controls input:focus{{border-color:var(--accent)}}
  .filter-group{{display:flex;gap:6px;flex-wrap:wrap}}
  .filter-btn{{padding:5px 12px;border-radius:16px;border:1px solid var(--border);background:var(--card);font-size:.78rem;cursor:pointer;transition:.12s}}
  .filter-btn.active{{background:var(--accent);color:#fff;border-color:var(--accent)}}
  .tbl-wrap{{overflow-x:auto;border-radius:10px;border:1px solid var(--border)}}
  table{{width:100%;border-collapse:collapse;background:var(--card)}}
  th{{background:#eef0f4;font-size:.75rem;text-transform:uppercase;letter-spacing:.05em;padding:10px 12px;text-align:left;cursor:pointer;user-select:none;white-space:nowrap;border-bottom:1px solid var(--border)}}
  th:hover{{background:#e2e6ed}}
  td{{padding:9px 12px;border-bottom:1px solid #eef0f4;font-size:.82rem;vertical-align:top;max-width:260px}}
  tr:hover td{{background:#f9fafb}}
  .badge{{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.72rem;font-weight:600}}
  .badge-aligned{{background:#d5f5e3;color:#1e8449}}
  .badge-mismatch{{background:#fdecea;color:#c0392b}}
  .badge-flag{{background:#f2f3f4;color:#717d7e}}
  .badge-high{{background:#d6eaf8;color:#1a5276}}
  .badge-medium{{background:#fef9e7;color:#7d6608}}
  .badge-low{{background:#fdedec;color:#922b21}}
  .expand-btn{{background:none;border:none;cursor:pointer;color:var(--accent);font-size:.78rem;padding:0}}
  .detail-row td{{background:#f9fafb;font-size:.8rem;color:var(--subtext);white-space:pre-wrap;line-height:1.6;padding:14px 20px;border-bottom:1px solid var(--border)}}
  .detail-row td strong{{color:var(--text)}}
  .sort-arrow{{opacity:.4;margin-left:3px}}
  .row-count{{font-size:.8rem;color:var(--subtext)}}
</style>
</head>
<body>

<header>
  <h1>When Could It Have Been?</h1>
  <p>Systematic analysis of 190 key inventions (1800–1969): earliest plausible dates, geographic alignment, and the factors that determined where each invention actually occurred.</p>
  <nav class="tabs">
    <button class="tab active" onclick="showTab('overview',this)">Overview</button>
    <button class="tab" onclick="showTab('geo',this)">Geographic Analysis</button>
    <button class="tab" onclick="showTab('factors',this)">Geographic Factors</button>
    <button class="tab" onclick="showTab('gaps',this)">Time Gaps</button>
    <button class="tab" onclick="showTab('table',this)">Full Table</button>
  </nav>
</header>

<main>

<!-- ══════════════════════════════════════════════════════════════════════════
     OVERVIEW
═══════════════════════════════════════════════════════════════════════════ -->
<section id="sec-overview" class="visible">
  <div class="stat-row">
    <div class="stat"><div class="num">{n_total}</div><div class="lbl">Inventions analysed</div></div>
    <div class="stat aligned"><div class="num">{n_aligned}</div><div class="lbl">Geographically aligned</div></div>
    <div class="stat mismatch"><div class="num">{n_mismatch}</div><div class="lbl">Geographic mismatches</div></div>
    <div class="stat flagged"><div class="num">{n_flag}</div><div class="lbl">Flagged (phenomenon/social)</div></div>
  </div>
  <div class="chart-row two">
    <div class="chart-box">
      <h3>Geographic Alignment</h3>
      <canvas id="donutChart"></canvas>
    </div>
    <div class="chart-box">
      <h3>Gap Distribution (years invention could have been earlier)</h3>
      <canvas id="gapBarChart"></canvas>
    </div>
  </div>
  <div class="chart-row">
    <div class="chart-box">
      <h3>Alignment by Category</h3>
      <canvas id="catChart"></canvas>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════════════════════════════════════
     GEOGRAPHIC ANALYSIS
═══════════════════════════════════════════════════════════════════════════ -->
<section id="sec-geo">
  <div class="geo-intro">
    <p>For each invention we ask: given available technology at the earliest plausible date, <em>where could it have been invented?</em> We then compare that set to where it <em>actually</em> was invented.
    <strong>ALIGNED</strong> means the actual location was among the plausible set. <strong>MISMATCH</strong> means history placed the invention somewhere that wasn't in the expected cluster.</p>
    <p style="margin-top:10px"><strong>{n_mismatch}</strong> of {n_total} inventions are mismatches — <strong>{n_mismatch/n_total*100:.0f}%</strong>. The cards below detail each case. See the <em>Geographic Factors</em> tab for an analysis of what drove these divergences.</p>
  </div>
  <div class="chart-row two">
    <div class="chart-box">
      <h3>Alignment Breakdown</h3>
      <canvas id="donutChart2"></canvas>
    </div>
    <div class="chart-box">
      <h3>Mismatches per Category</h3>
      <canvas id="missCatChart"></canvas>
    </div>
  </div>
  <div class="section-h2">Geographic Mismatch Cases ({n_mismatch})</div>
  <div class="mismatch-grid">{mismatch_cards_geo}</div>
</section>

<!-- ══════════════════════════════════════════════════════════════════════════
     GEOGRAPHIC FACTORS
═══════════════════════════════════════════════════════════════════════════ -->
<section id="sec-factors">
  <div class="factors-intro">
    <p>Two questions sit at the heart of the geographic analysis: <strong>what kept most inventions in predictable locations?</strong> and <strong>what pulled the exceptions somewhere else?</strong>
    The {n_aligned} aligned cases reveal five recurring forces that concentrated invention in expected centres.
    The {n_mismatch} mismatch cases resolve into six distinct drivers, each representing a different way that history departed from the path a purely capability-based forecast would have predicted.</p>
  </div>

  <!-- Part A: concentration factors -->
  <div class="section-h2">Part A — What kept inventions in predictable locations ({n_aligned} aligned cases)</div>
  <div class="cf-grid">
    {concentration_html}
  </div>

  <!-- Part B: divergence factors -->
  <div class="section-h2">Part B — What drew inventions to unexpected locations ({n_mismatch} mismatch cases)</div>
  <div class="chart-row two" style="margin-bottom:20px">
    <div class="chart-box">
      <h3>Mismatch cases by driving factor</h3>
      <canvas id="fcBarChart" style="max-height:260px"></canvas>
    </div>
    <div class="chart-box" style="font-size:.85rem;line-height:1.75;color:#444;padding:22px 24px">
      <h3 style="margin-bottom:12px">Reading the categories</h3>
      <p><strong>Peripheral genius</strong> — a capable individual happened to be working outside the main capability cluster, driven by personal circumstance, migration, or an institution that existed independently of the Western industrial mainstream.</p>
      <p style="margin-top:10px"><strong>American invention culture</strong> — the US patent system rewarded incremental mechanical recombination and commoditisation of existing craft, pulling inventions to the US even when European workshops had the underlying capability first.</p>
      <p style="margin-top:10px"><strong>Chronological mismatch</strong> — inventions where the binding constraint was social/motivational rather than technical; any capable civilisation at the actual date could have done it, and many earlier ones could have too.</p>
    </div>
  </div>
  <div class="factor-grid">
    {divergence_sections}
  </div>
</section>

<!-- ══════════════════════════════════════════════════════════════════════════
     TIME GAPS
═══════════════════════════════════════════════════════════════════════════ -->
<section id="sec-gaps">
  <div class="gap-intro">
    <p><strong>Gap</strong> = year actually invented − earliest plausible year. A gap of 50 means the invention could have existed 50 years before it did. Flagged inventions (phenomena, social systems) are excluded.</p>
    <p style="margin-top:8px">
      <span style="display:inline-block;width:10px;height:10px;background:var(--aligned);border-radius:50%;vertical-align:middle"></span> Aligned &nbsp;
      <span style="display:inline-block;width:10px;height:10px;background:var(--mismatch);border-radius:50%;vertical-align:middle"></span> Mismatch — hover a point for details.</p>
  </div>
  <div class="chart-row two">
    <div class="chart-box" style="grid-column:1/-1">
      <h3>Actual Year vs. Gap (how many years earlier it could have been)</h3>
      <canvas id="scatterChart" style="max-height:440px"></canvas>
    </div>
  </div>
  <div class="chart-row two">
    <div class="chart-box">
      <h3>Top 20 Largest Gaps</h3>
      <canvas id="topGapChart"></canvas>
    </div>
    <div class="chart-box">
      <h3>Gap Distribution</h3>
      <canvas id="gapBarChart2"></canvas>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════════════════════════════════════
     FULL TABLE
═══════════════════════════════════════════════════════════════════════════ -->
<section id="sec-table">
  <div class="table-controls">
    <input type="search" id="searchBox" placeholder="Search inventions, inventors, locations…" oninput="renderTable()">
    <div class="filter-group" id="flagFilter">
      <button class="filter-btn active" onclick="toggleFilter(this,'flag','ALL')" data-val="ALL">All</button>
      <button class="filter-btn" onclick="toggleFilter(this,'flag','ALIGNED')" data-val="ALIGNED">Aligned</button>
      <button class="filter-btn" onclick="toggleFilter(this,'flag','MISMATCH')" data-val="MISMATCH">Mismatch</button>
      <button class="filter-btn" onclick="toggleFilter(this,'flag','Flag')" data-val="Flag">Flagged</button>
    </div>
    <div class="filter-group" id="catFilter">
      <button class="filter-btn active" onclick="toggleFilter(this,'cat','ALL')" data-val="ALL">All categories</button>
      <button class="filter-btn" onclick="toggleFilter(this,'cat','Mechanical')" data-val="Mechanical">Mechanical</button>
      <button class="filter-btn" onclick="toggleFilter(this,'cat','Chemical')" data-val="Chemical">Chemical</button>
      <button class="filter-btn" onclick="toggleFilter(this,'cat','Electrical')" data-val="Electrical">Electrical</button>
      <button class="filter-btn" onclick="toggleFilter(this,'cat','Electronic')" data-val="Electronic">Electronic</button>
      <button class="filter-btn" onclick="toggleFilter(this,'cat','Medical')" data-val="Medical">Medical</button>
      <button class="filter-btn" onclick="toggleFilter(this,'cat','Other')" data-val="Other">Other</button>
    </div>
    <span class="row-count" id="rowCount"></span>
  </div>
  <div class="tbl-wrap">
    <table id="mainTable">
      <thead>
        <tr>
          <th onclick="sortTable('year')">Year<span class="sort-arrow" id="arr-year">↕</span></th>
          <th onclick="sortTable('invention')">Invention<span class="sort-arrow" id="arr-invention">↕</span></th>
          <th onclick="sortTable('category')">Category<span class="sort-arrow" id="arr-category">↕</span></th>
          <th onclick="sortTable('earliest_plausible')">Earliest Plausible<span class="sort-arrow" id="arr-earliest_plausible">↕</span></th>
          <th onclick="sortTable('gap')">Gap (yrs)<span class="sort-arrow" id="arr-gap">↕</span></th>
          <th onclick="sortTable('geographic_flag')">Geo Flag<span class="sort-arrow" id="arr-geographic_flag">↕</span></th>
          <th onclick="sortTable('confidence')">Confidence<span class="sort-arrow" id="arr-confidence">↕</span></th>
          <th>Detail</th>
        </tr>
      </thead>
      <tbody id="tableBody"></tbody>
    </table>
  </div>
</section>

</main>

<script>
const DATA     = {js_data};
const CATS_DATA= {cats_json};
const GAP_DATA = {gap_json};
const FC_LABELS= {fc_labels};
const FC_VALUES= {fc_values};
const FC_COLORS= {fc_colors};

// ── Tab navigation ───────────────────────────────────────────────────────────
function showTab(id, btn) {{
  document.querySelectorAll('section').forEach(s => s.classList.remove('visible'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('sec-' + id).classList.add('visible');
  btn.classList.add('active');
  if (id === 'table'   && !tableInit) initTable();
  if (id === 'gaps'    && !gapsInit)  initGaps();
  if (id === 'factors' && !factorsInit) initFactors();
}}

// ── Colour helpers ───────────────────────────────────────────────────────────
const C = {{
  ALIGNED:'#27ae60', MISMATCH:'#e74c3c', Flag:'#95a5a6',
  Mechanical:'#3498db', Chemical:'#9b59b6', Electrical:'#f39c12',
  Electronic:'#16a085', Medical:'#e91e63', Other:'#78909c', ''  :'#bdc3c7',
}};
const alpha = (h,a) => h + Math.round(a*255).toString(16).padStart(2,'0');
const aligned  = DATA.filter(d=>d.geographic_flag==='ALIGNED').length;
const mismatch = DATA.filter(d=>d.geographic_flag==='MISMATCH').length;
const flagged  = DATA.filter(d=>d.geographic_flag==='Flag').length;

// ── Overview charts ──────────────────────────────────────────────────────────
new Chart(document.getElementById('donutChart'), {{
  type:'doughnut',
  data:{{ labels:['Aligned ('+aligned+')','Mismatch ('+mismatch+')','Flagged ('+flagged+')'],
          datasets:[{{data:[aligned,mismatch,flagged],backgroundColor:[C.ALIGNED,C.MISMATCH,C.Flag],borderWidth:2}}] }},
  options:{{ plugins:{{ legend:{{position:'bottom'}} }} }}
}});

const gapLabels = Object.keys(GAP_DATA);
new Chart(document.getElementById('gapBarChart'), {{
  type:'bar',
  data:{{ labels:gapLabels,
          datasets:[{{label:'# inventions',data:Object.values(GAP_DATA),
            backgroundColor:gapLabels.map((_,i)=>`hsl(${{200+i*15}},65%,55%)`),borderRadius:4}}] }},
  options:{{ plugins:{{legend:{{display:false}}}}, scales:{{y:{{beginAtZero:true,ticks:{{stepSize:5}}}}}} }}
}});

const catOrder = ['Mechanical','Chemical','Electrical','Electronic','Medical','Other',''];
const catLabels = catOrder.filter(c=>CATS_DATA[c]);
new Chart(document.getElementById('catChart'), {{
  type:'bar',
  data:{{ labels:catLabels,
    datasets:[
      {{label:'Aligned', data:catLabels.map(c=>(CATS_DATA[c]||{{}}).ALIGNED||0), backgroundColor:alpha(C.ALIGNED,.8),borderRadius:3}},
      {{label:'Mismatch',data:catLabels.map(c=>(CATS_DATA[c]||{{}}).MISMATCH||0),backgroundColor:alpha(C.MISMATCH,.8),borderRadius:3}},
      {{label:'Flagged', data:catLabels.map(c=>(CATS_DATA[c]||{{}}).Flag||0),    backgroundColor:alpha(C.Flag,.8),borderRadius:3}},
    ] }},
  options:{{ plugins:{{legend:{{position:'bottom'}}}}, scales:{{x:{{stacked:true}},y:{{stacked:true,beginAtZero:true}}}} }}
}});

// ── Geo tab ──────────────────────────────────────────────────────────────────
new Chart(document.getElementById('donutChart2'), {{
  type:'doughnut',
  data:{{ labels:['Aligned ('+aligned+')','Mismatch ('+mismatch+')','Flagged ('+flagged+')'],
          datasets:[{{data:[aligned,mismatch,flagged],backgroundColor:[C.ALIGNED,C.MISMATCH,C.Flag],borderWidth:2}}] }},
  options:{{ plugins:{{legend:{{position:'bottom'}}}} }}
}});
new Chart(document.getElementById('missCatChart'), {{
  type:'bar',
  data:{{ labels:catLabels,
    datasets:[{{label:'Mismatches',data:catLabels.map(c=>(CATS_DATA[c]||{{}}).MISMATCH||0),
      backgroundColor:alpha(C.MISMATCH,.8),borderRadius:4}}] }},
  options:{{ indexAxis:'y', plugins:{{legend:{{display:false}}}}, scales:{{x:{{beginAtZero:true,ticks:{{stepSize:1}}}}}} }}
}});

// ── Factors tab ──────────────────────────────────────────────────────────────
let factorsInit = false;
function initFactors() {{
  factorsInit = true;
  new Chart(document.getElementById('fcBarChart'), {{
    type:'bar',
    data:{{ labels:FC_LABELS,
      datasets:[{{label:'Cases',data:FC_VALUES,backgroundColor:FC_COLORS,borderRadius:4}}] }},
    options:{{ indexAxis:'y', plugins:{{legend:{{display:false}}}}, scales:{{x:{{beginAtZero:true,ticks:{{stepSize:1}}}}}} }}
  }});
}}

// ── Gap / Scatter ────────────────────────────────────────────────────────────
let gapsInit = false;
function initGaps() {{
  gapsInit = true;
  const pts = DATA.filter(d=>d.gap!==null&&d.geographic_flag!=='Flag')
                  .map(d=>(({{x:+d.year,y:d.gap,label:d.invention,flag:d.geographic_flag}})));

  new Chart(document.getElementById('scatterChart'), {{
    type:'scatter',
    data:{{ datasets:[
      {{label:'Aligned', data:pts.filter(p=>p.flag==='ALIGNED'),
        backgroundColor:alpha(C.ALIGNED,.65),borderColor:C.ALIGNED,pointRadius:5,pointHoverRadius:8}},
      {{label:'Mismatch',data:pts.filter(p=>p.flag==='MISMATCH'),
        backgroundColor:alpha(C.MISMATCH,.75),borderColor:C.MISMATCH,pointRadius:6,pointHoverRadius:9}},
    ] }},
    options:{{ plugins:{{legend:{{position:'bottom'}},
      tooltip:{{callbacks:{{title:i=>i[0].raw.label,label:i=>`Year: ${{i.raw.x}}, Gap: ${{i.raw.y}} yrs`}}}} }},
      scales:{{ x:{{title:{{display:true,text:'Year of invention'}},min:1795,max:1975}},
                y:{{title:{{display:true,text:'Gap (years earlier it could have been)'}},beginAtZero:true}} }} }}
  }});

  const top20 = [...DATA].filter(d=>d.gap!==null).sort((a,b)=>b.gap-a.gap).slice(0,20);
  new Chart(document.getElementById('topGapChart'), {{
    type:'bar',
    data:{{ labels:top20.map(d=>d.invention.length>28?d.invention.slice(0,26)+'…':d.invention),
      datasets:[{{label:'Gap (years)',data:top20.map(d=>d.gap),
        backgroundColor:top20.map(d=>alpha(C[d.geographic_flag],.8)),borderRadius:3}}] }},
    options:{{ indexAxis:'y',
      plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{title:i=>top20[i[0].dataIndex].invention,label:i=>'Gap: '+i.raw+' years'}}}}}},
      scales:{{x:{{beginAtZero:true}}}} }}
  }});
  new Chart(document.getElementById('gapBarChart2'), {{
    type:'bar',
    data:{{ labels:Object.keys(GAP_DATA),
      datasets:[{{label:'# inventions',data:Object.values(GAP_DATA),
        backgroundColor:Object.keys(GAP_DATA).map((_,i)=>`hsl(${{200+i*15}},65%,55%)`),borderRadius:4}}] }},
    options:{{ plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true}}}} }}
  }});
}}

// ── Table ────────────────────────────────────────────────────────────────────
let tableInit=false, sortKey='year', sortAsc=true, flagFilter='ALL', catFilter='ALL';

function toggleFilter(btn,type,val){{
  document.getElementById(type+'Filter').querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  if(type==='flag') flagFilter=val; else catFilter=val;
  renderTable();
}}
function sortTable(key){{
  if(sortKey===key) sortAsc=!sortAsc; else {{sortKey=key;sortAsc=true;}}
  document.querySelectorAll('[id^="arr-"]').forEach(e=>e.textContent='↕');
  document.getElementById('arr-'+key).textContent=sortAsc?'↑':'↓';
  renderTable();
}}
function badgeFlag(f){{
  if(f==='ALIGNED')  return '<span class="badge badge-aligned">ALIGNED</span>';
  if(f==='MISMATCH') return '<span class="badge badge-mismatch">MISMATCH</span>';
  return '<span class="badge badge-flag">FLAG</span>';
}}
function badgeConf(c){{
  const m={{'High':'badge-high','Medium':'badge-medium','Low':'badge-low'}};
  return `<span class="badge ${{m[c]||'badge-flag'}}">${{c}}</span>`;
}}
function esc(s){{return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}}

function renderTable(){{
  const q=document.getElementById('searchBox').value.toLowerCase();
  let rows=DATA.filter(d=>{{
    if(flagFilter!=='ALL'&&d.geographic_flag!==flagFilter) return false;
    if(catFilter!=='ALL'&&d.category!==catFilter) return false;
    if(q&&!JSON.stringify(d).toLowerCase().includes(q)) return false;
    return true;
  }});
  rows.sort((a,b)=>{{
    let va=a[sortKey],vb=b[sortKey];
    if(va==null) va=-Infinity; if(vb==null) vb=-Infinity;
    return sortAsc?(va<vb?-1:va>vb?1:0):(va>vb?-1:va<vb?1:0);
  }});
  document.getElementById('rowCount').textContent=rows.length+' of '+DATA.length+' inventions';
  document.getElementById('tableBody').innerHTML=rows.map((d,i)=>{{
    const id='r'+i;
    return `<tr id="${{id}}">
      <td>${{d.year}}</td>
      <td style="font-weight:600">${{esc(d.invention)}}</td>
      <td>${{esc(d.category)}}</td>
      <td>${{esc(d.earliest_plausible)}}</td>
      <td style="font-variant-numeric:tabular-nums">${{d.gap!=null?d.gap:'—'}}</td>
      <td>${{badgeFlag(d.geographic_flag)}}</td>
      <td>${{badgeConf(d.confidence)}}</td>
      <td><button class="expand-btn" onclick="toggleDetail('${{id}}',this)" data-idx="${{DATA.indexOf(d)}}">▶ detail</button></td>
    </tr>`;
  }}).join('');
}}

function toggleDetail(rowId,btn){{
  const ex=document.getElementById('detail-'+rowId);
  if(ex){{ex.remove();btn.textContent='▶ detail';return;}}
  btn.textContent='▼ close';
  const d=DATA[+btn.dataset.idx];
  const tr=document.createElement('tr');
  tr.id='detail-'+rowId; tr.className='detail-row';
  const lines=(d.full_text||'').split('\\n').map(l=>esc(l));
  tr.innerHTML=`<td colspan="8"><strong>Inventor:</strong> ${{esc(d.inventor)}}<br>
<strong>Actual location:</strong> ${{esc(d.actual_location)}}<br>
<strong>Possible locations:</strong> ${{esc(d.possible_locations)}}<br>
<strong>Geographic note:</strong> ${{esc(d.geographic_note)}}<br><br>
<strong>Full Analysis:</strong><br>${{lines.join('<br>')}}</td>`;
  document.getElementById(rowId).after(tr);
}}

function initTable(){{tableInit=true;renderTable();}}
</script>
</body>
</html>
"""

with open("invention_analysis.html","w",encoding="utf-8") as f:
    f.write(html)

print(f"Wrote invention_analysis.html ({len(html):,} bytes)")
