#!/usr/bin/env python3
"""Write batch 18 (indices 119-125) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "First self-sustaining gas turbine",
        "year": 1903,
        "inventor": "Ægidius Elling",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1888–1895",
        "earliest_straightforward": "1895–1903",
        "actual_location": "Norway",
        "possible_locations": "United Kingdom; Germany; France; United States; Sweden",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. Norway was an unusual location for advanced precision engineering at this period; the UK, Germany, and France had far denser concentrations of high-precision machine shops, metallurgical expertise, and steam-turbine manufacturing capability that would have been required. Elling's success in Norway depended on personal genius and access to imported materials and knowledge rather than a deep local industrial ecosystem.",
        "confidence": "Medium",
        "full_text": """Invention: First self-sustaining gas turbine
Year actually invented: 1903
Earliest plausible: 1888–1895
Earliest straightforward: 1895–1903
Confidence: Medium
Actual location: Norway
Possible locations at earliest plausible date: United Kingdom, Germany, France, United States, Sweden
Geographic note: MISMATCH. Norway was an unusual location for advanced precision engineering at this period; the UK, Germany, and France had far denser concentrations of high-precision machine shops, metallurgical expertise, and steam-turbine manufacturing capability that would have been required. Elling's success in Norway depended on personal genius and access to imported materials and knowledge rather than a deep local industrial ecosystem.
Prerequisite technologies:
- Centrifugal blowers and compressors (industrial) [by 1860s] — external/team-reachable
- Steam turbine wheel manufacturing and blade attachment (Parsons 1884, De Laval 1889) [1884–1889] — external/team-reachable
- High-speed precision machining and dynamic balancing techniques [by 1880s] — external/team-reachable
- Pressurized combustion chambers for gaseous/liquid fuels [by 1870s] — external/team-reachable
- Thermodynamic cycle analysis (Rankine, Clausius, Joule-Brayton cycle description 1872) [by 1872] — external/team-reachable
- Heat-resistant nickel and chromium alloy steels (early grades) [by late 1880s–early 1890s] — external/team-reachable
- Precision bearing technology capable of high-temperature, high-speed shafts [by 1885] — external/team-reachable
Scientific theories / key empirical observations:
- Brayton/Joule thermodynamic cycle for gas compression and expansion [1872] — external/team-discoverable
- Empirical understanding of compressor surge and stall (discoverable by iterative testing) — team-discoverable
- Observation that net positive work requires compressor isentropic efficiency sufficiently high to overcome turbine entry temperature limitations — team-discoverable through iterative empirical testing
- Behavior of metals under sustained high-temperature stress (creep) — team-discoverable empirically, though formal theory postdates 1903
Explanation: The binding constraint was the intersection of centrifugal compressor efficiency and turbine-inlet temperature, both of which were gated by materials. Achieving net shaft output requires the turbine to produce more work than the compressor consumes, which demands either a high turbine-inlet temperature or a highly efficient compressor stage — ideally both. Before roughly 1888, no available alloy steel could sustain the combination of ~400–600 °C operating temperature, high rotational stress, and prolonged cyclic loading without rapid creep or fatigue failure; nickel-steel and early chromium-steel alloys reaching adequate grades only appeared in the late 1880s. Simultaneously, centrifugal compressor stage efficiency of ~60–70% (the minimum needed for net output) required precision impeller geometry and tight clearances that depended on the same machine-tool and dynamic-balancing advances that followed the Parsons and De Laval steam turbine programs after 1884. A motivated team with access to a first-class precision engineering workshop — most plausibly in the UK or Germany — could, after 1888, have combined Brayton-cycle analysis, De Laval-style turbine-wheel fabrication, and the best available heat-resistant alloys to build a net-positive gas turbine through iterative empirical development within a five-year window, placing the earliest plausible date at roughly 1888–1895. The task required no new scientific insight, only disciplined engineering iteration."""
    },
    {
        "invention": "Laminated safety glass",
        "year": 1903,
        "inventor": "Édouard Bénédictus",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1870–1880",
        "earliest_straightforward": "1875–1885",
        "actual_location": "Paris, France",
        "possible_locations": "United Kingdom (London/Birmingham); France (Paris); Germany (Berlin/Cologne); United States (New York/Philadelphia)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. France and the broader Western European industrial belt had mature plate glass industries, access to cellulose nitrate chemistry, and the skilled artisan-chemist workshops required. Paris is entirely consistent with the earliest plausible window.",
        "confidence": "Medium",
        "full_text": """Invention: Laminated safety glass
