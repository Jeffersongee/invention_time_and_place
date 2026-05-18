#!/usr/bin/env python3
"""Write batch 21 (indices 140-146) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Liquid fueled rocket launch",
        "year": 1926,
        "inventor": "Robert Goddard",
        "category": "Mechanical",
        "category2": "Chemical",
        "earliest_plausible": "1908–1912",
        "earliest_straightforward": "1915–1920",
        "actual_location": "Auburn, Massachusetts, USA",
        "possible_locations": "USA; Germany; UK; France",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA had strong industrial capacity for precision machining, cryogenic gas supply (industrial LOX became available ~1895–1900), and a culture of empirical engineering; Goddard's actual location matches the most plausible geography.",
        "confidence": "Medium",
        "full_text": """Invention: Liquid-fueled rocket launch
Year actually invented: 1926
Earliest plausible: 1908–1912
Earliest straightforward: 1915–1920
Confidence: Medium
Actual location: Auburn, Massachusetts, USA
Possible locations at earliest plausible date: USA, Germany, UK, France
Geographic note: ALIGNED. The USA had strong industrial capacity for precision machining, cryogenic gas supply (industrial LOX became available ~1895–1900), and a culture of empirical engineering; Goddard's actual location matches the most plausible geography.

Prerequisite technologies:
- De Laval convergent-divergent nozzle [1897] — external
- Industrial liquid oxygen production (Linde/Hampson liquefaction process) [1895–1898] — external
- High-pressure valve and fitting technology (industrial gas industry) [~1900] — external
- Precision machining of combustion chambers and injector heads [~1900] — external
- Congreve/Hale solid-propellant rockets (thrust vectoring, stabilization concepts) [1804–1844] — external
- Thin-walled metal tube fabrication and brazing/welding techniques [~1890s] — external
- Centrifugal and piston pump technology for liquids under pressure [~1880s] — external

Scientific theories / key empirical observations:
- Tsiolkovsky rocket equation (mass-ratio analysis of reaction propulsion) [1903] — external
- Thermodynamic theory of nozzle flow / isentropic expansion (Rankine, de Laval empirical work) [1880s–1897] — external
- Combustion calorimetry of hydrocarbon fuels and oxidizers [~1880s–1900] — external
- Cryogenic behavior of LOX: vapor pressure, boil-off rates, material compatibility at low temperature [~1898–1905, empirical] — team-discoverable
- Injector atomization and propellant mixing physics (spray combustion, empirical) [~1900s] — team-discoverable

Explanation: The binding constraint was not theoretical but practical: the integrated management of cryogenic liquid oxygen in a flight-weight system alongside a reliable high-frequency injector and a regeneratively or ablatively cooled combustion chamber that could sustain burn long enough to produce net thrust. The De Laval nozzle (1897) and industrial LOX (c. 1895–1900) together remove the two largest single blockers, meaning a motivated team working from roughly 1903 onward — when Tsiolkovsky's equation gave a quantitative design target — could in principle have converged on a working vehicle within five years of focused effort, placing earliest plausible around 1908–1912. The gap to actuality (~14–18 years from those prerequisites) reflects not missing science but the difficulty of empirically debugging injector spray patterns, chamber pressure instability, and LOX plumbing seals without institutional funding; Goddard worked largely alone and underfunded. A well-resourced German or British precision-engineering firm with dedicated industrial gas suppliers could have matched or beaten Goddard's timeline by roughly a decade, which is why 1908–1912 is plausible but not straightforward; straightforward execution with a proper engineering team and budget narrows to 1915–1920."""
    },
    {
        "invention": "Three-point hitch",
        "year": 1926,
        "inventor": "Harry Ferguson",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1895–1905",
        "earliest_straightforward": "1910–1920",
        "actual_location": "Ireland/UK",
        "possible_locations": "United Kingdom; United States; Germany; France",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The UK had the engineering base, agricultural machinery industry, and hydraulic engineering tradition needed to develop this system; Ireland/UK is entirely consistent with the earliest plausible locations.",
        "confidence": "Medium",
        "full_text": """Invention: Three-point hitch (tractor implement attachment system)
Year actually invented: 1926
Earliest plausible: 1895–1905
Earliest straightforward: 1910–1920
Confidence: Medium
Actual location: Ireland/UK
Possible locations at earliest plausible date: United Kingdom, United States, Germany, France
Geographic note: ALIGNED. The UK had the engineering base, agricultural machinery industry, and hydraulic engineering tradition needed to develop this system; Ireland/UK is entirely consistent with the earliest plausible locations.

