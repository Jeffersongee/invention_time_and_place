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

# ── Aggregate stats for the donut + bar charts ───────────────────────────────
cats = {}
for r in records:
    c = r["category"]
    if c not in cats:
        cats[c] = {"ALIGNED": 0, "MISMATCH": 0, "Flag": 0}
    gf = r["geographic_flag"]
    if gf in cats[c]:
        cats[c][gf] += 1

# Gap bucket counts (exclude Flag rows)
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

cats_json = json.dumps(cats)
gap_json  = json.dumps(gap_buckets)

# Counts for headline cards
n_aligned  = sum(1 for r in records if r["geographic_flag"] == "ALIGNED")
n_mismatch = sum(1 for r in records if r["geographic_flag"] == "MISMATCH")
n_flag     = sum(1 for r in records if r["geographic_flag"] == "Flag")
n_total    = len(records)

mismatches = [r for r in records if r["geographic_flag"] == "MISMATCH"]
mismatch_cards_html = ""
for r in mismatches:
    note = r["geographic_note"].replace("<", "&lt;").replace(">", "&gt;")
    loc  = r["actual_location"].replace("<", "&lt;").replace(">", "&gt;")
    pl   = r["possible_locations"].replace("<", "&lt;").replace(">", "&gt;")
    mismatch_cards_html += f"""
      <div class="mcard">
        <div class="mcard-year">{r['year']}</div>
        <div class="mcard-name">{r['invention']}</div>
        <div class="mcard-row"><span class="label-actual">Actual&nbsp;location</span><span>{loc}</span></div>
        <div class="mcard-row"><span class="label-possible">Plausible&nbsp;locations</span><span>{pl}</span></div>
        <div class="mcard-note">{note}</div>
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
  a{{color:var(--accent);text-decoration:none}}

  /* ── layout ── */
  header{{background:#1a2638;color:#fff;padding:28px 36px 0}}
  header h1{{font-size:1.8rem;font-weight:700;margin-bottom:4px}}
  header p{{opacity:.7;font-size:.95rem;max-width:600px;margin-bottom:18px}}
  .tabs{{display:flex;gap:0}}
  .tab{{padding:10px 22px;cursor:pointer;border-radius:6px 6px 0 0;font-size:.85rem;font-weight:600;opacity:.6;transition:.15s;border:none;background:none;color:#fff}}
  .tab.active{{background:var(--bg);color:var(--text);opacity:1}}
  .tab:hover:not(.active){{opacity:.9}}
  main{{padding:28px 36px;max-width:1280px;margin:0 auto}}
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
  .chart-row.three{{grid-template-columns:1fr 1fr 1fr}}
  .chart-box{{background:var(--card);border-radius:10px;padding:20px;border:1px solid var(--border)}}
  .chart-box h3{{font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--subtext);margin-bottom:14px}}
  .chart-box canvas{{max-height:300px}}

  /* ── geo section ── */
  .geo-intro{{background:var(--card);border-radius:10px;padding:20px 24px;border:1px solid var(--border);margin-bottom:20px;line-height:1.7}}
  .geo-intro strong{{color:var(--mismatch)}}

  .mismatch-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;margin-top:20px}}
  .mcard{{background:var(--card);border-radius:10px;border:2px solid #f5b7b1;padding:16px 18px}}
  .mcard-year{{font-size:.75rem;font-weight:700;color:var(--subtext);margin-bottom:2px}}
  .mcard-name{{font-size:1rem;font-weight:700;color:var(--text);margin-bottom:10px}}
  .mcard-row{{display:flex;gap:8px;align-items:baseline;margin-bottom:6px;font-size:.82rem}}
  .label-actual{{background:#fdecea;color:var(--mismatch);padding:1px 7px;border-radius:4px;font-weight:600;white-space:nowrap;flex-shrink:0}}
  .label-possible{{background:#eaf4fb;color:var(--accent);padding:1px 7px;border-radius:4px;font-weight:600;white-space:nowrap;flex-shrink:0}}
  .mcard-note{{font-size:.78rem;color:var(--subtext);margin-top:8px;padding-top:8px;border-top:1px solid var(--border);line-height:1.5}}

  /* ── gap scatter ── */
  .gap-intro{{background:var(--card);border-radius:10px;padding:20px 24px;border:1px solid var(--border);margin-bottom:20px;line-height:1.7}}
  #scatterWrap{{background:var(--card);border-radius:10px;padding:20px;border:1px solid var(--border)}}
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
  <p>Systematic analysis of 190 key inventions (1800–1969): earliest plausible dates, geographic alignment, and historical gaps between what was possible and what occurred.</p>
  <nav class="tabs">
    <button class="tab active" onclick="showTab('overview',this)">Overview</button>
    <button class="tab" onclick="showTab('geo',this)">Geographic Analysis</button>
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
    <p>For each invention, we ask: given the technology available at the earliest plausible date, <em>where could it have been invented?</em>
    We then compare that to where it <em>actually</em> was invented.
    <strong>ALIGNED</strong> means the actual location was among the plausible set. <strong>MISMATCH</strong> means history placed the invention somewhere that wasn't the most likely set of locations — a geographic counterfactual.</p>
    <p style="margin-top:10px"><strong>{n_mismatch}</strong> of the {n_total} inventions are mismatches — <strong>{n_mismatch/n_total*100:.0f}%</strong>.
    The cards below detail each case.</p>
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

  <h2 style="font-size:1rem;font-weight:700;margin:24px 0 10px;text-transform:uppercase;letter-spacing:.06em;color:var(--subtext)">
    Geographic Mismatch Cases ({n_mismatch})
  </h2>
  <div class="mismatch-grid">
    {mismatch_cards_html}
  </div>
</section>

<!-- ══════════════════════════════════════════════════════════════════════════
     TIME GAPS
═══════════════════════════════════════════════════════════════════════════ -->
<section id="sec-gaps">
  <div class="gap-intro">
    <p><strong>Gap</strong> = year actually invented − earliest plausible year. A gap of 50 means the invention could have existed 50 years earlier than it did. Flagged inventions (discoveries, social systems) are excluded.</p>
    <p style="margin-top:8px">Hover over a point to see the invention. <span style="display:inline-block;width:10px;height:10px;background:var(--aligned);border-radius:50%"></span> Aligned &nbsp;
    <span style="display:inline-block;width:10px;height:10px;background:var(--mismatch);border-radius:50%"></span> Mismatch</p>
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
// ── Data ────────────────────────────────────────────────────────────────────
const DATA = {js_data};
const CATS_DATA = {cats_json};
const GAP_DATA = {gap_json};

// ── Tab navigation ───────────────────────────────────────────────────────────
function showTab(id, btn) {{
  document.querySelectorAll('section').forEach(s => s.classList.remove('visible'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById('sec-' + id).classList.add('visible');
  btn.classList.add('active');
  if (id === 'table' && !tableInit) initTable();
  if (id === 'gaps' && !gapsInit) initGaps();
}}

// ── Colour helpers ───────────────────────────────────────────────────────────
const C = {{
  ALIGNED:  '#27ae60',
  MISMATCH: '#e74c3c',
  Flag:     '#95a5a6',
  Mechanical:'#3498db',
  Chemical:  '#9b59b6',
  Electrical:'#f39c12',
  Electronic:'#16a085',
  Medical:   '#e91e63',
  Other:     '#78909c',
  '':        '#bdc3c7',
}};
const ALPHA = (hex,a)=>hex+''+Math.round(a*255).toString(16).padStart(2,'0');

// ── Overview charts ──────────────────────────────────────────────────────────
const aligned  = DATA.filter(d=>d.geographic_flag==='ALIGNED').length;
const mismatch = DATA.filter(d=>d.geographic_flag==='MISMATCH').length;
const flagged  = DATA.filter(d=>d.geographic_flag==='Flag').length;

new Chart(document.getElementById('donutChart'), {{
  type:'doughnut',
  data:{{
    labels:['Aligned ('+aligned+')','Mismatch ('+mismatch+')','Flagged ('+flagged+')'],
    datasets:[{{data:[aligned,mismatch,flagged],backgroundColor:[C.ALIGNED,C.MISMATCH,C.Flag],borderWidth:2}}]
  }},
  options:{{plugins:{{legend:{{position:'bottom'}}}}}}
}});

const gapLabels = Object.keys(GAP_DATA);
new Chart(document.getElementById('gapBarChart'), {{
  type:'bar',
  data:{{
    labels:gapLabels,
    datasets:[{{label:'# inventions',data:Object.values(GAP_DATA),backgroundColor:gapLabels.map((_,i)=>
      `hsl(${{200 + i*15}},65%,55%)`),borderRadius:4}}]
  }},
  options:{{plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true,ticks:{{stepSize:5}}}}}}}}
}});

const catOrder = ['Mechanical','Chemical','Electrical','Electronic','Medical','Other',''];
const catLabels = catOrder.filter(c => CATS_DATA[c]);
new Chart(document.getElementById('catChart'), {{
  type:'bar',
  data:{{
    labels:catLabels,
    datasets:[
      {{label:'Aligned',  data:catLabels.map(c=>(CATS_DATA[c]||{{}}).ALIGNED||0),  backgroundColor:ALPHA(C.ALIGNED,.8),borderRadius:3}},
      {{label:'Mismatch', data:catLabels.map(c=>(CATS_DATA[c]||{{}}).MISMATCH||0), backgroundColor:ALPHA(C.MISMATCH,.8),borderRadius:3}},
      {{label:'Flagged',  data:catLabels.map(c=>(CATS_DATA[c]||{{}}).Flag||0),     backgroundColor:ALPHA(C.Flag,.8),borderRadius:3}},
    ]
  }},
  options:{{plugins:{{legend:{{position:'bottom'}}}},scales:{{x:{{stacked:true}},y:{{stacked:true,beginAtZero:true}}}}}}
}});

// ── Geo tab charts ───────────────────────────────────────────────────────────
new Chart(document.getElementById('donutChart2'), {{
  type:'doughnut',
  data:{{
    labels:['Aligned ('+aligned+')','Mismatch ('+mismatch+')','Flagged ('+flagged+')'],
    datasets:[{{data:[aligned,mismatch,flagged],backgroundColor:[C.ALIGNED,C.MISMATCH,C.Flag],borderWidth:2}}]
  }},
  options:{{plugins:{{legend:{{position:'bottom'}}}}}}
}});

new Chart(document.getElementById('missCatChart'), {{
  type:'bar',
  data:{{
    labels:catLabels,
    datasets:[{{
      label:'Mismatches',
      data:catLabels.map(c=>(CATS_DATA[c]||{{}}).MISMATCH||0),
      backgroundColor:ALPHA(C.MISMATCH,.8),borderRadius:4
    }}]
  }},
  options:{{
    indexAxis:'y',
    plugins:{{legend:{{display:false}}}},
    scales:{{x:{{beginAtZero:true,ticks:{{stepSize:1}}}}}}
  }}
}});

// ── Gap / Scatter charts ─────────────────────────────────────────────────────
let gapsInit = false;
function initGaps() {{
  gapsInit = true;
  const pts = DATA
    .filter(d=>d.gap!==null && d.geographic_flag!=='Flag')
    .map(d=>({{x:+d.year,y:d.gap,label:d.invention,flag:d.geographic_flag}}));

  new Chart(document.getElementById('scatterChart'), {{
    type:'scatter',
    data:{{
      datasets:[
        {{label:'Aligned', data:pts.filter(p=>p.flag==='ALIGNED'),
          backgroundColor:ALPHA(C.ALIGNED,.65),borderColor:C.ALIGNED,
          pointRadius:5,pointHoverRadius:8}},
        {{label:'Mismatch',data:pts.filter(p=>p.flag==='MISMATCH'),
          backgroundColor:ALPHA(C.MISMATCH,.75),borderColor:C.MISMATCH,
          pointRadius:6,pointHoverRadius:9}},
      ]
    }},
    options:{{
      plugins:{{
        legend:{{position:'bottom'}},
        tooltip:{{callbacks:{{
          title: items => items[0].raw.label,
          label: item => `Year: ${{item.raw.x}}, Gap: ${{item.raw.y}} yrs`
        }}}}
      }},
      scales:{{
        x:{{title:{{display:true,text:'Year of invention'}},min:1795,max:1975}},
        y:{{title:{{display:true,text:'Gap (years earlier it could have been)'}},beginAtZero:true}}
      }}
    }}
  }});

  // Top 20 gaps
  const top20 = [...DATA]
    .filter(d=>d.gap!==null)
    .sort((a,b)=>b.gap-a.gap)
    .slice(0,20);

  new Chart(document.getElementById('topGapChart'), {{
    type:'bar',
    data:{{
      labels:top20.map(d=>d.invention.length>28?d.invention.slice(0,26)+'…':d.invention),
      datasets:[{{
        label:'Gap (years)',
        data:top20.map(d=>d.gap),
        backgroundColor:top20.map(d=>ALPHA(C[d.geographic_flag],.8)),
        borderRadius:3
      }}]
    }},
    options:{{
      indexAxis:'y',
      plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{
        title:items=>top20[items[0].dataIndex].invention,
        label:i=>'Gap: '+i.raw+' years'
      }}}}}},
      scales:{{x:{{beginAtZero:true}}}}
    }}
  }});

  new Chart(document.getElementById('gapBarChart2'), {{
    type:'bar',
    data:{{
      labels:Object.keys(GAP_DATA),
      datasets:[{{label:'# inventions',data:Object.values(GAP_DATA),
        backgroundColor:Object.keys(GAP_DATA).map((_,i)=>`hsl(${{200+i*15}},65%,55%)`),borderRadius:4}}]
    }},
    options:{{plugins:{{legend:{{display:false}}}},scales:{{y:{{beginAtZero:true}}}}}}
  }});
}}

// ── Table ────────────────────────────────────────────────────────────────────
let tableInit = false, sortKey='year', sortAsc=true;
let flagFilter='ALL', catFilter='ALL';

function toggleFilter(btn, type, val) {{
  const grp = document.getElementById(type+'Filter');
  grp.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  if (type==='flag') flagFilter=val; else catFilter=val;
  renderTable();
}}

function sortTable(key) {{
  if (sortKey===key) sortAsc=!sortAsc; else {{ sortKey=key; sortAsc=true; }}
  document.querySelectorAll('[id^="arr-"]').forEach(el=>el.textContent='↕');
  document.getElementById('arr-'+key).textContent=sortAsc?'↑':'↓';
  renderTable();
}}

function badgeFlag(f) {{
  if (f==='ALIGNED')  return '<span class="badge badge-aligned">ALIGNED</span>';
  if (f==='MISMATCH') return '<span class="badge badge-mismatch">MISMATCH</span>';
  return '<span class="badge badge-flag">FLAG</span>';
}}
function badgeConf(c) {{
  if (c==='High')   return '<span class="badge badge-high">High</span>';
  if (c==='Medium') return '<span class="badge badge-medium">Medium</span>';
  if (c==='Low')    return '<span class="badge badge-low">Low</span>';
  return '<span class="badge badge-flag">Flag</span>';
}}

function esc(s) {{
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}}

function renderTable() {{
  const q = document.getElementById('searchBox').value.toLowerCase();
  let rows = DATA.filter(d=>{{
    if (flagFilter!=='ALL' && d.geographic_flag!==flagFilter) return false;
    if (catFilter!=='ALL' && d.category!==catFilter) return false;
    if (q && !JSON.stringify(d).toLowerCase().includes(q)) return false;
    return true;
  }});

  rows.sort((a,b)=>{{
    let va = a[sortKey], vb = b[sortKey];
    if (va===null||va===undefined) va=-Infinity;
    if (vb===null||vb===undefined) vb=-Infinity;
    if (va<vb) return sortAsc?-1:1;
    if (va>vb) return sortAsc?1:-1;
    return 0;
  }});

  document.getElementById('rowCount').textContent = rows.length + ' of ' + DATA.length + ' inventions';

  const tbody = document.getElementById('tableBody');
  tbody.innerHTML = rows.map((d,i)=>{{
    const id='r'+i;
    return `<tr id="${{id}}">
      <td>${{d.year}}</td>
      <td style="font-weight:600">${{esc(d.invention)}}</td>
      <td>${{esc(d.category)}}</td>
      <td>${{esc(d.earliest_plausible)}}</td>
      <td style="font-variant-numeric:tabular-nums">${{d.gap!==null?d.gap:'—'}}</td>
      <td>${{badgeFlag(d.geographic_flag)}}</td>
      <td>${{badgeConf(d.confidence)}}</td>
      <td><button class="expand-btn" onclick="toggleDetail('${{id}}',this)" data-idx="${{DATA.indexOf(d)}}">▶ detail</button></td>
    </tr>`;
  }}).join('');
}}

function toggleDetail(rowId, btn) {{
  const existing = document.getElementById('detail-'+rowId);
  if (existing) {{ existing.remove(); btn.textContent='▶ detail'; return; }}
  btn.textContent='▼ close';
  const row = document.getElementById(rowId);
  const d = DATA[+btn.dataset.idx];
  const tr = document.createElement('tr');
  tr.id = 'detail-'+rowId;
  tr.className = 'detail-row';
  const lines = (d.full_text||'').split('\\n').map(l=>esc(l));
  tr.innerHTML = `<td colspan="8"><strong>Inventor:</strong> ${{esc(d.inventor)}}<br>
<strong>Actual location:</strong> ${{esc(d.actual_location)}}<br>
<strong>Possible locations:</strong> ${{esc(d.possible_locations)}}<br>
<strong>Geographic note:</strong> ${{esc(d.geographic_note)}}<br><br>
<strong>Full Analysis:</strong><br>${{lines.join('<br>')}}</td>`;
  row.after(tr);
}}

function initTable() {{
  tableInit = true;
  renderTable();
}}
</script>
</body>
</html>
"""

with open("invention_analysis.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Wrote invention_analysis.html ({len(html):,} bytes, {len(html.split(chr(10)))} lines)")