Year actually invented: 1903
Earliest plausible: 1870–1880
Earliest straightforward: 1875–1885
Confidence: Medium
Actual location: Paris, France
Possible locations at earliest plausible date: United Kingdom (London/Birmingham), France (Paris), Germany (Berlin/Cologne), United States (New York/Philadelphia)
Geographic note: ALIGNED. France and the broader Western European industrial belt had mature plate glass industries, access to cellulose nitrate chemistry, and the skilled artisan-chemist workshops required. Paris is entirely consistent with the earliest plausible window.
Prerequisite technologies:
- Plate glass manufacturing (cylinder/cast plate methods) [mature by ~1840] — external
- Cellulose nitrate (collodion) synthesis [1846, Schönbein] — external
- Celluloid sheet production [1870, Hyatt] — external
- Solvent-based adhesive / plasticizer chemistry (camphor-plasticized celluloid) [~1870] — external
- Pressing and clamping jigs for laminating flat sheets [~1850s, standard workshop] — team-reachable
- Controlled drying/curing ovens for solvent evaporation [~1860s, available in industrial workshops] — team-reachable
Scientific theories / key empirical observations:
- Collodion film formation and adhesion to glass surfaces (standard photographic practice) [1851, Archer wet-plate process] — external
- Empirical observation that polymer films retain glass fragments on fracture (discoverable by directed drop-test program) — team-discoverable
- Plasticizer effect of camphor on nitrocellulose reducing brittleness [~1870] — external
- Adhesion mechanics of thin polymer films under stress (no new science required; empirical iteration suffices) — team-discoverable
Explanation: The binding item is the availability of flexible, film-forming cellulose nitrate sheets with adequate adhesion to glass, which arrived in practical form with Hyatt's camphor-plasticized celluloid around 1870. A directed program — motivated by carriage and railway glazing injuries, which were a recognized problem by the 1860s — could have assigned a chemist-artisan team to systematically test candidate interlayer materials (collodion solution cast directly onto glass, thin celluloid sheet pressed between plates, rubber-based films) using simple drop and impact tests. No new scientific framework is required: the adhesion of collodion to glass was already exploited in wet-plate photography from 1851, and the fragment-retention mechanism requires only the empirical observation that a bonded polymer film holds shards in place. The main iterative challenges — achieving uniform bondline thickness, preventing delamination from moisture and heat, and scaling flat-glass pressing — are engineering problems solvable within a five-year workshop program by the mid-1870s. Bénédictus's 1903 discovery was serendipitous in origin but not irreducibly so; the underlying combination of mature plate glass and available cellulose nitrate film was fully in place by ~1870–1875, placing the earliest plausible date in that window."""
    },
    {
        "invention": "First sustained, controlled powered flight",
        "year": 1903,
        "inventor": "Orville and Wilbur Wright",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1890–1900",
        "earliest_straightforward": "1897–1903",
        "actual_location": "Kitty Hawk, North Carolina, USA",
        "possible_locations": "United Kingdom; France; Germany; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA was a plausible location given its strong mechanical workshop culture, access to lightweight engine technology, and the active aeronautical community by the late 1890s; France and Germany were equally or more likely given their stronger engineering institutions and earlier glider traditions.",
        "confidence": "Medium",
        "full_text": """Invention: First sustained, controlled powered flight (airplane)
