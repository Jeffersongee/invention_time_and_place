#!/usr/bin/env python3
"""Write batch 25 (indices 168-174) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Atomic clock",
        "year": 1948,
        "inventor": "Harold Lyons (National Bureau of Standards)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1946–1947",
        "earliest_straightforward": "1949–1952",
        "actual_location": "Washington, D.C., USA",
        "possible_locations": "USA (NBS, MIT Rad Lab, Columbia University); UK (NPL, Cavendish Laboratory); USSR (academic physics centers)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual inventor worked at the U.S. National Bureau of Standards, which sits squarely within the cluster of institutions where all binding prerequisites were concentrated.",
        "confidence": "Medium",
        "full_text": """Invention: Atomic clock
Year actually invented: 1948
Earliest plausible: 1946–1947
Earliest straightforward: 1949–1952
Confidence: Medium
Actual location: Washington, D.C., USA
Possible locations at earliest plausible date: USA (NBS, MIT Rad Lab, Columbia University), UK (NPL, Cavendish Laboratory), possibly USSR (academic physics centers)
Geographic note: ALIGNED. The actual inventor worked at the U.S. National Bureau of Standards, which sits squarely within the cluster of institutions where all binding prerequisites were concentrated.

Prerequisite technologies:
- Microwave spectroscopy (ammonia absorption lines characterized) 1934–1946 — external (Cleeton & Williams 1934 first microwave ammonia spectroscopy; wartime radar work produced klystrons and microwave hardware)
- Klystron and microwave oscillator technology 1937–1943 — external (Varian brothers 1937; mass-produced by MIT Rad Lab during WWII)
- Waveguide components, microwave cavities, attenuators 1940–1945 — external (WWII radar program, widely documented by 1945)
- Quartz crystal oscillator / heterodyne frequency synthesis chain 1921–1940 — external (AT&T Bell Labs quartz standards; frequency division chains well-established)
- Lock-in amplifier / phase-sensitive detection 1941 — external (Coslett/Dicke; essential for narrow-line detection)
- Isidor Rabi's molecular beam magnetic resonance method 1938–1944 — external (Nobel 1944; directly inspired the atomic clock concept)
- Vacuum pumping adequate for molecular beam work 1930s — external (diffusion pumps, standard lab equipment)

Scientific theories / key empirical observations:
- Quantum mechanics of atomic/molecular energy levels and transition frequencies 1925–1930 — external
- Ammonia inversion frequency ~23.87 GHz characterized by Cleeton & Williams 1934 — external
- Stability and universality of atomic transition frequencies (implicit in quantum mechanics) 1925 — external
- Rabi's observation that molecular resonance could serve as a precision frequency reference 1945 — external
- Pound's microwave cavity stabilization techniques 1946 — external

Explanation: The binding constraint on the ammonia atomic clock was not any single missing technology but rather the convergence of two independent streams: microwave hardware capable of operating near 24 GHz, and a clear conceptual program to use molecular resonance as a clock standard. Cleeton and Williams observed the ammonia inversion line in 1934 but lacked both a stable enough source and the explicit timekeeping motivation. The wartime radar program (1940–1945) produced klystrons, waveguides, microwave cavities, crystal mixers, and precision frequency-chain techniques as commercially available or widely documented surplus. By late 1945, all hardware prerequisites existed as real artifacts sitting in radar surplus stores and MIT Rad Lab reports. Rabi publicly proposed using atomic transitions as frequency standards in 1945. A motivated team with access to this knowledge and surplus radar hardware could, in principle, have demonstrated a working ammonia absorption-stabilized oscillator in 1946–1947.

The reason 1946–1947 is the lower bound rather than earlier is the klystron's practical operating range near 23.87 GHz. The lock-in detection technique (Dicke, 1946) for extracting the narrow resonance signal from noise was itself published in 1946 and is on the critical path; a team could re-derive it, but it represents one significant empirical iteration. Without either the klystron or a workable narrow-line detection scheme, the project could not have started before 1945 at the earliest.

