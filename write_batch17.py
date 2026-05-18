#!/usr/bin/env python3
"""Write batch 17 (indices 112-118) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

entries = [
    {
        "invention": "Wireless telegraphy",
        "year": 1895,
        "inventor": "Guglielmo Marconi",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1890–1893",
        "earliest_straightforward": "1893–1895",
        "actual_location": "Italy / Bologna, Italy",
        "possible_locations": "United Kingdom; Germany; France; Italy; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. By 1890 the relevant electrical instrument-making expertise (induction coils, galvanometers, relays) and physics literature were widely distributed across Western Europe and the northeastern US; Bologna/London/Berlin/Paris are all plausible.",
        "confidence": "High",
        "full_text": """Invention: Wireless telegraphy
Year actually invented: 1895
Earliest plausible: 1890–1893
Earliest straightforward: 1893–1895
Confidence: High
Actual location: Italy / Bologna, Italy (later developed in England)
Possible locations at earliest plausible date: United Kingdom, Germany, France, Italy, United States
Geographic note: ALIGNED. By 1890 the relevant electrical instrument-making expertise (induction coils, galvanometers, relays) and physics literature were widely distributed across Western Europe and the northeastern US; Bologna/London/Berlin/Paris are all plausible.
Prerequisite technologies:
- Induction (Ruhmkorff) coil for high-voltage spark generation [1851] — external
- Spark-gap oscillator / Hertzian dipole apparatus [1887–1888] — external (Hertz off-limits as discovery, usable as published knowledge)
- Morse telegraph key and relay technology [1840s] — external
- Branly coherer (filings tube detector) [1890] — external (or team-reachable as a one-layer empirical refinement of known conductivity-under-spark observations from the 1850s–1870s, e.g., Varley, Calzecchi-Onesti)
- Sensitive relays and telegraph sounders [1850s–1870s] — external
- Elevated wire antennas / grounded conductors [team-reachable empirical iteration]
Scientific theories / key empirical observations:
- Maxwell's electromagnetic theory [1865] — external
- Hertz's experimental demonstration of EM wave propagation, reflection, polarization [1887–1888] — external (off-limits as team discovery)
- Branly's observation of resistance change in metal filings under EM disturbance [1890] — external/team-reachable
- Lodge's syntonic/tuning improvements and coherer tapping [1894] — team-reachable (empirical iteration within five years)
Explanation: The binding item is Hertz's 1887–1888 publication demonstrating that Maxwell's electromagnetic waves can be generated and detected across a room with spark-gap apparatus; this is off-limits as a team discovery but becomes fully usable external knowledge once published. Given a motivated inventor plus a skilled instrument workshop, every other ingredient — induction coils, Morse keying, sensitive relays, elevated antennas, and a filings-tube detector (Branly's coherer is a modest one-layer empirical step from earlier filings-conductivity observations) — was already in hand or easily reached by empirical iteration. Therefore the earliest plausible start is essentially "as soon as Hertz is on the bookshelf": a five-year program launched in 1888 could yield a working Morse-keyed wireless link by roughly 1890–1893, with a robust, reproducible system (matching Marconi's 1895 demo) emerging straightforwardly by 1893–1895. Branly's 1890 coherer accelerates the detector side but is not strictly binding, since a team could derive an equivalent filings detector empirically."""
    },
    {
        "invention": "X-ray",
        "year": 1895,
        "inventor": "Wilhelm Röntgen",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Würzburg, Germany",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: X-ray (discovery of X-radiation)
Year actually invented: 1895
Earliest plausible: Flag
Earliest straightforward: Flag
Confidence: Flag
Actual location: Würzburg, Germany
Possible locations at earliest plausible date: Flag
Geographic note: Flag
Explanation: The discovery of X-radiation is a canonical phenomenon-discovery, not an engineering achievement. Röntgen's 1895 discovery was a serendipitous accident — he noticed unexpected fluorescence on a screen while experimenting with a Crookes tube, revealing a previously unknown form of radiation. The rubric explicitly calls out serendipitous accidents that a directed program cannot replicate and identifies phenomenon-discovery as a flag criterion. A motivated engineering team in the 1890s could certainly construct high-voltage discharge tubes and fluorescent screens, but the discovery of X-rays required noticing an anomalous effect whose existence was entirely unknown and unsuspected. No directed program could have targeted "find X-rays" because the phenomenon was not known to exist. Earlier experimenters including Hittorf, Crookes, and Lenard had operated similar apparatus without recognizing the radiation, confirming that the discovery was not an inevitable engineering outcome but a contingent observational accident. Because the invention is fundamentally a phenomenon-discovery enabled by serendipity rather than directed engineering, all date and location fields are flagged per rubric."""
    },
    {
        "invention": "Cloth surgical mask",
        "year": 1897,
        "inventor": "Jan Mikulicz-Radecki",
        "category": "Medical",
        "category2": "",
        "earliest_plausible": "1867–1880",
        "earliest_straightforward": "1880–1895",
        "actual_location": "Poland/France (Breslau and Paris)",
        "possible_locations": "Germany; France; United Kingdom; Austria-Hungary; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Continental European surgical centers (especially German-speaking and French) were the leading sites for antiseptic/aseptic surgical innovation in the late 19th century, matching the actual invention locations.",
        "confidence": "High",
        "full_text": """Invention: Cloth surgical mask
Year actually invented: 1897
Earliest plausible: 1867–1880
Earliest straightforward: 1880–1895
Confidence: High
Actual location: Poland/France (Breslau and Paris)
Possible locations at earliest plausible date: Germany, France, United Kingdom, Austria-Hungary, United States
Geographic note: ALIGNED. Continental European surgical centers (especially German-speaking and French) were the leading sites for antiseptic/aseptic surgical innovation in the late 19th century, matching the actual invention locations.
Prerequisite technologies:
- Fine-weave cotton/linen gauze [ancient; mass-produced industrially by ~1850] — external
- Sterilization by boiling/steam (autoclave) [Chamberland autoclave 1879; boiling far earlier] — external
- Carbolic acid / antiseptic solutions [Lister 1867] — external
Scientific theories / key empirical observations:
- Germ theory of disease [Pasteur 1861, Koch 1876] — external
- Listerian antiseptic surgery [Lister 1867] — external
- Droplet/respiratory transmission of bacteria from speech (Flügge) [1897] — team-discoverable (simple culture-plate experiment)
Explanation: The artifact itself is trivial — a square of sterile gauze with ties — so the binding constraint is conceptual, not material: recognizing that the surgeon's own breath and speech droplets carry viable bacteria into the wound. Once germ theory (1861) and Listerian antisepsis (1867) were in place, a motivated surgeon-plus-artisan team could have run the empirical test (speak over a culture plate, observe colonies) within weeks and immediately adopted gauze masks, putting earliest plausible invention at roughly 1867–1880. The reason it took until 1897 is that early aseptic practice focused on hands, instruments, and gowns; Carl Flügge's 1897 droplet experiments were what finally made the respiratory-source insight obvious, and Mikulicz adopted the mask the same year. No new science, no precursor chain, and no serendipity is required — only the missing observation, which is well within a five-year empirical program for a post-1867 team."""
    },
    {
        "invention": "Polyethylene",
        "year": 1898,
        "inventor": "Hans von Pechmann",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Germany / Munich, Germany",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: Polyethylene
Year actually invented: 1898
Earliest plausible: Flag
Earliest straightforward: Flag
Confidence: Flag
Actual location: Germany / Munich, Germany
Possible locations at earliest plausible date: Flag
Geographic note: Flag
Explanation: Pechmann's 1898 polymethylene (later recognized as polyethylene) was an irreducibly serendipitous observation rather than a directed synthesis. Pechmann was studying diazomethane chemistry for entirely unrelated reasons — investigating its reactivity as a methylating agent and source of carbenes — when he noticed a white waxy precipitate at the bottom of an ether flask after the reagent had stood/decomposed. The binding constraint is conceptual, not material: in the 1890s no chemist was looking for "long-chain saturated hydrocarbon polymers," because the very concept of covalent macromolecules did not yet exist (Staudinger's macromolecular hypothesis dates to 1920 and was fiercely resisted into the 1930s). Without knowing that such structures are achievable and worth targeting, no rational research program of the era would have aimed at CH2 coupling to a waxy solid as a goal, nor recognized the product as a polymer rather than a curious impurity. The diazomethane route is also a dead end industrially (toxic, explosive, low yield); the industrially relevant polyethylene (ICI, 1933) came from an entirely different high-pressure ethylene route with no conceptual connection to Pechmann's observation. Both the serendipitous-accident and the phenomenon-discovery criteria apply, so this entry is flagged."""
    },
    {
        "invention": "Nickel cadmium rechargeable battery",
        "year": 1899,
        "inventor": "Waldemar Jungner",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1860–1870",
        "earliest_straightforward": "1875–1885",
        "actual_location": "Sweden / Stockholm, Sweden",
        "possible_locations": "United Kingdom; France; Germany; Sweden; United States; Belgium; Austria-Hungary",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrial-scale electrochemistry, refined cadmium, and KOH production were available across Western/Central Europe and the northeastern US by the 1860s, so Sweden is one of many plausible loci.",
        "confidence": "Medium",
        "full_text": """Invention: Nickel cadmium rechargeable battery
Year actually invented: 1899
Earliest plausible: 1860–1870
Earliest straightforward: 1875–1885
Confidence: Medium
Actual location: Sweden / Stockholm, Sweden
Possible locations at earliest plausible date: United Kingdom, France, Germany, Sweden, United States, Belgium, Austria-Hungary
Geographic note: ALIGNED. Industrial-scale electrochemistry, refined cadmium, and KOH production were available across Western/Central Europe and the northeastern US by the 1860s, so Sweden is one of many plausible loci.
Prerequisite technologies:
- Cadmium metal, refined and commercially available [1817–1850] — external/team-reachable
- Nickel metal and nickel salts (sulfate, nitrate, hydroxide) [1751–1850] — external/team-reachable
- Potassium hydroxide via causticization of potash (and post-LeBlanc routes) [pre-1860] — external/team-reachable
- Lead-acid secondary cell as paradigm of rechargeable cells [1859, Planté] — external/team-reachable
- Galvanic cell construction: porous separators, perforated metal supports, sealed jars [1830s–1850s] — external/team-reachable
- Electroplating practice for depositing Cd and Ni onto metal substrates [1840s] — external/team-reachable
- Steady DC sources for cycling (Daniell/Grove batteries; later dynamos) [1836–1870s] — external/team-reachable
Scientific theories / key empirical observations:
- Faraday's laws of electrolysis [1834] — external/team-discoverable
- Reversibility of electrochemical reactions, demonstrated by Planté [1859] — external/team-discoverable
- Stability of nickel and cadmium hydroxides in concentrated alkali (corrosion resistance) [empirically known mid-1800s] — external/team-discoverable
- Higher-valent nickel oxide/oxyhydroxide formation under anodic oxidation in alkali [observed 1840s–1860s] — external/team-discoverable
Explanation: Once Planté (1859) established the secondary-cell paradigm, building a Cd/NiOOH/KOH cell is essentially a systematic electrochemical screening problem rather than a new-science problem: all four materials (Cd, Ni compounds, KOH, iron/nickel-plated containers) were industrially available, and the underlying empirical fact — that nickel in alkali oxidizes to a higher-valent active mass and that cadmium in alkali plates and strips reversibly without dendritic shorting like zinc — is discoverable by a five-year directed program of cycling candidate electrode pairs. The binding item is therefore the lead-acid precedent itself (1859); given that, a motivated inventor plus skilled workshop could have arrived at NiCd by the mid-to-late 1860s, with 1875–1885 being the comfortably straightforward window once Planté-style pasted-plate construction and laboratory dynamos were widespread. The ~30-year delay to 1899 reflects the dominance of lead-acid commercial development and the absence of a market pull for lighter alkaline cells until traction and portable applications emerged in the 1890s, not a missing prerequisite."""
    },
    {
        "invention": "Zeppelin LZ-1 Rigid airship",
        "year": 1900,
        "inventor": "Ferdinand von Zeppelin",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1888–1895",
        "earliest_straightforward": "1895–1900",
        "actual_location": "Friedrichshafen, Germany",
        "possible_locations": "Germany; France; United Kingdom; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrialized nations with aluminum smelting, precision machine shops, and internal combustion engine manufacturing were concentrated in Western Europe and the US; Germany held a particular lead in engines and metalworking.",
        "confidence": "Medium",
        "full_text": """Invention: Zeppelin LZ-1 Rigid airship
Year actually invented: 1900
Earliest plausible: 1888-1895
Earliest straightforward: 1895-1900
Confidence: Medium
Actual location: Friedrichshafen, Germany
Possible locations at earliest plausible date: Germany, France, United Kingdom, United States
Geographic note: ALIGNED. Industrialized nations with aluminum smelting, precision machine shops, and internal combustion engine manufacturing were concentrated in Western Europe and the US; Germany held a particular lead in engines and metalworking.
Prerequisite technologies:
- Hall-Héroult electrolytic aluminum process [1886] — external/team-reachable
- Daimler/Otto internal combustion engine, lightweight petrol [1885] — external/team-reachable
- Rubberized/doped cotton fabric for envelopes [1840s-1880s, Charliere balloons] — external/team-reachable
- Industrial hydrogen production (zinc-acid, iron-steam) [pre-1800] — external/team-reachable
- Goldbeater's skin / impermeable gas cell membranes [used in balloons since 1780s] — external/team-reachable
- Precision riveted lightweight metal truss/girder construction [1880s, bridges and bicycles] — external/team-reachable
- Aerial propeller theory and practice [Henson, Stringfellow, Renard 1850s-1884] — external/team-reachable
- Powered non-rigid airship demonstrations (Giffard 1852, Renard & Krebs La France 1884) [1852-1884] — external/team-reachable
Scientific theories / key empirical observations:
- Archimedean buoyancy in gases [classical] — external/team-discoverable
- Aerodynamic drag scaling with shape (streamlined body) [Newton, Cayley 1809] — external/team-discoverable
- Strength-to-weight optimization of triangulated trusses [19th c. structural engineering] — external/team-discoverable
- Power required for steady level flight at low speed [Renard's empirical work, 1880s] — external/team-discoverable
Explanation: The binding item is the lightweight petrol internal combustion engine (Daimler 1885); without it, no powerplant has the power-to-weight ratio to drive a hull-shaped airship faster than prevailing winds, which is the entire point distinguishing a dirigible from a free balloon. Once that engine exists, every other piece is on the shelf: Hall-Héroult aluminum (1886) provides the structural metal, but a determined team could plausibly substitute spruce, bamboo, or thin-walled steel tubing with wire bracing (Schwarz built an all-aluminum rigid in 1897, and wood-framed rigid concepts were proposed by David Schwarz and others), so aluminum is enabling but not strictly binding. Hydrogen, varnished cotton gas cells, and propeller design were all mature from balloon practice. The "one layer" of precursor work the workshop must do is integrating a long, hull-shaped rigid frame with internal lift cells and twin engine gondolas — an engineering integration, not new science. Earliest plausible 1888-1895 reflects the few years needed after Daimler's engine matured to refine power-to-weight and to prototype the frame; straightforward 1895-1900 matches the historical track once Schwarz and Zeppelin began serious work."""
    },
    {
        "invention": "Powered suction vacuum cleaner",
        "year": 1901,
        "inventor": "Hubert Cecil Booth",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1830–1850",
        "earliest_straightforward": "1860–1880",
        "actual_location": "United Kingdom / London, UK",
        "possible_locations": "United Kingdom; France; United States; Prussia/Germany; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrial Britain and France had the centrifugal fans, fine textile manufacturing, and steam-power infrastructure required; the actual invention location fits squarely within this set.",
        "confidence": "Medium",
        "full_text": """Invention: Powered suction vacuum cleaner
Year actually invented: 1901
Earliest plausible: 1830–1850
Earliest straightforward: 1860–1880
Confidence: Medium
Actual location: United Kingdom / London, UK
Possible locations at earliest plausible date: United Kingdom, France, United States, Prussia/Germany, Belgium
Geographic note: ALIGNED. Industrial Britain and France had the centrifugal fans, fine textile manufacturing, and steam-power infrastructure required; the actual invention location fits squarely within this set.
Prerequisite technologies:
- Centrifugal fan (Guibal mine ventilator, high-volume axial/centrifugal blowers) [1827–1860] — external
- Reciprocating piston air pump capable of sustained partial vacuum [1650s, refined 1700s–1800s] — external
- Stationary or portable steam engine (small horsepower, belt-driven) [1800s–1820s] — external
- Fine-weave woven cotton/linen filter cloth (flour-mill bolting cloth, bag filters) [pre-1800] — external
- Flexible hose (leather, rubberized canvas after Goodyear vulcanization 1839; earlier leather fire hose) [1820s–1840s] — external
- Rigid nozzle/wand fabrication (sheet metal, brazed tubing) [pre-1800] — external
- Electric motor (only needed for electric variant) [1870s–1880s practical] — external
Scientific theories / key empirical observations:
- Pressure differential drives airflow; suction = negative pressure (Torricelli/Boyle) [1640s–1660s] — external
- Permeable fabric retains particulates while passing air (empirical, known from milling and winnowing) [pre-1800] — external
- Centrifugal action of a rotating impeller generates sustained pressure differential [early 1800s] — external
Explanation: The binding constraint is NOT the electric motor — it is the integration of a centrifugal fan (or piston pump) with a fabric bag filter and a flexible hose to capture dust at a domestic/commercial scale. By the 1830s, all components existed: centrifugal blowers were used in foundries and mines, bolting cloth filtered flour dust, leather hose handled fire-pump pressures, and small steam engines could drive belt-coupled fans. A motivated team could empirically tune fan geometry and bag porosity to achieve the modest 40–50 Pa suction needed; Booth's own 1901 demonstration used a piston pump, proving electric drive is incidental. The earliest plausible window (1830–1850) reflects the maturation of flexible hose and portable steam power; the straightforward window (1860–1880) reflects when a horse-drawn or stationary commercial unit becomes a routine engineering exercise. The 50–70-year gap from plausibility to actual invention is a demand/conceptual gap (carpets were beaten outdoors; nobody framed dust-removal-by-suction as a product) rather than a technical one."""
    },
]

with open(CHECKPOINT, "a", encoding="utf-8") as f:
    for entry in entries:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
