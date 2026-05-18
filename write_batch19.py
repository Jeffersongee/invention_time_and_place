#!/usr/bin/env python3
"""Write batch 19 (indices 126-132) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Cellophane",
        "year": 1908,
        "inventor": "Jacques Brandenberger",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1893–1896",
        "earliest_straightforward": "1897–1900",
        "actual_location": "France",
        "possible_locations": "United Kingdom; France; Germany; Switzerland; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The viscose process originated in the UK (Cross, Bevan, Beadle, 1892), and industrial textile chemistry was concentrated in Britain, France, Germany, and Switzerland — all plausible sites for immediate follow-on film-casting work.",
        "confidence": "High",
        "full_text": """Invention: Cellophane (regenerated cellulose film)
Year actually invented: 1908
Earliest plausible: 1893–1896
Earliest straightforward: 1897–1900
Confidence: High
Actual location: France
Possible locations at earliest plausible date: United Kingdom, France, Germany, Switzerland, Belgium
Geographic note: ALIGNED. The viscose process originated in the UK (Cross, Bevan, Beadle, 1892), and industrial textile chemistry was concentrated in Britain, France, Germany, and Switzerland — all plausible sites for immediate follow-on film-casting work.
Prerequisite technologies:
- Cellulose dissolution in carbon disulfide / NaOH to form viscose [1892] — external/team-reachable
- Acid regeneration bath (sulfuric acid precipitation of xanthate back to cellulose) [1892] — external/team-reachable
- Spinneret fiber extrusion geometry for rayon [1892–1894] — external/team-reachable
- Flat slit die / doctor-blade casting geometry (analogous to glass plate casting, paper coating) [pre-1890] — team-reachable
- Glycerin or similar polyol as plasticizer for cellulosic films [pre-1890, established in collodion/nitrocellulose film work] — external/team-reachable
- Continuous take-up rollers and tension management for thin wet films [pre-1890, paper/textile machinery] — team-reachable
Scientific theories / key empirical observations:
- Cellulose xanthate chemistry and xanthation reaction mechanism [1892] — external/team-discoverable
- Empirical observation that viscose regenerated as a film (not fiber) when cast on a flat surface and immersed in acid [discoverable by 1893 with bench trials] — team-discoverable
- Plasticization of regenerated cellulose with glycerin to prevent brittleness [empirically discoverable within 1–2 years of first film casting] — team-discoverable
- Optical clarity of regenerated cellulose versus nitrocellulose (no camphor needed, lower flammability) [observable property, no theory required] — team-discoverable
Explanation: The binding constraint is the 1892 viscose process patent (Cross, Bevan, Beadle), which is the only non-trivial prerequisite; all other steps — replacing a round spinneret with a flat slit die, immersing the extrudate in the same acid regeneration bath already used for fiber, and adding glycerin as plasticizer — are straightforward engineering adaptations requiring no new science and no chaining of novel precursor technologies. A motivated team with access to the 1892 patent literature and bench-scale viscose synthesis equipment could plausibly have produced a continuous transparent regenerated-cellulose film within one to four years of that patent, placing the earliest plausible date at 1893–1896. The 12–16 year gap to Brandenberger's 1908 work reflects the absence of commercial motivation (no obvious application for transparent film had been identified) and the fact that the rayon industry's entire engineering focus was on fiber spinning geometry, not sheet casting — Brandenberger himself arrived at cellophane while attempting to make tablecloths waterproof, an accidental redirection of purpose rather than a technical barrier. No serendipitous or off-limits phenomenon is implicated; the delay was motivational and attentional, not scientific or engineering."""
    },
    {
        "invention": "Haber-Bosch process",
        "year": 1909,
        "inventor": "Fritz Haber",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1895–1905",
        "earliest_straightforward": "1900–1910",
        "actual_location": "Germany (Karlsruhe / Oppau)",
        "possible_locations": "Germany; United Kingdom; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Germany's strong industrial chemistry infrastructure, world-leading chemical engineering firms (BASF), and university-industry linkages made it the natural locus; Britain and France had comparable high-pressure engineering capability but weaker integration of academic thermodynamics with industrial scale-up.",
        "confidence": "Medium",
        "full_text": """Invention: Haber-Bosch process (nitrogen fixation by catalytic ammonia synthesis)