The gap between earliest plausible (1946–1947) and earliest straightforward (1949–1952) reflects real engineering friction: stabilizing a klystron to a narrow molecular line while rejecting pressure-broadening, thermal drift, and AC Stark shifts requires iterative calibration not obvious from the spectroscopic literature alone. Lyons's team itself took roughly 1945–1948 to go from concept to demonstration, even with institutional backing and direct access to the right people. A team starting fresh in 1946 without NBS organizational momentum would likely need three to four years, placing straightforward convergence around 1949–1952. The actual 1948 date therefore reflects Lyons's focused institutional effort."""
    },
    {
        "invention": "Basic oxygen steelmaking (BOF / LD process)",
        "year": 1948,
        "inventor": "Robert Durrer; commercialized by VOEST (Linz, Austria)",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1928–1932",
        "earliest_straightforward": "1935–1940",
        "actual_location": "Switzerland / Austria (Linz, Donawitz)",
        "possible_locations": "Germany; United Kingdom; United States; France; Belgium; Austria; Sweden",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Austria is among the leading steel-producing nations with deep metallurgical research infrastructure. The actual commercialization site (Linz/Donawitz) is consistent with the possible-locations list.",
        "confidence": "Medium",
        "full_text": """Invention: Basic oxygen steelmaking (LD process / BOF process)
Year actually invented: 1948
Earliest plausible: 1928–1932
Earliest straightforward: 1935–1940
Confidence: Medium
Actual location: Switzerland / Austria (Durrer in Switzerland; commercialized in Linz and Donawitz, Austria)
Possible locations at earliest plausible date: Germany, United Kingdom, United States, France, Belgium, Austria, Sweden
Geographic note: ALIGNED. Austria is among the leading steel-producing nations with deep metallurgical research infrastructure. The actual commercialization site (Linz/Donawitz) is consistent with the possible-locations list.

Prerequisite technologies:
- Bessemer converter (air-blown molten iron refining) [1856] — external
- Open-hearth (Siemens-Martin) furnace [1865] — external
- Industrial-scale liquid oxygen production (Linde-Hampson process) [1895] — external
- Linde air separation / tonnage oxygen plants [1902–1910] — external
- Water-cooled tuyere / lance technology [pre-1900] — external
- High-pressure oxygen piping and valve engineering [~1910–1920] — external
- Refractory basic lining (dolomite/magnesite) capable of resisting oxidizing conditions [~1880, Sidney Gilchrist Thomas process] — external
- Practical oxygen purity >95% at industrial quantities [~1920s] — external

Scientific theories / key empirical observations:
- Carbon oxidation thermodynamics in iron melts (understood qualitatively from Bessemer era, quantitatively developed through 1870s–1900s) — external
- Role of nitrogen in steel embrittlement (recognized by early 20th century) — external
- Oxidation kinetics of Si, Mn, C, P in molten iron (progressively characterized 1880s–1920s) — external
- Flame/combustion behavior with enriched oxygen (well understood by 1900s from industrial gas cutting and welding) — external
- Heat balance of oxygen blowing vs. air blowing (calculable once oxygen costs and thermodynamics were in hand, ~1920s) — external

Explanation: The binding constraint for basic oxygen steelmaking is not a scientific discovery but an engineering and economic one: the availability of cheap, high-purity oxygen in tonnage quantities. The Linde-Hampson liquefaction process dates to 1895, and by roughly 1910–1920 industrial oxygen plants were supplying oxygen for cutting and welding at commercially viable cost. By the mid-1920s, tonnage oxygen was available at several industrial centers in Europe and North America. A motivated team with knowledge of Bessemer nitrogen problems and access to industrial oxygen could have begun serious lance-blowing experiments no earlier than roughly 1925–1928, and after two to four years of empirical iteration on vessel geometry, lance height, oxygen flow rates, and refractory selection, a working pilot-scale demonstration was achievable by 1928–1932. The water-cooled lance itself is a straightforward piece of mechanical engineering once high-pressure oxygen piping practice was established; it is squarely within one-layer-of-precursor reach.

The reason the earliest plausible date is set at 1928–1932 rather than earlier is twofold. First, oxygen at the required purity and throughput for a meaningful steelmaking heat was not commercially practical before the mid-1920s. Second, the Bessemer process was economically dominant and the nitrogen problem, while known, was not perceived as the limiting industrial constraint until open-hearth furnaces had displaced Bessemer for quality steel. The gap between 1928–1932 (earliest plausible) and 1935–1940 (earliest straightforward) reflects realistic time for a small team to iterate on refractory wear, lance position, heat balance surprises, and vessel tipping mechanics without foreknowledge of the final design.

