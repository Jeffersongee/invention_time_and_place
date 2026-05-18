#!/usr/bin/env python3
"""Write batch 24 (indices 161-167) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Atomic bomb",
        "year": 1945,
        "inventor": "Manhattan Project team",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Los Alamos, New Mexico, USA",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: Atomic bomb (uranium gun-type and plutonium implosion fission weapon)
Year actually invented: 1945
Earliest plausible: Flag
Earliest straightforward: Flag
Confidence: Flag
Actual location: Los Alamos, New Mexico, USA
Possible locations at earliest plausible date: Flag
Geographic note: Flag

Prerequisite technologies:
- Nuclear fission discovery (Hahn/Strassmann/Meitner/Frisch) [1938–1939] — external
- Bohr-Wheeler fission theory and critical mass concept [1939] — external
- Neutron cross-section and multiplication factor measurements [1939–1942] — team-reachable empirically, but requires cyclotron/accelerator infrastructure beyond bench scale
- Uranium isotope separation (electromagnetic calutrons or gaseous diffusion cascades) [1940–1945] — requires massive industrial infrastructure; not one layer of precursor tech
- Nuclear reactor (to produce plutonium) [1942, CP-1] — itself requires refined uranium, graphite moderator, precise geometry; a distinct major engineering project
- Precision explosive lens fabrication and simultaneous multi-point detonation (implosion) [1943–1945] — team-reachable in principle, but depends on prior plutonium availability
- Electronic firing circuits with microsecond synchronization [1940s] — team-reachable

Scientific theories / key empirical observations:
- Liquid drop model of nucleus [1936] — external
- Chain reaction criticality conditions and neutron multiplication [1939] — external/team-discoverable post-fission publication
- Fast-neutron vs. thermal-neutron fission cross-sections [1939–1941] — team-reachable empirically with existing accelerators
- Spontaneous fission rate of Pu-240 (disqualifying gun-type for plutonium) [1944] — team-discoverable, but only after plutonium is produced

Explanation: The atomic bomb is flagged because both weapon designs are irreducibly dependent on two separate industrial-scale engineering projects — isotope separation and plutonium production — that cannot be collapsed into "one layer of precursor tech" buildable by a five-person artisan team. Uranium-235 separation requires either a gaseous diffusion cascade of thousands of barrier stages or electromagnetic separators of the calutron scale; even the smallest functional separation plant exceeds any plausible bench or pilot-scale effort by orders of magnitude. Plutonium production requires a sustained chain-reacting pile with many tonnes of refined uranium and high-purity graphite moderator, itself a major engineering project. These are not knowledge gaps a skilled team could close empirically in five years; they are fundamentally infrastructure and industrial-scale mass-production constraints. The implosion design adds a further requirement — explosive lens arrays with microsecond simultaneous detonation across dozens of points — which is in principle team-reachable but is moot without fissile material. Because the binding constraints are irreducibly organizational and industrial (not merely knowledge gaps or single-layer precursor technology buildable at artisan scale), this invention is flagged under criterion (c): fundamentally organizational/industrial rather than an engineering problem solvable by the stipulated team model."""
    },
    {
        "invention": "Microwave oven",
        "year": 1945,
        "inventor": "Percy Spencer",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1941–1943",
        "earliest_straightforward": "1943–1946",
        "actual_location": "Cambridge, Massachusetts, USA",
        "possible_locations": "United Kingdom; United States; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The cavity magnetron was developed in the UK (1940) and shared with the US via the Tizard Mission; both nations had the technical infrastructure and wartime radar programs to support directed microwave-heating research by 1941–1943.",
        "confidence": "Medium",
        "full_text": """Invention: Microwave oven
Year actually invented: 1945
Earliest plausible: 1941–1943
Earliest straightforward: 1943–1946
Confidence: Medium
Actual location: Cambridge, Massachusetts, USA
Possible locations at earliest plausible date: United Kingdom, United States, Germany
Geographic note: ALIGNED. The cavity magnetron was developed in the UK (1940) and shared with the US via the Tizard Mission; both nations had the technical infrastructure and wartime radar programs to support directed microwave-heating research by 1941–1943.

Prerequisite technologies:
- Magnetron (early oscillator type) [1921] — external
- Cavity magnetron (high-power, ~10 cm wavelength) [1940, Randall & Boot, UK] — external
- Waveguide and microwave plumbing techniques [late 1930s–1940] — external
- Industrial RF/dielectric heating (wood drying, glue curing) [late 1930s] — external/team-reachable
- Metal cavity enclosure fabrication [pre-1940] — external
- Basic thermostat and power-control circuitry [pre-1940] — external

Scientific theories / key empirical observations:
- Dielectric heating theory: polar molecules absorb RF energy and convert it to heat [1920s–1930s, well published] — external
- Microwave penetration depth in food-like dielectrics [empirically measurable by team, 1940–1941] — team-discoverable
- Standing-wave hot-spot behavior in enclosed cavities [team-discoverable via empirical iteration] — team-discoverable
- Optimal frequency band (~2.4 GHz) for food heating balance of penetration vs. absorption [team-discoverable empirically] — team-discoverable

Explanation: The binding item is the cavity magnetron (1940), which for the first time made available compact, high-power microwave energy at centimeter wavelengths. Once that device existed as external knowledge, a directed engineering team tasked with "heat food using RF/microwave energy" could draw on the well-understood theory of dielectric heating (published through the 1930s and industrially practiced for wood and rubber processing), fabricate a metal enclosure to contain and concentrate microwave energy, and empirically iterate on cavity geometry, power levels, and frequency to achieve uniform food heating — all within a five-year window. No new scientific framework is required; the team needs only to redirect existing radar hardware toward a civilian heating application and solve the straightforward engineering problems of safety enclosure, power control, and even heating. The historical accident of Spencer's chocolate bar is irrelevant to this assessment: the invention as an engineering artifact is fully achievable by directed effort once the magnetron is in hand, and the FLAG criterion does not apply because the artifact does not depend on the accident being reproduced. The earliest plausible date of 1941–1943 reflects the roughly one-to-two years needed to acquire cavity magnetrons, characterize dielectric heating behavior in foodstuffs, and build a working prototype enclosure; the straightforward date of 1943–1946 accounts for the additional iteration required to reach a functional, controllable appliance rather than a laboratory curiosity."""
    },
    {
        "invention": "Radiocarbon dating",
        "year": 1946,
        "inventor": "Willard Libby",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1943–1946",
        "earliest_straightforward": "1946–1950",
        "actual_location": "Chicago, Illinois, USA",
        "possible_locations": "USA; UK; Canada",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The combination of cyclotron infrastructure, Manhattan Project-era isotope research, and concentrated nuclear physics expertise made the USA — and specifically wartime/postwar Chicago — the near-exclusive plausible site at this date.",
        "confidence": "Medium",
        "full_text": """Invention: Radiocarbon dating (C-14 / carbon-14 radiometric dating)
Year actually invented: 1946
Earliest plausible: 1943–1946
Earliest straightforward: 1946–1950
Confidence: Medium
Actual location: Chicago, Illinois, USA
Possible locations at earliest plausible date: USA, UK, Canada
Geographic note: ALIGNED. The combination of cyclotron infrastructure, Manhattan Project-era isotope research, and concentrated nuclear physics expertise made the USA — and specifically wartime/postwar Chicago — the near-exclusive plausible site at this date.

Prerequisite technologies:
- Geiger-Müller radiation detector [1928] — external
- Cyclotron for isotope production and identification [1930] — external
- Mass spectrometry (isotope separation and measurement) [1919] — external
- High-sensitivity low-background radiation counting apparatus [~1940–1945] — team-reachable (one engineering layer: shielding + amplification improvements on existing Geiger counters)
- Cosmic ray detection and flux measurement instrumentation [1912–1935] — external

Scientific theories / key empirical observations:
- Radioactivity and radioactive decay law (half-life concept) [1896–1902, Becquerel, Rutherford, Soddy] — external
- Cosmic ray identification (Hess, 1912) — external
- Neutron discovery (Chadwick, 1932) — external
- Mechanism of cosmic-ray spallation producing atmospheric neutrons, which transmute N-14 to C-14 (Korff, 1939–1940) — external
- C-14 identified as a natural atmospheric isotope with measurable activity (Ruben and Kamen, 1940) — external
- C-14 half-life measured at ~5,730 years (~1940–1947, refined over time) — external by 1940s
- Assumption of steady-state atmospheric C-14 / C-12 ratio and biological uptake equilibrium — team-discoverable (empirical verification via measurement of contemporaneous organic samples, one engineering layer)

Explanation: The binding constraint is the convergence of two independent prerequisite chains, both of which closed only around 1939–1943: (1) the identification of C-14 as a naturally occurring atmospheric isotope produced by cosmic-ray neutron bombardment of nitrogen (Korff, Ruben, and Kamen, 1939–1940), and (2) the development of sufficiently sensitive, low-background radiation counting apparatus capable of detecting the extremely weak beta activity in ancient carbon samples. Before Korff's 1939 theoretical prediction and Ruben/Kamen's 1940 experimental confirmation of natural C-14, no team — however motivated — could have conceived the dating mechanism, because the existence of the natural atmospheric reservoir was unknown. Once those results were published, a directed team with access to wartime isotope infrastructure and Geiger counter technology could in principle have assembled Libby's methodology: collect organic samples of known age, measure their C-14 activity relative to living material, verify the exponential decay curve, and derive ages. The key non-obvious engineering insight Libby contributed — anticoincidence shielding of the detector to suppress cosmic-ray background noise enough to measure ancient sample activity — was a sophisticated but reachable one-layer engineering improvement on existing radiation-counting practice, not a new scientific discovery. No serendipity flag is warranted; the conceptual framework was fully constructable from published knowledge by 1941–1943, and the instrumentation challenge, while demanding, was within the scope of a skilled wartime physics/engineering team. The 1943 earliest plausible date reflects the minimum time after the Ruben/Kamen 1940 publication for a team to assemble the background-suppression apparatus, verify the steady-state equilibrium assumption empirically, and calibrate against archaeologically dated samples."""
    },
    {
        "invention": "Ejector seat",
        "year": 1946,
        "inventor": "James Marti",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1918–1922",
        "earliest_straightforward": "1935–1940",
        "actual_location": "England",
        "possible_locations": "United Kingdom; Germany; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The UK was a leading aviation and ordnance engineering nation; Martin-Baker's eventual solution drew on precisely the industrial and military expertise concentrated there and in peer nations.",
        "confidence": "Medium",
        "full_text": """Invention: Ejector seat (aircraft pilot emergency escape system)
Year actually invented: 1946
Earliest plausible: 1918–1922
Earliest straightforward: 1935–1940
Confidence: Medium
Actual location: England
Possible locations at earliest plausible date: United Kingdom, Germany, France, United States
Geographic note: ALIGNED. The UK was a leading aviation and ordnance engineering nation; Martin-Baker's eventual solution drew on precisely the industrial and military expertise concentrated there and in peer nations.

Prerequisite technologies:
- Explosive/propellant cartridges (cordite, black powder) [1889 / centuries] — external/team-reachable
- Parachute (reliable, folded, rip-cord deployed) [1797–1910s] — external/team-reachable
- Aircraft cockpit and fuselage structural engineering [1903–1915] — external/team-reachable
- Seat rail / linear guide systems (ordnance, elevator, industrial) [pre-1900] — external/team-reachable
- Occupant harness and restraint design [1910s aviation] — external/team-reachable
- Compressed gas cylinders (high-pressure, reliable) [1880s] — external/team-reachable
- Canopy jettison or breaker mechanism [1930s, team-reachable one layer] — team-reachable
- Human-factors load tolerance data (rough empirical, ~20g spinal limit) [WWI aviation medicine, 1914–1918] — external/team-reachable

Scientific theories / key empirical observations:
- Newtonian mechanics / impulse-momentum for controlled cartridge thrust [pre-1800] — external
- Empirical ballistics and propellant burn-rate characterization [18th–19th c.] — external
- Aviation medicine: human tolerance to rapid acceleration along spinal axis [1914–1918, refined WWII] — external/team-discoverable empirically
- Drag and terminal velocity of a human body in freefall [19th c. physics, parachute experiments] — external

Explanation: The binding item is the combination of a reliable high-speed aircraft that makes manual bailout impractical and the empirical calibration of a propellant cartridge delivering tolerable spinal acceleration (~20g). All hardware components — cordite cartridges, parachutes, seat rails, harnesses, compressed gas — existed by the end of World War I, and a motivated team could have assembled a test rig and iterated cartridge charge versus measured deceleration loads on an instrumented dummy within a five-year window. The earliest plausible date is therefore approximately 1918–1922: WWI produced both high-performance aircraft where bailout was dangerous and the ordnance/aviation engineering community needed to solve it, though the acute operational demand for speeds truly defeating manual bailout did not peak until the late 1930s jet era, making 1935–1940 the earliest straightforward date when demand, materials, and institutional urgency converged. The gap between earliest plausible (~1920) and actual (1946) is roughly 25 years, explained primarily by the absence of acute operational need (propeller aircraft at WWI speeds still permitted manual bailout in many cases) rather than any missing technical capability."""
    },
    {
        "invention": "Holography",
        "year": 1947,
        "inventor": "Dennis Gabor",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1895–1905",
        "earliest_straightforward": "1910–1920",
        "actual_location": "Rugby, England (British Thomson-Houston)",
        "possible_locations": "Germany; France; United Kingdom",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. United Kingdom is among the listed plausible locations, though the leading centers for precision optics and wave optics theory in 1895–1905 were Germany (Zeiss/Abbe) and France (Lippmann's Paris lab); Germany or France would have been the most probable independent discovery sites, but England remains a plausible location.",
        "confidence": "Medium",
        "full_text": """Invention: Holography (wavefront reconstruction photography)
Year actually invented: 1947
Earliest plausible: 1895–1905
Earliest straightforward: 1910–1920
Confidence: Medium
Actual location: Rugby, England (British Thomson-Houston)
Possible locations at earliest plausible date: Germany, France, United Kingdom
Geographic note: ALIGNED. United Kingdom is among the listed plausible locations, though the leading centers for precision optics and wave optics theory in 1895–1905 were Germany (Zeiss/Abbe) and France (Lippmann's Paris lab); Germany or France would have been the most probable independent discovery sites, but England remains a plausible location.

Prerequisite technologies:
- Fine-grain photographic emulsions (silver halide, sub-micron grain) [1880s] — external/team-reachable
- Lippmann interference color photography (demonstrated interference fringes in emulsion) [1891] — external/team-reachable
- Mercury arc lamp (high-pressure, intense line spectrum) [1900s] — external/team-reachable
- Pinhole spatial filter for quasi-coherent illumination [1890s, standard optics bench technique] — external/team-reachable
- Precision optical bench and vibration isolation [1880s] — external/team-reachable
- Zone plate theory (Rayleigh, Soret) and diffraction grating fabrication [1870s–1880s] — external/team-reachable
- High-resolution photographic plates (Lippmann plates, Wratten) [1891–1900s] — external/team-reachable

Scientific theories / key empirical observations:
- Wave optics: Young double-slit interference [1801] — external
- Fresnel diffraction and wavefront theory [1818] — external
- Abbe theory of image formation via diffraction [1873] — external
- Lippmann's empirical demonstration that interference fringes can be stably recorded in photographic emulsion [1891] — external
- Reconstruction of wavefronts from recorded diffraction patterns (zone plate analogy) [1870s–1880s] — external/team-discoverable
- Recognition that a reference beam encodes phase information alongside amplitude [team-discoverable by ~1895 given Lippmann + Abbe]

Explanation: The binding constraint on holography was not any missing material technology but the conceptual leap of recognizing that recording an interference pattern between an object beam and a coherent reference beam encodes full wavefront (phase + amplitude) information, and that illuminating the developed plate reconstructs the original wavefront. By 1891, Lippmann had already demonstrated that standing-wave interference fringes could be fixed in fine-grain emulsion and later reconstructed to reproduce color — this is structurally the same physical act as holographic recording. Abbe's 1873 theory established that diffraction patterns carry complete image information. A motivated team in 1895–1905, working in a precision optics environment (Zeiss, or Lippmann's own Paris laboratory), could have extended Lippmann's apparatus by introducing an oblique or separated reference beam, empirically observed that the resulting interference pattern reconstructed a 3D wavefront on illumination, and thereby demonstrated the holographic principle. The mercury arc lamp with spatial filtering was available by the early 1900s and provides adequate spatial coherence over the short path-length differences needed for a bench demonstration. The ~45-year gap between this earliest plausible date and 1947 is explained primarily by the absence of any perceived need: electron microscopy correction (Gabor's actual motivation) did not exist as a problem before the 1940s, and no one in the 1890s–1910s was searching for wavefront recording as such. The technology and theory were fully sufficient; the invention waited on problem framing, not capability."""
    },
    {
        "invention": "Hydraulic fracturing",
        "year": 1947,
        "inventor": "Floyd Farris & J. B. Clark, Stanolind",
        "category": "",
        "category2": "",
        "earliest_plausible": "1895–1905",
        "earliest_straightforward": "1910–1920",
        "actual_location": "Kansas, USA (Hugoton gas field)",
        "possible_locations": "USA (Pennsylvania, Ohio, West Virginia oil regions); Romania; Russia (Baku region)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The invention emerged in the USA, which by the 1890s–1900s had the world's most developed petroleum industry, the highest concentration of well-drilling expertise, and mature high-pressure pump technology — precisely the conditions required for earliest plausible development.",
        "confidence": "Medium",
        "full_text": """Invention: Hydraulic fracturing (hydraulic fracking for oil/gas well stimulation)
Year actually invented: 1947
Earliest plausible: 1895–1905
Earliest straightforward: 1910–1920
Confidence: Medium
Actual location: Kansas, USA (Hugoton gas field)
Possible locations at earliest plausible date: USA (Pennsylvania, Ohio, West Virginia oil regions), Romania, Russia (Baku region)
Geographic note: ALIGNED. The invention emerged in the USA, which by the 1890s–1900s had the world's most developed petroleum industry, the highest concentration of well-drilling expertise, and mature high-pressure pump technology — precisely the conditions required for earliest plausible development.

Prerequisite technologies:
- High-pressure reciprocating pumps (>3000 psi capable) [1870s–1890s] — external; industrial pump technology for water and oil pipelines was well-developed by the 1880s
- Cable-tool and rotary drilling rigs capable of deep wellbores [1860s–1890s] — external
- Wellbore packer/isolation tool (inflatable or mechanical) [1870s–1880s] — external; rubber packer technology existed in the oil patch by the 1870s; team could refine for pressure isolation
- Viscous gelled fluid (napalm-like gel, thick crude oil, or gum-water) as fracturing medium [team-reachable by 1890s] — team can formulate empirically from known thickening agents (linseed oil, rosin, gum arabic)
- Sand/gravel as proppant [1880s] — external; already used as filter medium and in well completions
- Nitroglycerin well shooting (explosive well stimulation) [1865] — external; established practice demonstrating that downhole pressure increase improves productivity

Scientific theories / key empirical observations:
- Elasticity of solids and fracture mechanics (Hooke's Law, Rankine, Kirsch stress solutions) [1678–1890s] — external; engineering literature on rock and material fracture available; team need not derive theory, only apply empirically
- Observation that well productivity correlates with natural fracture density [team-discoverable by 1890s] — empirical field observation available to any attentive petroleum engineer
- In-situ stress orientation governs fracture azimuth (vertical vs. horizontal fracture regime) [team-discoverable empirically by ~1900] — team can observe fracture behavior in outcrops and core samples and infer directionality without formal geomechanics theory
- Pressure-volume behavior of fluids in confined rock (empirical Darcy's Law, 1856) [1856] — external

Explanation: The binding constraint is not any single piece of unavailable technology but rather the conceptual reorientation from explosive stimulation (nitroglycerin shooting, practiced since 1865) to controlled hydraulic pressure as a fracture-creating mechanism. By the mid-1890s, all hardware prerequisites existed: high-pressure steam-driven or gasoline-driven pump plungers capable of sustained >3000 psi output were commercially available for pipeline and boiler service; rubber or lead wellbore packers were in routine use; sand and gravel were obvious proppant candidates; and viscous oils or gum solutions were known thickeners. A motivated team at a major oil-producing region — Pennsylvania, Ohio, or Baku — could within five years empirically establish that sustained fluid injection at pressures above formation breakdown creates productive fractures, observe that sand injected with the fluid holds them open, and optimize fluid viscosity and pump rate by trial and error without requiring any new scientific framework. The one-layer precursor fabrication needed is a purpose-built high-pressure downhole injection string with a reliable packer, which is a straightforward adaptation of existing tubular and packer technology. The ~50-year gap between earliest plausible (~1895–1905) and actual invention (1947) is attributable to the dominance of the nitroglycerin paradigm, the absence of institutional pressure to optimize tight formations when prolific conventional fields were abundant, and the lack of a systematic research program in well stimulation until Stanolind established one in the 1940s — none of these are FLAG-worthy scientific barriers."""
    },
    {
        "invention": "Transistor",
        "year": 1947,
        "inventor": "John Bardeen & Walter Brattain; theory by William Shockley",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1944–1946",
        "earliest_straightforward": "1946–1948",
        "actual_location": "Murray Hill, New Jersey, USA (Bell Labs)",
        "possible_locations": "USA; UK; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred at Bell Labs, USA, which had the deepest concentration of semiconductor expertise, WWII radar germanium purification infrastructure, and institutional support for solid-state research; UK and Germany also had sufficient radar-driven germanium work and band theory knowledge to be plausible alternate sites.",
        "confidence": "Medium",
        "full_text": """Invention: Transistor (point-contact transistor)
Year actually invented: 1947
Earliest plausible: 1944–1946
Earliest straightforward: 1946–1948
Confidence: Medium
Actual location: Murray Hill, New Jersey, USA (Bell Labs)
Possible locations at earliest plausible date: USA, UK, Germany
Geographic note: ALIGNED. The actual invention occurred at Bell Labs, USA, which had the deepest concentration of semiconductor expertise, WWII radar germanium purification infrastructure, and institutional support for solid-state research; UK and Germany also had sufficient radar-driven germanium work and band theory knowledge to be plausible alternate sites.

Prerequisite technologies:
- Crystal rectifier (point-contact diode) for radar [1940–1944] — external
- High-purity germanium preparation (Czochralski pulling, zone-purification precursors) [1944–1945] — external (WWII radar program)
- Fine mechanical needle/whisker contact fabrication and positioning [1940s] — external/team-reachable
- Low-noise electrical measurement equipment (oscilloscopes, lock-in-style amplifiers) [1940s] — external

Scientific theories / key empirical observations:
- Band theory of semiconductors, p-type/n-type distinction (Wilson 1931, Mott 1939) [1931–1939] — external by 1940
- Minority carrier injection concept (derivable from band theory + empirical rectifier behavior) [1940s] — team-discoverable given external band theory
- Surface state theory explaining contact behavior (Bardeen 1947) [1947] — team-discoverable; binding item
- Empirical observation that two closely-spaced contacts produce amplification [discoverable by systematic sweep of contact geometry] — team-discoverable

Explanation: The binding constraint is surface state theory (Bardeen 1947): without understanding that surface states pin the Fermi level and suppress the bulk field-effect, a team pursuing field-effect amplification would repeatedly fail and have no framework to redirect toward the two-contact minority-carrier geometry that actually worked. However, surface state theory is itself derivable from band theory (external by 1940) plus careful empirical study of rectifier anomalies — it does not require a new scientific framework, only a focused theoretical extension that a team with a skilled solid-state theorist could reach in one layer of precursor work. Given WWII-quality germanium (available 1944–1945), external band theory, and a team including both an empirical device engineer and a semiconductor theorist, the point-contact geometry could plausibly be discovered by systematic variation of contact spacing and type on high-purity germanium by 1944–1946, with 1946 being the most credible earliest-plausible year. The straightforward date aligns closely with the actual 1947 date, confirming Bell Labs achieved this near the engineering frontier with no major historical slack."""
    },
]

with open(CHECKPOINT, "a") as f:
    for entry in entries:
        f.write(json.dumps(entry) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
