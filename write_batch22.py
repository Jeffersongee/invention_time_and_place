#!/usr/bin/env python3
"""Write batch 22 (indices 147-153) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Recirculating ball screw",
        "year": 1929,
        "inventor": "Rudolph G. Boehm",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1895–1905",
        "earliest_straightforward": "1910–1920",
        "actual_location": "USA",
        "possible_locations": "USA; UK; Germany; France",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA, UK, and Germany all had mature precision machine tool industries and ball bearing manufacturing by the mid-1890s; the actual invention in the USA is consistent with this distribution.",
        "confidence": "Medium",
        "full_text": """Invention: Recirculating ball screw
Year actually invented: 1929
Earliest plausible: 1895–1905
Earliest straightforward: 1910–1920
Confidence: Medium
Actual location: USA
Possible locations at earliest plausible date: USA, UK, Germany, France
Geographic note: ALIGNED. The USA, UK, and Germany all had mature precision machine tool industries and ball bearing manufacturing by the mid-1890s; the actual invention in the USA is consistent with this distribution.

Prerequisite technologies:
- Precision screw-cutting lathes [~1800–1820] — external/team-reachable
- Hardened steel ball bearings (radial load) [~1880s] — external/team-reachable
- Thread grinding machines capable of tight tolerances on hardened steel [~1885–1895] — external/team-reachable
- Ball bearing retainer and raceway design [~1880s] — external/team-reachable
- Precision measurement and gauging [~1870s–1880s] — external/team-reachable
- Case-hardening and heat treatment of steel [~1880s–1890s] — external/team-reachable

Scientific theories / key empirical observations:
- Rolling friction substantially lower than sliding friction [pre-1800] — external
- Hertz contact stress theory [1881] — external/team-reachable
- Thread helix geometry and mechanical advantage [pre-1800] — external
- Ball recirculation geometry requiring return tube or deflector — team-discoverable by iteration

Explanation: Binding constraint is thread grinding technology capable of producing hardened helical grooves to close tolerances, available late 1880s to mid-1890s. By ~1895 a motivated team could have combined hardened steel balls, ground helical raceways, and a ball-return tube into a functioning recirculating ball screw. The ~30-year gap is attributable to lack of application demand (plain lead screws were adequate). No flag warranted."""
    },
    {
        "invention": "Phase-contrast microscopy",
        "year": 1930,
        "inventor": "Frits Zernike",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1880–1890",
        "earliest_straightforward": "1895–1905",
        "actual_location": "Netherlands (Groningen)",
        "possible_locations": "Germany; United Kingdom; France; Austria",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. The earliest plausible window aligns with German and British optical industries (Zeiss, Abbe's Jena), not the Netherlands; Zernike's actual location was peripheral to the major optical manufacturing centers.",
        "confidence": "Medium",
        "full_text": """Invention: Phase-contrast microscopy