The gap from the earliest straightforward date to the actual invention date (1948) is explained primarily by institutional and economic factors: the Great Depression suppressed capital investment in new steelmaking in the 1930s, and World War II redirected metallurgical engineering effort entirely. Durrer had been experimenting with oxygen enrichment through the late 1930s and during the war; his 1948 demonstration followed directly from a wartime research thread. The postwar reconstruction context in Austria, with pressing need to rebuild steel capacity cheaply, provided both the motivation and the VOEST institutional backing to push the process to commercial scale."""
    },
    {
        "invention": "Bertie the Brain (interactive electronic game)",
        "year": 1950,
        "inventor": "Josef Kates (Canadian National Exhibition)",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1845–1855",
        "earliest_straightforward": "1905–1920",
        "actual_location": "Toronto, Ontario, Canada",
        "possible_locations": "United Kingdom (London, Birmingham); France (Paris); USA (Boston, New York, Philadelphia); Prussia/German states (Berlin, Hamburg)",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. At the earliest plausible date (~1845–1855), the prerequisite relay manufacturing and electrical instrument-making ecosystem was concentrated in the UK, northeastern USA, France, and the German states. Canada had a nascent telegraph network by 1847 but lacked the dense layer of relay manufacturers and electrical workshop infrastructure needed to pursue this project independently.",
        "confidence": "Medium",
        "full_text": """Invention: "Bertie the Brain" — first publicly demonstrated interactive electronic game
Year actually invented: 1950
Earliest plausible: 1845–1855
Earliest straightforward: 1905–1920
Confidence: Medium
Actual location: Toronto, Ontario, Canada
Possible locations at earliest plausible date: United Kingdom (London, Birmingham — center of telegraph relay manufacturing and instrument-making); France (Paris — leading instrument-making workshops and early national telegraph network); USA (Boston, New York, Philadelphia — advanced telegraph industry with commercial relay production by 1845); Prussia/German states (Berlin, Hamburg — growing instrument and telegraph industry)
Geographic note: MISMATCH. At the earliest plausible date (~1845–1855), the prerequisite relay manufacturing and electrical instrument-making ecosystem was concentrated in the UK, northeastern USA, France, and the German states — the heart of the telegraph engineering world. Canada had a nascent telegraph network by 1847 but lacked the dense layer of relay manufacturers, electrical workshop infrastructure, and instrument-making expertise needed to pursue this project independently. Toronto in 1950 was plausible given wartime and postwar electronics development, but the actual location is a meaningful geographic mismatch relative to the earliest plausible window.

Prerequisite technologies:
- Electromechanical relay [1835, Joseph Henry; commercial telegraph-grade relays by ~1844] — external
- Reliable sustained electrical current (Daniell cell / zinc-copper battery) [1836] — external
- Manual electrical switch for player input [co-developed with telegraph, ~1840s] — external
- Electrical indicator output (galvanometer, mechanical flag, or bell; incandescent lamp post-1879) [1840s for basic indicators; 1879 for lamp-based display] — external
- Relay switching logic (series-wired = AND, parallel = OR, normally-closed contacts = NOT) implementing a tic-tac-toe decision tree [relay network logic empirically reachable by iterating on telegraph relay configurations] — team-reachable (one precursor layer)
- Enumeration and hardcoding of tic-tac-toe game tree [pure combinatorial reasoning; no scientific knowledge required] — team-reachable

Scientific theories / key empirical observations:
- Galvani/Volta electrochemical current [1800] — external; off-limits phenomenon, must pre-exist
- Oersted electromagnetism (current deflects compass; basis of relay operation) [1820] — external; off-limits phenomenon, must pre-exist
- Practical electromagnet construction (Sturgeon 1824, Henry 1820s–1830s) [1824–1835] — external
- Faraday induction [1831] — external; off-limits; not directly required for relay/switch-based logic
- Shannon's symbolic analysis of relay and switching circuits [1938] — external but not binding; empirical relay wiring suffices for a simple game tree without formal Boolean algebra
- Game-tree / decision-tree reasoning for finite combinatorial games — team-discoverable

