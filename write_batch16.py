#!/usr/bin/env python3
"""Write batch 16 (indices 105-111) to checkpoint."""
import json

CHECKPOINT = "/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl"

ELECTRIC_OVEN_FULL = """Invention: Electric oven (resistive heating oven)
Year actually invented: 1892
Earliest plausible: 1871–1878
Earliest straightforward: 1880–1888
Confidence: Medium
Actual location: Ottawa, Canada
Possible locations at earliest plausible date: France (Paris), United Kingdom (London), United States (New York, Boston), Germany (Berlin, Munich)
Geographic note: MISMATCH. The binding constraint is access to practical dynamo-supplied kilowatt-scale current; by 1871–1878 this capacity existed primarily in France (Gramme) and the UK/US (early industrial generators), not in Ottawa, which lacked central-station power infrastructure until the late 1880s.
Prerequisite technologies:
- Resistance wire / nichrome-class conductors (platinum, iron, nickel alloys) [1840s–1860s] — external
- Gramme continuous-current dynamo providing kilowatt-scale output [1871] — external
- Insulated wire and basic electrical connectors [1840s] — external
- Enclosed iron cooking chamber with thermal insulation (existing oven craft) [pre-1800] — external
- Carbon-arc and incandescent lamp engineering (thermal load management) [1878–1880] — external
- Edison central-station DC distribution [1882] — external (binding for straightforward range)
Scientific theories / key empirical observations:
- Joule heating (I²R dissipation) published by Joule [1841] — external
- Ohm's Law quantifying resistance and current [1827] — external
- Faraday induction enabling generator design [1831] — external (off-limits for team-discovery; usable as published knowledge)
- Empirical calibration of resistive element geometry for sustained cooking temperatures — team-reachable via iteration
Explanation: The binding constraint is not Joule's Law (published 1841) nor resistive wire fabrication (feasible from the 1840s), but the availability of a sustained kilowatt-scale current source capable of holding cooking temperatures for the duration of a meal. Battery banks of the 1840s–1860s could briefly achieve high currents but could not economically sustain the continuous 1–3 kW load required for practical cooking without prohibitive cost and electrolyte replenishment. The Gramme dynamo (1871) was the first commercially replicable machine capable of delivering smooth, continuous DC at cooking-relevant power levels; a motivated team working from 1871 onward could wind resistive coils from available platinum or iron wire, enclose them in an adapted iron oven body, and empirically tune element geometry to achieve 200–250 °C chamber temperatures — all within the one-layer team-build rule. The earliest plausible window (1871–1878) therefore opens with the Gramme dynamo and closes before Edison's central-station infrastructure (1882), requiring the team to operate with a dedicated on-site generator rather than grid supply. The straightforward window (1880–1888) opens once Edison-class central stations make kilowatt-scale load practical for multiple independent teams and closes just before Ahearn's 1892 demonstration."""