Year actually invented: 1930
Earliest plausible: 1880–1890
Earliest straightforward: 1895–1905
Confidence: Medium
Actual location: Netherlands (Groningen)
Possible locations at earliest plausible date: Germany, United Kingdom, France, Austria
Geographic note: MISMATCH. The earliest plausible window aligns with German and British optical industries (Zeiss, Abbe's Jena), not the Netherlands; Zernike's actual location was peripheral to the major optical manufacturing centers.

Prerequisite technologies:
- High-quality achromatic/apochromatic microscope objectives [1870s–1880s] — external
- Annular diaphragm/aperture stop fabrication [pre-1850] — external
- Thin optical glass plate grinding and coating to precise tolerances [1870s] — team-reachable
- Coherent illumination with condenser control [1870s] — external

Scientific theories / key empirical observations:
- Abbe diffraction theory of microscope image formation [1873] — external
- Optical path length and phase retardation in thin transparent media (Fresnel/Young) [1820s–1830s] — external
- Understanding that λ/4 phase shift converts phase contrast to amplitude contrast [team-discoverable after 1873]

Explanation: Binding item is Abbe's 1873 diffraction theory. Once that framework existed, a skilled optical team had all prerequisites. The gap from 1873 to 1930 (~57 years) reflects failure of imaginative synthesis — no one thought to exploit the back focal plane for phase manipulation. The earliest straightforward (1895–1905) benefits from Köhler illumination (1893) and improved glass quality. Gap is under 100 years."""
    },
    {
        "invention": "Electron microscope",
        "year": 1931,
        "inventor": "Ernst Ruska, with Max Knoll",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1927–1930",
        "earliest_straightforward": "1930–1935",
        "actual_location": "Berlin, Germany",
        "possible_locations": "Germany; United Kingdom; United States; France",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Berlin was the global center of electron physics and vacuum tube engineering in the late 1920s; the actual invention occurred exactly where conditions were most favorable.",
        "confidence": "High",
        "full_text": """Invention: Electron microscope
Year actually invented: 1931
Earliest plausible: 1927–1930
Earliest straightforward: 1930–1935
Confidence: High
Actual location: Berlin, Germany
Possible locations at earliest plausible date: Germany, United Kingdom, United States, France
Geographic note: ALIGNED. Berlin was the global center of electron physics and vacuum tube engineering in the late 1920s; the actual invention occurred exactly where conditions were most favorable.

Prerequisite technologies:
- Cathode ray tube / electron gun [1897, Braun] — external
- High-vacuum pumping (Gaede) [1905–1910] — external
- Solenoid magnetic focusing coils [pre-1900] — external
- Fluorescent screen detection [1890s] — external
- Photographic plate recording [1840s] — external
- Busch magnetic lens theory and demonstration [1926] — external

Scientific theories / key empirical observations:
- de Broglie matter-wave hypothesis (electron wavelength) [1924] — external
- Davisson-Germer electron diffraction confirmation [1927] — external
- Electron scattering and beam collimation behavior [1890s–1920s] — external

Explanation: Binding item is de Broglie 1924 + Busch 1926. Without de Broglie, no engineer has reason to pursue electron imaging. Once both are in hand (confirmed by Davisson-Germer 1927), a team could assemble electron gun, magnetic focusing, and fluorescent detector by ~1930. The 1931 actual date is close to the theoretical minimum."""
    },
    {
        "invention": "FM Radio",
        "year": 1933,
        "inventor": "Edwin Armstrong",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1928–1932",
        "earliest_straightforward": "1931–1934",
        "actual_location": "New York, USA",
        "possible_locations": "USA; Germany; UK",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA led in radio engineering and commercial radio infrastructure in the late 1920s–early 1930s.",
        "confidence": "Medium",
        "full_text": """Invention: FM radio broadcast system
Year actually invented: 1933
Earliest plausible: 1928–1932
Earliest straightforward: 1931–1934
Confidence: Medium
Actual location: New York, USA
Possible locations at earliest plausible date: USA, Germany, UK
Geographic note: ALIGNED. The USA led in radio engineering and commercial radio infrastructure in the late 1920s–early 1930s.

Prerequisite technologies:
- Superheterodyne receiver [1918, Armstrong] — external/team-reachable
- Wideband IF amplifier stages [~1926–1928] — team-reachable (one layer using screen-grid pentode tubes)
- Screen-grid pentode vacuum tube [1926–1928] — external/team-reachable
- Limiter circuit — team-reachable
- Frequency discriminator/slope detector — team-reachable
- Stable variable-frequency RF oscillator — team-reachable
- Reactance tube modulator — team-reachable

Scientific theories / key empirical observations:
- Hertz RF wave propagation [1887–1890] — external/team-usable
- Carson bandwidth analysis of FM [1922] — external; team must empirically refute
- Noise suppression via limiting + wide deviation — team-discoverable empirically ~1926–1930

Explanation: Binding constraint was stable wideband IF amplification, enabled by the screen-grid pentode (~1926–1928). Carson's 1922 dismissal of FM created a conceptual barrier. A team with pentode tubes, superheterodyne architecture, and empirical observation of impulse noise being amplitude-structured could iterate to a working FM system by 1928–1932. The one-layer precursor is the wideband IF chain. Gap from ~1928 to 1933 is modest."""
    },
    {
        "invention": "Lightweight folding wheelchair",
        "year": 1933,
        "inventor": "Harry C. Jennings Sr. & Herbert Everest",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1893–1898",
        "earliest_straightforward": "1900–1910",
        "actual_location": "USA",
        "possible_locations": "USA; UK; Germany; France",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. All four nations had mature bicycle industries and thin-wall steel tubing by the mid-1890s.",
        "confidence": "High",
        "full_text": """Invention: Lightweight folding wheelchair
Year actually invented: 1933
Earliest plausible: 1893–1898
Earliest straightforward: 1900–1910
Confidence: High
Actual location: USA
Possible locations at earliest plausible date: USA, UK, Germany, France
Geographic note: ALIGNED. All four nations had mature bicycle industries and thin-wall steel tubing by the mid-1890s.

Prerequisite technologies:
- Thin-wall steel tubing, bicycle industry [1885–1890] — external
- Swaged and brazed tube joints [1880s] — external
- Lightweight rubber tires and wheels (bicycle technology) [1888–1890] — external
- X-frame folding geometry (folding camp stools) [mid-19th century] — external
- Footrest/armrest hardware, hinges and locking pins [by 1880s] — external

Scientific theories / key empirical observations:
- Beam and column mechanics (hollow vs. solid sections) [by 1870s] — external
- Steel alloy properties and tube-drawing [1880s] — external

Explanation: Every element was commercially available by early 1890s. The bicycle boom produced an entire industry for lightweight steel tubing directly transferable. The X-brace folding mechanism was already in mass-produced camp furniture. The ~35-year gap to 1933 reflects demand (need for car-transportable wheelchair not present until widespread automobile ownership) rather than technical barrier. Not flagged."""
    },
    {
        "invention": "Nylon synthetic fiber",
        "year": 1935,
        "inventor": "Wallace Carothers",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1924–1928",
        "earliest_straightforward": "1928–1933",
        "actual_location": "Wilmington, Delaware, USA (DuPont)",
        "possible_locations": "Germany; United Kingdom; United States; Switzerland",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention in the USA at a well-resourced industrial lab is consistent with the earliest plausible window that also favors Germany and the UK.",
        "confidence": "Medium",
        "full_text": """Invention: Nylon (polyamide synthetic fiber)
Year actually invented: 1935
Earliest plausible: 1924–1928
Earliest straightforward: 1928–1933
Confidence: Medium
Actual location: Wilmington, Delaware, USA (DuPont)
Possible locations at earliest plausible date: Germany, United Kingdom, United States, Switzerland
Geographic note: ALIGNED. The actual invention in the USA at a well-resourced industrial lab is consistent with the earliest plausible window that also favors Germany and the UK.

Prerequisite technologies:
- Condensation polymerization apparatus [1880s–1910s] — external/team-reachable
- Industrial organic synthesis of diamines and dicarboxylic acids [1890s–1910s] — external/team-reachable
- Viscose/cellulose fiber spinning equipment [1900–1910] — external/team-reachable
- High-vacuum molecular-weight measurement [1910s] — external/team-reachable

Scientific theories / key empirical observations:
- Staudinger macromolecule hypothesis [1920] — external (binding constraint)
- Fischer esterification and condensation reaction chemistry [1890s] — external
- Polyesters and polyamides of sufficient chain length can be melt-drawn into fibers — team-discoverable by systematic iteration

Explanation: Binding constraint is Staudinger's 1920 macromolecule hypothesis. Before 1920, high-MW polymers were misunderstood as colloids, misdirecting synthesis. Once Staudinger's framework propagated (~1922–1924), a well-funded team with organic chemistry expertise could systematically sweep AA+BB polyamide pairs and iterate to a fiber-grade product. Melt-spinning is a single engineering layer from viscose equipment. Earliest plausible 1924–1928; straightforward 1928–1933 reflecting time needed for monomers and chain-length optimization."""
    },
    {
        "invention": "Programmable computer",
        "year": 1938,
        "inventor": "Konrad Zuse",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1880–1890",
        "earliest_straightforward": "1900–1910",
        "actual_location": "Berlin, Germany",
        "possible_locations": "United Kingdom; United States; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Germany (Berlin) is among the plausible locations alongside the UK and USA, which had stronger concentrations of relay-switching engineering and mechanical computing heritage (Babbage legacy); since the actual invention occurred in Germany and Germany is listed as a plausible site, the entry is ALIGNED.",
        "confidence": "Medium",
        "full_text": """Invention: Programmable computer (electromechanical relay-based)
Year actually invented: 1938
Earliest plausible: 1880–1890
Earliest straightforward: 1900–1910
Confidence: Medium
Actual location: Berlin, Germany
Possible locations at earliest plausible date: United Kingdom, United States, Germany
Geographic note: ALIGNED. Germany (Berlin) is among the plausible locations alongside the UK and USA, which had stronger concentrations of relay-switching engineering and mechanical computing heritage (Babbage legacy); since the actual invention occurred in Germany and Germany is listed as a plausible site, the entry is ALIGNED.

Prerequisite technologies:
- Telegraph relay as binary switch [1844] — external/team-reachable
- Relay circuit wiring and multi-stage relay logic [1850s–1860s] — external/team-reachable
- Punched tape / Jacquard loom program input concept [1801; punched telegraph tape 1846] — external/team-reachable
- Mechanical counter and register mechanisms [1820s–1850s] — external/team-reachable
- Hollerith punched-card tabulation [1890] — external
- Binary number representation [1703, Leibniz] — external

Scientific theories / key empirical observations:
- Boolean algebra [Boole 1854] — external; relay AND/OR/NOT also team-discoverable empirically by wiring relays in series/parallel
- Shannon's relay-circuit/Boolean equivalence [1937] — external after 1937; NOT a hard prerequisite
- Conditional branching and looping — team-discoverable from Jacquard/Babbage concepts

Explanation: Binding item is the conceptual synthesis of relay switching logic + stored sequential instruction stream (punched tape) + binary register arithmetic as a unified machine. All hardware prerequisites were available by mid-1880s. A motivated telegraph/instrument engineer with Babbage's published work could synthesize relay-logic registers with punched-tape sequencing by ~1880–1890. The ~50-year gap to 1938 reflects a conceptual-synthesis gap (no perceived need) — demand/perception gap, NOT flagged per rubric."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