Explanation: The binding prerequisite for an interactive electronic game is the electromechanical relay (commercially available by ~1844 through the telegraph industry), which is the only pre-vacuum-tube switching element capable of implementing conditional game logic. All other physical components were simultaneously available: Daniell-cell batteries (1836) for sustained current, manual switches for player input, and galvanometers or mechanical indicators for output. The conceptual challenge — implementing a tic-tac-toe decision tree in relay circuitry — is entirely team-reachable without formal switching algebra: a motivated engineer can enumerate all reachable board states, identify the 8 win conditions, and wire relay arrays in series/parallel combinations to detect wins, determine optimal responses, and trigger output indicators. This is tedious but not beyond a skilled telegraph engineer with 5 years of focused effort. With relays commercially available by ~1844, the earliest plausible window is 1845–1855.

The earliest straightforward date of 1905–1920 reflects the point at which relay logic had become mature engineering art in telephone exchange switching, vacuum tubes offered a faster alternative, and the conceptual toolkit (logical switching networks, enumerated state machines) was part of the ordinary electrical engineering repertoire. A competent team in 1910 could follow a reasonable engineering program — enumerate states, wire relay logic, add lamp-based display — without exceptional insight or luck.

The ~95-year gap to the actual 1950 date is almost entirely a motivation gap rather than a technological one. Building a machine to play a parlor game against humans had no commercial, military, or institutional rationale before the computer era. Kates built Bertie the Brain explicitly as a public demonstration of computing concepts at the 1950 Canadian National Exhibition, a motivation that presupposes the existence of the broader computing movement of the 1940s. The underlying relay and vacuum-tube technology had been sufficient for decades. This is a demand/motivation gap which, per the rubric, does not warrant flagging the entry."""
    },
    {
        "invention": "Tokamak fusion reactor concept",
        "year": 1950,
        "inventor": "Igor Tamm & Andrei Sakharov",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1944–1948",
        "earliest_straightforward": "1948–1953",
        "actual_location": "Moscow, USSR",
        "possible_locations": "USSR (Moscow — Kurchatov Institute, FIAN); USA (Princeton, Los Alamos, Berkeley); United Kingdom (Harwell, AERE); Sweden (Royal Institute of Technology — Alfvén's group)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USSR was among the very small set of locations capable of this synthesis at the earliest plausible date, requiring simultaneous access to thermonuclear cross-section knowledge, Alfvén's MHD framework, and a motivated institutional program. Only national nuclear-weapons programs (USSR, USA, UK) and Alfvén's Swedish group had the necessary combination.",
        "confidence": "Medium",
        "full_text": """Invention: Tokamak fusion reactor concept
