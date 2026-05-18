#!/usr/bin/env python3
"""Write batch 20 (indices 133-139) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Kaplan axial-flow adjustable blade turbine",
        "year": 1913,
        "inventor": "Viktor Kaplan",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1885–1895",
        "earliest_straightforward": "1895–1905",
        "actual_location": "Austria (Brünn/Brno)",
        "possible_locations": "United Kingdom; Germany; France; Austria-Hungary; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Austria-Hungary had strong mechanical engineering capacity by the 1880s–1890s, with Brno specifically hosting significant industrial infrastructure; the invention fits squarely within the Central European hydraulic engineering tradition that produced the Francis turbine refinements of the same era.",
        "confidence": "Medium",
        "full_text": """Invention: Kaplan axial-flow adjustable-blade turbine
Year actually invented: 1913
Earliest plausible: 1885–1895
Earliest straightforward: 1895–1905
Confidence: Medium
Actual location: Austria (Brünn/Brno)
Possible locations at earliest plausible date: United Kingdom, Germany, France, Austria-Hungary, United States
Geographic note: ALIGNED. Austria-Hungary had strong mechanical engineering capacity by the 1880s–1890s, with Brno specifically hosting significant industrial infrastructure; the invention fits squarely within the Central European hydraulic engineering tradition that produced the Francis turbine refinements of the same era.
Prerequisite technologies:
- Francis inward-flow reaction turbine [1849] — external/team-reachable
- Pelton impulse wheel [1870s] — external/team-reachable
- Precision machined bevel gears and pivot bearings (for blade-pitch adjustment mechanism) [1860s–1870s] — external/team-reachable
- Hydraulic governing and servo-actuator systems (for dynamic blade adjustment under load) [1870s–1880s] — external/team-reachable
- Cast-iron and later steel fabrication for large runner hubs [1860s] — external/team-reachable
- Sealed shaft and hub lubrication systems under water pressure [1870s] — external/team-reachable
Scientific theories / key empirical observations:
- Rankine's vortex and momentum theory of turbomachinery [1865] — external/team-reachable
- Reynolds's pipe-flow and turbulence theory [1883] — external/team-reachable
- Empirical observation that axial-flow propeller geometry produces high specific speed suitable for low-head, high-discharge sites [observable by ~1880 via marine screw propeller analogy] — external/team-discoverable
- Hydraulic similarity laws (specific speed, affinity laws) allowing scale-model testing [1870s–1880s] — external/team-reachable
- Blade-element / lifting-line theory for propeller blade profiling [early 1900s, Drzewiecki 1892 preliminary work] — external/team-discoverable at earlier date via empirical iteration
Explanation: The binding constraint was not the adjustable-pitch mechanism in isolation — variable-pitch propellers had marine precedents by the 1840s (Griffiths/Smith adjustable ship propellers) and precision pivot bearings were available well before 1885. The true binding item was the convergence of three things simultaneously: (1) recognition that an axial-flow propeller geometry, rather than the dominant centrifugal/mixed-flow Francis geometry, was hydraulically superior for very low heads (roughly under 10 m) and high volumetric flow, (2) the availability of hydraulic similarity scaling laws and laboratory flume testing infrastructure that allowed iterative empirical optimization of blade profile and hub geometry without requiring full-scale builds, and (3) the practical sealing and mechanical linkage problem of transmitting blade-pitch adjustment forces through a rotating hub submerged under water pressure — solvable with 1880s workshop practice but requiring non-trivial ingenuity. A motivated team working from Rankine momentum theory, marine propeller empiricism, and Francis turbine hydraulic test data could plausibly have reached a working axial-flow adjustable-blade runner by the late 1880s to mid-1890s; the "straightforward" range shifts to 1895–1905 because the hydraulic similarity framework and precision hub machining were more mature by then, reducing the iteration burden. The ~18–28 year gap between earliest plausible and actual (1913) is explained primarily by the fact that low-head hydroelectric development was not economically urgent until widespread rural electrification demand emerged in the 1900s, removing the market incentive that would have motivated earlier focused development."""
    },
    {
        "invention": "Stainless Steel",
        "year": 1915,
        "inventor": "Harry Brearley",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1895–1905",
        "earliest_straightforward": "1905–1912",
        "actual_location": "Sheffield, England",
        "possible_locations": "England (Sheffield); France (Paris); Germany (Essen/Krupp works); United States (Pittsburgh)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Sheffield was the world center of specialty steel production and had the metallurgical expertise, industrial infrastructure, and motivated commercial demand to have pursued this work earliest; the actual invention there is fully consistent with the earliest plausible location.",
        "confidence": "Medium",
        "full_text": """Invention: Stainless steel