Year actually invented: 1909
Earliest plausible: 1895–1905
Earliest straightforward: 1900–1910
Confidence: Medium
Actual location: Germany (Karlsruhe / Oppau)
Possible locations at earliest plausible date: Germany, United Kingdom, France, United States
Geographic note: ALIGNED. Germany's strong industrial chemistry infrastructure, world-leading chemical engineering firms (BASF), and university-industry linkages made it the natural locus; Britain and France had comparable high-pressure engineering capability but weaker integration of academic thermodynamics with industrial scale-up.

Prerequisite technologies:
- Industrial hydrogen production (water-gas or coke-oven byproduct) [~1880s] — external/team-reachable
- High-pressure vessel and valve engineering (>150 atm, steel alloy vessels) [~1880–1895] — external/team-reachable
- Seamless steel tube and thick-walled cylinder manufacture [~1885–1895] — external/team-reachable
- Reciprocating compressor technology capable of >200 atm [~1890–1900] — external/team-reachable
- Industrial nitrogen separation from air (Linde liquefaction / fractionation) [1895] — external/team-reachable
- Iron-based heterogeneous catalyst preparation and promotion (K2O, Al2O3 doping) [empirically discoverable within 3–5 year systematic screen] — team-reachable
- Heat-exchanger / recuperator design for gas recycling [~1870s–1890s] — external/team-reachable
- Recycle-loop reactor engineering (unreacted gas recirculation) [~1900, conceptually straightforward] — team-reachable

Scientific theories / key empirical observations:
- Le Chatelier's principle (equilibrium shifts under pressure/temperature) [1884] — external/team-discoverable
- Gibbs free-energy thermodynamics and chemical equilibrium formalism [1876–1878] — external/team-discoverable
- Nernst's thermodynamic calculations of ammonia equilibrium constants [1907; earlier empirical bracketing possible by ~1900] — external/team-discoverable
- Empirical observation that N2 + H2 → NH3 reaction proceeds measurably above 300°C at elevated pressure [demonstrable by systematic experiment ~1890s] — team-discoverable
- Poisoning and promotion effects in heterogeneous catalysis (Sabatier, Mond, others) [~1895–1905] — external/team-discoverable