Year actually invented: 1903
Earliest plausible: 1890–1900
Earliest straightforward: 1897–1903
Confidence: Medium
Actual location: Kitty Hawk, North Carolina, USA
Possible locations at earliest plausible date: United Kingdom, France, Germany, United States
Geographic note: ALIGNED. The USA was a plausible location given its strong mechanical workshop culture, access to lightweight engine technology, and the active aeronautical community by the late 1890s; France and Germany were equally or more likely given their stronger engineering institutions and earlier glider traditions.
Prerequisite technologies:
- Lightweight steam engine (sufficient power-to-weight) [1860s–1870s] — external/team-reachable, though marginal; gasoline engine preferred
- Practical internal combustion / gasoline engine (Daimler, Benz) [1885–1890] — external/team-reachable
- Biplane structural frame and wire bracing (Chanute, Wenham) [1866–1896] — external/team-reachable
- Reliable cambered airfoil data (Lilienthal's tables) [1889] — external/team-reachable
- Twisted-surface (wing-warping) or equivalent lateral control concept [1896–1899] — team-reachable within five-year sprint
- Efficient propeller design via empirical iteration (screw propeller theory from marine engineering) [1840s–1880s] — team-reachable
- Lightweight chain-and-sprocket drive transmission [1880s] — external/team-reachable
- Fabric-and-wood composite airframe construction techniques [1890s] — external/team-reachable
- Reliable ignition and carburetion for small gasoline engines [1890–1895] — external/team-reachable
Scientific theories / key empirical observations:
- Newtonian and Bernoulli lift principles (qualitative) [pre-1800] — external
- Cayley's identification of lift/drag/thrust triad and fixed-wing concept [1799–1809] — external
- Systematic measurement of lift and drag coefficients (Lilienthal, Langley) [1889–1896] — external/team-discoverable
- Recognition that lateral (roll) control is the binding control problem, not pitch alone [1890s, Lilienthal crashes] — team-discoverable via empirical glider iteration
- Observation that propeller efficiency scales with blade twist and aspect ratio (marine propeller data) [1850s–1880s] — external
Explanation: The binding constraint was not power-to-weight ratio alone but the convergence of three sub-problems: (1) sufficient aerodynamic data to select a wing geometry that actually generates net positive lift at practical speeds, (2) a three-axis control system — particularly roll control — without which any powered aircraft immediately departs controlled flight, and (3) a gasoline engine light and reliable enough to provide the required thrust-to-weight margin. Lilienthal's published lift tables (1889) and his glider flights through 1896 supplied the aerodynamic empirical base; Chanute's 1896 biplane glider demonstrated structural adequacy; Daimler/Benz engines by 1890 demonstrated that gasoline powerplants below roughly 5 kg/kW were manufacturable by a skilled workshop. The roll-control insight (that differential wing lift must be actively managed) was discoverable empirically by any team conducting sustained glider trials — Lilienthal's fatal 1896 crash made the problem vivid, and wing-warping or ailerons are a one-layer mechanical solution requiring no new science. A motivated team with access to Lilienthal's tables, a purpose-built wind tunnel for airfoil validation, and a commissioned lightweight gasoline engine could plausibly have achieved sustained controlled flight by the mid-to-late 1890s; the earliest plausible date is pushed back only to roughly 1890 because the necessary gasoline engine did not exist before ~1885 and required several years of reliability iteration before a workshop could confidently specify one for aviation use."""
    },
    {
        "invention": "Fleming valve",
        "year": 1904,
        "inventor": "John Ambrose Fleming",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1884–1888",
        "earliest_straightforward": "1890–1897",
        "actual_location": "London, England",
        "possible_locations": "United Kingdom; United States; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The UK and US led in both incandescent lamp development and early electrical/telegraphic engineering; London, Menlo Park (NJ), and Berlin had the industrial-workshop infrastructure and vacuum-glass expertise required.",
        "confidence": "Medium",
        "full_text": """Invention: Fleming valve (thermionic diode)
Year actually invented: 1904
Earliest plausible: 1884–1888
Earliest straightforward: 1890–1897
Confidence: Medium
Actual location: London, England
Possible locations at earliest plausible date: United Kingdom, United States, Germany
Geographic note: ALIGNED. The UK and US led in both incandescent lamp development and early electrical/telegraphic engineering; London, Menlo Park (NJ), and Berlin had the industrial-workshop infrastructure and vacuum-glass expertise required.
Prerequisite technologies:
- High-vacuum glass envelope (Sprengel/Geissler pump technology) [1865–1875] — external
- Incandescent filament lamp (carbon filament in evacuated glass bulb) [1879] — external
- Platinum or carbon wire sealed into glass (hermetic lead-through) [1870s] — external
- Sensitive galvanometer / current-detection instrumentation [1820s–1860s] — external
- DC power supply stable enough to bias an anode plate [1870s] — external
Scientific theories / key empirical observations:
- Edison effect (unidirectional current from hot filament to cold plate in vacuum, published by Edison 1883, fully described by Fleming in published literature 1883–1884) [1883] — external
- Qualitative understanding that current flows from hot to cold electrode but not reverse (empirical, no theoretical explanation required) [1883–1884] — team-discoverable by systematic variation
- Recognition that the asymmetric conduction could rectify AC or detect oscillating signals (functional reframing, not new science) [team-reachable within 1–2 years of Edison effect publication]
Explanation: The binding item is the Edison effect observation of 1883, without which a directed team would have no empirical basis for expecting unidirectional vacuum conduction. Once Edison's 1883 patent and Fleming's 1884 published description of the effect were available, a motivated team already operating an incandescent-lamp workshop (providing the vacuum envelope, filament, and sealed-lead-through skills as one layer of precursor tech) could within one to four years have systematically explored the asymmetric conduction, inserted a second electrode as a plate, and demonstrated rectification — all by empirical iteration without needing electron theory (Thomson's electron was not identified until 1897). The earliest plausible date is therefore 1884–1888: achievable immediately after the Edison effect entered the published literature, given access to a lamp-making workshop. The straightforward date of 1890–1897 reflects the realistic lag for a team to reframe the curiosity as a practical rectifier and refine vacuum and sealing techniques to reliable production quality. The 20-year gap between earliest plausible (1884) and actual invention (1904) is not technologically driven but motivational: no compelling application (wireless telegraphy rectification) existed until Marconi's work in the late 1890s, so no one was looking for exactly this device until Fleming combined the Edison effect with the telegraphy-detector problem in 1904."""
    },
    {
        "invention": "First free helicopter flight",
        "year": 1907,
        "inventor": "Paul Cornu",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1900–1905",
        "earliest_straightforward": "1905–1910",
        "actual_location": "Lisieux, France",
        "possible_locations": "France; Germany; United Kingdom; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. France in the early 1900s had leading internal combustion engine manufacturers (Antoinette, Renault, Darracq) and a vibrant aviation engineering community, making it the most plausible location for this work at the earliest plausible date.",
        "confidence": "Medium",
        "full_text": """Invention: First free helicopter flight
Year actually invented: 1907
Earliest plausible: 1900–1905
Earliest straightforward: 1905–1910
Confidence: Medium
Actual location: Lisieux, France
Possible locations at earliest plausible date: France, Germany, United Kingdom, United States
Geographic note: ALIGNED. France in the early 1900s had leading internal combustion engine manufacturers (Antoinette, Renault, Darracq) and a vibrant aviation engineering community, making it the most plausible location for this work at the earliest plausible date.
Prerequisite technologies:
- Lightweight internal combustion engine (high power-to-weight ratio, ~24hp at under ~250kg total system weight) [1900–1903] — external; Antoinette and other auto/aero engines reached viable power-to-weight ratios by ~1901–1903
- Counter-rotating rotor configuration (torque cancellation without tail rotor) [1784, refined 1870s–1900s] — team-reachable from Launoy-Bienvenu toy and subsequent models
- Steel tube or timber frame lightweight structural construction [1890s] — external
- Belt/chain transmission from engine to rotors [1880s] — external
- Fabric-covered rotor blades with cambered or flat profile [1890s] — team-reachable empirically
- Rubber-band and steam-powered model helicopters demonstrating rotor lift at small scale [1784–1870s] — external
Scientific theories / key empirical observations:
- Blade element theory (Drzewiecki, 1892) and momentum theory of propellers (Rankine, 1865; Froude, 1889) — external; sufficient for empirical rotor sizing
- Fixed-wing aerodynamics and lift/drag relationships (Lilienthal, 1889; Langley, 1891; Wright, 1900–1903) — external; transferable to rotor blade design
- Empirical observation that rotor diameter and RPM govern lift (from model helicopters) — team-discoverable
- Understanding that torque reaction requires counteraction (observable in models) — team-discoverable
- Power-to-weight scaling laws (understood qualitatively by engineers by 1890s) — external
Explanation: The binding constraint was the power-to-weight ratio of available internal combustion engines. Prior to roughly 1900–1902, no engine existed that could produce sufficient shaft horsepower at an airframe-compatible weight; steam engines were far too heavy, and early gasoline engines were not much better. Once the automobile and early aviation races drove rapid engine development — yielding units like the Antoinette producing 24–50hp at weights under 100kg by 1902–1903 — the remaining engineering challenges (rotor blade geometry, counter-rotation for torque cancellation, structural framing) were all soluble by an empirically-minded team without new science. The Wright brothers' 1903 success is not a prerequisite but a strong parallel signal that the engine threshold had been crossed. A motivated team with access to a 1901–1903 vintage aero engine, knowledge of Launoy-Bienvenu counter-rotating models, and Lilienthal/Wright aerodynamic tables could plausibly have achieved a brief free hover by 1903–1905; 1900 is the floor because the engine simply did not exist before then. The gap between earliest plausible (~1900–1905) and actual (1907) is small and reflects normal engineering iteration time rather than any missing scientific breakthrough."""
    },
    {
        "invention": "Bakelite",
        "year": 1907,
        "inventor": "Leo Baekeland",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1902–1907",
        "earliest_straightforward": "1904–1907",
        "actual_location": "Yonkers, New York, USA",
        "possible_locations": "USA; Germany; United Kingdom; France; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in the USA, and the USA was one of several plausible locations given its strong industrial chemistry infrastructure and access to coal-tar byproducts; Germany and the UK were equally or more likely candidates given their leading dye and synthetic chemistry industries.",
        "confidence": "Medium",
        "full_text": """Invention: Bakelite (first synthetic thermoset plastic)
Year actually invented: 1907
Earliest plausible: 1902–1907
Earliest straightforward: 1904–1907
Confidence: Medium
Actual location: Yonkers, New York, USA
Possible locations at earliest plausible date: USA, Germany, United Kingdom, France, Belgium
Geographic note: ALIGNED. The actual invention occurred in the USA, and the USA was one of several plausible locations given its strong industrial chemistry infrastructure and access to coal-tar byproducts; Germany and the UK were equally or more likely candidates given their leading dye and synthetic chemistry industries.
Prerequisite technologies:
- Coal-tar phenol and formaldehyde production at industrial scale [1870s] — external
- Condensation reaction glassware and heating apparatus (reflux condensers, autoclaves) [1880s] — external
- Shellac and natural resin molding/compression techniques [pre-1900] — external
- Pressure molds and heated die-casting equipment for resins [1890s] — external
- Analytical methods for tracking resin viscosity and cure state (empirical titration, softening-point tests) [1890s] — external
Scientific theories / key empirical observations:
- Baeyer's observation that phenol and aldehydes yield intractable resinous condensates [1872] — external
- Kleeberg's systematic phenol-formaldehyde condensation work establishing resin formation conditions [1891] — external
- Lebach's published characterization of phenol-formaldehyde resin intermediates and identification of soluble resole vs. insoluble final-stage products [1902] — external; this is the binding item
- Recognition that excess formaldehyde and controlled heating stages govern final product properties [empirically team-reachable from Lebach 1902 + iteration] — team-reachable
Explanation: The core chemical barrier was not synthesis of a phenol-formaldehyde resin — Baeyer documented that in 1872 — but the controlled, reproducible transition from a fusible resole intermediate to a hard, infusible, non-brittle thermoset without charring or voids. Baeyer (1872) and Kleeberg (1891) established that phenol and formaldehyde react to form resinous solids, but neither characterized the intermediate stages well enough to permit process control. Lebach's 1902 publication is the binding item: it identified distinct soluble and insoluble phases in the condensation sequence, giving a motivated team the conceptual map needed to design a staged heating protocol. With Lebach's 1902 results in hand, a well-resourced team of engineers with access to industrial autoclaves and compression molds could empirically optimize acid/base catalysis ratios, formaldehyde-to-phenol stoichiometry, cure temperature profiles, and filler blending within roughly two to five years — yielding an earliest plausible window of 1902–1907. The lower bound is set at 1902 because without Lebach's published phase characterization a team would have no reliable guide to avoid the brittle, foamy, or soluble failure modes that plagued all pre-1902 attempts. The gap between actual invention (1907) and earliest plausible (1902) is small and explained entirely by the time required for empirical process optimization after the 1902 binding publication, not by any missing scientific framework."""
    },
    {
        "invention": "Ramjet concept",
        "year": 1907,
        "inventor": "Rene Lorin",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1935–1942",
        "earliest_straightforward": "1939–1945",
        "actual_location": "France",
        "possible_locations": "Germany; United Kingdom; United States; France; USSR",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. By the mid-1930s, all major industrial powers had the aeronautical, materials, and fuel infrastructure to pursue a working ramjet; France is one of several plausible locations and retains capability through the actual first flight (Leduc, 1949).",
        "confidence": "Medium",
        "full_text": """Invention: Ramjet concept (stovepipe ramjet)
Year actually invented: 1907
Earliest plausible: 1935–1942
Earliest straightforward: 1939–1945
Confidence: Medium
Actual location: France
Possible locations at earliest plausible date: Germany, United Kingdom, United States, France, USSR
Geographic note: ALIGNED. By the mid-1930s, all major industrial powers had the aeronautical, materials, and fuel infrastructure to pursue a working ramjet; France is one of several plausible locations and retains capability through the actual first flight (Leduc, 1949).
Prerequisite technologies:
- High-speed aircraft or rocket sled capable of ~300–500 mph launch assist [1928–1935] — external/team-reachable
- Heat-resistant alloys (chrome-nickel steels, Inconel precursors) for combustion chamber [1920s–1930s] — external/team-reachable
- Fuel injection and atomization systems (carburetor/injector technology) [1900–1920] — external/team-reachable
- Wind tunnel capable of high-subsonic testing [1920s] — external/team-reachable
- Precision sheet-metal fabrication for inlet/nozzle geometry [1900s] — external/team-reachable
- Auxiliary ignition source (spark igniter) for initial combustion [1900s] — external/team-reachable
Scientific theories / key empirical observations:
- Bernoulli / compressible flow theory (inlet ram compression via deceleration) [1738, extended by Rankine-Hugoniot 1870s] — external/team-discoverable
- Conservation of momentum / Newton's third law applied to jet propulsion [1687] — external/team-discoverable
- Empirical observation that combustion chamber pressure rises with ram velocity (no theory required, verifiable by testing) [team-discoverable] — external/team-discoverable
- Stoichiometry of hydrocarbon combustion (fuel-air ratio for stable burn) [1800s] — external/team-discoverable
- Nozzle expansion and exhaust velocity (de Laval nozzle principles, subsonic regime) [1897] — external/team-discoverable
Explanation: NOTE: Lorin's 1907 "invention" was a conceptual paper proposal, not a working prototype; achieving a functioning working device in 1907 was not feasible, so the historical inventor pushed the envelope on concept well ahead of engineering reality — the earliest plausible date for a working ramjet (1935–1942) substantially post-dates the concept date (1907). The binding constraint is not the concept — Lorin stated it clearly in 1907 — but the launch platform and combustion stability at testable speeds. A working ramjet requires inlet velocities of roughly Mach 0.3–0.5 minimum to sustain combustion without a rotating compressor; achieving and sustaining that speed during a ground or flight test requires either a sufficiently fast towing aircraft or a rocket-assisted sled, neither of which existed in practical, repeatable form before the late 1920s. The second binding constraint is heat-resistant combustion-chamber materials: at sustained high-subsonic flow with continuous combustion, early mild steels warp or burn through within seconds, requiring chrome-nickel alloys that only became reliably available and machineable in the early 1930s. A motivated team in 1935 could have mounted a ramjet duct on a fast biplane or rocket sled, iterated empirically on inlet geometry and fuel-injection placement, and demonstrated sustained thrust — consistent with the 1935–1942 window; the 1939–1945 "straightforward" band reflects the moment when high-speed aircraft (400+ mph fighters) became common enough to serve as off-the-shelf tow or drop-launch platforms. No new scientific framework is required; all needed fluid-mechanics principles were published, and the team could substitute empirical iteration for formal compressible-flow theory."""
    },
]

with open(CHECKPOINT, "a", encoding="utf-8") as f:
    for entry in entries:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