entries = [
    {
        "invention": "Chlorofluorocarbon refrigerant",
        "year": 1890,
        "inventor": "Frederic Swarts",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1850–1870",
        "earliest_straightforward": "1880–1890",
        "actual_location": "Belgium / Ghent, Belgium",
        "possible_locations": "Belgium; France; Germany; United Kingdom; Sweden",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Mid-19th-century organic halogen chemistry was concentrated in Western European academic labs (Paris, Giessen, Ghent, London), where chlorocarbon chemistry and HF handling were already practiced.",
        "confidence": "Medium",
        "full_text": """Invention: Chlorofluorocarbon (CFC) synthesis
Year actually invented: 1890
Earliest plausible: 1850–1870
Earliest straightforward: 1880–1890
Confidence: Medium
Actual location: Belgium / Ghent, Belgium
Possible locations at earliest plausible date: Belgium, France, Germany, United Kingdom, Sweden
Geographic note: ALIGNED. Mid-19th-century organic halogen chemistry was concentrated in Western European academic labs (Paris, Giessen, Ghent, London), where chlorocarbon chemistry and HF handling were already practiced.
Prerequisite technologies:
- Anhydrous hydrogen fluoride preparation [1771, Scheele] — external/team-reachable
- Chloroform and other chlorocarbons via halogenation [1831, Soubeiran/Liebig] — external/team-reachable
- Antimony trichloride and antimony halide chemistry [early 1800s] — external/team-reachable
- Lead/platinum/copper apparatus for HF-resistant work [early-mid 1800s] — external/team-reachable
- Sealed-tube and pressure reaction techniques (Carius tube) [1860s] — external/team-reachable
- Halogen-exchange (metathesis) reactions on organic halides [1830s–40s, Dumas/Regnault] — external/team-reachable
Scientific theories / key empirical observations:
- Concept of substitution in organic chemistry (Dumas) [1834] — external/team-discoverable
- Recognition that metal fluorides can transfer F to carbon-bound halogens [team-discoverable empirically by ~1850] — team-discoverable
- Structural/valence theory of carbon (Kekulé) [1858] — external/team-discoverable
- Stability of C–F bond once formed (empirical) [team-discoverable] — team-discoverable
Explanation: The binding item is the empirical realization that a mild metal fluoride (SbF3, prepared from SbCl3 + HF) can selectively swap chlorine for fluorine on a carbon skeleton without destroying the molecule — a one-layer precursor (making SbF3 in situ) the team can build. All the surrounding pieces — anhydrous HF (1771), chlorocarbons like CHCl3 (1831), Dumas-style halogen substitution (1830s), HF-resistant lead/platinum vessels, and Carius-style sealed tubes — were in hand by mid-century. A motivated inventor with a skilled chemistry workshop, given five years of empirical iteration on antimony, mercury, silver, and arsenic fluorides reacting with chloroform and carbon tetrachloride, could plausibly have isolated CHClF2 or CCl2F2 by 1850–1870; the actual 1890 date reflects that no one was specifically targeting C–F compounds, not a missing prerequisite. The "straightforward" window of 1880–1890 corresponds to Moissan's isolation of F2 (1886) sharpening interest in organofluorine work, which is when Swarts in fact succeeded."""
    },
    {
        "invention": "Pre-cut folding cardboard box",
        "year": 1890,
        "inventor": "Robert Gair",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1820–1840",
        "earliest_straightforward": "1850–1870",
        "actual_location": "Brooklyn, New York, USA",
        "possible_locations": "Britain; France; Germany; USA; Netherlands",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrializing regions with established paper mills, printing trades, and iron-frame press manufacture all qualify; Gair's Brooklyn location fits the broader pattern of papermaking and printing centers.",
        "confidence": "High",
        "full_text": """Invention: Pre-cut folding cardboard box
Year actually invented: 1890
Earliest plausible: 1820–1840
Earliest straightforward: 1850–1870
Confidence: High
Actual location: Brooklyn, New York, USA
Possible locations at earliest plausible date: Britain, France, Germany, USA, Netherlands
Geographic note: ALIGNED. Industrializing regions with established paper mills, printing trades, and iron-frame press manufacture all qualify; Gair's Brooklyn location fits the broader pattern of papermaking and printing centers.
Prerequisite technologies:
- Stiff paperboard / pasteboard [c. 1750, mature by 1820] — external
- Iron-frame platen/flatbed press capable of high pressure [c. 1800–1820, Stanhope press] — external
- Steel rule and engraved die cutting (used in bookbinding, leather, paper) [c. 1810–1830] — external/team-reachable
- Mechanical creasing/scoring techniques (bookbinding spine creasers) [pre-1830] — external
- Powered press drive (hand, treadle, or steam) [1820s] — external
Scientific theories / key empirical observations:
- Geometry of unfolding a prismatic box into a flat net [ancient, trivial] — external
- Empirical observation that a creased fiber sheet folds cleanly along the crease [pre-1800, bookbinding craft knowledge] — external
- Observation that a raised rule under pressure can simultaneously cut adjacent material if taller [team-discoverable within 5 years]
Explanation: The binding constraint is the combined cut-and-crease die press, not the paperboard or the concept. Pasteboard had existed for a century, and folded paper boxes (hand-cut, hand-creased) were already in use for hats, collars, and pharmaceuticals well before 1890. The conceptual leap — that a single die with sharp steel rules at full height for cutting and blunt rules at lower height for creasing could do both in one platen stroke — is exactly the kind of empirical iteration a skilled press-shop could achieve once iron-frame presses and steel rule were available. Gair himself reportedly stumbled on the idea after a metal rule shifted in his bag press and cut where it should have creased; a motivated team given five years and a Stanhope-class press (available by 1820) would converge on the same solution deliberately. Hence earliest plausible 1820–1840, with straightforward commercial realization once cheap machine-made paperboard and steam-driven presses were widespread by mid-century."""
    },
    {
        "invention": "Zipper",
        "year": 1891,
        "inventor": "Whitcomb Judson",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1750–1800",
        "earliest_straightforward": "1820–1850",
        "actual_location": "United States / Chicago, USA",
        "possible_locations": "England; France; Switzerland; Germany (Saxony/Nuremberg); Netherlands; Italy (northern)",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. Earliest plausible centers are European clock/watch and small-metal-goods workshops (Geneva, Sheffield, Birmingham, Nuremberg); the actual 1891 US invention reflects late industrial-era tinkering rather than a binding tech constraint.",
        "confidence": "Medium",
        "full_text": """Invention: Zipper (slide fastener)
Year actually invented: 1891
Earliest plausible: 1750–1800
Earliest straightforward: 1820–1850
Confidence: Medium
Actual location: United States / Chicago, USA
Possible locations at earliest plausible date: England, France, Switzerland, Germany (Saxony/Nuremberg), Netherlands, Italy (northern)
Geographic note: MISMATCH. Earliest plausible centers are European clock/watch and small-metal-goods workshops (Geneva, Sheffield, Birmingham, Nuremberg); the actual 1891 US invention reflects late industrial-era tinkering rather than a binding tech constraint.
Prerequisite technologies:
- Precision metal stamping / die-cutting for small uniform parts [c. 1700, mature by 1750] — external (clockmaking, button-making, buckle trade)
- Drawn/rolled sheet brass and steel [c. 1700–1750] — external
- Woven cotton/linen tape with reliable selvedge [pre-1700] — external
- Stitching of metal findings to fabric (hook-and-eye closures) [c. 1600s] — external
- Coiled or leaf springs small enough for the hook tension [c. 1600s, watchmaking] — external
- Files, jigs, and fixtures for repeatable small-parts assembly [c. 1700] — team-reachable
Scientific theories / key empirical observations:
- Geometric insight: a sliding cam/wedge can sequentially engage paired interlocking elements [team-discoverable, no theory required] — team-discoverable
- Empirical tuning of hook geometry and tape spacing for reliable engagement [team-discoverable] — team-discoverable
Explanation: The zipper requires no scientific framework whatsoever; it is a pure mechanical-geometry invention built from button-, buckle-, and hook-and-eye-making techniques that were fully mature in European small-metal workshops by the mid-18th century. The binding constraint is dimensional uniformity of the stamped hooks and consistent tape spacing — sloppy parts jam the slider — and this precision was achievable in clock/watch and button trades from roughly 1700–1750. A motivated inventor with a Geneva or Birmingham workshop in 1750–1800 could iterate empirically to a working clasp-locker; by 1820–1850, with rolled sheet steel and improved stamping presses, it becomes straightforward. The 140-year gap to 1891 reflects the absence of demand (existing buttons and hook-and-eye closures were "good enough") rather than any missing prerequisite, so the gap is explained by cultural/market lag, not technical impossibility."""
    },
    {
        "invention": "Cinematograph",
        "year": 1892,
        "inventor": "Leon Bouly",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1880–1885",
        "earliest_straightforward": "1888–1892",
        "actual_location": "France / Lyon, France",
        "possible_locations": "France; United Kingdom; United States; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Late 19th-century photographic and precision-mechanical innovation was concentrated in France, Britain, Germany, and the US, all of which had the optical, chemical, and mechanical infrastructure required.",
        "confidence": "Medium",
        "full_text": """Invention: Cinematograph (motion picture camera and projector)
Year actually invented: 1892
Earliest plausible: 1880-1885
Earliest straightforward: 1888-1892
Confidence: Medium
Actual location: France / Lyon, France
Possible locations at earliest plausible date: France, United Kingdom, United States, Germany
Geographic note: ALIGNED. Late 19th-century photographic and precision-mechanical innovation was concentrated in France, Britain, Germany, and the US, all of which had the optical, chemical, and mechanical infrastructure required.
Prerequisite technologies:
- Flexible roll film (paper-based, Eastman) [1885] — external/team-reachable
- Flexible perforated celluloid film [1889] — external/team-reachable (one-layer precursor before 1889; nitrocellulose dopes were known from the 1860s and Hyatt's celluloid from 1870, so a workshop could fabricate transparent strip stock)
- Geneva drive / intermittent gear mechanisms [pre-1880] — external/team-reachable
- Maltese cross and cam-and-pin escapements (clockwork) [pre-1800] — external/team-reachable
- Magic lantern with condenser optics and projection lens [17th c., refined 1800s] — external/team-reachable
- Limelight (oxy-hydrogen) and carbon arc lamp [1820s-1870s] — external/team-reachable
- Fast gelatin dry-plate emulsion (~1/25 s exposures) [1878-1880] — external/team-reachable
- Muybridge/Marey chronophotography (sequential frame capture) [1878-1882] — external/team-reachable
- Zoetrope/praxinoscope persistence-of-vision devices [1834/1877] — external/team-reachable
- Precision-machined cams, sprockets, and registration pins [pre-1880] — external/team-reachable
Scientific theories / key empirical observations:
- Persistence of vision / phi phenomenon (perceptual fusion above ~10-16 Hz) [Plateau 1829; Roget 1824] — external/team-discoverable
- Photochemistry of silver halide gelatin emulsions [1870s] — external/team-discoverable
- Geometric optics for projection (conjugate focus, illuminance vs. distance) [pre-1700] — external/team-discoverable
- Nitrocellulose chemistry (collodion, celluloid) [1846-1870] — external/team-discoverable
Explanation: The binding item is a transparent, dimensionally stable, perforated long-strip film stock that can survive intermittent yanking past a gate at 12-16 fps without tearing or shrinking out of registration; everything else (intermittent claw movements, rotary shutters, condenser-lens projection, limelight or arc illumination, persistence-of-vision theory) was demonstrably available by the late 1870s. Eastman's transparent celluloid roll film of 1889 is the historical unblocking event, but a motivated workshop with one layer of precursor work could have cast and perforated nitrocellulose strip stock from the mid-1870s celluloid industry, pushing earliest plausible to roughly 1880-1885; the straightforward window opens in 1888-1892 once Eastman-grade celluloid and Marey's chronophotographic camera concepts converge, exactly when Bouly, Edison/Dickson, and the Lumières all reached the threshold independently."""
    },
    {
        "invention": "Electric oven",
        "year": 1892,
        "inventor": "Thomas Ahearn",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1871–1878",
        "earliest_straightforward": "1880–1888",
        "actual_location": "Ottawa, Canada",
        "possible_locations": "France (Paris); United Kingdom (London); United States (New York, Boston); Germany (Berlin, Munich)",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. The binding constraint is access to practical dynamo-supplied kilowatt-scale current; by 1871–1878 this capacity existed primarily in France (Gramme) and the UK/US (early industrial generators), not in Ottawa, which lacked central-station power infrastructure until the late 1880s.",
        "confidence": "Medium",
        "full_text": ELECTRIC_OVEN_FULL
    },
    {
        "invention": "Compression \"diesel\" engine",
        "year": 1893,
        "inventor": "Rudolph Diesel",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1870–1880",
        "earliest_straightforward": "1885–1893",
        "actual_location": "Germany (Augsburg, Germany)",
        "possible_locations": "Germany; United Kingdom; France; Belgium; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Germany, Britain, France, and the U.S. all had the steel metallurgy, precision machining, and internal combustion engine experimentation needed; the actual invention in Germany fits squarely within this industrial heartland.",
        "confidence": "Medium",
        "full_text": """Invention: Compression ignition (diesel) engine
Year actually invented: 1893
Earliest plausible: 1870–1880
Earliest straightforward: 1885–1893
Confidence: Medium
Actual location: Germany (Augsburg, Germany)
Possible locations at earliest plausible date: Germany, United Kingdom, France, Belgium, United States
Geographic note: ALIGNED. Germany, Britain, France, and the U.S. all had the steel metallurgy, precision machining, and internal combustion engine experimentation needed; the actual invention in Germany fits squarely within this industrial heartland.
Prerequisite technologies:
- Bessemer steel / open-hearth steel for high-pressure cylinders [1856–1865] — external
- Precision machining of cylinders and pistons (interchangeable parts, Whitworth tolerances) [1850s–1860s] — external
- Liquid fuel atomization / spray injection (perfume atomizers, kerosene burners, air-blast injection) [1860s] — team-reachable (one-layer precursor)
- Internal combustion engine architecture (Lenoir 1860, Otto/Langen 1867, Otto four-stroke 1876) [1860–1876] — external
- Petroleum distillates / kerosene as liquid fuel [1850s–1860s] — external
- High-pressure compressors and pressure vessels (steam locomotive boilers, air compressors for mining) [1850s–1870s] — external
- Mechanical fuel pumps and cam-driven valve timing [1860s] — external
Scientific theories / key empirical observations:
- Adiabatic compression heating (Gay-Lussac, Poisson, well known) [pre-1830] — external
- Fire piston demonstrating compression ignition of tinder [pre-1800, widespread by 1830s] — external (key empirical anchor)
- Carnot thermodynamic efficiency / role of temperature ratio [1824, formalized by Clausius 1850s] — external
- Empirical observation that compressed air ignites volatile fuels (known from fire pistons and pneumatic experiments) [pre-1850] — external
Explanation: The compression-ignition phenomenon was not a hidden scientific discovery — the fire piston had demonstrated auto-ignition of fuel in compressed air for over a century before Diesel, and adiabatic heating was textbook physics by 1850. Diesel's contribution was a theoretical efficiency argument (Carnot-based), but a motivated engineering team did not need that argument: they needed only to scale up a fire-piston principle into a working engine. The binding constraint is metallurgy and precision machining for cylinders that can sustain ~5–7 MPa repeatedly without leakage or failure, plus a reliable high-pressure fuel injection system. Bessemer steel (1856) and precision machine tools were available by the 1860s, and Otto-cycle engine architecture was demonstrated by 1860–1876, supplying the mechanical template. A team in 1870–1880 could plausibly iterate a heavy-walled, high-compression engine with air-blast kerosene injection — the same air-blast injection Diesel himself used. The straightforward window (1885–1893) reflects the maturation of seamless steel tubing, better injection pumps, and accumulated IC-engine know-how that made success near-certain rather than merely plausible. The binding item is high-pressure fuel injection hardware paired with cylinder metallurgy."""
    },
    {
        "invention": "Rubber surgical gloves",
        "year": 1893,
        "inventor": "William Halstead",
        "category": "Medical",
        "category2": "",
        "earliest_plausible": "1867–1875",
        "earliest_straightforward": "1880–1893",
        "actual_location": "USA / Baltimore, USA (Johns Hopkins)",
        "possible_locations": "UK (London, Glasgow, Edinburgh); Germany (Berlin); France (Paris); USA (Boston, New York, Baltimore); Austria (Vienna)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Centers of antiseptic surgical practice and rubber manufacturing co-located across Western Europe and the US Northeast in the 1860s–1880s; the actual US invention fits this distribution.",
        "confidence": "Medium",
        "full_text": """Invention: Rubber surgical gloves
Year actually invented: 1893
Earliest plausible: 1867–1875
Earliest straightforward: 1880–1893
Confidence: Medium
Actual location: USA / Baltimore, USA (Johns Hopkins)
Possible locations at earliest plausible date: UK (London, Glasgow, Edinburgh), Germany (Berlin), France (Paris), USA (Boston, New York, Baltimore), Austria (Vienna)
Geographic note: ALIGNED. Centers of antiseptic surgical practice and rubber manufacturing co-located across Western Europe and the US Northeast in the 1860s–1880s; the actual US invention fits this distribution.
Prerequisite technologies:
- Vulcanized rubber (Goodyear/Hancock) [1839–1844] — external
- Thin-walled rubber articles: balloons, condoms, chemists' gloves [1850s–1860s] — external
- Latex dipping / thin-film rubber forming [1860s] — external
- Sterilization of instruments by boiling/steam [1880s] — external (team-reachable from 1867)
- Carbolic acid antiseptic technique [1867] — external
Scientific theories / key empirical observations:
- Semmelweis: handwashing reduces childbed fever [1847] — external
- Pasteur: germ theory of disease [1861] — external
- Lister: antiseptic surgery [1867] — external
- Empirical observation: carbolic acid causes dermatitis on hands of surgical staff [1860s–1880s] — team-discoverable
Explanation: The binding constraint is conceptual/motivational, not material. Thin, dexterous vulcanized rubber gloves were already commercially available for chemists and household use by the 1860s, and latex dipping for thin-film articles was mature; an artisan workshop could readily produce a thin surgical-weight glove. What was missing before 1867 was a coherent reason to wear them in surgery — Semmelweis's 1847 handwashing observation was rejected by the profession and lacked a germ-theoretic framework, so it would not have driven adoption alone. Once Lister's antiseptic system (1867) was published, the motivated inventor + workshop has both the goal (barrier against contamination and against carbolic-acid-induced dermatitis, the actual proximate trigger for Halsted) and the materials, making 1867–1875 the earliest plausible window. The 20+ year lag to 1893 reflects medical-cultural inertia rather than any technical or theoretical gap, so the earliest straightforward window (1880–1893) tracks the maturation of aseptic technique rather than new capability."""
    },
]

with open(CHECKPOINT, "a", encoding="utf-8") as f:
    for entry in entries:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Wrote {len(entries)} entries to checkpoint.")
