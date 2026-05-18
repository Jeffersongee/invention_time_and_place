#!/usr/bin/env python3
"""Write batch 26 (indices 175-181) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Silicon solar photovoltaic cell",
        "year": 1954,
        "inventor": "Calvin Fuller, Daryl Chapin & Gerald Pearson (Bell Labs)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1951–1953",
        "earliest_straightforward": "1953–1956",
        "actual_location": "Murray Hill, New Jersey, USA",
        "possible_locations": "USA (Bell Labs or comparable industrial research lab); UK (GEC, TRE); Germany (Siemens research); USSR (academic semiconductor groups)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA had the densest concentration of semiconductor expertise post-WWII, and Bell Labs in particular had the transistor program infrastructure that made this convergence near-inevitable.",
        "confidence": "High",
        "full_text": """Invention: Silicon solar photovoltaic cell (practical efficiency ~6%)
Year actually invented: 1954
Earliest plausible: 1951–1953
Earliest straightforward: 1953–1956
Confidence: High
Actual location: Murray Hill, New Jersey, USA
Possible locations at earliest plausible date: USA (Bell Labs or comparable industrial research lab), UK (GEC, TRE), Germany (Siemens research), USSR (academic semiconductor groups)
Geographic note: ALIGNED. The USA had the densest concentration of semiconductor expertise post-WWII, and Bell Labs in particular had the transistor program infrastructure that made this convergence near-inevitable.

Prerequisite technologies:
- Photovoltaic effect (Becquerel 1839) — external (published, off-limits as phenomenon but fully usable as knowledge)
- Selenium photocell / early solid-state photovoltaics (1873–1883) — external
- Quantum mechanical band theory of solids (Wilson, Bloch, 1930–1932) — external
- p-n junction theory (Shockley diode model, 1949) — external
- Zone-refining / float-zone silicon purification (Pfann, 1952) — external (published and commercially adjacent by 1952–1953)
- Czochralski crystal pulling adapted for silicon (Teal & Little, Bell Labs, 1950) — external
- Diffusion doping to form a shallow p-n junction in silicon — team-reachable (one-layer precursor; achievable by a skilled team with knowledge of junction transistor fabrication)

Scientific theories / key empirical observations:
- Photovoltaic effect in semiconductors — external (off-limits as phenomenon but usable from 1839)
- Band gap theory explaining photon absorption and carrier generation — external (Wilson 1931)
- Minority carrier diffusion length and collection efficiency in p-n junctions — external by 1950–1952 (Shockley–Read–Hall recombination, 1952)
- Silicon p-n junctions produce measurable photovoltage — team-discoverable; follows logically from junction transistor physics once high-purity silicon is available
- Shallow junction maximizes photon collection in silicon's absorption depth — team-reachable by empirical iteration

Explanation: The binding constraint is not scientific theory but materials: high-purity, single-crystal silicon with controlled p-n junction doping. Before Teal and Little's Czochralski silicon pulling (1950) and Pfann's zone-refining (1952), silicon of sufficient purity and crystalline quality did not exist outside a handful of experimental samples. The transistor program at Bell Labs was the industrial forcing function that produced this materials infrastructure. A motivated team beginning work in 1951 would have had access to Czochralski-grown silicon (just published), Shockley's junction theory (1949), and the rapidly expanding transistor doping literature. They could plausibly have achieved a working p-n junction photovoltaic cell within two to three years of focused effort, placing the earliest plausible window at 1951–1953.

The one non-commercial precursor the team would need to build is a reliable diffusion-doping process to form a shallow, low-resistance p-n junction in silicon. This is solidly within the "one layer" rule: it requires no new science, only careful empirical process development using a furnace, dopant gases, and iteration. A competent semiconductor team in 1951 could have converged on a workable diffusion schedule within one to two years given the junction transistor literature as a guide. The efficiency target of ~6% is achievable without any optimization beyond what basic band-gap physics predicts for silicon under AM1 illumination.