Prerequisite technologies:
- Internal combustion tractor (practical farm tractor) [1892, Froelich; commercially viable ~1900] — external
- Hydraulic cylinder / hydraulic actuation (single-acting hydraulic jack) [1795, Bramah press; practical small hydraulic cylinders by ~1880s] — external
- Wrought iron / mild steel fabricated linkage arms [widely available by 1850s] — external
- Pin-and-clevis hitch and drawbar implement attachment [mid-19th century] — external
- Mechanical draft animal implements (plows with adjustable depth) [ancient, refined by 1800s] — external
- Differential screw and lever-geometry mechanical advantage principles [well understood by 1800s] — external
- Pump and valve technology for hydraulic control (small hand or engine-driven pumps) [1870s–1880s] — external

Scientific theories / key empirical observations:
- Pascal's law (hydraulic pressure transmission) [1648, Pascal; engineering application by 1800s] — external
- Three-point (triangulated) linkage geometry provides kinematic constraint (stable orientation under load) [empirically obvious to any competent draughtsman by mid-19th century] — team-discoverable
- Draft force = horizontal soil resistance on implement; measurable with a spring dynamometer [1800s agricultural science] — external
- Feedback/governor principle (constant-force regulation via mechanical sensing) [Watt centrifugal governor 1788; spring-loaded relief valves 1860s] — team-discoverable adaptation
- Tractor weight transfer onto rear axle under draft load (improves traction) — team-discoverable empirically within a few seasons of testing

Explanation: The binding constraint was not geometry or hydraulics in isolation but the availability of a practical farm tractor as the host machine. The three-point linkage is geometrically trivial once a tractor exists — a motivated engineer-artisan team could have designed the triangulated linkage and a simple single-acting hydraulic lift cylinder (using Bramah-derived technology) within one iterative season after a reliable tractor was available. The hydraulic draft-control feedback loop — measuring compressive or tensile force on the top link and routing it to a hydraulic valve — is one layer of precursor engineering above basic hydraulic actuation, but it is squarely within empirical mechanical engineering of the late 19th century (spring-loaded governors, relief valves, and force-sensing levers were all standard). Had a team been motivated around 1895–1905 (shortly after the first viable IC tractors), the full Ferguson System geometry and hydraulic draft control could plausibly have been assembled by ~1900–1905. The gap between that estimate and 1926 is explained by the slow commercial adoption of tractors (horse draft remained dominant until WWI), lack of clear economic motivation to replace the simpler trailing drawbar until tractor horsepower and field speeds made implement depth control an acute problem, and the fact that no one was specifically tasked with solving implement-tractor integration as a unified engineering problem rather than an afterthought."""
    },
    {
        "invention": "First public live-image television demo",
        "year": 1926,
        "inventor": "John Logie baird",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1910–1912",
        "earliest_straightforward": "1912–1918",
        "actual_location": "London, England",
        "possible_locations": "United Kingdom; Germany; United States; France",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in London, which was among the leading centers for electrical engineering and vacuum tube development in the early twentieth century; the UK, Germany, France, and the US all had the requisite industrial and knowledge infrastructure by the earliest plausible window.",
        "confidence": "Medium",
        "full_text": """Invention: First public live-image television demonstration (mechanical TV)
Year actually invented: 1926
Earliest plausible: 1910–1912
Earliest straightforward: 1912–1918
Confidence: Medium
Actual location: London, England
Possible locations at earliest plausible date: United Kingdom, Germany, United States, France
Geographic note: ALIGNED. The actual invention occurred in London, which was among the leading centers for electrical engineering and vacuum tube development in the early twentieth century; the UK, Germany, France, and the US all had the requisite industrial and knowledge infrastructure by the earliest plausible window.

Prerequisite technologies:
- Nipkow disc scanning patent [1884] — external
- Selenium photoconductor cell (photoconductance effect, Smith & May) [1873] — external
- Thallium oxysulphide (thalofide) photocell with improved infrared sensitivity (Case) [1917] — external (binding for sensitivity; team-reachable analogue possible ~1910 with selenium stacks)
- Triode vacuum tube (de Forest Audion / Fleming valve refinements) [1906–1908] — external
- Multistage amplifier chains with adequate gain (~40–60 dB) [1912–1915] — external
- Neon glow lamp / Geissler discharge tube for display [1898–1910] — external
- Synchronization methods (mechanical governor, tuning-fork, or motor-driven) [1880s–1900s] — external
- Telephone/telegraph wiring infrastructure for signal transmission [1880s] — external