Year actually invented: 1915
Earliest plausible: 1895–1905
Earliest straightforward: 1905–1912
Confidence: Medium
Actual location: Sheffield, England
Possible locations at earliest plausible date: England (Sheffield), France (Paris), Germany (Essen/Krupp works), United States (Pittsburgh)
Geographic note: ALIGNED. Sheffield was the world center of specialty steel production and had the metallurgical expertise, industrial infrastructure, and motivated commercial demand to have pursued this work earliest; the actual invention there is fully consistent with the earliest plausible location.
Prerequisite technologies:
- Bessemer / open-hearth steelmaking [1856/1860s] — external
- Industrial chromium metal production (Moissan electrothermic furnace) [1893–1895] — external
- Ferrochromium alloy production at scale [1880s–1890s] — external
- Systematic alloy composition testing with controlled carbon content [1880s] — team-reachable
- Acid / salt corrosion testing protocols for metals [well-established by 1880s] — external
Scientific theories / key empirical observations:
- Faraday observation that chromium additions improve corrosion resistance in iron alloys [1822] — external
- Berthier chromium-iron alloy corrosion work [1821] — external
- Moissan high-chromium iron alloys (~60% Cr) demonstrating chromium incorporation into steel matrix [1890s] — external
- Hadfield systematic chromium-steel studies (hardness, brittleness at varying Cr %) [1892] — external
- Empirical recognition that passive oxide films protect metals (general principle understood by 1880s) — external
- Low-carbon requirement for workable chromium steel (team-discoverable by iteration within 2–3 years) — team-reachable
Explanation: By the mid-1890s every binding prerequisite was in place: Faraday and Berthier had publicly flagged chromium's corrosion-resistance effect as early as 1821–1822, Moissan's furnace made high-purity ferrochromium commercially available around 1893–1895, and Sheffield workshops already possessed open-hearth furnaces capable of making low-carbon steel. A directed program — "find a steel alloy resistant to acid and salt corrosion for cutlery or chemical plant use" — staffed by a motivated Sheffield steelmaster and skilled metallurgists would have systematically swept chromium content from ~5% to ~20% while controlling carbon; within the five-year window they would empirically discover the sharp passivation threshold near 10.5% Cr and the necessity of keeping carbon below ~0.1% for workability. The serendipity in Brearley's actual discovery (he noticed undissolved specimens in a scrap pile) was incidental, not structurally necessary; a corrosion-testing protocol would have reproduced the same result by design. The gap between earliest plausible (~1895) and actual (1915) is roughly 20 years, explained primarily by the absence of a commercially motivated, directed corrosion-resistance research program — metallurgists were pursuing hardness and strength, not corrosion resistance — rather than any missing science or technology."""
    },
    {
        "invention": "First practical battle tanks",
        "year": 1915,
        "inventor": "Walter Wilson & William Tritton; Eugène Brillié",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1885–1895",
        "earliest_straightforward": "1900–1910",
        "actual_location": "Lincoln, England / Bordeaux, France",
        "possible_locations": "United Kingdom; France; Germany; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in the UK and France, both of which had the industrial capacity, steel manufacturing, and military-industrial investment necessary at the earliest plausible date. No mismatch.",
        "confidence": "Medium",
        "full_text": """Invention: First practical battle tanks
Year actually invented: 1915
Earliest plausible: 1885–1895
Earliest straightforward: 1900–1910
Confidence: Medium
Actual location: Lincoln, England / Bordeaux, France
Possible locations at earliest plausible date: United Kingdom, France, Germany, United States
Geographic note: ALIGNED. The actual invention occurred in the UK and France, both of which had the industrial capacity, steel manufacturing, and military-industrial investment necessary at the earliest plausible date. No mismatch.

Prerequisite technologies:
- Continuous track / caterpillar tread concept [1770s–1880s, practical: 1901–1904] — team-reachable; empirical iteration on linked-plate or belt tracks over rough terrain was feasible before Lombard/Holt; the core idea of distributing weight over a moving belt was patented in various forms from the 1850s onward
- Internal combustion engine (practical, vehicle-grade) [1885–1886, Daimler/Benz] — external; by 1885 a motivated team could source or replicate a working petrol engine; steam traction engines were available earlier but do not qualify (see Explanation)
- Rolled homogeneous armor steel (face-hardened plate) [1890s] — external; naval armor steel was mature by the 1880s; scaling down to vehicle panels was an engineering, not scientific, challenge
- Differential steering / clutch-and-brake track steering [1890s–1900s] — team-reachable; agricultural and traction-engine steering mechanisms provided the empirical base; a one-layer derivation for tracked steering is within team scope
- Wheeled armored vehicles / armored trains [1890s] — external; armored trains were common in colonial warfare (1880s–1890s); armored motor cars appeared ~1900; the concept of a mobile armored fighting platform was militarily established
- Machine gun (portable, reliable) [1884, Maxim] — external; by 1884 a crew-served automatic weapon suitable for vehicle mounting existed
- Spring/suspension load management for heavy tracked chassis [1900s] — team-reachable; one layer of empirical iteration from traction engine suspension

Scientific theories / key empirical observations:
- Ground pressure distribution principle (weight spread over track contact area reduces sinkage in soft ground) [empirical, well-understood by 1880s agricultural engineers] — team-discoverable through direct field testing
- Internal combustion thermodynamics (Otto cycle) [1876] — external; practically demonstrated; team needs engineering application, not new science
- Ballistic protection (plate thickness vs. projectile energy) [empirical naval/fortress data, 1860s–1880s] — external; sufficient empirical tables existed from ironclad warship experience
- Engine power-to-weight scaling (the binding empirical constraint) [1885–1910, iterative] — team-discoverable; early ICEs had poor power-to-weight; achieving ~10–15 hp/ton to move a 15–25 ton armored vehicle required iterative engine and drivetrain development, achievable within a 5-year motivated program by ~1895 with the Daimler-era engine base

Explanation: The binding constraint was not any single missing scientific insight but the convergence of engine power-to-weight ratio with the mechanical reliability of continuous tracks under load. Steam traction engines, while available from the 1860s–1870s, cannot substitute for the ICE in this context: a steam traction engine capable of hauling a 15–20 ton armored fighting vehicle cross-country would itself weigh 20–40 tons, require a tender for coal and water, demand a crew of stokers, and need water replenishment every 1–3 hours — disqualifying it from the "practical" designation regardless of mechanical feasibility. The ICE (Daimler, 1885) is therefore the binding lower bound because it is the earliest power plant with sufficient power-to-weight for a field-operable armored tracked vehicle; before 1885, no available prime mover meets the "practical" qualifier. By 1885, all necessary scientific knowledge existed: the Otto-cycle engine, face-hardened armor steel, the caterpillar-track concept, and the Maxim gun. What was absent was a working integration: early ICEs produced insufficient torque and were mechanically fragile under the vibration and load of a heavy cross-country vehicle, and no one had built a tracked chassis robust enough to carry armor plate over broken ground. A motivated team starting in 1885 — drawing on Daimler engines, naval armor plate scaled to vehicle dimensions, and the empirical track-laying work already visible in agricultural machinery — could plausibly have produced a functional if crude armored tracked vehicle within five years, placing the earliest plausible date at approximately 1885–1895. The straightforward window (1900–1910) reflects the point at which Holt/Lombard tractors had already demonstrated reliable tracked locomotion in commercial use, armor steel was standardized, and medium-weight petrol engines were off-the-shelf; a team in that window faced an operational concept gap (military resistance to novel weapons) more than a technical one."""
    },
    {
        "invention": "Czocharlski crystal pulling",
        "year": 1916,
        "inventor": "Jan Czochralski",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1895–1910",
        "earliest_straightforward": "1905–1915",
        "actual_location": "Frankfurt, Germany",
        "possible_locations": "Germany; United Kingdom; France; Austria-Hungary",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Germany was a world leader in industrial chemistry and metallurgy in the late 19th century, and the actual invention occurred there; a motivated team with comparable resources would most plausibly have been located in Germany, the UK, France, or Austria-Hungary.",
        "confidence": "Medium",
        "full_text": """Invention: Czochralski crystal pulling process
Year actually invented: 1916
Earliest plausible: 1895–1910
Earliest straightforward: 1905–1915
Confidence: Medium
Actual location: Frankfurt, Germany
Possible locations at earliest plausible date: Germany, United Kingdom, France, Austria-Hungary
Geographic note: ALIGNED. Germany was a world leader in industrial chemistry and metallurgy in the late 19th century, and the actual invention occurred there; a motivated team with comparable resources would most plausibly have been located in Germany, the UK, France, or Austria-Hungary.
Prerequisite technologies:
- High-temperature crucible furnaces capable of melting metals (tin mp 232°C, lead mp 327°C) [ancient–pre-1800] — external/team-reachable
- Precision temperature measurement (thermocouples, pyrometers) [1821–1870s] — external/team-reachable
- Controlled mechanical pulling/lifting apparatus (screw mechanisms, clockwork drives) [pre-1800, refined 1800s] — external/team-reachable
- Controlled atmospheric enclosures (to reduce oxidation) [1880s–1890s] — external/team-reachable
- Seed crystal preparation and handling techniques [1880s] — external/team-reachable
Scientific theories / key empirical observations:
- Crystallographic theory and unit cell concepts (Haüy, Bravais) [1784–1848] — external/team-discoverable
- Empirical observation that slow, controlled solidification produces larger single crystals [mid-1800s] — external/team-discoverable
- Metal solidification and dendrite suppression studies (Tammann's work on crystallization rates) [1890s–1900s] — external/team-discoverable
- Recognition that a seed crystal can orient and propagate a single-crystal lattice [1890s] — external/team-discoverable
- Le Chatelier and Roberts-Austen work on thermal analysis and cooling curves [1887–1899] — external/team-discoverable
Explanation: The Czochralski process requires no exotic science: melting a low-melting-point metal (tin), maintaining temperature just above the melting point using a thermocouple-regulated furnace (available by the 1870s–1890s), touching a seed crystal to the melt surface, and withdrawing it slowly with a mechanical puller while rotating — all of which are within reach of a motivated metallurgist-engineer team by approximately 1895–1910. Tammann's extensive work on crystallization kinetics (published from the 1890s onward) provided the empirical framework for understanding why slow pulling produces single crystals. The binding item is the convergence of precise near-melting-point temperature control with a slow, steady mechanical pulling mechanism; both were available by roughly 1895. Although Czochralski's actual discovery arose from accidentally dipping his pen into molten tin, this accident was not structurally necessary for a directed team: a systematic program of crystal-growth-from-melt experiments — a natural extension of Tammann's published crystallization work — would have explored pulling, zone-refining, and withdrawal geometries as a matter of course. The pulling geometry would have been a foreseeable test within a ~5-year systematic program, placing the earliest plausible date at 1895–1910. The straightforward window (1905–1915) reflects the point at which Tammann's crystallization kinetics framework was fully published and precision thermocouple-regulated furnaces were standard laboratory equipment."""
    },
    {
        "invention": "Crystal oscillator",
        "year": 1917,
        "inventor": "Alexander Nicholson",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1909–1912",
        "earliest_straightforward": "1912–1915",
        "actual_location": "New York, USA",
        "possible_locations": "USA (New York, Pittsburgh); UK (London); Germany (Berlin, Munich); France (Paris)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in the USA, which by 1909–1912 had mature electrical engineering infrastructure, leading vacuum tube development, and strong industrial research labs (AT&T, GE, Westinghouse) capable of supporting this work.",
        "confidence": "Medium",
        "full_text": """Invention: Crystal oscillator (quartz/Rochelle salt piezoelectric frequency standard)
Year actually invented: 1917
Earliest plausible: 1909–1912
Earliest straightforward: 1912–1915
Confidence: Medium
Actual location: New York, USA
Possible locations at earliest plausible date: USA (New York, Pittsburgh), UK (London), Germany (Berlin, Munich), France (Paris)
Geographic note: ALIGNED. The actual invention occurred in the USA, which by 1909–1912 had mature electrical engineering infrastructure, leading vacuum tube development, and strong industrial research labs (AT&T, GE, Westinghouse) capable of supporting this work.
Prerequisite technologies:
- Piezoelectric effect (published knowledge) [1880] — external (Curie brothers; off-limits for team discovery, but fully usable as published knowledge by 1880)
- Rochelle salt crystal preparation and quartz cutting/grinding to precise dimensions [1880s–1900s] — team-reachable (precision mechanical grinding and crystallography techniques existed; iterative empirical refinement is within team scope)
- De Forest triode vacuum tube (amplifier capable of sustaining oscillation) [1906] — external (binding prerequisite; no sustained electronic feedback oscillator is possible without a gain element)
- Feedback/regenerative circuit topology (positive feedback sustaining oscillation at resonant frequency) [1912–1913, Armstrong/Meissner/De Forest independent discoveries] — team-discoverable (regeneration emerges naturally from device iteration with triodes; the insight was simultaneously and independently reached by at least three experimenters in 1912–1913, indicating it is readily discoverable by any competent triode user within a few years of tube availability)
- Stable DC power supply sufficient for vacuum tube operation [1900s] — team-reachable (rectified mains or battery supplies existed)
- Frequency measurement instrumentation (wavemeter, resonant cavity, comparison to tuning fork standard) [1900s] — team-reachable
Scientific theories / key empirical observations:
- Piezoelectricity: mechanical stress on certain crystals produces a charge, and conversely an applied field produces mechanical deformation [1880] — external/not team-discoverable (Curie brothers; off-limits phenomenon, but published and usable)
- Mechanical resonance and Q-factor: a crystal has a very sharp mechanical resonance with high Q, yielding frequency stability superior to LC circuits [empirically observable, 1880s onward] — team-discoverable by empirical observation once piezoelectricity is known
- Barkhausen/triode oscillation conditions: gain × feedback ≥ 1 sustains oscillation [1913–1915] — team-discoverable (the condition emerges empirically from triode device testing; Armstrong, Meissner, and De Forest all discovered it independently in 1912–1913 within months of each other, confirming it is readily discoverable rather than requiring a unique insight)
- Crystal equivalent circuit (motional impedance model): the crystal behaves as a very high-Q series RLC resonator, explainable without new science once the piezoelectric effect and mechanical resonance are accepted [team-discoverable by empirical iteration post-1906]
Explanation: The binding constraint is the De Forest triode (1906), not the piezoelectric effect or crystal preparation. Piezoelectricity had been published since 1880 and quartz/Rochelle salt preparation was iteratively reachable. However, without a vacuum tube capable of amplification and sustained feedback oscillation, a crystal can only be driven passively as a filter or detector — it cannot serve as a self-sustaining frequency standard. Once the triode was available (post-1906), a motivated team working with triode circuits would empirically discover positive feedback oscillation within a few years of experimentation — the regenerative circuit was independently discovered by Armstrong, Meissner, and De Forest in 1912–1913, demonstrating it is team-discoverable rather than requiring a unique published source. Allowing roughly two to three years for the team to combine the triode (1906) with empirical feedback discovery and crystal grinding yields an earliest plausible date of 1909–1912. The straightforward window (1912–1915) reflects the point at which the regenerative topology had been published and verified by multiple groups. No new scientific framework is required. No serendipitous accident is implicated. The gap between earliest plausible (~1909) and actual invention (1917) is under ten years and reflects the normal lag between component availability and system-level synthesis."""
    },
    {
        "invention": "Fischer-Tropsch coal-to-liquid process",
        "year": 1925,
        "inventor": "Franz Fischer & Hans Tropsch",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1900–1910",
        "earliest_straightforward": "1910–1920",
        "actual_location": "Germany (Kaiser Wilhelm Institute, Mülheim)",
        "possible_locations": "Germany; United Kingdom; France; Belgium; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in Germany, which was also among the most likely locations at the earliest plausible date given its dominant position in industrial chemistry, coal chemistry, and catalysis research from the late 19th century onward.",
        "confidence": "Medium",
        "full_text": """Invention: Fischer-Tropsch coal-to-liquid process
Year actually invented: 1925
Earliest plausible: 1900–1910
Earliest straightforward: 1910–1920
Confidence: Medium
Actual location: Germany (Kaiser Wilhelm Institute, Mülheim)
Possible locations at earliest plausible date: Germany, United Kingdom, France, Belgium, United States
Geographic note: ALIGNED. The actual invention occurred in Germany, which was also among the most likely locations at the earliest plausible date given its dominant position in industrial chemistry, coal chemistry, and catalysis research from the late 19th century onward.
Prerequisite technologies:
- Coal gasification to syngas (CO + H2) [~1780s–1800s, Murdoch/Leblanc era] — external
- Water-gas process (steam over hot coke) [1873, Thaddeus Lowe] — external
- High-pressure reaction vessels and industrial autoclave engineering [1880s–1890s] — external
- Iron and cobalt as industrial catalysts, basic preparation methods [1890s] — external
- Contact process and industrial heterogeneous catalysis infrastructure [1875–1890s] — external
- Fractional distillation and hydrocarbon product analysis techniques [1860s–1870s] — external
Scientific theories / key empirical observations:
- Sabatier catalytic hydrogenation over nickel/cobalt (CO + H2 → CH4, hydrocarbons) [1897–1902] — external; directly points toward liquid-range products
- Methanation and Fischer's own earlier CO hydrogenation work [1902–1913] — external/team-discoverable
- Bergius high-pressure coal hydrogenation [1913] — external; demonstrates coal → liquid hydrocarbons is chemically achievable
- Water-gas shift equilibrium understood quantitatively [~1900–1910] — external
- Recognition that catalyst choice and operating temperature/pressure shift product distribution toward liquids vs. methane [team-discoverable by systematic empirical iteration, ~1900–1910]
Explanation: The binding constraint was not any missing scientific framework but rather the absence of the key empirical observation — made accessible by Sabatier (1897–1902) — that CO + H2 over metal catalysts produces hydrocarbons beyond methane, combined with the practical insight that tuning catalyst composition (cobalt vs. nickel vs. iron) and moderating temperature suppresses methanation in favor of liquid-range products. A motivated team with access to Sabatier's published results, standard coal-gasification plant technology, and industrial autoclave hardware could in principle have identified the liquid-product regime empirically by ~1900–1910, placing the earliest plausible window there; the straightforward window shifts to 1910–1920 once the Bergius precedent (1913) further validated the coal-to-liquids concept and high-pressure hydrocarbon chemistry became a recognized industrial target. The gap from ~1900 to the actual 1925 date is modest (~15–25 years) and reflects the time required for Fischer's own systematic program of CO hydrogenation studies rather than any hard scientific barrier, so no Flag is warranted."""
    },
    {
        "invention": "Yagi-Uda directional antenna",
        "year": 1926,
        "inventor": "Shintarō Uda with Hidetsugu Yagi",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1905–1910",
        "earliest_straightforward": "1910–1915",
        "actual_location": "Sendai, Japan (Tohoku University)",
        "possible_locations": "United Kingdom; Germany; France; United States; Italy",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. Japan was a plausible but unlikely leader at the earliest plausible date; the dominant RF experimentation centers in 1905–1915 were in Europe and the United States, where Marconi, Braun, and their contemporaries had dense workshop infrastructure and institutional backing.",
        "confidence": "Medium",
        "full_text": """Invention: Yagi-Uda directional antenna
Year actually invented: 1926
Earliest plausible: 1905–1910
Earliest straightforward: 1910–1915
Confidence: Medium
Actual location: Sendai, Japan (Tohoku University)
Possible locations at earliest plausible date: United Kingdom, Germany, France, United States, Italy
Geographic note: MISMATCH. Japan was a plausible but unlikely leader at the earliest plausible date; the dominant RF experimentation centers in 1905–1915 were in Europe and the United States, where Marconi, Braun, and their contemporaries had dense workshop infrastructure and institutional backing.
Prerequisite technologies:
- Half-wave dipole antenna [1886, Hertz] — external
- Tuned circuit / resonant antenna design [1900, Braun/Marconi era] — external
- Continuous-wave (CW) radio transmitters (arc or Alexanderson alternator) [1903–1906] — external
- Wavemeters and calibrated RF measuring instruments [~1900] — external/team-reachable
- Mechanical metal-working to produce accurately spaced parallel rod elements [pre-1900] — team-reachable
Scientific theories / key empirical observations:
- Hertz's demonstration of electromagnetic wave reflection and diffraction [1888] — external
- Empirical observation that a nearby resonant conductor re-radiates and can redirect RF energy (parasitic coupling) [discoverable ~1900–1905 by empirical iteration] — team-discoverable
- Understanding that element spacing (~0.1–0.25 wavelength) and element length detuning determine director vs. reflector behavior [team-discoverable by systematic sweep, ~2–4 years of iteration] — team-discoverable
- Directional gain measurable via comparative field-strength meter readings [team-reachable once CW sources and galvanometer detectors available] — team-reachable
Explanation: The binding constraint is not scientific theory but empirical discovery of parasitic element behavior and the availability of stable continuous-wave RF sources needed to make directional gain measurable. With spark-gap transmitters the broadband, damped-wave output makes systematic directivity measurements noisy and unreliable; a team working after ~1905 would have access to arc transmitters or early alternator sources giving stable CW signals, a wavemeter for tuning, and Hertz's published work on re-radiation from resonant conductors. Given that foundation, a motivated engineer-artisan team could empirically discover that a slightly shortened nearby rod acts as a director and a slightly lengthened one as a reflector through a systematic length-and-spacing sweep — no new science required. The single layer of precursor fabrication (cutting and spacing metallic rod elements to a fraction of a wavelength) is trivially within workshop capability. The gap of roughly 15–20 years between earliest plausible (1905–1910) and actual invention (1926) reflects institutional geography: the insight was available to any competent RF engineering team in Europe or North America well before Uda pursued it, but it was not pursued because the commercial priority of early wireless was omnidirectional coverage (broadcast and ship-to-shore), not directivity, leaving the concept latent until Uda's focused academic investigation."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