The gap between the earliest plausible date (1951–1953) and the actual date (1954) is very small — essentially just one to two years — and is explained by the fact that the Bell Labs team was not initially targeting solar energy. Pearson, Fuller, and Chapin converged on the silicon p-n junction approach only after Chapin's prior work on selenium cells revealed their fundamental efficiency ceiling. A team explicitly tasked with maximizing photovoltaic efficiency from the outset would likely have reached the same result on approximately the same timeline or perhaps one year faster."""
    },
    {
        "invention": "Hovercraft (air-cushion vehicle)",
        "year": 1955,
        "inventor": "Christopher Cockerell",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1870–1880",
        "earliest_straightforward": "1890–1900",
        "actual_location": "Somerleyton, Suffolk, England",
        "possible_locations": "United Kingdom; United States; France; Germany; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. England is within the UK, which appears in the possible-locations list.",
        "confidence": "Medium",
        "full_text": """Invention: Hovercraft (air-cushion vehicle)
Year actually invented: 1955
Earliest plausible: 1870–1880
Earliest straightforward: 1890–1900
Confidence: Medium
Actual location: Somerleyton, Suffolk, England
Possible locations at earliest plausible date: United Kingdom, United States, France, Germany, Belgium
Geographic note: ALIGNED. England is within the UK, which appears in the possible-locations list.

Prerequisite technologies:
- Centrifugal fans/blowers: commercially available by ~1860s — external (Sirocco-type industrial fans well-established by 1880s)
- Steam engines or internal combustion engines: steam available ~1800s — external; practical IC engines ~1876 (Otto cycle) — external
- Sheet metal fabrication and riveting: available throughout 19th century — external
- Rubber or oilcloth for flexible seals: available ~1840s post-vulcanization (Goodyear 1844) — external
- Centrifugal pump fluid mechanics (Euler, ~1754): theoretical basis for fan/duct design available well before 1870 — external
- Flexible peripheral skirt: not commercially available pre-1955, but achievable by team using rubberized canvas or oiled leather without new science — team-reachable

Scientific theories / key empirical observations:
- Bernoulli's principle and fluid continuity equations (Bernoulli 1738, Euler 1752): provide theoretical basis for pressure differentials under cushion — external
- Momentum curtain / peripheral jet geometry: the core Cockerell insight — empirically discoverable via simple bench experiments without new science; no phenomenon discovery required
- Ground effect aerodynamics: documented in early aviation literature (1910s–1920s) but not strictly necessary — external
- Fan and duct efficiency relationships: understood via engineering practice well before 1870 — external

Explanation: The hovercraft's operating principle requires no new scientific discovery. The peripheral jet insight — that directing fan airflow around the perimeter of a hull creates a more efficient pressure seal than open downward blasting — is straightforwardly derivable from fluid statics and is empirically discoverable with bench-top experiments (Cockerell's own famous demonstration used a vacuum cleaner, a cat food tin, and a coffee tin). A motivated engineer with access to 1870s knowledge of fluid mechanics, centrifugal fans, and vulcanized rubber would face no fundamental barrier. The binding constraint is not science but practical engineering: achieving sufficient thrust-to-weight ratio to lift a craft meaningfully, and sealing the cushion well enough to demonstrate sustained hover.

The 1870–1880 earliest plausible window reflects that all hard prerequisites are in place: industrial centrifugal fans are commercially available, steam engines provide adequate power (at weight penalty), and rubberized fabric enables a rudimentary flexible seal. A team could build a small demonstration craft within five years of focused effort. The central obstacle is conceptual, not material: the peripheral jet geometry is non-obvious, and without aviation culture prompting interest in ground-effect phenomena, the motivation to pursue it is less clear. However, under the rubric's assumption of a motivated inventor, this is not a blocking constraint.

The 1890–1900 earliest straightforward window reflects the availability of light internal combustion engines (post-Otto 1876, post-Daimler 1885), which remove the weight-penalty problem of steam and make a practically useful — not merely demonstrable — hovercraft feasible. With a petrol engine, rubberized-canvas peripheral skirt, and sheet-metal hull, a small team could plausibly build and test a craft capable of carrying a person over calm water or flat ground. The large gap to 1955 reflects absence of commercial motivation and niche application rather than technical barrier."""
    },
    {
        "invention": "Intermodal shipping container",
        "year": 1956,
        "inventor": "Malcolm McLean (Pan-Atlantic Steamship)",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1830–1845",
        "earliest_straightforward": "1890–1910",
        "actual_location": "Newark, New Jersey, USA",
        "possible_locations": "United Kingdom (Liverpool, London, Glasgow); Belgium (Antwerp); United States (New York, Baltimore, Boston)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. United States appears in the possible-locations list. The earliest plausible window (1830–1845) most favored British and Belgian port cities, but the actual location in the USA is ALIGNED since USA appears in the list.",
        "confidence": "Medium",
        "full_text": """Invention: Intermodal shipping container (standardized steel container for multimodal freight)
Year actually invented: 1956
Earliest plausible: 1830–1845
Earliest straightforward: 1890–1910
Confidence: Medium
Actual location: Newark, New Jersey, USA
Possible locations at earliest plausible date: United Kingdom (Liverpool, London, Glasgow), Belgium (Antwerp), United States (New York, Baltimore, Boston)
Geographic note: ALIGNED. United States appears in the possible-locations list. The earliest plausible window (1830–1845) most favored British and Belgian port cities, but the actual location in the USA is ALIGNED since USA appears in the list. Note: at the 1830–1845 earliest plausible date, the UK and Belgium were better-positioned than the US, but by the straightforward window (1890–1910) the US was fully plausible.

Prerequisite technologies:
- Wrought iron / mild steel sheet fabrication and riveting at scale [pre-1830] — external
- Standardized corner castings (or equivalent interlock fitting) — requires precision machining — team-reachable
- Rail flatcar capable of carrying the load and dimensions [pre-1830] — external
- Dockside crane or gantry capable of lifting 10–20 ton loads [Liverpool's Albert Dock 1846 had hydraulic cranes ~5 tons] — external (tight at 1830, comfortable by 1840–1845)
- Road truck chassis with mounting points — external

Scientific theories / key empirical observations:
- Yield strength and fatigue properties of mild steel (understood by ~1860s) — external
- Structural engineering: column buckling and corner-load transfer for stacking (Euler column theory 1744) — external
- No novel physics required — pure mechanical and civil engineering

Explanation: The container's value is overwhelmingly network-effects-driven, but the physical artifact — the corner casting geometry, the twistlock, the structural spec allowing eight-high stacking at sea — is genuinely engineered. Not flagged: a motivated team can build one working system (one terminal, one ship, one truck fleet) and demonstrate it without industry-wide adoption, exactly as McLean did with Pan-Atlantic Steamship in 1956. Earliest plausible (1830–1845): wrought-iron box construction at required scale was within reach of British ironworkers by the 1830s. Early UK railways (Liverpool & Manchester, 1830) immediately used removable road-vehicle bodies on flatcars. A motivated team in 1835 could specify a fixed-dimension wrought-iron box with bolted corner brackets, build a matching shipboard cradle, and demonstrate end-to-end transfer at Liverpool docks. The binding constraint is crane capacity: hydraulic cranes at major ports by the early 1840s could handle ~5 tons; 1840–1845 is more comfortable than 1830. Steel (Bessemer) is not needed — wrought iron suffices. Twistlocks are not strictly necessary; bolted corner fittings work.

Earliest straightforward (1890–1910): by 1890, every physical ingredient is commercially off the shelf: Bessemer/open-hearth mild steel plate, hydraulic dock cranes rated to 20+ tonnes, transcontinental rail networks, standardized machined fittings. The reason this didn't happen until 1956 is almost entirely the coordination problem: vested interests of longshoremen's unions, rail tariff regulation, and the US interstate commerce regulatory regime. McLean's genius was organizational and financial — he bought a steamship company while owning a trucking company, exploiting a regulatory loophole. These institutional barriers are not technical obstacles and do not trigger a flag per rubric. The 66-year gap from straightforward to actual reflects demand and regulatory factors, not missing technology."""
    },
    {
        "invention": "Hard disk drive (random-access magnetic disk storage)",
        "year": 1956,
        "inventor": "Reynold B. Johnson and team (IBM San Jose)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1952–1954",
        "earliest_straightforward": "1954–1956",
        "actual_location": "San Jose, California, USA",
        "possible_locations": "USA (San Jose, Boston/MIT area, Bell Labs NJ); UK (National Physical Laboratory, Ferranti Manchester); Germany (Telefunken Berlin)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. IBM San Jose is within the identified cluster of plausible locations.",
        "confidence": "Medium",
        "full_text": """Invention: Hard disk drive (random-access magnetic disk storage)
Year actually invented: 1956
Earliest plausible: 1952–1954
Earliest straightforward: 1954–1956
Confidence: Medium
Actual location: San Jose, California, USA
Possible locations at earliest plausible date: USA (San Jose, Boston/MIT area, Bell Labs NJ), UK (National Physical Laboratory, Ferranti Manchester), Germany (Telefunken Berlin)
Geographic note: ALIGNED. IBM San Jose is within the identified cluster of plausible locations.

Prerequisite technologies:
- Magnetic drum memory (commercially available ~1950–1952) — external
- Magnetic tape recording and iron-oxide particle coating on flexible substrate (commercially mature by ~1948–1950 via BIOS/FIAT reports on German tape technology) — external
- Precision aluminum disk substrate machining (aerospace-grade, available ~1948+) — external
- Wideband magnetic read/write head design (derived from tape recorder heads, ~1948+) — external
- Air-bearing hydrodynamics (Reynolds lubrication equation, 1886; applied to slider bearings in precision machinery, ~1940s) — external
- Servo-mechanical positioning systems (fire-control and radar servos, mature by 1945–1948) — external
- Flying-head air-bearing self-stabilization (head geometry, surface finish tolerances, spring pressure interaction) — team-reachable as one-layer precursor (empirical iteration; no new science required)

Scientific theories / key empirical observations:
- Hysteresis loop in ferromagnetic materials (Ewing, 1890s); basis of binary magnetic recording — external
- Reynolds lubrication theory (1886) — flying head air-bearing behavior self-consistent with rotating-disk geometry at sufficient surface speed — external
- Particulate magnetic recording medium: iron oxide (γ-Fe₂O₃) dispersed in binder — external
- SNR and bandwidth requirements for digital magnetic recording — external by ~1948–1952 from drum memory work
- Flying-head tribology: self-stabilizing air cushion with light spring load — team-discoverable (empirical iteration on head geometry and spring force)

Explanation: The binding constraint is the flying-head air bearing, not the magnetic coating or the electronics. The RAMAC team essentially painted tape-style slurry onto aluminum disks — a straightforward adaptation of tape technology available to any engineer with access to post-1948 tape manufacturing literature. Wideband amplification and servo positioning were both mature by 1950 from radar and early drum-memory work. The one genuinely non-obvious element was discovering that a contoured slider with light spring pressure would fly stably on a thin air cushion rather than crashing. This is empirical, not new science: the Reynolds lubrication equation had been known since 1886, and air-bearing spindle designs existed in precision metrology by the late 1940s. A motivated team with those references could have worked out the geometry experimentally within one to two years of focused effort.

Earliest plausible (1952–1954) reflects the convergence of three independently necessary threads: magnetic drum memory as a working commercial product (de-risking the digital read/write head, ~1950–1952), postwar iron-oxide tape coating knowledge fully published (~1948–1950 via BIOS/FIAT reports on German tape technology), and precision disk-grinding and surface-finish capability (aerospace-grade aluminum machining, available in USA and UK by ~1948). Given these three streams, a team assembled in 1950–1951 could plausibly have demonstrated a flying-head disk storage device by 1952–1954, roughly two to four years ahead of the actual RAMAC. Straightforward range (1954–1956) acknowledges that the head-disk tribology iteration — head geometry, surface finish tolerances, head-load mechanics — required non-trivial empirical work even for a well-funded team, consistent with IBM's own 1952–1956 development timeline."""
    },
    {
        "invention": "Logic Theorist (first AI program / automated theorem prover)",
        "year": 1956,
        "inventor": "Allen Newell, Herbert Simon & Cliff Shaw (Carnegie Mellon / RAND)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1952–1954",
        "earliest_straightforward": "1954–1956",
        "actual_location": "Pittsburgh, PA / Santa Monica, CA, USA",
        "possible_locations": "USA (Princeton IAS, MIT, RAND, Bell Labs); UK (University of Manchester, Cambridge)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual location (CMU/RAND, USA) is within the plausible set.",
        "confidence": "Medium",
        "full_text": """Invention: Logic Theorist (first AI program / automated theorem prover)
Year actually invented: 1956
Earliest plausible: 1952–1954
Earliest straightforward: 1954–1956
Confidence: Medium
Actual location: Pittsburgh, PA / Santa Monica, CA (Carnegie Mellon / RAND), USA
Possible locations at earliest plausible date: USA (Princeton IAS, MIT, RAND, Bell Labs), UK (University of Manchester, Cambridge)
Geographic note: ALIGNED. The actual location (CMU/RAND, USA) is within the plausible set.

Prerequisite technologies:
- Stored-program digital computer with adequate RAM (EDVAC, IAS machine, UNIVAC I, IBM 701, Manchester Mark 1, EDSAC — all operational by 1951–1952) — external
- Reliable high-speed magnetic core or drum memory (practical by 1951–1953) — external
- Assembly-level or macro-level programming sufficient to implement recursive data structures — external/team-reachable
- Access to a machine with enough addressable word-length memory to represent symbolic expressions — external
- Hand-coded list representation in assembly/machine language (the Logic Theorist itself solved this) — team-reachable (one-layer precursor)

Scientific theories / key empirical observations:
- Whitehead & Russell's Principia Mathematica (1910–1913): the axiom system and inference rules serving as the problem domain — external
- Church's lambda calculus (1936) and Turing's computability theory (1936): formal basis for computation as symbol manipulation — external
- Von Neumann stored-program architecture (1945–1948): program and data in same memory, enabling self-referential data structures — external
- Turing's "Computing Machinery and Intelligence" (1950): explicit articulation that machines could simulate reasoning — external
- Shannon's "Programming a Computer for Playing Chess" (1950): first published heuristic search strategy for a combinatorial problem — external (critical conceptual precursor)
- George Pólya's "How to Solve It" (1945): heuristic problem-solving methods that directly inspired means-ends analysis — external

Explanation: The hard lower bound is the availability of a stored-program machine reliable enough to run a non-trivial symbolic program for minutes at a time without hardware failure. That threshold was crossed by 1951–1952: the IAS machine at Princeton, EDSAC at Cambridge, the Manchester Mark 1, UNIVAC I (delivered May 1951), and the IBM 701 (delivered April 1953) all meet the minimum bar. A motivated team with access to any of these machines and institutional computing time could begin the engineering work. The list-processing requirement is the only genuine software-infrastructure obstacle; the Logic Theorist itself solved this by hand-coding its own list representation in assembly/machine language on the JOHNNIAC — within the one-layer-of-precursor rule.

The conceptual ingredients were all published and available before 1952. Shannon's 1950 chess paper is the direct intellectual ancestor of heuristic search: it explicitly distinguishes exhaustive ("Type A") from selective ("Type B") search. Pólya's heuristics, Turing's 1950 paper, and the formal logic tradition (Russell, Hilbert, Gödel) were all in print. The critical intellectual leap — representing logical inference rules as data structures and applying heuristic selection — required no new scientific discovery, only the synthesis of existing ideas. A motivated team at IAS, MIT, or RAND in 1952, with Shannon's paper and access to a stored-program machine, could plausibly have made the same synthesis.

The reason 1952–1954 rather than 1950–1951 is the lower bound is twofold. First, machine reliability and available compute time were genuinely marginal in 1950–1951. Second, the conceptual synthesis requires awareness of Shannon's 1950 paper and Pólya's heuristics alongside the formal logic substrate — a team would need at minimum 1–2 years of familiarity with these. The "straightforward" range of 1954–1956 reflects the more likely case where a team needs time to acquire reliable compute access and debug a non-trivial symbolic program under the constraints of early batch-processing environments."""
    },
    {
        "invention": "Laser / optical amplifier concept (theoretical proposal)",
        "year": 1958,
        "inventor": "Gordon Gould; Arthur Schawlow & Charles Townes (Columbia/Bell Labs)",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1930–1935",
        "earliest_straightforward": "1940–1950",
        "actual_location": "New York, USA (Columbia University)",
        "possible_locations": "Germany (Berlin, Munich, Jena optics and physics institutes); USA (Columbia, MIT, Bell Labs); USSR (Moscow/Leningrad — Ioffe Institute, Vavilov fluorescence group); UK (Cambridge Cavendish Laboratory); France (Paris — optical tradition)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. USA (Columbia, MIT, Bell Labs) appears in the possible-locations list, and the actual location (Columbia University, New York) is explicitly named. Germany was arguably the best-positioned location in 1930–1935, but the actual origin in the USA is ALIGNED per the rubric.",
        "confidence": "Medium",
        "full_text": """Invention: Laser / optical amplifier concept (theoretical proposal)
Year actually invented: 1957–1958
Earliest plausible: 1930–1935
Earliest straightforward: 1940–1950
Confidence: Medium
Actual location: New York, USA (Columbia University — Townes, Schawlow, Gould)
Possible locations at earliest plausible date: Germany (Berlin, Munich, Jena optics and physics institutes); USA (Columbia, MIT, Bell Labs); USSR (Moscow/Leningrad — Ioffe Institute, Vavilov fluorescence group); UK (Cambridge Cavendish Laboratory); France (Paris — optical tradition, Fabry-Pérot legacy)
Geographic note: ALIGNED. USA (Columbia, MIT, Bell Labs) appears in the possible-locations list, and the actual location (Columbia University, New York) is explicitly named. Germany was arguably the single best-positioned location in 1930–1935 given its leadership in theoretical quantum physics and precision optical spectroscopy, but the actual origin in the USA is ALIGNED per the rubric.

Prerequisite technologies:
- Fabry-Pérot etalon (parallel-mirror optical resonator) [1899, Fabry & Pérot] — external; essential for defining the cavity concept
- Synthetic ruby (Verneuil flame-fusion process) [1902] — external; provides a specific gain medium with characterized Cr³⁺ energy levels
- Optical spectroscopy of ruby and other fluorescent media [1900s–1930s] — external; provides absorption/emission cross-sections and excited-state lifetime data
- High-intensity pulsed discharge lamps (xenon flash / stroboscopes) [Edgerton xenon strobe, 1931; earlier Geissler-type discharge tubes, 1857] — team-reachable for the 1930 candidate date

Scientific theories / key empirical observations:
- Einstein's quantum theory of radiation, including stimulated emission [1917] — external; the binding item; without this there is no theoretical basis for coherent light amplification
- Bohr atomic model and discrete energy levels [1913] — external
- Full quantum mechanics (Heisenberg, Schrödinger, Dirac) [1925–1927] — external; required to compute transition rates and gain cross-sections rigorously
- Boltzmann statistical mechanics and thermal equilibrium population distributions [1870s–1900] — external
- Optical fluorescence and excited-state lifetime (Wood, Vavilov) [1900s–1920s] — external; establishes empirically that excited states persist long enough as a reservoir
- Population inversion produces gain rather than absorption — team-discoverable: this follows directly by algebra from Einstein 1917 A and B coefficients when a team is specifically tasked with designing a light amplifier

Explanation: The binding item for the theoretical laser proposal is Einstein's 1917 stimulated-emission theory, which establishes that an atom in an excited state can be triggered by an incoming photon to emit a second, identical photon. Before 1917, there is no theoretical basis for the concept. With the 1917 paper in hand, plus the full quantum-mechanical framework of 1925–27, the Fabry-Pérot etalon (1899) as the resonator concept, and spectroscopic data on fluorescent media available by the early 1930s, a team specifically tasked with "build a device that amplifies light via stimulated emission" has all the ingredients for a paper design. The key non-obvious insight — population inversion reverses absorption into gain — follows algebraically from Einstein's A and B coefficients. A sharp theorist directed at this goal in 1930–1935 could have derived the gain condition, proposed a Fabry-Pérot cavity, and proposed optical pumping via a pulsed discharge lamp.

The ~25-year gap between this earliest plausible date and the actual 1957–1958 proposals is explained by two factors: first, no one was motivated to look — stimulated emission was treated as a minor correction in thermal systems, and the amplifier engineering tradition was in the microwave domain; second, the Nazi purge of German physics (1933–) decimated the community best-positioned for this work in the 1930s, and the problem had to wait for the MASER (1953–54) to serve as the conceptual prompt and existence proof that stimulated-emission amplifiers could be built in practice. The "earliest straightforward" range of 1940–1950 reflects that by then, optical pumping techniques, xenon flash technology, and the growing community of physicists working on microwave amplifiers (radar-era) would have made convergence likely within a decade of being motivated."""
    },
    {
        "invention": "IBM 610 Auto-Point Computer (early personal computer)",
        "year": 1957,
        "inventor": "IBM Research, Endicott, New York (John W. Lentz, designer)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1948–1950",
        "earliest_straightforward": "1951–1953",
        "actual_location": "Endicott, New York, USA",
        "possible_locations": "USA (MIT, Bell Labs, RCA, IBM); UK (Cambridge, Manchester, NPL); France (Paris — Bull/CNRS); Germany (Göttingen — limited postwar); Sweden (KTH Stockholm)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Endicott, NY is within the US industrial-academic complex that dominates the earliest plausible list.",
        "confidence": "Medium",
        "full_text": """Invention: IBM 610 Auto-Point Computer (early single-user / "personal" computer)
Year actually invented: 1957
Earliest plausible: 1948–1950
Earliest straightforward: 1951–1953
Confidence: Medium
Actual location: Endicott, New York, USA
Possible locations at earliest plausible date: USA (MIT, Bell Labs, RCA, IBM), UK (Cambridge, Manchester, NPL), France (Paris — Bull/CNRS), Germany (Göttingen — limited postwar), Sweden (KTH Stockholm)
Geographic note: ALIGNED. Endicott, NY is within the US industrial-academic complex that dominates the earliest plausible list.

Prerequisite technologies:
- Triode vacuum tubes (stable, miniaturized — 12AX7-era small signal tubes, available by mid-1940s) — external
- Williams tube or mercury delay-line storage (Williams/Kilburn 1947; mercury delay lines ~1944–1945) — external
- Typewriter-derived keyboard input mechanism (mature by 1900s; teletype-style encoding well-established by 1930s) — external
- Paper tape I/O (well-established by 1930s in teletype systems) — external
- Stored-program concept (Manchester Baby June 1948; EDSAC May 1949) — external; binding item: demonstrated June 1948
- Floating-point arithmetic units (Zuse Z3 1941; practical implementations mid-1940s) — external
- Custom compact chassis and simplified instruction set (for a desk-scale machine) — team-reachable (one-layer precursor)

Scientific theories / key empirical observations:
- Boolean algebra applied to switching circuits (Shannon 1937) — external
- Stored-program architecture (von Neumann report 1945; demonstrated 1948) — external
- Williams tube electrostatic storage (Williams & Kilburn, 1946–1947) — external
- Thermionic emission / triode amplification (Fleming 1904, De Forest 1906) — external
- Binary arithmetic and two's complement representation — external

Explanation: The IBM 610's core functional concept — a desk-sized, single-user, keyboard-operable stored-program computer — depends on three binding prerequisites: a practical stored-program architecture, compact random-access memory, and miniaturized vacuum tube logic. The stored-program concept was demonstrated in working hardware by June 1948 (Manchester Baby) — that 1948 date is the hard lower bound. Given this, the earliest plausible window is 1948–1950. A highly motivated workshop team in 1948 could access Williams tube storage (1947), teletype-derived keyboard encoding, paper tape I/O, and triode vacuum tube logic (well-characterized). The IBM 610 used roughly 170 vacuum tubes — a very modest count. A simplified single-user machine targeting floating-point scientific calculation could be built with far fewer components, reducing power and chassis requirements. The one allowed precursor is a custom compact chassis design and simplified instruction set optimized for single-user desk operation.

The earliest straightforward window (1951–1953) reflects when magnetic core memory (Forrester's Whirlwind core plane, demonstrated 1953) begins to offer an alternative to the finicky Williams tube, commercial small-signal tubes have well-characterized failure rates, and the broader computing community has accumulated rich published design templates (EDSAC, ACE, IAS machine). By 1951, a motivated engineer could read Wilkes's published EDSAC account, survey Williams tube implementations, and design a deliberately simplified single-user machine. The ~7-year gap to 1957 is almost entirely organizational: who would fund a "personal" computer in 1948–1950 when the prevailing model was shared batch-processing? This is a demand/motivation gap which per the rubric does not trigger a flag."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
