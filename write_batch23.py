#!/usr/bin/env python3
"""Write batch 23 (indices 154-160) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Nuclear fission",
        "year": 1938,
        "inventor": "Otto Hahn, Fritz Strassmann; Lise Meitner & Otto Frisch",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Berlin, Germany / Stockholm, Sweden",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: Nuclear fission (discovery)
Year actually invented: 1938
Earliest plausible: Flag
Earliest straightforward: Flag
Confidence: Flag
Actual location: Berlin, Germany / Stockholm, Sweden
Possible locations at earliest plausible date: Flag
Geographic note: Flag

Prerequisite technologies:
- Neutron source (Ra-Be or cyclotron) [1932] — external/team-reachable
- Ionization chamber and Geiger counter [1908–1928] — external/team-reachable
- Chemical separation and radiochemical analysis techniques [1900s–1930s] — external/team-reachable

Scientific theories / key empirical observations:
- Discovery of the neutron (Chadwick) [1932] — external
- Artificial radioactivity via neutron bombardment (Fermi 1934) — external
- Liquid-drop model of the nucleus [1936–1939] — external

Explanation: Nuclear fission is explicitly listed as an off-limits phenomenon in the rubric (1938). It satisfies FLAG criteria on multiple grounds: it is irreducibly a phenomenon-discovery — the realization that heavy nuclei can split under neutron bombardment is not an engineering achievement but the uncovering of a previously unknown nuclear process. Prior consensus held that neutron bombardment of uranium produced transuranic elements, not lighter nuclei. No motivated engineering team could have been directed to produce this discovery on schedule because the target phenomenon was not known to exist."""
    },
    {
        "invention": "Defibrilator",
        "year": 1939,
        "inventor": "Naum Gurvich",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1902–1910",
        "earliest_straightforward": "1910–1920",
        "actual_location": "Moscow, USSR",
        "possible_locations": "Germany; United Kingdom; France; United States",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. The binding prerequisites (Prevost-Batelli 1899, Einthoven ECG 1903) were available in Western European and American research centers by 1905; the actual invention occurred in the USSR in 1939.",
        "confidence": "High",
        "full_text": """Invention: Defibrillator
Year actually invented: 1939
Earliest plausible: 1902–1910
Earliest straightforward: 1910–1920
Confidence: High
Actual location: Moscow, USSR
Possible locations at earliest plausible date: Germany, United Kingdom, France, United States
Geographic note: MISMATCH. The binding prerequisites (Prevost-Batelli 1899, Einthoven ECG 1903) were available in Western European and American research centers by 1905; the actual invention occurred in the USSR in 1939.

Prerequisite technologies:
- Leyden jar / capacitor discharge circuit [1745, mature by 1890s] — external
- Reliable AC mains electrical supply [1880s–1890s] — external
- ECG (Einthoven electrocardiograph) [1903] — external
- Chest electrode design [~1900, from galvanic/electrotherapy practice] — team-reachable
- Electrotherapy apparatus (variable voltage, controllable discharge) [1880s] — external

Scientific theories / key empirical observations:
- Galvani/Volta: electrical stimulation of excitable tissue [1800] — external (off-limits, usable as published knowledge)
- Prevost and Batelli: strong shocks both induce and terminate ventricular fibrillation [1899] — external
- Cardiac conduction and fibrillation as electrical phenomenon [~1890s–1900s] — external
- Capacitor discharge waveform characterization [by 1900] — team-reachable

Explanation: Binding prerequisite is Prevost-Batelli 1899 + ECG 1903. A motivated team with animal surgery facility, standard electrical workshop equipment (capacitor bank, adjustable resistors), and ECG monitoring could systematically vary shock energy, waveform, and electrode placement. The gap to 1939 reflects niche underfunded field and lack of clinical urgency recognition before 1920s-1930s."""
    },
    {
        "invention": "Plutonium isolation",
        "year": 1940,
        "inventor": "Glenn T. Seaborg, Arthur Wahl & Joseph Kennedy",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1938–1940",
        "earliest_straightforward": "1939–1941",
        "actual_location": "Berkeley, California, USA",
        "possible_locations": "USA (Berkeley, Chicago); UK (Cavendish); Germany (Kaiser Wilhelm Institute); France (Paris)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Berkeley had the most advanced cyclotron infrastructure; other plausible sites had comparable nuclear physics programs.",
        "confidence": "Medium",
        "full_text": """Invention: Plutonium isolation
Year actually invented: 1940
Earliest plausible: 1938–1940
Earliest straightforward: 1939–1941
Confidence: Medium
Actual location: Berkeley, California, USA
Possible locations at earliest plausible date: USA (Berkeley, Chicago), UK (Cavendish), Germany (Kaiser Wilhelm Institute), France (Paris)
Geographic note: ALIGNED. Berkeley had the most advanced cyclotron infrastructure; other plausible sites had comparable nuclear physics programs.

Prerequisite technologies:
- Cyclotron [1930, Lawrence] — external
- Neutron source and deuteron beam [1932] — external
- Ion exchange and precipitation chemical separation [1920s–1930s] — external
- Geiger-Müller counters [1928] — external
- Fermi's neutron bombardment / transuranium synthesis [1934] — external

Scientific theories / key empirical observations:
- Radioactivity and decay chains [1896, Becquerel] — external
- Nuclear fission and transmutation feasibility [1938] — external
- Beta decay theory [1934, Fermi] — external

Explanation: Binding constraint is nuclear fission's publication (late 1938, external knowledge usable per rubric), which confirmed heavy-nucleus transmutation was achievable. Seaborg's team deliberately designed neutron-bombardment targeting U-238, predicted the two-step beta-decay chain to Z=94 on theoretical grounds, then confirmed it through systematic precipitation and ion-exchange chemistry. Not serendipitous. One-layer precursor: refining radiochemical separation to microgram sensitivity. Earliest plausible 1938–1940, essentially coinciding with actual date."""
    },
    {
        "invention": "Cavity Magnetron",
        "year": 1940,
        "inventor": "John Randall & Harry Boot",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1922–1926",
        "earliest_straightforward": "1926–1930",
        "actual_location": "Birmingham, England",
        "possible_locations": "USA; Germany; UK",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. UK, USA, and Germany all had comparable vacuum tube and precision machining capability in the mid-1920s.",
        "confidence": "Medium",
        "full_text": """Invention: Cavity magnetron (high-power microwave oscillator)
Year actually invented: 1940
Earliest plausible: 1922–1926
Earliest straightforward: 1926–1930
Confidence: Medium
Actual location: Birmingham, England
Possible locations at earliest plausible date: USA, Germany, UK
Geographic note: ALIGNED. UK, USA, and Germany all had comparable vacuum tube and precision machining capability in the mid-1920s.

Prerequisite technologies:
- Thermionic cathode / triode vacuum tube [1904–1913] — external
- High vacuum pumping [~1910–1915] — external
- Split-anode magnetron (Hull 1921) — external; establishes crossed-field E×B principle
- Barkhausen-Kurz oscillator [1920] — external
- Precision metal machining to centimeter tolerances [by ~1900] — external
- Permanent magnet materials for axial field [~1900s] — external
- Copper electroforming and brazing [~1910s] — team-reachable

Scientific theories / key empirical observations:
- Maxwell's electromagnetic theory / resonant cavity modes [1865] — external
- Hertz RF wave demonstration [1887] — external (usable as published knowledge)
- Hull's empirical characterization of electron cyclotron motion [1921] — external
- Resonant cavity Q-factor theory [team-discoverable from Maxwell ~1920s]

Explanation: Binding item is Hull's 1921 split-anode magnetron paper. Once that is available, the resonant-cavity anode is a one-layer engineering extension — replacing split anode with multi-cavity slotted copper block dimensioned empirically to target centimeter wavelength. No new science needed. The 14-year gap to 1940 reflects absence of compelling radar demand signal before late 1930s."""
    },
    {
        "invention": "PET Fiber",
        "year": 1941,
        "inventor": "John R. Whinfield & James T. Dickson",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1936–1938",
        "earliest_straightforward": "1938–1941",
        "actual_location": "England (Accrington, ICI)",
        "possible_locations": "United Kingdom; United States; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. England, the USA, and Germany were all leading centers of industrial polymer chemistry in the late 1930s.",
        "confidence": "High",
        "full_text": """Invention: Polyethylene terephthalate (PET) fiber (Terylene/Dacron)
Year actually invented: 1941
Earliest plausible: 1936–1938
Earliest straightforward: 1938–1941
Confidence: High
Actual location: England (Accrington, ICI)
Possible locations at earliest plausible date: United Kingdom, United States, Germany
Geographic note: ALIGNED. England, the USA, and Germany were all leading centers of industrial polymer chemistry in the late 1930s.

Prerequisite technologies:
- Melt-spinning equipment for synthetic fibers [1935] — external (developed for nylon)
- Condensation polymerization reactor technology [1930–1935] — external/team-reachable
- Terephthalic acid synthesis (aromatic diacid) [~1900s, well-established by 1930s] — external
- Ethylene glycol production (industrial-scale) [~1920s] — external
- High-vacuum distillation for monomer purification [1920s] — external/team-reachable

Scientific theories / key empirical observations:
- Staudinger macromolecule hypothesis [1920] — external
- Carothers' condensation polymerization framework [1930–1935] — external
- Carothers' finding that aliphatic polyesters melt too low for fiber use [1930–1935] — external (motivates aromatic substitution)

Explanation: Binding item is Carothers' published work (1930–1935) which established fiber-forming criteria and directly pointed teams toward aromatic diacids as solution. Terephthalic acid was a known commodity. Given Carothers' publications and commercial nylon by 1935–1936, a motivated team could synthesize and melt-spin PET within ~2–3 years, placing earliest plausible at 1936–1938. Gap to 1941 is wartime/institutional constraints."""
    },
    {
        "invention": "V-2 (A-4) long-range ballistic missile",
        "year": 1942,
        "inventor": "Wernher von Braun with the Peenemünde Army Research Center",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1933–1938",
        "earliest_straightforward": "1938–1945",
        "actual_location": "Peenemünde, Germany",
        "possible_locations": "Germany; United States; Soviet Union; United Kingdom",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Germany led due to institutional funding and coordination; US (Goddard) and Soviet Union (GIRD) had credible parallel programs.",
        "confidence": "Medium",
        "full_text": """Invention: V-2 (A-4) long-range ballistic missile
Year actually invented: 1942
Earliest plausible: 1933–1938
Earliest straightforward: 1938–1945
Confidence: Medium
Actual location: Peenemünde, Germany
Possible locations at earliest plausible date: Germany, United States, Soviet Union, United Kingdom
Geographic note: ALIGNED. Germany led due to institutional funding and coordination; US (Goddard) and Soviet Union (GIRD) had credible parallel programs.

Prerequisite technologies:
- Goddard liquid-fueled rocket [1926] — external
- De Laval nozzle [1897] — external
- Industrial liquid oxygen production [1895–1900] — external
- Gyroscope-based stabilization [1852, refined 1900s–1920s] — external
- Steam turbine and centrifugal pump engineering (basis for turbopump) [1880s–1900s] — external
- Ablative/regenerative cooling for combustion chamber [1920s–1930s] — team-reachable
- Graphite vane materials for exhaust [1920s industrial graphite] — external

Scientific theories / key empirical observations:
- Tsiolkovsky rocket equation [1903] — external
- Oberth's theoretical work on liquid rockets [1923] — external
- Aerodynamic stability of finned projectiles at supersonic speeds [pre-1930 ballistics] — external
- Gyroscopic precession as stabilization/guidance signal [1800s applied by 1910s] — external

Explanation: Binding constraint was engineering integration challenge of scaling pressure-fed liquid rocket by ~two orders of magnitude in thrust while adding inertial guidance, turbopump feed, and supersonic airframe — all as a unified system. All constituent elements available by late 1920s. A well-funded team could have begun in ~1928–1930 and reached V-2-class vehicle by 1933–1938. One-layer precursor: turbopump scaling from Goddard's pressure-fed baseline. The actual 1942 date falls within the earliest straightforward range, reflecting expected complexity of a large systems-integration challenge."""
    },
    {
        "invention": "Influenza vaccine",
        "year": 1944,
        "inventor": "Thomas Francis Jr. & Jonas Salk",
        "category": "",
        "category2": "",
        "earliest_plausible": "1936–1938",
        "earliest_straightforward": "1938–1940",
        "actual_location": "Ann Arbor, Michigan, USA",
        "possible_locations": "United Kingdom (MRC); USA (Rockefeller Institute, U Michigan); Australia (Walter and Eliza Hall Institute)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA was among best-positioned locations given strong institutional infrastructure, wartime funding, and access to Burnet's egg-culture methodology.",
        "confidence": "High",
        "full_text": """Invention: Influenza vaccine (killed-virus inactivated vaccine)
Year actually invented: 1944
Earliest plausible: 1936–1938
Earliest straightforward: 1938–1940
Confidence: High
Actual location: Ann Arbor, Michigan, USA
Possible locations at earliest plausible date: United Kingdom (MRC), USA (Rockefeller Institute, U Michigan), Australia (Walter and Eliza Hall Institute)
Geographic note: ALIGNED. The USA was among best-positioned locations given strong institutional infrastructure, wartime funding, and access to Burnet's egg-culture methodology.

Prerequisite technologies:
- Embryonated hen's egg culture for influenza virus [Burnet 1935–1936] — external
- Formaldehyde inactivation of pathogens for vaccine preparation [~1911, refined through 1920s] — external
- Hypodermic syringe / intramuscular injection [~1850s] — external
- Fermentation/culture laboratory infrastructure and sterile technique [~1880s] — external
- Filtration to confirm viral (non-bacterial) agents [~1890s–1910s] — external

Scientific theories / key empirical observations:
- Influenza confirmed as a virus [Smith, Andrewes & Laidlaw 1933] — external
- Killed-pathogen immunization principle [Salmon & Smith 1886; Wright typhoid vaccine 1896] — external
- Antigenic specificity of influenza strains — team-discoverable post-1933

Explanation: Binding constraint is Burnet's 1935–1936 egg-culture demonstration. All other components (formalin inactivation, killed-pathogen immunology, sterile injection) were fully established by mid-1930s. A motivated team in 1936 could have applied Burnet's method, grown virus, inactivated it, and iterated to effective dose within five years. The ~6-year gap to 1944 is explained by absence of sustained institutional funding and urgent demand before WWII."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