Scientific theories / key empirical observations:
- Photoelectric / photoconductance effect and its quantitative behavior [1873–1905] — external
- Thermionic emission and space-charge amplification (Richardson, Fleming, de Forest) [1904–1908] — external
- Bandwidth-resolution trade-off for scanning systems (empirical, no new science required) — team-discoverable
- Signal-to-noise requirements for gray-scale reproduction at ~10 fps (empirical iteration) — team-discoverable

Explanation: The binding constraint separating Rignoux's 1909 static-image transmission from Baird's 1926 live moving-image demonstration was not any single unavailable component but the combination of two coupled bottlenecks: (1) sufficiently sensitive and fast-responding photoelectric/photoconductor cells to follow brightness variations at the ~12.5 fps frame rate across many scan lines, and (2) multistage triode amplifier chains with enough stable gain (~40–60 dB) to bring the feeble photocell current up to a level capable of modulating a neon display lamp with adequate contrast. The Nipkow disc, synchronization mechanics, and neon lamp were all available before 1910. However, practical triode amplifiers with reliable gain did not exist until roughly 1912–1915, and sufficiently sensitive photocells (selenium stacks could work with effort, the superior thalofide cell arrived only in 1917) were marginal before that window. The lower bound of 1910 reflects when early triode tubes first became available for experimentation; a motivated team working from ~1910 onward could iterate toward usable selenium-cell sensitivity and exploit early triodes as they matured (~1910–1912), making a crude live-image demonstration possible by approximately 1910–1912 at the optimistic end, with a more realistic coordinated effort assembling all elements landing in 1912–1918. No new scientific frameworks were required: every element was reachable by empirical engineering iteration on published knowledge, making this a case of coordination and incremental optimization rather than fundamental discovery."""
    },
    {
        "invention": "Quartz Clock",
        "year": 1927,
        "inventor": "Warren Marrison & J. W. Horton",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1922–1925",
        "earliest_straightforward": "1925–1928",
        "actual_location": "New York, USA",
        "possible_locations": "USA (Bell Labs, GE, Western Electric); UK (NPL, Marconi); Germany (PTR, Telefunken)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The invention required advanced vacuum tube electronics, precision machining, and institutional radio/telecom research infrastructure — all concentrated in the same USA/UK/Germany triangle that actually produced it. No geographic mismatch.",
        "confidence": "High",
        "full_text": """Invention: Quartz clock (quartz crystal frequency standard as timekeeping device)
Year actually invented: 1927
Earliest plausible: 1922–1925
Earliest straightforward: 1925–1928
Confidence: High
Actual location: New York, USA
Possible locations at earliest plausible date: USA (Bell Labs, GE, Western Electric), UK (NPL, Marconi), Germany (PTR, Telefunken)
Geographic note: ALIGNED. The invention required advanced vacuum tube electronics, precision machining, and institutional radio/telecom research infrastructure — all concentrated in the same USA/UK/Germany triangle that actually produced it. No geographic mismatch.

Prerequisite technologies:
- Piezoelectric effect (Curie brothers, 1880) [1880] — external knowledge (off-limits for team discovery, but published and usable)
- Quartz crystal oscillator for radio frequency control (Cady, 1921; Nicolson, 1917) [1917–1921] — external/team-reachable
- Vacuum tube triode amplifier (De Forest, 1906; Fleming, 1904) [1906] — external/team-reachable
- Heterodyne and beat-frequency detection circuits [1913] — external/team-reachable
- Frequency divider / cascaded divider circuits using vacuum tubes [~1920–1924] — team-reachable (one layer of precursor; requires iteration but no new science)
- Precision crystal grinding and temperature-controlled (thermostated) crystal mount [~1918–1922] — team-reachable (empirical iteration on existing machining + oven techniques)
- Synchronous motor driven by AC frequency standard [pre-1920] — external/team-reachable
- Precision gear train and clock display mechanism [pre-1900] — external/team-reachable

Scientific theories / key empirical observations:
- Piezoelectricity as a quantitative phenomenon (Curie, 1880; Lippmann theoretical prediction, 1881) [1880–1881] — external (off-limits for team discovery; usable as published knowledge post-1880)
- Mechanical resonance of quartz as an exceptionally high-Q oscillator (low internal damping, high stability) [empirically observable by ~1918] — team-discoverable via iteration
- Temperature coefficient of quartz resonance frequency; existence of AT/BT cut orientations with near-zero TC [~1920s empirically] — team-discoverable (empirical grinding/testing, no new science)
- Frequency stability of crystal oscillator superior to LC circuit by orders of magnitude [empirically demonstrated Cady 1921] — external/team-reachable