Year actually invented: 1950
Earliest plausible: 1944–1948
Earliest straightforward: 1948–1953
Confidence: Medium
Actual location: Moscow, USSR
Possible locations at earliest plausible date: USSR (Moscow — Kurchatov Institute, FIAN); USA (Princeton, Los Alamos, Berkeley — institutions with thermonuclear program access); United Kingdom (Harwell, Atomic Energy Research Establishment); Sweden (Royal Institute of Technology — Alfvén's group)
Geographic note: ALIGNED. The USSR was among the very small set of locations capable of this synthesis at the earliest plausible date, requiring simultaneous access to classified thermonuclear cross-section data, Alfvén's MHD framework, and a motivated institutional program. Only national nuclear-weapons programs (USSR, USA, UK) and Alfvén's Swedish group had the necessary combination of plasma physics depth and fusion motivation.

Prerequisite technologies:
- Large-scale electromagnetic coil technology and solenoid windings [late 19th c., routine by 1900] — external
- High-vacuum chamber technology (rotary and diffusion pumps capable of ~10^-5 torr) [Gaede 1905; mercury vapor pump 1915; oil diffusion pump ~1920s] — external
- Practical transformer/induction technology for driving toroidal plasma current [Faraday induction 1831; practical transformers 1880s] — external
- High-power pulsed capacitor-discharge systems for plasma heating [1930s–1940s, from radar/weapons programs] — external
- Controlled gas discharge tubes and early pinch discharge experiments [1920s–1940s] — external

Scientific theories / key empirical observations:
- Oersted's current-produces-magnetic-field [1820] — external; off-limits for team discovery, usable as external knowledge
- Faraday electromagnetic induction [1831] — external; off-limits for team discovery, usable as external knowledge
- Maxwell's electromagnetic field equations [1865] — external; full framework required for field geometry calculations
- Lorentz force law on charged particles in magnetic fields [1895] — external; essential for particle orbit analysis
- Gamow quantum tunneling applied to nuclear reactions [1928] — external; enables calculation that fusion is possible at attainable temperatures
- Bethe's stellar nucleosynthesis papers establishing that light-nucleus fusion releases energy at high temperatures [1939] — external; binding scientific knowledge without which the target phenomenon is undefined
- D-T and D-D thermonuclear cross-section measurements [late 1930s–1944, partly from Manhattan Project] — external; quantitative data needed to set temperature targets (~10^8 K for D-T)
- Alfvén's magnetohydrodynamics (MHD) theory — plasma as a conducting fluid governed by coupled electromagnetic and fluid equations [1942] — external; binding theoretical framework for bulk plasma behavior in magnetic fields
- Single-particle drift theory: gradient drift and curvature drift of charged particles in non-uniform or curved magnetic fields — team-discoverable from Lorentz force + Maxwell's equations by systematic analytical derivation
- MHD stability of the toroidal + poloidal field configuration — team-discoverable by systematic analysis building on Alfvén's framework

Explanation: The tokamak concept is a theoretical engineering design specification — not the discovery of a new physical phenomenon — and should not be flagged. It applies known electromagnetic and plasma physics principles to specify a geometry (toroidal vessel + external toroidal-field coils + transformer-driven toroidal plasma current producing a poloidal field) that creates helical magnetic field lines capable of preventing the net particle drift that would destroy confinement in a pure toroidal field. The two binding prerequisites are Bethe's 1939 stellar fusion papers (establishing that hydrogen-isotope fusion is the target phenomenon and setting the temperature regime) and Alfvén's 1942 MHD theory (providing the framework for analyzing bulk plasma behavior in magnetic fields). Without Bethe, there is no defined engineering target; without Alfvén, a team cannot reason rigorously about plasma stability as distinct from individual particle orbits.

After both prerequisites are in hand (post-1942), the remaining intellectual steps are within reach of a small highly-skilled theoretical physics team without new scientific discovery: the magnetic drift formulas are derivable from Lorentz force equations and Maxwell's equations already on the books since 1895 and 1865 respectively. Recognizing that the drift problem is solved by adding a poloidal field — creating helical field lines that average out the vertical drift over one helical orbit — is a further analytical step requiring perhaps 1–2 years of focused work. This places earliest plausible at 1944–1948, with the lower bound set by Alfvén's 1942 paper plus minimum realistic development time.

The actual invention date of 1950–1951 falls just inside the earliest straightforward window. This near-coincidence reflects the specific historical circumstances: Tamm and Sakharov were already working in the Soviet thermonuclear weapons program, which gave them both the thermodynamic target (D-T fusion at ~10^8 K), classified cross-section data, and institutional pressure to solve the confinement problem rapidly. The West reached the same conceptual destination almost simultaneously (Spitzer's stellarator concept, Princeton, 1951), confirming that by ~1950 the prerequisites were fully in place for independent convergence."""
    },
    {
        "invention": "Float glass process",
        "year": 1952,
        "inventor": "Alastair Pilkington (Pilkington Brothers)",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1918–1925",
        "earliest_straightforward": "1930–1945",
        "actual_location": "St Helens, Lancashire, UK",
        "possible_locations": "UK (St Helens/Lancashire glass district); Germany (Rhineland glass and chemical industry); Belgium (Charleroi/Liège glass region); France (Saint-Gobain); USA (Toledo, Ohio; Pittsburgh, Pennsylvania)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. UK (St Helens/Lancashire glass district) appears in the possible-locations list and was indeed a leading candidate. The process could equally have emerged from Germany, Belgium, France, or US glass districts, all with equivalent glass-furnace technology, industrial gas supply, and access to refined tin by the 1920s.",
        "confidence": "Medium",
        "full_text": """Invention: Float glass process
Year actually invented: 1952
Earliest plausible: 1918–1925
Earliest straightforward: 1930–1945
Confidence: Medium
Actual location: St Helens, Lancashire, UK (Pilkington Brothers)
Possible locations at earliest plausible date: UK (St Helens/Lancashire glass district); Germany (Rhineland glass and chemical industry — BASF/Bayer corridor, Jena glassworks); Belgium (Charleroi/Liège glass region); France (Saint-Gobain, Seine/Loire glass districts); USA (Toledo, Ohio — Libbey-Owens glass center; Pittsburgh, Pennsylvania)
Geographic note: ALIGNED. UK (St Helens/Lancashire glass district) appears in the possible-locations list and was indeed a leading candidate. The process could equally have emerged from Germany, Belgium, France, or US glass districts, all of which had equivalent glass-furnace technology, industrial gas supply, and access to refined tin by the 1920s.

Prerequisite technologies:
- High-temperature continuous glass tank furnace (Siemens regenerative furnace ~1867; continuous glass tanks ~1870s–1880s) — external
- Refined commercial tin metal (antiquity for tin; modern refining well-established by 18th c.) — external
- Sealed refractory-lined chamber / controlled-atmosphere furnace capable of containing inert/reducing gas at 600–1100°C (metallurgical reducing-atmosphere practice well-established ~1880s–1910s) — team-reachable as one precursor (adapting existing metallurgical sealed-atmosphere furnace design to a glass tin-bath geometry)
- Industrial nitrogen gas supply (Linde air separation, first nitrogen plant 1908; commercial availability ~1910–1915) — external
- Annealing lehr for controlled glass cooling (in use in plate glass industry by ~1890s) — external
- Temperature measurement and control (thermocouples, optical pyrometers, ~1890s–1910s) — external
- Concept of floating glass on a denser liquid metal bath (Bessemer ~1848–1860s; Heal US patent 1902) — external

Scientific theories / key empirical observations:
- Density of glass (~2.5 g/cm³) less than molten tin (~6.5 g/cm³ at process temperature) — known from elementary materials science, external
- Tin oxidizes in air to SnO₂ (dross) at elevated temperatures — team-discoverable through early iteration (any attempt at an open tin bath immediately produces dross contamination)
- Reducing atmosphere (H₂, CO, or N₂/H₂ mix) prevents metal oxidation — well-established metallurgical empirical observation, external
- Viscosity-temperature relationship of soda-lime glass allows self-leveling at ~1000°C — known empirically to glass technologists by late 19th c., external
- Glass achieves fire-polished surface when cooled from liquid state without mechanical contact — known empirically, external

Explanation: The float glass process requires no new scientific phenomena — it combines the concept of floating glass on molten tin (publicly known since Bessemer's mid-19th century experiments and Heal's 1902 US patent) with the metallurgical practice of maintaining a reducing/inert atmosphere over molten metal to prevent oxidation. The binding constraint is not any fundamental discovery but rather the intersection of two available technologies: (1) industrial nitrogen supply, commercially available from Linde air separation plants from approximately 1910–1915, and (2) sealed controlled-atmosphere chamber technology, routinely used in metallurgical bright-annealing and case-hardening furnaces by the 1900s–1910s. A motivated team at a glass works in ~1918–1925, having read Heal's 1902 patent and aware of standard metallurgical sealed-atmosphere practice, could have built the reducing-atmosphere tin-bath chamber as their one allowed precursor layer, using industrial N₂/H₂, and produced fire-polished flat glass of prototype quality within five years.

The earliest straightforward date is pushed to 1930–1945 because the concept requires a team to connect three distinct industrial traditions — glass-forming, molten-metal handling, and controlled-atmosphere metallurgy — that rarely overlapped in practice, and because commercial inertia (the plate glass industry's sunk investment in grinding and polishing lines) would have suppressed motivation even for teams that recognized the possibility.

The roughly 30-year gap between the earliest plausible date (~1920) and the actual date (1952) is almost entirely explained by institutional and commercial factors, not technical ones. The plate glass industry had invested heavily in continuous grinding and polishing lines by the 1920s and had little incentive to pursue a radically different approach. Pilkington Brothers, the actual inventor's employer, was a relative latecomer to large-scale plate glass and thus had more to gain from a disruptive process; Alastair Pilkington's insight was connecting Heal's 1902 patent concept to modern controlled-atmosphere engineering. The 50-year gap from Heal's patent (1902) to Pilkington's conception (1952) represents a classic case of a correct idea sitting dormant because no institution with both the incentive and the capability chose to pursue it."""
    },
    {
        "invention": "Thermonuclear weapon (hydrogen bomb)",
        "year": 1952,
        "inventor": "Edward Teller & Stanislaw Ulam",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Eniwetok Atoll / USA",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: Thermonuclear weapon (hydrogen bomb / fusion weapon)
Year actually invented: 1952
Earliest plausible: Flag
Earliest straightforward: Flag
Confidence: Flag
Actual location: Eniwetok Atoll / USA
Possible locations at earliest plausible date: Flag
Geographic note: Flag

Prerequisite technologies:
- Working implosion-type fission bomb (atomic bomb) [1945] — external (but itself flagged; see explanation)
- Electromagnetic isotope separation (calutron / EMIS for lithium-6) [1944] — external, but requires industrial-scale EMIS plant (Y-12 Oak Ridge scale)
- Tritium production reactors (Savannah River / Hanford-class) [1952] — external, but requires purpose-built industrial reactors far beyond workshop scale
- Deuterium liquefaction and cryogenic containment systems [1940s] — external
- High-speed computing for hydrodynamic implosion calculations (ENIAC-class) [1945] — external
- Radiation case / pusher / tamper assembly engineering [1951] — external (Teller-Ulam, classified)

Scientific theories / key empirical observations:
- Nuclear fusion cross-sections (D-T, D-D, D-He3) [1934–1940s] — external once published
- Thermonuclear ignition threshold theory [1942–1946] — external once published, but classified
- Radiation transport and opacity theory [1930s–1940s] — external (published)
- Teller-Ulam radiation implosion concept [1951] — classified; the core design insight was never published and remains classified; not accessible from open literature

Explanation: The thermonuclear weapon fails the rubric's flagging criteria on multiple, independent, and irreducible grounds. The most direct flag trigger is that its essential prerequisite — a working implosion-type fission bomb — is itself already flagged under the atomic bomb entry on organizational/industrial grounds. The fission primary cannot be built by a small motivated workshop team in any plausible timeline; it requires industrial-scale isotope separation (Y-12/K-25 facilities employing tens of thousands) and purpose-built reactor complexes (Hanford). Because the thermonuclear weapon's functionality depends entirely on the fission primary delivering a multi-kiloton X-ray pulse on a nanosecond timescale, the flag propagates directly.

The second independent flag is the Teller-Ulam design concept itself. The critical physical insight — that radiation pressure (X-ray flux) from the primary can compress the secondary to fusion conditions before hydrodynamic disassembly occurs — is not derivable from any published open literature. It was arrived at by a small group of extraordinary physicists working with classified test data, classified equation-of-state measurements, and iterative classified computing runs on institutional machines. Prior approaches (the "Super" or classical design, pursued 1942–1950) were known by insiders to be physically unworkable and were abandoned only after classified analysis. A workshop team with access only to open literature would pursue the classical Super, which does not work, and would have no empirical feedback mechanism to correct course.

The third flag is the tritium/lithium-6 production requirement. Even the "dry" lithium deuteride design requires lithium-6 enriched to ~95% from natural lithium (7.5% Li-6), accomplished at the Y-12 EMIS plant at industrial scale. Any one of these flag grounds alone might be arguable; together they make the flag mandatory. The invention is inseparable from the specific institutional and classified-knowledge context of the U.S. postwar nuclear weapons program."""
    },
    {
        "invention": "Helical scan video tape recorder (VTR)",
        "year": 1953,
        "inventor": "Norikazu Sawazaki (Toshiba); Eduard Schüller (AEG)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1947–1950",
        "earliest_straightforward": "1950–1955",
        "actual_location": "Tokyo, Japan (Toshiba) / AEG, Germany",
        "possible_locations": "USA (RCA Princeton labs, Ampex Redwood City, Bell Labs); UK (BBC Research Department, Marconi); Germany (AEG, BASF); Japan (Toshiba, NHK technical laboratories)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Japan (Toshiba, NHK technical laboratories) and Germany (AEG, BASF) both appear in the possible-locations list. The co-invention in Japan and Germany reflects specific institutional choices; the USA had the deepest concentration of relevant wideband electronics expertise but did not pursue it commercially at that time.",
        "confidence": "Medium",
        "full_text": """Invention: Helical scan video tape recorder (VTR)
Year actually invented: 1953
Earliest plausible: 1947–1950
Earliest straightforward: 1950–1955
Confidence: Medium
Actual location: Tokyo, Japan (Toshiba Research Laboratory) / independently AEG, Germany
Possible locations at earliest plausible date: USA (RCA Princeton labs, Ampex Redwood City, Bell Labs, NBC/CBS broadcast engineering); UK (BBC Research Department, Marconi); Germany (AEG, BASF); Japan (Toshiba, NHK technical laboratories)
Geographic note: ALIGNED. Japan (Toshiba, NHK technical laboratories) and Germany (AEG, BASF) both appear in the possible-locations list. The co-invention in Japan and Germany reflects specific institutional choices; the USA had the deepest concentration of relevant wideband electronics expertise but did not pursue it commercially at that time.

Prerequisite technologies:
- Magnetic tape with adequate high-frequency response (gamma-ferric-oxide coating): BASF 1939 / 3M Scotch 111 1948 — external (commercially reliable supply available 1948)
- Wideband vacuum tube amplifiers capable of ~4 MHz bandwidth (from WWII radar pulse electronics): 1944–1946 — external
- Precision rotating drum with stable high-speed bearings (gyroscope and aircraft instrument heritage): 1940s — team-reachable (precision machine shop could fabricate drum and bearing set as the one allowed precursor)
- Small-gap magnetic recording head in high-permeability alloy or ferrite (from audio Magnetophon engineering): 1933/1940s — external
- Television signal electronics and sync-separation circuitry: 1939–1948 — external
- Rotating-head concept (the key architectural insight): patented by Masterson/RCA 1950 — team-reachable via engineering iteration (a team iterating on linear-transport video recording encounters the speed wall and logically explores rotating the head as an alternative)

Scientific theories / key empirical observations:
- Electromagnetic induction and magnetic recording physics (Faraday 1831; Poulsen wire recorder 1898; Magnetophon operational theory 1930s–40s) — external; the induction phenomenon is off-limits to discover, but fully established well before the candidate date
- AC bias recording technique for high-frequency fidelity (Carlson & Carpenter patent 1921; Camras/Japanese refinement 1938–1941) — external
- Relationship between head-to-tape relative velocity and recordable signal bandwidth — team-discoverable; a team iterating on linear-transport video recording will empirically discover this relationship directly from prototyping work, motivating the rotating-head solution
- Skin depth and gap-length constraints on recording head design for high-frequency signals — external, established in audio engineering literature by mid-1940s

Explanation: The helical scan VTR is an engineering architecture invention, not a scientific discovery. Its binding prerequisites are commercially available gamma-ferric-oxide magnetic tape (reliably available from 3M by 1948, from BASF by 1939 but not accessible outside Germany during WWII), wideband electronics from the wartime radar tradition (available 1945–1946), precision rotating drum fabrication (team-reachable as the one allowed precursor), and the architectural insight of rotating the recording head rather than moving the tape at impossibly high linear speed. This rotating-head insight is team-reachable: any motivated team iterating empirically on recording a 4 MHz video signal with linear tape transport will immediately confront the speed wall (tape would need to run at ~30 feet/second for linear recording, which is mechanically impractical) and explore head rotation as the engineering escape. The earliest plausible date of 1947–1950 is set by the convergence of adequate commercial tape supply (post-1945 access to German oxide technology; 3M Scotch 111 in 1948), wideband amplifier know-how from radar, and the mechanical precision tradition from gyroscopes and aircraft instruments.

The gap to the actual 1953 date is modest and explained by the fact that broadcast television only reached mass adoption in the USA in 1948–1950, creating the commercial and institutional motivation for video recording for the first time; without that motivating context, no team had reason to attempt it. Germany's AEG/BASF had the longest magnetic recording heritage and were a natural first mover, but wartime disruption and postwar occupation constraints explain why Germany did not lead sooner; the USA's RCA conceived the helical scan patent in 1950 but failed to pursue it commercially; Japan's Toshiba, motivated by NHK broadcast needs, and AEG independently converged on practical prototypes in 1953–1954. The geographic outcome — Japan and Germany as actual inventors rather than the USA — is a mild historical contingency driven by institutional choices rather than technical necessity."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