Explanation: The binding constraint was the convergence of three independently difficult requirements: (1) high-pressure containment reliably above 150–200 atm, which required seamless-steel and precision-valve technology that matured only in the 1890s; (2) thermodynamic guidance from Le Chatelier's principle (1884) and quantitative equilibrium data, without which an empirical search would waste decades on conditions giving negligible yield; and (3) a promoted iron catalyst, which required a systematic empirical screen (Haber tested hundreds of candidates) but was team-reachable once the thermodynamic window was known. Nernst's 1907 equilibrium calculations were a significant accelerant but not strictly necessary—a well-funded team with Le Chatelier's framework, Gibbs thermodynamics, and access to 1890s high-pressure hardware could have bracketed the optimal pressure-temperature regime empirically by roughly 1895–1900 and found a workable promoted-iron catalyst within a further five-year campaign, placing the earliest plausible date around 1895–1905. The gap from the earliest plausible date to the actual date (1909) is modest and reflects the real historical difficulty of the catalyst screen and scale-up engineering rather than any missing scientific framework; no serendipitous accident flag is warranted."""
    },
    {
        "invention": "First static-image television transmission",
        "year": 1909,
        "inventor": "Georges Rignoux & A. Fournier",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1886–1890",
        "earliest_straightforward": "1895–1905",
        "actual_location": "Paris, France",
        "possible_locations": "United Kingdom; Germany; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. France was a leading center of electrical and optical experimentation in the late 19th century, and Paris had the artisan workshops and telegraph infrastructure required; no geographic mismatch with the actual invention site.",
        "confidence": "Medium",
        "full_text": """Invention: First static-image television transmission
Year actually invented: 1909
Earliest plausible: 1886–1890
Earliest straightforward: 1895–1905
Confidence: Medium
Actual location: Paris, France
Possible locations at earliest plausible date: United Kingdom, Germany, France, United States
Geographic note: ALIGNED. France was a leading center of electrical and optical experimentation in the late 19th century, and Paris had the artisan workshops and telegraph infrastructure required; no geographic mismatch with the actual invention site.

Prerequisite technologies:
- Selenium photoconductivity (Willoughby Smith / May, 1873) [1873] — external
- Selenium cell fabrication as practical photoresistor [~1875–1878] — external/team-reachable
- Nipkow scanning disc patent [1884] — external
- Electrical telegraph and synchronization techniques [1840s–1870s] — external
- Galvanometer / sensitive current detector for receiver [1820s–1870s] — external
- Mechanical clockwork / synchronous motor drive for scanning disc [1870s–1880s] — external
- Multi-element array wiring and switching (matrix addressing of 64 cells) [1880s] — team-reachable within five years

Scientific theories / key empirical observations:
- Selenium photoconductivity (resistance varies with light intensity) [1873] — external
- Ohm's Law and basic circuit theory sufficient for operation [1827] — external
- Persistence of vision / image decomposition into discrete elements (conceptual basis) [1870s popular science] — external
- Synchronization requirement for scanning transmitter and receiver (empirical, derivable from telegraph practice) — team-discoverable

Explanation: The binding constraint is the confluence of the Nipkow disc (1884) and reliable selenium cell fabrication mature enough to build a 64-element receiver array with adequate sensitivity. Selenium photoconductivity was published in 1873 and practical selenium cells were demonstrated by the late 1870s, but producing 64 matched, stable cells with consistent sensitivity required refined fabrication technique that was not routine until the early-to-mid 1880s. Once the Nipkow disc appeared in 1884 and provided the conceptual and mechanical framework for sequential spatial scanning, a motivated team with access to a precision instrument workshop could, within five years, combine synchronous mechanical scanning at the transmitter with a switched selenium-cell array at the receiver and telegraph-grade electrical transmission between them — no new science required, only careful empirical iteration on cell matching, synchronization, and signal sensitivity. The earliest plausible window is therefore 1886–1890, immediately after Nipkow; the later straightforward range (1895–1905) reflects the additional time needed for selenium-cell fabrication methods and synchronous motor drives to become widely available to a non-specialist workshop."""
    },
    {
        "invention": "Cloud chamber",
        "year": 1911,
        "inventor": "CTR Wilson",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1897–1902",
        "earliest_straightforward": "1903–1908",
        "actual_location": "Cambridge, England",
        "possible_locations": "England; Germany; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The earliest plausible window centers on Cambridge and similar university workshop environments in Western Europe and the United States, all of which had access to Wilson's 1897 published results, X-ray sources, and skilled glassblowers by 1897–1900.",
        "confidence": "Medium",
        "full_text": """Invention: Cloud chamber (Wilson cloud chamber)
Year actually invented: 1911
Earliest plausible: 1897–1902
Earliest straightforward: 1903–1908
Confidence: Medium
Actual location: Cambridge, England
Possible locations at earliest plausible date: England, Germany, France, United States
Geographic note: ALIGNED. The earliest plausible window centers on Cambridge and similar university workshop environments in Western Europe and the United States, all of which had access to Wilson's 1897 published results, X-ray sources, and skilled glassblowers by 1897–1900.
Prerequisite technologies:
- High-quality optical glass vessels and precision glassblowing [~1880s] — external/team-reachable
- Piston or diaphragm mechanism for rapid adiabatic expansion [~1880s] — external/team-reachable
- Vacuum pump and pressure control hardware [~1850s] — external/team-reachable
- X-ray source (Röntgen tube) for ionizing the gas [1895] — external/team-reachable
- Photographic plate or ground-glass screen for track recording [~1880s] — external/team-reachable
Scientific theories / key empirical observations:
- Adiabatic expansion produces supersaturation and condensation (Aitken nucleation work) [1880–1888] — external/team-discoverable
- Ions act as condensation nuclei in supersaturated vapor (Wilson, published 1897) [1897] — external/team-discoverable
- X-rays and radioactive emissions ionize gas (Röntgen 1895, Becquerel 1896) — external/team-discoverable
Explanation: The binding item is Wilson's 1897 published result that ions serve as condensation nuclei in a supersaturated water-vapor expansion chamber. Once that finding entered the public literature, a directed team of motivated engineers and skilled instrument-makers faced no remaining scientific unknowns: the adiabatic-expansion technique was established by Aitken's nucleation studies in the 1880s, X-ray tubes provided a controllable ionizing source from 1895 onward, and the mechanical and optical components (glass vessels, expansion pistons, photographic recording) were all off-the-shelf workshop capabilities. A competent team working from Wilson's 1897 paper could have designed, iterated, and optimized a functional particle-track chamber within three to five years, placing the earliest plausible date at 1897–1902. The straightforward window is pushed to 1903–1908 because achieving clean, reproducible tracks—rather than mere droplet clouds—required iterative calibration of expansion ratio, vapor pressure, and illumination geometry that Wilson himself took several years to refine even with full knowledge of the principle; a fresh team would face the same empirical iteration. The original discovery required Wilson's particular curiosity-driven program of atmospheric optics research, but that serendipitous origin is irrelevant post-1897 because the phenomenon and the instrument concept were already in the published record and available for deliberate engineering reproduction."""
    },
    {
        "invention": "Electric slot cars",
        "year": 1912,
        "inventor": "Lionel Corporation",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1887–1892",
        "earliest_straightforward": "1893–1898",
        "actual_location": "New York, USA",
        "possible_locations": "United Kingdom; Germany; USA",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA, UK, and Germany all had mature electrical manufacturing industries and toy/model engineering traditions by the late 1880s; the actual inventor (Lionel, New York) fits squarely within this cluster.",
        "confidence": "High",
        "full_text": """Invention: Electric slot cars (electric toy train on slotted track)
Year actually invented: 1912
Earliest plausible: 1887–1892
Earliest straightforward: 1893–1898
Confidence: High
Actual location: New York, USA
Possible locations at earliest plausible date: United Kingdom, Germany, USA
Geographic note: ALIGNED. The USA, UK, and Germany all had mature electrical manufacturing industries and toy/model engineering traditions by the late 1880s; the actual inventor (Lionel, New York) fits squarely within this cluster.

Prerequisite technologies:
- Small DC electric motors (fractional-horsepower, fingertip-scale) [1880–1885] — external; commercially available from multiple manufacturers by mid-1880s
- Insulated two-rail track construction with reliable electrical isolation between rails [1880s] — team-reachable; straightforward adaptation of full-scale railway practice using shellac or rubber insulation
- Sliding/rolling current-pickup contacts (brushes, wipers) [1879–1882] — external; used in dynamos and early electric streetcar experiments
- Pressed or drawn sheet-metal track fabrication [1870s] — external; standard tinplate toy industry technique
- Center-slot guide channel in tinplate track [team-reachable in 1–2 years] — team-reachable; trivial stamping modification to existing toy rail profiles
- Small dry-cell or wet-cell batteries sufficient to power a fingertip motor [1880s] — external; Leclanché cells widely available from ~1868; improved zinc-carbon cells by 1880s
- Rubber or shellac wire insulation for low-voltage wiring [1870s] — external

Scientific theories / key empirical observations:
- Ohm's Law and basic DC circuit behavior [published 1827, textbook-standard by 1860s] — external
- Empirical observation that small motors scale approximately with volume (torque) but weight scales with cube of size, so miniaturization is viable for light loads [known empirically by 1880s] — external
- Contact resistance at sliding pickups manageable at low voltage if contact area and spring pressure are sufficient [demonstrated in dynamo brush practice by 1879] — external

Explanation: The binding constraint was not any single unavailable component but the commercial motivation to combine existing elements at fingertip scale. Every prerequisite — small DC motors, tinplate track stamping, sliding current pickups, and low-voltage insulation — was available by roughly 1885–1887. A motivated team could stamp a slotted two-rail tinplate track using existing toy-industry tooling, wind a small laminated-armature motor to fit inside a cast or pressed car body, and connect pickup pins to the motor brushes without requiring any new science or a second layer of precursor invention. The straightforward date is pushed slightly later (1893–1898) because the market signal — that electrically powered novelty toys were commercially viable — was only clearly established after the 1893 Chicago World's Fair electrification boom and the concurrent success of early electric streetcar toys; before that a workshop would have needed independent entrepreneurial vision to pursue the concept. The ~20-year gap between earliest plausible (1887) and actual invention (1912) is explained by market timing and capitalization rather than technical impossibility: Lionel's founder Joshua Cowen was motivated by the retail demonstration novelty market that crystallized around 1900, not by any technical breakthrough that finally unlocked the design."""
    },
    {
        "invention": "First articulated electric trams",
        "year": 1912,
        "inventor": "Boston Elevated Railway",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1893–1897",
        "earliest_straightforward": "1897–1902",
        "actual_location": "Boston, Massachusetts, USA",
        "possible_locations": "USA (Boston, Philadelphia, Chicago); United Kingdom (London, Glasgow); Germany (Berlin, Hamburg); Belgium (Brussels)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA had dense urban electric tram networks and strong car-building industry by the mid-1890s; Boston specifically was an early adopter of electric traction and had the operational incentive of high-capacity urban corridors. Europe (Germany, Belgium) had comparable engineering capacity and dense city networks.",
        "confidence": "Medium",
        "full_text": """Invention: First articulated electric trams
Year actually invented: 1912
Earliest plausible: 1893–1897
Earliest straightforward: 1897–1902
Confidence: Medium
Actual location: Boston, Massachusetts, USA
Possible locations at earliest plausible date: USA (Boston, Philadelphia, Chicago), United Kingdom (London, Glasgow), Germany (Berlin, Hamburg), Belgium (Brussels)
Geographic note: ALIGNED. The USA had dense urban electric tram networks and strong car-building industry by the mid-1890s; Boston specifically was an early adopter of electric traction and had the operational incentive of high-capacity urban corridors. Europe (Germany, Belgium) had comparable engineering capacity and dense city networks.
Prerequisite technologies:
- Electric street railway (overhead trolley) [1888, Frank Sprague, Richmond VA] — external
- Articulated joint / flexible gangway for railway carriages [1870s–1880s, various] — external
- Bogies / swiveling trucks for street railways [1880s–1890s] — external
- Brill and Pullman-type semi-permanent car coupling technology [1880s–1890s] — external
- Flexible electrical conduit and inter-car wiring connectors [1880s–1890s] — external
Scientific theories / key empirical observations:
- No new science required; all phenomena (electromagnetism, mechanical engineering of pivoting joints) were thoroughly understood by 1888 — external
- Empirical understanding of bogie geometry and curve negotiation for articulated loads [1880s, railway engineering practice] — external/team-discoverable
- Load distribution across shared bogie under traction and braking forces — team-discoverable by iteration
Explanation: The binding constraint was not scientific but operational and institutional. Every individual component — electric traction, flexible articulated joints, shared bogies, inter-car electrical connections — existed independently by the early 1890s. A motivated team could have combined them by roughly 1893–1897, with the main engineering challenge being the design of a shared bogie that handles both the pivoting articulation geometry and the traction/braking forces without binding on tight urban curves; this is a mechanical iteration problem solvable empirically within a five-year workshop program. The actual 15–20 year gap between the maturity of electric trams (1888–1893) and the 1912 Boston car reflects institutional inertia: transit operators were satisfied with two-axle single-body cars, car builders had no commercial incentive to redesign their product lines, and regulatory/track gauge constraints discouraged longer vehicles. No serendipitous discovery was required and no missing science held the concept back; the delay was purely one of perceived operational need meeting available engineering will."""
    },
    {
        "invention": "Bergius high-pressure coal hydrogenation process",
        "year": 1913,
        "inventor": "Friedrich Bergius",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1910–1915",
        "earliest_straightforward": "1913–1918",
        "actual_location": "Germany (Hannover/Rheinau)",
        "possible_locations": "Germany; United Kingdom; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Germany in this era led in industrial chemistry, high-pressure engineering, and coal chemistry, with the necessary academic-industrial infrastructure concentrated in the same region where Bergius worked.",
        "confidence": "High",
        "full_text": """Invention: Bergius high-pressure coal hydrogenation process
Year actually invented: 1913
Earliest plausible: 1910–1915
Earliest straightforward: 1913–1918
Confidence: High
Actual location: Germany (Hannover/Rheinau)
Possible locations at earliest plausible date: Germany, United Kingdom, France, United States
Geographic note: ALIGNED. Germany in this era led in industrial chemistry, high-pressure engineering, and coal chemistry, with the necessary academic-industrial infrastructure concentrated in the same region where Bergius worked.
Prerequisite technologies:
- High-pressure vessel fabrication (200–700 atm sustained) [1909–1912] — team-reachable, requires extending Haber-Bosch vessel technology upward in pressure rating; one layer of precursor development
- Hydrogen gas production at scale (steam reforming, water-gas shift, electrolysis) [~1900s] — external
- Coal pulverization and slurry-handling equipment [~1880s–1900s] — external
- Iron/tin catalyst preparation and handling under pressure [~1900s] — external
- High-temperature, high-pressure valve and seal engineering [~1900s–1910s] — team-reachable
Scientific theories / key empirical observations:
- Sabatier catalytic hydrogenation of organic compounds [1897] — external
- Haber-Bosch demonstration that sustained industrial high-pressure synthesis is feasible [1909] — external (binding enabling observation)
- Empirical coal chemistry and carbonization knowledge [~1880s–1900s] — external
- Thermodynamic understanding of hydrogenation equilibria at elevated temperature and pressure [~1900s] — external
Explanation: The binding constraint was the engineering demonstration that extreme-pressure vessels (well above 200 atm) could be safely fabricated, operated continuously, and sealed against hydrogen embrittlement and leakage — a problem distinct from Haber-Bosch in degree if not in kind. Before the Haber-Bosch process proved in 1909 that sustained high-pressure industrial synthesis was achievable, no team could have credibly designed or commissioned the pressure vessels Bergius required, and hydrogen embrittlement of steel at these conditions was not yet an understood engineering problem with known mitigations. Sabatier's 1897 catalytic hydrogenation work supplied the chemical concept, and Bergius himself acknowledged the Haber-Bosch demonstration as the direct inspiration; with both pieces in hand by 1909–1910, a well-resourced German industrial chemistry team could in principle have begun the empirical pressure-vessel scaling and coal slurry trials within five years. The earliest plausible date is therefore 1910–1915, essentially coinciding with the actual invention, because no earlier enabling foundation existed for the high-pressure engineering side, and no location outside the industrial-chemistry powerhouses of Germany, the UK, France, or the United States had the requisite workshop capacity."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