Explanation: The binding constraint beyond the crystal oscillator (1917–1921) was the vacuum-tube frequency divider chain. A quartz crystal cut for convenient radio work resonates at tens to hundreds of kilohertz; to drive a seconds display, that frequency must be divided down by factors of 10,000–100,000. Reliable cascaded vacuum-tube divider circuits (multivibrators and trigger circuits) became practicable only after the triode amplifier was mature and the circuit topology was understood — the multivibrator was introduced by Abraham and Bloch in 1919, and reliable cascaded division required iterative empirical refinement of tube biasing over roughly 2–4 years. A motivated Bell Labs-class team with access to Cady's 1921 crystal oscillator work, Abraham–Bloch multivibrators, and precision machining could plausibly have assembled all layers by 1922–1925, with the thermostated crystal housing and division chain being the iterative (not scientifically novel) engineering work. No new scientific framework was required after 1921; the gap of only ~6 years from crystal oscillator to quartz clock reflects exactly this one layer of circuit engineering development, confirming the estimate."""
    },
    {
        "invention": "Discovery of penicillin's antibiotic action",
        "year": 1928,
        "inventor": "Alexander Fleming",
        "category": "Medical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "London, England",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: Discovery of penicillin's antibiotic action
Year actually invented: 1928
Earliest plausible: Flag
Earliest straightforward: Flag
Confidence: Flag
Actual location: London, England
Possible locations at earliest plausible date: Flag
Geographic note: Flag
Explanation: Fleming's discovery of penicillin's antibiotic action is the canonical example of a serendipitous accident explicitly named in the rubric as unreplicable by a directed program. The discovery depended on an unplanned confluence of events: a Penicillium mold spore contaminating an open culture plate, the plate being left unattended during a vacation period, and ambient temperatures that allowed the mold to grow before the bacteria crowded it out. No motivated team of engineers, however skilled, could have designed an experiment to produce this outcome without already knowing that Penicillium produces a bacteria-killing substance — which is precisely what was not known. There was no theoretical framework pointing toward fungal-derived antibacterial agents, no systematic research program that would have logically arrived at this petri dish observation, and the phenomenon itself (selective bacterial inhibition by a mold metabolite) was the discovery, not an application of prior knowledge. Because the triggering event is an accidental observation of a previously unknown phenomenon rather than the engineering application of known science, this entry cannot be assigned an earliest plausible date and is flagged in all relevant fields."""
    },
    {
        "invention": "Turbojet",
        "year": 1928,
        "inventor": "Frank Whittle",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1908–1915",
        "earliest_straightforward": "1918–1925",
        "actual_location": "England",
        "possible_locations": "United Kingdom; Germany; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Britain had the leading steam turbine industry (Parsons), strong precision engineering workshops, and military aviation incentive post-WWI; the actual invention occurred there as expected.",
        "confidence": "Medium",
        "full_text": """Invention: Turbojet engine (patent concept)
Year actually invented: 1928
Earliest plausible: 1908–1915
Earliest straightforward: 1918–1925
Confidence: Medium
Actual location: England
Possible locations at earliest plausible date: United Kingdom, Germany, France, United States
Geographic note: ALIGNED. Britain had the leading steam turbine industry (Parsons), strong precision engineering workshops, and military aviation incentive post-WWI; the actual invention occurred there as expected.
Prerequisite technologies:
- Parsons steam turbine (axial blading, rotodynamic principles) [1884] — external
- De Laval steam turbine (impulse staging, convergent-divergent nozzle) [1889] — external
- Elling self-sustaining gas turbine (compressor-combustion-turbine closed cycle proven) [1903] — external
- Centrifugal compressor theory and practice (Rateau, Roots) [1890s–1905] — external
- High-temperature nickel-chrome alloy steels (early heat-resistant alloys) [1906–1910] — external/team-reachable
- Precision machined close-tolerance rotating assemblies (bearing and seal technology) [~1900] — external
- Aerodynamic blade profile theory (Joukowski, Kutta) [1902–1906] — external
- Liquid fuel atomizing burners (kerosene/petroleum combustion chambers) [~1900] — external
- Aircraft engine metallurgy and lightweight casting (aluminum alloys for compressor) [1910s] — external
Scientific theories / key empirical observations:
- Thermodynamic Brayton/Joule cycle analysis (ideal gas turbine cycle efficiency) [1872] — external
- Rankine's turbomachinery theory and velocity triangles [1865–1880] — external
- Reynolds number and viscous flow in blade passages [1883] — external
- Empirical observation: compressor surge and stall behavior (team-discoverable by iterative rig testing) — team-discoverable
- Empirical observation: combustion stability in high-velocity airflow requires flame-holder geometry (team-discoverable) — team-discoverable
- High turbine inlet temperature requirement: metal creep limits at sustained >700°C (team-discoverable, constrains cycle efficiency) — team-discoverable
Explanation: The binding constraint is not conceptual but material and thermodynamic: a turbojet producing net thrust at flight-useful compression ratios requires turbine inlet temperatures of roughly 700–900°C sustained continuously, which demands heat-resistant alloys that only became reliably available (Nimonic precursors, austenitic steels) in the 1910s–1920s. Elling's 1903 gas turbine proved the compressor-combustion-turbine cycle but ran at low turbine inlet temperatures with marginal net output; scaling to useful thrust demands a compressor with adiabatic efficiency above ~70% and turbine blades that survive prolonged high-temperature, high-stress rotation — both achievable by an expert team after ~1908 using Parsons/de Laval blade geometry, Rateau centrifugal compressor know-how, and early chrome-nickel steels, but only marginally so before ~1910. A motivated team with access to precision machine shops, Elling's published results, and contemporary alloy suppliers could in principle have filed a workable patent concept by 1910–1912 and demonstrated a bench-running prototype by 1913–1915; the main gap versus the actual 1928 patent date reflects the absence of a compelling military aviation pull before WWI and Whittle's singular insight in linking jet propulsion to high-altitude flight efficiency rather than any fundamental scientific barrier."""
    },
    {
        "invention": "First practical all-electric television",
        "year": 1928,
        "inventor": "Philo Farnsworth",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1910–1915",
        "earliest_straightforward": "1920–1925",
        "actual_location": "San Francisco, California, USA",
        "possible_locations": "United Kingdom; Germany; USA",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA had the industrial infrastructure, vacuum tube expertise, and entrepreneurial culture to support this work by the 1920s; Germany and UK were equally plausible given their leadership in cathode ray tube and vacuum tube development.",
        "confidence": "Medium",
        "full_text": """Invention: First practical all-electric television (electronic TV)
Year actually invented: 1928
Earliest plausible: 1910–1915
Earliest straightforward: 1920–1925
Confidence: Medium
Actual location: San Francisco, California, USA
Possible locations at earliest plausible date: United Kingdom, Germany, USA
Geographic note: ALIGNED. The USA had the industrial infrastructure, vacuum tube expertise, and entrepreneurial culture to support this work by the 1920s; Germany and UK were equally plausible given their leadership in cathode ray tube and vacuum tube development.

Prerequisite technologies:
- Cathode ray tube (Braun tube) [1897, Germany] — external/team-reachable
- High-vacuum tube pumping (Gaede molecular pump) [1905–1910] — external/team-reachable
- Triode vacuum tube amplifier (de Forest audion) [1906] — external/team-reachable
- Photoemissive surface (cesium-oxide or similar alkali-metal coatings with adequate sensitivity) [~1910–1913, Elster & Geitel refinements] — external/team-reachable
- Electron beam deflection (electrostatic and magnetic) [1897 onward] — external/team-reachable
- Synchronization signaling for scan timing [~1900s telegraph/radio practice] — team-reachable within project
- Wideband electronic amplification (multi-stage) [~1915, radio/telephony work] — external/team-reachable

Scientific theories / key empirical observations:
- Photoelectric effect (Hertz observation 1887; Einstein explanation 1905) — external, usable as published knowledge
- Electron as discrete particle (Thomson 1897) — external
- Thermionic emission and space charge (Richardson, Fleming, 1904–1906) — external
- Scanning raster principle (Nipkow conceptual patent 1884) — external, establishes the conceptual framework even in mechanical form
- Secondary emission and photoemissive yield measurements [~1910s] — external/team-discoverable

Explanation: The binding constraint was not the underlying science but the combination of two engineering problems that both required post-1905 vacuum technology: (1) achieving a photoemissive surface sensitive enough to generate a usable electron current from a scene image in real time, and (2) pumping the image dissector and CRT to sufficiently high vacuum that the electron beam remained coherent over the tube length. Both became practically solvable only after the Gaede high-vacuum pump (~1905–1910) and the refinement of alkali-metal photocathodes by Elster and Geitel (~1910–1913). With those two elements in hand, a motivated team of vacuum-tube engineers — already versed in triode amplification and CRT deflection — could in principle have assembled a working all-electronic image dissector and CRT display by roughly 1910–1915, though the wideband multi-stage amplification needed to preserve image detail would have pushed a clean, demonstrable result closer to 1920–1925. No new scientific framework was required; every needed phenomenon was published and empirically accessible. The gap between the earliest plausible date (~1910) and the actual date (1928) is therefore under 20 years and reflects the practical engineering time needed to converge on adequate photocathode sensitivity, vacuum integrity, and synchronization — not any missing theory."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
