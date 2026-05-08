INVENTION DATING PROJECT — ORCHESTRATION PROMPT
I will provide you a CSV of ~190 inventions. For each invention, estimate how early it could plausibly have been invented, using the rubric below. You will orchestrate the work using parallel sub-agents and produce two output files.
================================================================
TASK SUMMARY
================================================================
For each invention in the input CSV, produce two date ranges:

Earliest plausible — earliest year a motivated team with one or two lucky guesses could have built it
Earliest straightforward — earliest year multiple independent teams would converge on it within a decade or two of being motivated
You will work through the inventions in batches of 7, spawning one sub-agent per invention IN PARALLEL within each batch (single tool-use message containing 7 Agent calls). After each batch, spawn a quality-check agent. When all batches are complete, produce two output files.
================================================================
INPUT
================================================================
The user will provide a CSV file with three columns: invention name, year actually invented, inventor. Read it from the path the user specifies (or from /uploads if attached).
================================================================
OUTPUTS
================================================================
Save both files to the workspace folder so the user can access them via computer:// links.
File 1: inventions_with_dates.csv

Preserve all original columns.
Append two new columns:
Earliest plausible — year range like "1820–1840", a single year like "1750", "antiquity", or "Flag" if the entry was flagged
Earliest straightforward — same format
Use UTF-8 encoding. Em-dashes are fine.
File 2: inventions_full_analysis.docx

