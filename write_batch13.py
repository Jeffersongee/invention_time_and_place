import json

CHECKPOINT = '/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl'

entries = [
    {
        "invention": "Telephone",
        "year": "1876",
        "inventor": "Alexander Graham Bell",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1837–1845",
        "earliest_straightforward": "1845–1855",
        "actual_location": "Boston, Massachusetts, USA",
        "possible_locations": "United Kingdom; Germany; France; USA (eastern seaboard)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in the USA, which by the 1870s had deep telegraph infrastructure and skilled instrument makers; however, the earliest plausible window centers on Britain and Germany, where electromagnetic instrument-making craft was most advanced in the 1837–1845 period, making either location viable.",
        "confidence": "Medium",
        "full_text": """Invention: Telephone
Year actually invented: 1876
Earliest plausible: 1837–1845
Earliest straightforward: 1845–1855
Confidence: Medium
Actual location: Boston, Massachusetts, USA
Possible locations at earliest plausible date: United Kingdom, Germany, France, USA (eastern seaboard)
Geographic note: ALIGNED. The actual invention occurred in the USA, which by the 1870s had deep telegraph infrastructure and skilled instrument makers; however, the earliest plausible window centers on Britain and Germany, where electromagnetic instrument-making craft was most advanced in the 1837–1845 period, making either location viable.
Prerequisite technologies:
- Faraday electromagnetic induction [1831] — external after 1831
- Fine-gauge insulated wire drawing and winding [∼1830s] — external/team-reachable
- Galvanometers and sensitive coil-wound electromagnetic instruments [∼1825–1835] — external/team-reachable
- Precision thin metal membrane / diaphragm fabrication [∼1820s] — external/team-reachable
- Telegraph wire transmission infrastructure and practice [∼1837, Cooke & Wheatstone / Morse] — external/team-reachable
- Magnets (permanent steel bar magnets, later electromagnets) [pre-1800 / ∼1820s] — external/team-reachable
Scientific theories / key empirical observations:
- Oersted: current produces magnetic field [1820] — external after 1820
- Faraday: changing magnetic flux induces EMF in a conductor [1831] — external after 1831
- Empirical knowledge that vibrating membranes can reproduce complex sound waveforms [pre-1800] — external
- Empirical observation that varying current through an electromagnet varies its attractive force on a nearby iron diaphragm [team-discoverable by ∼1835 given Faraday]
- Reis 1861: musical tones transmissible via make-break current modulation [1861] — external after 1861
Explanation: The binding constraint is not scientific knowledge but craft precision: producing a thin, uniformly tensioned iron or steel membrane with the correct compliance to respond to audio-frequency pressure variations, paired with a tightly wound fine-wire coil of sufficient turns to generate a detectable induced EMF at voice frequencies, and a receiver electromagnet strong enough to move an output diaphragm perceptibly. All necessary science is available after Faraday 1831. A motivated team with access to precision instrument makers could empirically iterate toward a working magneto-induction transmitter by the late 1830s to mid-1840s: the telegraph boom of the late 1830s supplied fine insulated wire, experienced coil winders, and the conceptual model of transmitting signals electrically over distance. The gap between Reis (1861, tones only) and Bell (1876, intelligible speech) shows the membrane-sensitivity tuning was genuinely difficult, but an empirically driven team specifically targeting continuous current modulation rather than make-break switching could have converged on the solution a full generation earlier; the earliest plausible date is therefore set at ∼1837–1845, with straightforward achievement more likely by 1845–1855 once telegraph craft matured and fine-wire coil winding became routine."""
    },
    {
        "invention": "Phonograph",
        "year": "1877",
        "inventor": "Thomas Edison",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1857–1860",
        "earliest_straightforward": "1865–1870",
        "actual_location": "Menlo Park, New Jersey, USA",
        "possible_locations": "France (Paris); United Kingdom (London); Germany (Berlin or Leipzig); USA (any major industrial city)",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. The actual invention occurred in the USA, but the earliest plausible date clusters around France, where Scott de Martinville built the phonautograph in 1857 and where the conceptual and physical prerequisites were most concentrated. A motivated team in Paris, London, or Berlin was better positioned than any American city at that date.",
        "confidence": "Medium",
        "full_text": """Invention: Phonograph
Year actually invented: 1877
Earliest plausible: 1857–1860
Earliest straightforward: 1865–1870
Confidence: Medium
Actual location: Menlo Park, New Jersey, USA
Possible locations at earliest plausible date: France (Paris), United Kingdom (London), Germany (Berlin or Leipzig), USA (any major industrial city)
Geographic note: MISMATCH. The actual invention occurred in the USA, but the earliest plausible date clusters around France, where Scott de Martinville built the phonautograph in 1857 and where the conceptual and physical prerequisites were most concentrated. A motivated team in Paris, London, or Berlin was better positioned than any American city at that date.
Prerequisite technologies:
- Rotating cylinder or drum mechanism [pre-1800] — external/team-reachable
- Smoked-paper or lampblack recording surface [pre-1850] — external/team-reachable
- Thin metal or animal-membrane diaphragm [pre-1840] — external/team-reachable
- Lightweight stylus coupled to a diaphragm (phonautograph, Scott) [1857] — external/team-reachable
- Hand crank or clockwork drive for consistent cylinder rotation [pre-1820] — external/team-reachable
- Tin foil or wax-coated cylinder as a deformable recording medium — team-reachable
- Precision mechanical fabrication (watchmaking, instrument-making trades) [pre-1850] — external/team-reachable
Scientific theories / key empirical observations:
- Acoustic resonance and membrane vibration (Chladni figures, Savart) [1820s] — external/team-discoverable
- Observation that a stylus dragged across a grooved surface reproduces the groove’s shape as motion [pre-1850] — team-discoverable
- Recognition that groove geometry encodes waveform and that retracing reverses the encoding — team-discoverable
- Understanding that air displacement by a vibrating membrane produces audible sound [pre-1800] — external/team-discoverable
Explanation: The binding constraint was not technical but conceptual: the realization that a groove encoding vibrational motion can be retraced to reproduce that motion as sound. Every physical component needed for the phonograph was available or trivially within one layer of fabrication by 1857, the year Scott de Martinville completed the phonautograph. Scott himself framed his device as a transcription tool, not a playback device. A motivated team with the phonautograph in hand, tasked with asking “can this groove be read back?”, would have needed only empirical iteration — substituting a deformable medium (tin foil over a hard cylinder) for smoked paper, pressing a fresh stylus into the groove, and listening. No new scientific framework is required. The 20-year gap between earliest plausible (1857–1860) and actual invention (1877) is attributable almost entirely to the absence of a motivated actor who reframed the question from recording to playback, not to any missing technology or knowledge."""
    },
    {
        "invention": "Closed-circuit rebreather",
        "year": "1878",
        "inventor": "Henry Fleuss",
        "category": "Mechanical",
        "category2": "Chemical",
        "earliest_plausible": "1845–1855",
        "earliest_straightforward": "1855–1865",
        "actual_location": "London, England",
        "possible_locations": "England (London/Birmingham); France (Paris); Germany (Prussia/Berlin); United States (industrial centers)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrial Britain in the mid-19th century had the strongest concentration of precision metalworking, chemical manufacturing (including caustic potash production), and practical diving/mining engineering motivation, making London or Birmingham the most natural origin point.",
        "confidence": "Medium",
        "full_text": """Invention: Closed-circuit rebreather (self-contained underwater breathing apparatus)
Year actually invented: 1878
Earliest plausible: 1845–1855
Earliest straightforward: 1855–1865
Confidence: Medium
Actual location: London, England
Possible locations at earliest plausible date: England (London, Birmingham), France (Paris), Germany (Prussia/Berlin), United States (industrial centers)
Geographic note: ALIGNED. Industrial Britain in the mid-19th century had the strongest concentration of precision metalworking, chemical manufacturing (including caustic potash production), and practical diving/mining engineering motivation, making London or Birmingham the most natural origin point.
Prerequisite technologies:
- Small compressed-gas cylinder capable of holding oxygen at useful pressure [∼1810–1820 wrought-iron pressure vessels; copper/steel by ∼1840] — external/team-reachable
- Pressure-reducing valve [∼1837–1845, gas engineering and locomotive safety-valve work] — external/team-reachable
- Flexible rubber or oiled-cloth breathing bag [∼1823–1830, Macintosh rubberized fabric; vulcanized rubber by 1844] — external/team-reachable
- Mouthpiece and nose clip [∼1820s, diving bell operators] — external/team-reachable
- CO2 absorber: potassium hydroxide (caustic potash) [available commercially since ∼1800–1810] — external/team-reachable
- Open-circuit helmet diving apparatus (Siebe closed helmet) [1837] — external/team-reachable
- Production of oxygen in moderate quantity [∼1774–1800; small-cylinder filling feasible by ∼1840s] — external/team-reachable
Scientific theories / key empirical observations:
- CO2 toxicity / irrespirable atmospheres [Black, Priestley, Lavoisier ∼1750–1800] — external/team-discoverable
- Oxygen-enriched breathing sustains life [Priestley 1774; Davy ∼1800] — external/team-discoverable
- Caustic potash (KOH) absorbs CO2 from gas streams [∼1810–1830] — external/team-discoverable
- High-pressure gas containment and release engineering [∼1800–1840] — external/team-discoverable
Explanation: The binding item is the simultaneous availability of a reliable small compressed-oxygen cylinder with a workable pressure-reducing valve, paired with the recognition that KOH granules in a breathing circuit could scrub CO2 continuously. By roughly 1845 all constituent technologies existed in isolation — vulcanized rubber for bags and seals (post-1844), caustic potash as commodity chemical, wrought-iron or copper pressure vessels, and basic valve engineering from the gas and steam trades. A single motivated engineer in an industrial city could have assembled them within five years without requiring any new scientific discovery. The actual date of 1878 is roughly 20–30 years later than the earliest plausible date, likely because no pressing operational need was acute enough to drive systematic engineering effort until Fleuss pursued it for flooded-mine rescue."""
    },
    {
        "invention": "Pelton Wheel",
        "year": "1878",
        "inventor": "Lester Allan Pelton",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1830–1845",
        "earliest_straightforward": "1845–1860",
        "actual_location": "Nevada/California, USA",
        "possible_locations": "United Kingdom; France; Switzerland; USA (northeastern industrial centers)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA and Western Europe shared the same industrial and hydraulic engineering knowledge base by the 1830s–1840s; the actual location (mining-era California) reflects opportunistic context, but the invention could plausibly have emerged wherever high-head water sources and industrial demand coincided, particularly in Alpine Europe or the Appalachian/northeastern USA.",
        "confidence": "Medium",
        "full_text": """Invention: Pelton wheel (impulse water turbine)
Year actually invented: 1878
Earliest plausible: 1830–1845
Earliest straightforward: 1845–1860
Confidence: Medium
Actual location: Nevada/California, USA
Possible locations at earliest plausible date: United Kingdom, France, Switzerland, USA (northeastern industrial centers)
Geographic note: ALIGNED. The USA and Western Europe shared the same industrial and hydraulic engineering knowledge base by the 1830s–1840s; the actual location (mining-era California) reflects opportunistic context, but the invention could plausibly have emerged wherever high-head water sources and industrial demand coincided, particularly in Alpine Europe or the Appalachian/northeastern USA.
Prerequisite technologies:
- Cast iron and wrought iron precision casting/machining [∼1800–1820] — external/team-reachable
- High-pressure nozzle and pipe technology [∼1810–1830] — external/team-reachable
- Overshot and impulse water wheels (established millwright practice) [pre-1800] — external/team-reachable
- Lathe and mechanical workshop tooling to shape curved bucket forms [∼1800–1820] — external/team-reachable
- Pelton-style bearing and axle technology (from mill machinery) [pre-1800] — external/team-reachable
Scientific theories / key empirical observations:
- Euler’s hydraulic turbine theory and momentum transfer principles (1754) — external/team-discoverable
- Empirical understanding that redirecting a jet 180° extracts maximum kinetic energy [pre-1800] — external/team-discoverable
- Knowledge that reaction turbines (Fourneyron, 1827) lose efficiency at high heads — motivating impulse designs [1827–1840] — external/team-discoverable
- Empirical bucket-geometry testing (iterative shape optimization) — team-reachable
Explanation: The Pelton wheel’s binding constraint is not materials or scientific theory — Newtonian momentum transfer and the efficiency advantage of 180° jet deflection are derivable from knowledge available by 1800. The limiting factors are (1) the practical availability of sustained high-velocity jets, requiring reliable high-head pipe and nozzle technology mature by roughly 1820–1835, and (2) the motivating engineering context of high-head sites. The split-cup geometry is the key design insight; a motivated team doing systematic bucket-shape trials would arrive at the concave split-cup form empirically within a reasonable iteration cycle. By the 1830s, Fourneyron’s reaction turbine work had established turbine engineering as a serious discipline, skilled pattern-makers and millwrights could fabricate the required bucket shapes, and high-head mining and Alpine power sites provided both the resource and the demand."""
    },
    {
        "invention": "Incandescent light bulb",
        "year": "1879",
        "inventor": "Thomas Edison",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1825–1840",
        "earliest_straightforward": "1865–1879",
        "actual_location": "Menlo Park, New Jersey, USA; Newcastle, England",
        "possible_locations": "United Kingdom; France; Germany (Prussia); United States; Netherlands",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. By the 1820s–1830s, glassblowing centers, battery-making capacity, and barometer/mercury-pump traditions existed across Britain, France, and the German states — the same craft ecosystem that later produced Swan and Edison.",
        "confidence": "Medium",
        "full_text": """Invention: Incandescent light bulb (practical, long-lasting)
Year actually invented: 1879
Earliest plausible: 1825–1840
Earliest straightforward: 1865–1879
Confidence: Medium
Actual location: Menlo Park, New Jersey, USA; Newcastle, England
Possible locations at earliest plausible date: United Kingdom, France, Germany (Prussia), United States, Netherlands
Geographic note: ALIGNED. By the 1820s–1830s, glassblowing centers, battery-making capacity, and barometer/mercury-pump traditions existed across Britain, France, and the German states — the same craft ecosystem that later produced Swan and Edison.
Prerequisite technologies:
- Voltaic pile / reliable DC source [1800] — external (off-limits phenomenon, usable after published date)
- Lead-glass blowing & sealing of metal-to-glass leads [pre-1700] — external
- Mercury barometer principle [Torricelli 1644] — external
- Sprengel-style mercury fall pump (high vacuum) — team-reachable; built as the one allowed precursor by iterating on the barometer/aspirator tradition
- Drawn carbon filaments (carbonized natural fiber) [pre-1800] — external
- Platinum wire for lead-in seals [18th c.] — external
Scientific theories / key empirical observations:
- Joule heating of conductors (resistive incandescence, Davy ∼1802 with platinum strips) [1802] — external/team-discoverable
- Oxidation of hot carbon in air requires evacuation [18th c. combustion knowledge] — external
- High-resistance, small-radiating-surface filament minimizes power per candle (engineering insight) — team-discoverable through iteration
Explanation: Once Volta’s pile (1800) is available as external knowledge, every remaining ingredient is craft-level engineering accessible to an 1820s–1830s artisan workshop. Davy had already demonstrated incandescence of platinum and carbon strips by 1802; the failure mode of carbon (oxidation) was understood from ordinary combustion chemistry, and the fix (evacuate the bulb or seal in inert gas) is an engineering response, not a scientific discovery. The binding item is the high-vacuum envelope: per the rubric’s worked example, the Sprengel-style mercury fall pump is team-reachable as the one allowed precursor, built by iterating on the well-established Torricellian barometer and water-aspirator traditions. Carbonized fibers, platinum lead-ins, and lead-glass envelopes were all routine artisan capabilities by 1820. Five motivated years spent on filament geometry, seal integrity, and pump iteration would converge on a practical long-lasting bulb. The hard floor is Volta 1800; allowing ∼25–40 years for the pile to diffuse and for a workshop to assemble the program gives 1825–1840 as earliest plausible. The earliest straightforward window (1865–1879) reflects the historical path once the Sprengel pump existed off-the-shelf and dynamo power made bulbs commercially compelling."""
    },
    {
        "invention": "Carbon arc welding",
        "year": "1881",
        "inventor": "Nikolay Benardo and Stanislaw Olszewski",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1871–1876",
        "earliest_straightforward": "1875–1881",
        "actual_location": "Paris, France",
        "possible_locations": "United Kingdom; France; Germany; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrial nations with access to Gramme-type dynamos and established electrical workshops (UK, France, Germany, USA) all had the infrastructure to support this work by the early 1870s; Paris was a natural hub given Gramme’s presence there.",
        "confidence": "Medium",
        "full_text": """Invention: Carbon arc welding
Year actually invented: 1881
Earliest plausible: 1871–1876
Earliest straightforward: 1875–1881
Confidence: Medium
Actual location: Paris, France
Possible locations at earliest plausible date: United Kingdom, France, Germany, United States
Geographic note: ALIGNED. Industrial nations with access to Gramme-type dynamos and established electrical workshops (UK, France, Germany, USA) all had the infrastructure to support this work by the early 1870s; Paris was a natural hub given Gramme’s presence there.
Prerequisite technologies:
- Voltaic pile / galvanic battery [1800] — external
- Carbon electrodes (retort carbon, gas-works carbon rods) [∼1840s–1850s] — external/team-reachable
- Gramme dynamo (practical high-current continuous DC generator) [1871] — external; binding hardware prerequisite
- Carbon arc lamp (demonstrates sustained arc technique) [1870s] — external
- Metal-working and foundry tooling [pre-1800] — external
Scientific theories / key empirical observations:
- Carbon arc demonstration (Davy, ∼2000 voltaic cells) [1802] — external
- Ohm’s Law [1827] — external
- Empirical observation that arc temperature far exceeds combustion flames [∼1840s–1860s] — external
- Joule heating / calorimetric work [1840s] — external
Explanation: The binding constraint is not knowledge but sustained high-current DC power. Davy’s 1802 arc used ∼2000 voltaic cells — enormous, expensive, and short-lived — producing insufficient continuous energy to melt a workpiece rather than merely illuminate it. Battery arrays through the 1860s could in principle be scaled, but the cost and impracticality made systematic metal-fusion experiments unlikely. The Gramme dynamo (1871) changed the calculus entirely: it provided cheap, continuous, high-current DC from a rotating machine, making arc welding economically and practically feasible. A well-resourced team with access to a Gramme machine could, by 1871–1876, empirically discover that a carbon arc held close to a metal surface melts and fuses it, then iterate on electrode geometry, arc gap, and motion technique within the five-year window. No new science is required. The gap between 1802 (arc demonstrated) and 1871 (practical dynamo) explains why the invention did not occur earlier despite apparent conceptual simplicity."""
    },
    {
        "invention": "Recoil-operated machine gun",
        "year": "1884",
        "inventor": "Hiram Maxim",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1872–1876",
        "earliest_straightforward": "1878–1882",
        "actual_location": "London, England",
        "possible_locations": "United Kingdom; United States; Germany; France; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The UK and US were the leading centers of precision metalworking and small-arms manufacturing in the 1870s, and London/Birmingham in particular had the skilled artisan workshops and commercial arms industry necessary to develop and iterate on a recoil-operated mechanism.",
        "confidence": "Medium",
        "full_text": """Invention: Recoil-operated automatic machine gun (Maxim gun)
Year actually invented: 1884
Earliest plausible: 1872–1876
Earliest straightforward: 1878–1882
Confidence: Medium
Actual location: London, England
Possible locations at earliest plausible date: United Kingdom, United States, Germany, France, Belgium
Geographic note: ALIGNED. The UK and US were the leading centers of precision metalworking and small-arms manufacturing in the 1870s, and London/Birmingham in particular had the skilled artisan workshops and commercial arms industry necessary to develop and iterate on a recoil-operated mechanism.
Prerequisite technologies:
- Self-contained rimfire and centerfire metallic cartridges [1856–1866] — external/team-reachable
- Reliable centerfire primer (Boxer/Berdan) [1866–1869] — external/team-reachable
- Drawn brass cartridge cases [1860s] — external/team-reachable
- Precision rifle barrel and chamber machining [1850s–1860s] — external/team-reachable
- Industrial milling and interchangeable-parts manufacture [1850s] — external/team-reachable
- Toggle-link or similar mechanical locking mechanism [1840s–1866] — external/team-reachable
- Cloth or linked belt feed system for ammunition — team-reachable within 1–2 years
- Recoil buffer / spring return mechanism [1860s] — external/team-reachable
- Gatling gun demonstrating rapid-fire feasibility [1862] — external
Scientific theories / key empirical observations:
- Newton’s third law / impulse-momentum as engineering principle [pre-1700] — external
- Empirical observation that breech and barrel move rearward under firing stress [pre-1850] — external/team-discoverable
- Relationship between chamber pressure curve, bolt timing, and extraction force — team-discoverable
- Metallurgical understanding of brass work-hardening and annealing [1860s] — external
Explanation: The binding constraint is the convergence of two engineering prerequisites: sufficiently robust centerfire metallic cartridges (reliably available by ∼1869–1872 with Boxer/Berdan primers and drawn-brass cases) and the precision machining capability for a self-timing recoil-operated bolt. By approximately 1872, both conditions were met in the UK and US arms industry. A motivated inventor with a skilled gunsmithing workshop could, within a five-year development window, empirically iterate through locking-mechanism designs and belt-feed concepts to arrive at a functioning recoil-operated single-barrel automatic. The gap from ∼1872 to Maxim’s 1884 actual invention reflects primarily the absence of a motivated inventor focused on this specific problem."""
    }
]

with open(CHECKPOINT, 'a') as f:
    for entry in entries:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Wrote {len(entries)} entries to checkpoint.")

# Verify
with open(CHECKPOINT) as f:
    total = sum(1 for _ in f)
print(f"Total entries now: {total}")