One section per invention, in the order they appear in the input CSV.
Each section starts with a Heading 2 of the invention name.
Each section contains the full structured entry (year actually invented, both dates, confidence, prerequisite technologies, scientific theories, explanation).
USE THE docx SKILL — read its [SKILL.md](http://SKILL.md) file first before producing the document.
================================================================
PROCESS
================================================================

Read the input CSV. Print a confirmation: how many inventions, what the columns look like.
Group inventions into batches of 7. The last batch may be smaller.
For each batch:
Spawn 7 sub-agents in parallel — issue all 7 Agent tool calls in a SINGLE tool-use message — each with the per-invention prompt template below, filled in for one invention.
Wait for all 7 to return.
Spawn ONE quality-check agent with all 7 outputs.
For any entry the check agent says needs rework: re-spawn that single sub-agent ONCE with the check agent's specific concerns appended. Use the second result. Do not re-run more than once.
Append the validated entries to a running collection (in memory, e.g., a Python list).
After all batches:
Write the modified CSV.
Use the docx skill to write the full-analysis document.
Report the final summary to the user with computer:// links to both files.
Use the opus model for both per-invention agents and check agents — this is reasoning-heavy work.
================================================================
ESTIMATION RUBRIC (this is what every per-invention agent will use)
================================================================
WHAT YOU'RE DOING Estimate how much earlier each invention could plausibly have been invented within its own technological tradition, given the materials, tools, and knowledge available at the time. The list spans roughly 1800–1970 and is mostly Western, so "tradition" means the Western tradition reaching back as far as antiquity if the technology genuinely permits. For inventions outside the Western tradition, use the relevant tradition. Don't refuse to assign early dates just because they fall before some intuitive cutoff — if the prerequisites were genuinely in place in 200 BC, say so.
THE HYPOTHETICAL TEAM For each candidate year, imagine:

One motivated inventor whose explicit goal is to build this specific invention.
A workshop of HIGHLY-SKILLED artisans, technicians, or engineers appropriate to the candidate year — e.g., a top instrument-maker in 1750, a leading machinist in 1860, a senior electronics technician in 1955. Well above the typical practitioner, but not requiring once-in-a-generation talent.
Five years of focused project work.
Access to all knowledge and empirical findings published or otherwise established anywhere in the world by the candidate year.
Materials in lab/prototype quantities, not industrial scale. A working prototype is the goal.
THE TEAM ARE ENGINEERS AND ARTISANS, NOT SCIENTISTS. They iterate on the device they're trying to build. They do NOT conduct dedicated scientific experiments motivated by curiosity about underlying nature. This distinction is the most important rule in this prompt.
WHAT THE TEAM CAN DO

Use any technology already extant in the candidate year.
Use any empirical phenomenon, scientific observation, or theoretical result already published or established anywhere in the world by the candidate year.
Iterate empirically on the target invention itself, discovering whatever phenomena naturally emerge from that iteration. A workshop iterating on furnace design will notice that pre-heating the blast improves fuel efficiency. A workshop iterating on lamp filaments will notice that thinner wires reach incandescence at lower currents.
Build ONE LAYER of precursor technology themselves within the 5-year window, but only if that precursor is buildable from technology and knowledge already extant in the candidate year. NO CHAINED RECURSION.
WHAT THE TEAM CANNOT DO

Invent fundamentally new mathematical or scientific frameworks. Off-limits unless already established by the candidate year:
Maxwell's equations (formal electromagnetism)
Classical or statistical thermodynamics as formal theory
Germ theory of disease as theoretical framework
Modern atomic theory
Quantum mechanics, relativity
Modern organic / structural chemistry as formal theory
Solid-state / band theory of semiconductors (~1930s)
Theoretical computer science and computability (Turing, ~1936)
Information theory (Shannon, 1948)
Modern molecular biology (DNA structure 1953, central dogma, etc.)
Conduct dedicated scientific experiments establishing fundamental phenomena. THE TEST: would a competent engineer or artisan of the candidate year, focused on building a useful thing, set up this exact experiment? If only because they already suspected the result, treat the phenomenon as off-limits until its historical discovery. Off-limits phenomena (illustrative, not exhaustive):
Galvani / Volta animal-electricity observations — 1791 / 1800
Oersted's effect (current deflects a compass) — 1820
Seebeck / thermoelectricity — 1821
Faraday's electromagnetic rotation — 1821
Faraday's induction — 1831
Photovoltaic effect (Becquerel) — 1839
Piezoelectricity — 1880
Hertz / generation and detection of radio-frequency electromagnetic waves — 1887
Photoelectric effect — 1887
Radioactivity — 1896
Superconductivity — 1911
Nuclear fission — 1938 IMPORTANT: Static electricity (friction generation, Leyden jar effects, electrostatic conduction) is NOT on the off-limits list — known and worked with since antiquity, systematized from Gilbert (~1600). Treat as available freely.
Replicate serendipitous historical accidents on demand. If the historical invention hinged on an unforeseeable accident — Goodyear's stove, Roentgen's fluorescent screen, Fleming's petri dish, Perkin's mauve, the Curies and the photographic plate, Spencer's melted chocolate bar, Plunkett's Teflon — the team cannot be assumed to luck into the same accident. FLAG these rather than dating them.
DELIVERABLE: TWO DATE RANGES

Earliest plausible: motivated, insightful team with one or two lucky guesses going their way could produce a working version. Best-case but not miraculous.
Earliest straightforward: prerequisites widely enough available that multiple independent teams would converge within a decade or two of being motivated to try.

GEOGRAPHIC ANALYSIS
For each invention, also identify which locations around the world had the conditions needed to produce it at the earliest plausible date, and compare that to where the invention was actually made.

Actual location: Identify the country (and city if notable) where the invention was actually made. Use your knowledge or web search if needed.

Possible locations: At the earliest plausible date, which countries or cities had sufficient conditions that a motivated team there could have produced this invention? Evaluate each candidate location against:
- Industrial/manufacturing infrastructure appropriate to the invention (e.g., precision metalworking, glassblowing, chemical works)
- Access to prerequisite materials (locally produced or reliably imported)
- Scientific institutions and published knowledge available to practitioners (universities, academies, technical journals, instrument-makers' networks)
- Skilled labor pool: artisans, engineers, or technicians of the type required
- Economic demand or demonstrated cultural/institutional motivation for this class of innovation

List all plausible locations, not just the historically prominent ones. Be specific: name countries and, where the distinction matters, specific cities or regions (e.g., "Lancashire textile districts", "Paris instrument-making workshops", "Rhine industrial corridor").

Geographic flag: If the set of possible locations at the earliest plausible date is notably different from — or substantially broader or narrower than — the actual location of invention, note this explicitly. Examples of what to flag:
- "Multiple European industrial centers could have produced this; British origin was geographically contingent."
- "Only Britain had the prerequisite coal-iron-steam infrastructure at the earliest plausible date, making the actual origin unsurprising."
- "The actual inventor worked in the USA, but at the earliest plausible date (~1830) the required instrument-making capacity existed only in Paris and London."

OUTPUT FORMAT (per invention) — exact field names, blank line between entries:
Invention: <name> Year actually invented: <year> Earliest plausible: <year range> Earliest straightforward: <year range> Confidence: <Low | Medium | High | Flag>
Actual location: <country / city, country>
Possible locations at earliest plausible date: <comma-separated list of countries or cities>
Geographic note: <1–2 sentences: were the possible locations broadly similar to the actual location, or notably different? Highlight any surprising mismatches.>
Prerequisite technologies: For each item, list the historical date when it first became available and mark either:

external — must already be extant in the candidate year; team cannot produce it themselves
team-reachable — team can build it within the 5-year project window as their one allowed precursor
Scientific theories / key empirical observations: For each item, list the historical date and mark either:

external — team cannot discover this; must already be published/established by candidate year (includes off-limits frameworks/phenomena)
team-discoverable — phenomenon emerges naturally from project iteration on the target
Explanation: One paragraph (~3–6 sentences). Call out the binding item explicitly (latest-dated "external" item) and explain why other items are or aren't binding.
WHEN TO FLAG

Invention's identity is poorly defined.
Historical breakthrough required a serendipitous accident the team can't reasonably replicate.
Invention is fundamentally a new scientific framework rather than a buildable artifact (e.g., the discovery of a phenomenon).
Invention is fundamentally social, economic, or organizational.
Binding constraint is a phenomenon that required dedicated scientific investigation, and that discovery hadn't yet occurred by the candidate year.
Year actually invented is ambiguous.
A flagged entry includes Invention name, Year actually invented, Confidence: Flag, and a paragraph explaining the issue.
SANITY CHECKS

If "earliest plausible" is LATER than year actually invented, keep it and note that the historical inventor pushed the envelope.
If gap exceeds ~100 years, the Explanation must include at least one sentence on why it took so long historically.
WORKED EXAMPLES (study these — they calibrate the rubric)
Invention: Neilson's hot blast Year actually invented: 1828 Earliest plausible: 1400–1500 Earliest straightforward: 1700–1750 Confidence: Medium
Actual location: Scotland, UK
Possible locations at earliest plausible date: England, Belgium (Liège/Charleroi coal-iron region), German Rhineland, France (Lorraine), Scandinavia (Sweden's Bergslagen iron district)
Geographic note: By 1700–1750 the possible locations and the actual location (British Isles) are closely aligned — all the leading iron-producing regions of northwest Europe had equivalent furnace capacity. The British origin reflects Britain's early lead in iron output but is not uniquely determined; any of the continental iron districts could have produced this.
Prerequisite technologies:

True high-shaft blast furnace producing pig iron [14th–15th c. Europe] — external (the team cannot develop a true blast furnace from scratch in five years; required centuries of accumulated metallurgical and industrial development)
Ducting capable of carrying heated air, clay or iron [antiquity] — external, non-binding
Heat source for pre-heating the blast (bellows-blown fire, recovered furnace exhaust) [antiquity] — external, non-binding
Scientific theories / key empirical observations:

Insight that pre-heating combustion air improves fuel efficiency — team-discoverable via project iteration on furnace fuel efficiency
(No formal scientific framework required)
Explanation: Hot blast requires only that the air entering a working blast furnace be pre-heated. Ducting and heat-production long predate the blast furnace, and the efficiency insight falls naturally out of an ironmaster iterating on the furnace itself. The binding item is the true high-shaft blast furnace (14th–15th c.), since the team can't develop one from scratch in five years. The 400+ year gap to 1828 reflects conceptual non-obviousness — nobody happened to try.
Invention: Practical incandescent light bulb Year actually invented: 1879 Earliest plausible: 1825–1840 Earliest straightforward: 1865–1875 Confidence: Medium
Actual location: Menlo Park, New Jersey, USA (Edison); also independently Tyne and Wear, England (Swan)
Possible locations at earliest plausible date: England (London, Birmingham — leading centers of electrical instrument-making and glassblowing), France (Paris), Germany (Berlin), USA (east-coast workshop cities)
Geographic note: The possible locations and the actual locations broadly overlap — Britain and the northeastern USA were both plausible, and indeed both produced independent inventors (Swan and Edison). France and Germany were also within reach by the 1860s–1870s. The dual British/American origin is unsurprising; this was not geographically contingent on any single place.
Prerequisite technologies:

Sustained electrical current source: voltaic pile [1800], Daniell cell [1836] — external (battery existence depends on the off-limits voltaic effect)
High-vacuum pump: mercury barometer principle [Torricelli 1644]; Sprengel mercury pump [1865] — team-reachable (the team can iterate on the barometer/aspirator tradition to build a high-vacuum pump as their one allowed precursor)
Glass-blowing for bulb form [antiquity] — external, non-binding
Filament material: carbon, fine metal wire [ancient] — external, non-binding
Scientific theories / key empirical observations:

Voltaic effect [Galvani 1791 / Volta 1800] — external; off-limits phenomenon
Current heats fine conductors and produces visible incandescence [Davy and others, early 1800s] — external, established before any plausible candidate year for the bulb
Explanation: The genuine constraints are sustained current (off-limits before 1800) and a hard vacuum (team-reachable). The binding item is the voltaic pile at 1800. Glass, filaments, and Davy-era empirical knowledge of current-induced glow are all in place from the late 1820s. The historical 1879 date reflects much later commercial-grade vacuum pumps and filament refinement, neither of which is a fundamental block to a working prototype several decades earlier.
Invention: Laser (ruby laser, first practical demonstration) Year actually invented: 1960 Earliest plausible: 1930–1940 Earliest straightforward: 1950–1960 Confidence: Medium
Actual location: Hughes Research Laboratories, Malibu, California, USA
Possible locations at earliest plausible date: USA (major industrial research labs — Bell Labs, GE, RCA, university physics departments); Germany (Physikalisch-Technische Reichsanstalt, major university optics labs — Jena, Munich); Soviet Union (after ~1945, state optics institutes); UK (Cavendish, NPL) to a lesser degree
Geographic note: The actual location (USA) is among the most plausible but not uniquely so — German optics and physics labs of the 1930s had equivalent crystal-growth and optical-pumping capacity, and did produce foundational stimulated-emission theory (Einstein, in Berlin). The USA became the dominant site by the 1950s due to defense-funded research labs; the German collapse in WWII is the main reason a German team did not get there first.
Prerequisite technologies:

Synthetic single-crystal ruby (Verneuil flame-fusion process) [1902] — external (industrial crystal-growth process; not buildable in 5 years)
High-intensity pulsed optical pump (xenon flashlamp) [~1930s; underlying gas-discharge tubes and capacitor-discharge engineering, 19th c.] — team-reachable (buildable as the one allowed precursor)
Reflective end coatings (silvered for ruby) [18th–19th c.] — external, non-binding
Fabry-Perot resonator [1899] — external, non-binding
Scientific theories / key empirical observations:

Einstein's stimulated emission and population inversion, within the quantum theory of radiation [1917] — external; off-limits framework
Atomic spectra and energy levels [Bohr 1913; full quantum mechanics 1925–1927] — external Explanation: The laser is a clean framework-bound case. Most physical components were in place by the early 20th century, and the high-intensity pulsed pump is team-reachable from 19th-c. capacitor-discharge engineering. The binding item is Einstein's 1917 stimulated-emission framework: pre-1917 a team has no reason to suspect coherent light amplification is possible. With the framework available, a 1930s team could plausibly attempt a ruby laser. By the early 1950s, multiple teams converged within a decade. ================================================================ PER-INVENTION AGENT PROMPT TEMPLATE ================================================================ When spawning a sub-agent for a single invention, use this prompt with {NAME}, {YEAR}, {INVENTOR} filled in:
You are estimating the earliest plausible invention date for ONE invention. Apply the rubric below carefully and produce output in the exact specified format. Think hard before answering.

[INSERT FULL RUBRIC FROM ABOVE — copy the entire ESTIMATION RUBRIC section, including all three worked examples]

INVENTION TO EVALUATE:
- Name: {NAME}
- Year actually invented: {YEAR}
- Inventor: {INVENTOR}

You may use web search if you need to verify a specific date or technical fact, but rely on your judgment for the analytical work.

Return ONLY the structured entry in the exact format specified. No preamble, no postamble.
If a re-run is needed (because the check agent flagged the entry), append:


PRIOR ATTEMPT FAILED REVIEW. The check agent's specific concerns:
{CONCERNS}

Address these concerns directly. Produce a fresh entry that resolves them.
================================================================
CHECK AGENT PROMPT TEMPLATE
================================================================
When spawning a check agent for a batch:

You are reviewing a batch of invention-dating entries for quality and rubric adherence.

[INSERT FULL RUBRIC FROM ABOVE — copy the entire ESTIMATION RUBRIC section, including all three worked examples]

ENTRIES TO REVIEW (one per invention, blank line between):

[PASTE THE BATCH'S ENTRIES HERE]

For each entry, check:
1. FORMAT: all required fields present and in the right order; correct labels. This now includes: Actual location, Possible locations at earliest plausible date, and Geographic note.
2. INTERNAL CONSISTENCY: earliest plausible ≤ earliest straightforward (or both flagged); the binding item is identified in the Explanation; the Explanation references the prerequisites/observations listed.
3. RUBRIC ADHERENCE:
   - Off-limits phenomena are not assumed discoverable by the team. Especially watch for: Oersted's effect (1820), Faraday's induction (1831), photovoltaic effect (1839), photoelectric effect (1887), radioactivity (1896). If any of these are listed as "team-discoverable," that's an error.
   - Frameworks (Maxwell, thermodynamics, quantum mechanics, semiconductors, etc.) are not assumed available before their historical date.
   - Serendipitous accidents (Goodyear, Roentgen, Fleming, Perkin, Spencer, Plunkett) are flagged.
   - Inventions that are really phenomena-discoveries (e.g., "the photovoltaic effect," "electromagnetic induction") are flagged.
4. DATE SANITY: no obvious anachronisms. The "binding item" date should match the earliest-plausible lower bound.
5. SANITY-CHECK RULE: if the gap between actual-invented and earliest-plausible exceeds 100 years, the Explanation must include why it took so long historically.
6. GEOGRAPHIC ANALYSIS:
   - Actual location must be provided and plausible (flag if obviously wrong).
   - Possible locations must be grounded in the prerequisite infrastructure identified — if a prerequisite requires, say, precision chemical manufacturing, then only locations with that capacity should be listed.
   - The Geographic note must explicitly flag any meaningful mismatch between the possible locations and the actual location. A note that simply says "many places could have done this" without naming them, or that ignores a clear geographic mismatch, is insufficient.
   - Watch for geographic anachronisms: don't list a country as a possible location if the required infrastructure wasn't present there at the earliest plausible date (e.g., don't list the USA as a possible location for an invention whose earliest plausible date is 1650).

Output a brief report listing any entries that need rework, with specific concerns. Format:

REWORK NEEDED:
- {Invention name}: {specific concerns, 1-3 sentences}
- {...}

ALL OTHERS PASS.

If everything passes, just output: "ALL ENTRIES PASS."
================================================================
CSV WRITING
================================================================
When writing the output CSV:

Preserve the input column order and all original data exactly.
Append these columns at the end, in this order:
  1. Earliest plausible
  2. Earliest straightforward
  3. Actual location
  4. Possible locations
  5. Geographic flag — write "MISMATCH" if the possible locations differ notably from the actual location (i.e., the actual location was not the most likely or only plausible place); write "ALIGNED" if the actual location was among the most plausible or uniquely positioned; write "Flag" if the invention entry itself was flagged.
For flagged entries, write "Flag" in all five new columns.
For ranges, use en-dash format like "1820–1840" (en-dash, not hyphen).
For pre-CE dates, write like "antiquity" or "~700 BCE" or "~50 CE".
For Possible locations, separate multiple entries with semicolons (not commas, to avoid CSV parsing issues).
Use Python's csv module or pandas. Make sure the file is valid UTF-8.
================================================================
DOCX WRITING
================================================================
Before producing the docx, READ the docx skill's [SKILL.md](http://SKILL.md) file. Follow its guidance.
Document structure:

Title: "Earliest Plausible Invention Dates: Analysis"
Brief intro paragraph (1–2 sentences) explaining the document's purpose and pointing to the companion CSV.
One section per invention, in input-CSV order:
Heading 2: invention name
The full structured entry as plain paragraphs/lists (mirror the structured format we used in chat), including the Actual location, Possible locations, and Geographic note fields.
If the Geographic flag is "MISMATCH", bold the Geographic note so it stands out in the document.
Optional: a final "Summary" section noting how many inventions were flagged, how many had geographic mismatches (MISMATCH), and the total count.
================================================================
ORCHESTRATION DETAILS
================================================================

PARALLEL DISPATCH: when sending a batch of 7 sub-agents, issue all 7 Agent tool calls in a SINGLE tool-use message. The Cowork harness will run them concurrently. Do NOT issue them serially across messages.
Use TodoWrite or equivalent to track progress: one todo per batch, marked in_progress when the batch starts and completed when its check agent passes.
If any sub-agent returns an error or a malformed entry, treat that as "needs rework" and re-spawn once.
Maintain the running collection of validated entries in memory throughout.
================================================================
DELIVERABLE
================================================================
When done, send a single short message to the user with:

computer:// link to the CSV file.
computer:// link to the DOCX file.
A short summary: "Processed N inventions. M were flagged. G had geographic mismatches (actual location differed from most plausible locations). Notable patterns: ..." If any entries persistently failed quality review (failed twice), list them so the user knows to spot-check.