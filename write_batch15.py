import json

CHECKPOINT = '/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl'

entries = [
    {
        "invention": "Bayer alumina process",
        "year": "1887",
        "inventor": "Carl Bayer",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1830–1850",
        "earliest_straightforward": "1865–1880",
        "actual_location": "Saint Petersburg, Russia",
        "possible_locations": "France; United Kingdom; Germany (Prussia/Saxony); Russia; Austria-Hungary; Sweden; Belgium; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Major European industrial chemistry centers (Germany, France, UK) had the alkali industry, pressure-vessel craftsmanship, and aluminum-chemistry awareness needed; the actual Russian invention fits within this set.",
        "confidence": "Medium",
        "full_text": """Invention: Bayer alumina process
Year actually invented: 1887
Earliest plausible: 1830–1850
Earliest straightforward: 1865–1880
Confidence: Medium
Actual location: Saint Petersburg, Russia
Possible locations at earliest plausible date: France, United Kingdom, Germany (Prussia/Saxony), Russia, Austria-Hungary, Sweden, Belgium, United States
Geographic note: ALIGNED. Major European industrial chemistry centers (Germany, France, UK) had the alkali industry, pressure-vessel craftsmanship, and aluminum-chemistry awareness needed; the actual Russian invention fits within this set.
Prerequisite technologies:
- Industrial caustic soda (NaOH) via LeBlanc process [1790s] — external
- Pressure-rated iron/steel vessels and autoclaves (steam-boiler practice) [1810s–1850s] — external
- Identification of bauxite ore as aluminum-rich mineral (Berthier) [1821] — external
- Calcination kilns / rotary calciners for converting hydroxide to oxide [pre-1850] — external/team-reachable
- Filtration and crystallizer equipment for hot caustic liquors [mid-19th c.] — external
Scientific theories / key empirical observations:
- Amphoteric behavior of alumina; solubility of Al(OH)3 in strong alkali [early 19th c.] — external
- Wöhler's isolation of metallic aluminum [1827] — external
- Empirical observation that seeding a supersaturated sodium aluminate liquor precipitates Al(OH)3 selectively — team-discoverable
- Knowledge that iron oxides and silica behave differently from alumina toward hot NaOH — team-discoverable
Explanation: The binding item is industrial-scale, pressure-tight alkaline digestion equipment combined with a market motivation to make pure alumina. All chemistry pieces — amphoteric alumina, NaOH availability, bauxite identification, calcination — are firmly in place by the 1820s–30s, and a motivated workshop with Papin-descended pressure vessels could empirically discover the seeded precipitation cycle within five years; this gives an earliest plausible window of 1830–1850. However, before the Hall-Héroult electrolytic demand (1886) there was essentially no market pulling for tonnage-scale pure alumina, which is why the straightforward window slips to 1865–1880, when caustic soda was cheap (Solvay), steel autoclaves were routine, and aluminum chemistry was a recognized industrial target. No off-limits phenomena or serendipity are required; the gap to actual invention is under 100 years and is explained by demand-pull rather than missing capability."""
    },
    {
        "invention": "Wind-generated electricity",
        "year": "1887",
        "inventor": "James Blyth",
        "category": "Mechanical",
        "category2": "Electrical",
        "earliest_plausible": "1867–1870",
        "earliest_straightforward": "1870–1875",
        "actual_location": "Marykirk, Scotland, United Kingdom",
        "possible_locations": "United Kingdom; France; Germany; Belgium; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The required dynamo expertise (Gramme in France/Belgium, Siemens in Germany/UK) and lead-acid battery work (Planté in France) clustered in Western Europe, with the UK already a hub of windmill and electrical engineering.",
        "confidence": "High",
        "full_text": """Invention: Wind-generated electricity (wind turbine charging system)
Year actually invented: 1887
Earliest plausible: 1867–1870
Earliest straightforward: 1870–1875
Confidence: High
Actual location: Marykirk, Scotland, United Kingdom
Possible locations at earliest plausible date: United Kingdom, France, Germany, Belgium, United States
Geographic note: ALIGNED. The required dynamo expertise (Gramme in France/Belgium, Siemens in Germany/UK) and lead-acid battery work (Planté in France) clustered in Western Europe, with the UK already a hub of windmill and electrical engineering.
Prerequisite technologies:
- Windmill/wind rotor with governor and tail vane [pre-1800] — external
- Lead-acid accumulator (Planté) [1859] — external
- Self-excited dynamo (Siemens/Wheatstone/Varley) [1866–1867] — external
- Gramme ring dynamo (commercially practical DC generator) [1871] — external
- Belt/gear mechanical coupling and shafting [pre-1800] — external
- Incandescent or arc lamps as load [arc lamps 1860s] — external
Scientific theories / key empirical observations:
- Electromagnetic induction (Faraday) [1831] — external
- Ohm's law and basic circuit theory [1827] — external
- Electrochemistry of secondary cells (Planté) [1859] — external
Explanation: The binding constraint is the practical self-excited dynamo capable of charging an accumulator at variable shaft speeds; once Siemens/Wheatstone demonstrated self-excitation in 1866–1867 and Planté's lead-acid cell (1859) was available, the remaining work is straightforward mechanical integration well within a skilled artisan workshop. A motivated team in 1867 could plausibly assemble a working charging windmill within their five-year window using arc-lamp loads, with the design becoming routine after the Gramme dynamo (1871). No new scientific framework, off-limits phenomenon, or chained precursor is required, so confidence is high. The ∼20-year gap to Blyth's 1887 demonstration reflects lack of motivation rather than missing capability."""
    },
    {
        "invention": "Gold cyanidation",
        "year": "1887",
        "inventor": "MacArthur–Forrest brothers & John S. MacArthur",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1845–1855",
        "earliest_straightforward": "1860–1875",
        "actual_location": "Glasgow, Scotland, United Kingdom",
        "possible_locations": "United Kingdom; France; Germany (Prussia/Saxony); Austria-Hungary; United States; Sweden; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The chemical industry capable of producing cyanides at scale and the mining/metallurgical workshops needed to test the process were concentrated in industrial Britain and continental Europe by mid-19th century, matching the actual locus of invention.",
        "confidence": "High",
        "full_text": """Invention: Gold cyanidation (MacArthur-Forrest process)
Year actually invented: 1887
Earliest plausible: 1845–1855
Earliest straightforward: 1860–1875
Confidence: High
Actual location: Glasgow, Scotland, United Kingdom
Possible locations at earliest plausible date: United Kingdom, France, Germany (Prussia/Saxony), Austria-Hungary, United States, Sweden, Belgium
Geographic note: ALIGNED. The chemical industry capable of producing cyanides at scale and the mining/metallurgical workshops needed to test the process were concentrated in industrial Britain and continental Europe by mid-19th century, matching the actual locus of invention.
Prerequisite technologies:
- Commercial alkali metal cyanide (KCN/NaCN) production [∼1840s] — external/team-reachable
- Ore crushing/stamp mills and agitation tanks [ancient–1800s] — external/team-reachable
- Zinc metal in commercial quantities [late 1700s] — external/team-reachable
- Filtration/percolation vat technology [1700s–1800s] — external/team-reachable
- Basic assay chemistry for gold [ancient–1700s] — external/team-reachable
Scientific theories / key empirical observations:
- Gold dissolves in alkaline cyanide solution in presence of air (Bagration 1843; Elsner 1846) — external/team-discoverable
- Electrochemical activity series — zinc displaces gold from solution [∼1800–1810] — external/team-discoverable
- Role of dissolved oxygen as the oxidizer in cyanide leaching (Elsner 1846) — external/team-discoverable
Explanation: The binding constraint is the published empirical observation that gold dissolves in dilute cyanide solutions in the presence of air, established by Bagration (1843) and given quantitative form by Elsner (1846). All other prerequisites — commercial KCN, stamp mills, agitation/percolation vats, and zinc-shaving precipitation — were in place by the 1840s. A motivated inventor plus skilled artisan workshop, given Bagration's 1843 paper, could within five years run empirical leach trials on crushed ore, optimize cyanide concentration and aeration, and adopt zinc-shaving precipitation, yielding a working process by ∼1845–1855. The straightforward window (1860–1875) reflects when soaring gold-mining demand and cheaper bulk cyanide made the economic case obvious; MacArthur-Forrest's 1887 patent was delayed roughly 30–40 years past technical feasibility, primarily by lack of a motivated team."""
    },
    {
        "invention": "Ballpoint pen",
        "year": "1888",
        "inventor": "John Loud",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1500–1600",
        "earliest_straightforward": "1700–1800",
        "actual_location": "Weymouth, Massachusetts, USA",
        "possible_locations": "Northern Italy; Southern Germany (Nuremberg/Augsburg); Flanders; France; Ottoman Empire; Ming China; Mughal India",
        "geographic_flag": "MISMATCH",
        "geographic_note": "MISMATCH. Loud's actual 1888 US invention reflects late-19th-century American patent activity, but the underlying craft (precision ball-bearing metalwork, viscous inks, reservoir pens) was achievable centuries earlier in any major metalworking center. Renaissance Italian/German workshops had ample capability.",
        "confidence": "Medium",
        "full_text": """Invention: Ballpoint pen (Loud-style rough-surface marker)
Year actually invented: 1888
Earliest plausible: 1500–1600
Earliest straightforward: 1700–1800
Confidence: Medium
Actual location: Weymouth, Massachusetts, USA
Possible locations at earliest plausible date: Northern Italy, Southern Germany (Nuremberg/Augsburg), Flanders, France, Ottoman Empire, Ming China, Mughal India
Geographic note: MISMATCH. Loud's actual 1888 US invention reflects late-19th-century American patent activity, but the underlying craft (precision ball-bearing metalwork, viscous inks, reservoir pens) was achievable centuries earlier in any major metalworking center. Renaissance Italian/German workshops had ample capability.
Prerequisite technologies:
- Precision metalworking and small-ball production (musket/arquebus shot, jeweler's beads) [c. 1500] — external/team-reachable
- Hardened steel suitable for a small ball and socket [c. 1400] — external/team-reachable
- Reservoir/tube pens (al-Mu'izz's reservoir pen 953 CE; da Vinci sketches) [c. 1500] — external/team-reachable
- Viscous oil-based inks (oil-based printing ink, Gutenberg) [c. 1450] — external/team-reachable
- Lathe/file/drill capable of small-bore socket tolerances [c. 1500] — external/team-reachable
Scientific theories / key empirical observations:
- Capillary action and surface tension behavior of viscous fluids (empirical) [ancient] — team-discoverable
- Empirical observation that a rolling ball transfers viscous fluid (analogous to inking rollers in printing) [c. 1450] — team-discoverable
Explanation: The Loud device is a rough-surface marker, not a fine writing pen, so the demanding micron-level tolerances of Bíró (1938) are not the binding constraint. The binding item is precision small-ball-and-socket fitting tight enough to retain viscous oil-based ink without leaking yet free enough to roll under pressure — a capability well within the reach of a Renaissance-era master metalworker familiar with shot-making, jeweled bearings, and clockwork. Oil-based viscous inks were already in industrial use after Gutenberg (c. 1450), and reservoir pens existed since the 10th century. A motivated inventor plus a top metalworking shop could iterate empirically to a working leather/rough-surface marker by the early 1500s. The gap to 1888 (~300–400 years) is explained primarily by lack of demand: quills and dip pens served writing needs adequately, and rough-surface marking was a niche industrial problem that only became salient with industrialized leather, lumber, and shipping in the 19th century."""
    },
    {
        "invention": "Kinetoscope motion picture viewer",
        "year": "1888",
        "inventor": "Thomas Edison and WKL Dickson",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1882–1885",
        "earliest_straightforward": "1888–1890",
        "actual_location": "West Orange, New Jersey, USA",
        "possible_locations": "USA; United Kingdom; France; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Late-19th-century photographic and electrical innovation was concentrated in the US and Western Europe, where Edison, Marey, Muybridge, Friese-Greene, and the Lumières all operated within the same technological milieu.",
        "confidence": "High",
        "full_text": """Invention: Kinetoscope (motion picture viewer)
Year actually invented: 1888
Earliest plausible: 1882–1885
Earliest straightforward: 1888–1890
Confidence: High
Actual location: West Orange, New Jersey, USA
Possible locations at earliest plausible date: USA, United Kingdom, France, Germany
Geographic note: ALIGNED. Late-19th-century photographic and electrical innovation was concentrated in the US and Western Europe, where Edison, Marey, Muybridge, Friese-Greene, and the Lumières all operated within the same technological milieu.
Prerequisite technologies:
- Dry gelatin photographic emulsion (fast enough for short exposures) [1878] — external/team-reachable
- Flexible roll film base — paper (Eastman-Walker roll holder, 1885) or collodion/nitrocellulose ribbon — external/team-reachable
- Sprocket-driven intermittent transport mechanisms (sewing machines, Geneva-style escapements) [1860s] — external/team-reachable
- Practical incandescent lamp for backlighting [1879] — external/team-reachable
- Small DC electric motor [1870s] — external/team-reachable
- Chronophotographic capture (Muybridge serial cameras 1878; Marey fusil photographique 1882) [1882] — external/team-reachable
Scientific theories / key empirical observations:
- Persistence of vision / phi-phenomenon (Plateau, Roget) [1820s–1830s] — external/team-discoverable
- Empirical frame rates (~10–16 fps) sufficient for fused motion (zoetrope, phenakistoscope tradition) [1830s] — external/team-discoverable
- Photochemistry of silver halide gelatin emulsions [1870s] — external/team-discoverable
Explanation: The binding constraint is a long, mechanically robust, transparent-or-translucent flexible film strip that can be perforated and pulled intermittently past an aperture without tearing. By 1882 a motivated team had fast gelatin dry plates, Muybridge/Marey serial photography, Edison-style incandescent lamps, small DC motors, and precision sprocket/escapement mechanics; the one-layer precursor they must build is the film medium itself. Eastman's paper roll film (1885) is the realistic earliest substrate, and a determined workshop could plausibly produce a sensitized translucent paper or thin gelatin/collodion ribbon a few years earlier, making 1882–1885 the earliest plausible window. A truly straightforward build, with durable transparent celluloid roll film commercially available, lands at 1888–1890, matching the historical date."""
    },
    {
        "invention": "Experimental proof of radio waves",
        "year": "1888",
        "inventor": "Heinrich Hertz",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Karlsruhe, Germany",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag",
        "confidence": "Flag",
        "full_text": """Invention: Experimental proof of radio waves
Year actually invented: 1888
Confidence: Flag
Actual location: Karlsruhe, Germany
Explanation: This entry is flagged because the "invention" is fundamentally the experimental discovery of a scientific phenomenon (free-space electromagnetic waves) rather than a buildable artifact with a defined function. The Hertz 1887 experiment is explicitly listed as an off-limits phenomenon: the binding constraint is not the apparatus (a spark-gap transmitter and resonant loop receiver could be built from mid-19th-century components) but rather the directed scientific investigation required to (a) believe Maxwell's prediction was worth chasing, (b) design a detector sensitive enough to register a faint spark in a resonant loop across a darkened room, and (c) interpret the resulting sparks as standing-wave evidence of propagating EM radiation. An engineering team without the scientific framework would have no reason to look for, or way to recognize, the effect — the artifact only "works" as an invention once interpreted through Maxwellian theory, and the recognition itself is the off-limits phenomenon. Hence Flag rather than a date range."""
    },
    {
        "invention": "Practical pneumatic tyre",
        "year": "1888",
        "inventor": "John Dunlop",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1845–1855",
        "earliest_straightforward": "1870–1880",
        "actual_location": "Belfast, Northern Ireland, United Kingdom",
        "possible_locations": "United Kingdom; France; United States; Germany",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Vulcanized rubber manufacturing, fabric weaving, and precision metalwork were all concentrated in Britain and the northeastern US by mid-century, matching Dunlop's actual location.",
        "confidence": "Medium",
        "full_text": """Invention: Practical pneumatic tyre
Year actually invented: 1888
Earliest plausible: 1845–1855
Earliest straightforward: 1870–1880
Confidence: Medium
Actual location: Belfast, Northern Ireland, United Kingdom
Possible locations at earliest plausible date: United Kingdom, France, United States, Germany
Geographic note: ALIGNED. Vulcanized rubber manufacturing, fabric weaving, and precision metalwork were all concentrated in Britain and the northeastern US by mid-century, matching Dunlop's actual location.
Prerequisite technologies:
- Vulcanized rubber [1844] — external/team-reachable
- Woven cotton canvas / duck cloth [pre-1800] — external/team-reachable
- Wire-drawn steel and machined brass valves [pre-1850] — external/team-reachable
- Spoked wire bicycle wheel with hollow rim [c. 1870, but wooden/iron rims usable earlier] — external/team-reachable
- Rubber cement / solution adhesives [c. 1830s] — external/team-reachable
- Hand or foot air pump [pre-1800] — external/team-reachable
Scientific theories / key empirical observations:
- Boyle's law / behavior of compressed gas in elastic vessels [1662] — external
- Empirical observation that an air cushion rolls with lower hysteresis than solid rubber on rough roads — team-discoverable
- Observation that separate inner tube + outer carcass solves puncture-repair and stress-separation — team-discoverable
Explanation: The binding constraint is not any single missing technology — every component existed by 1845, which is why Thomson patented his "Aerial Wheel" the year after vulcanization. The constraint is a market/application pull: a smooth-running vehicle light enough that rolling resistance and rider comfort dominate over load capacity, which is what the safety bicycle (1885) provided. A motivated team in 1845–1855 with vulcanized rubber, canvas, brass valves, and rubber cement could absolutely build a working pneumatic tyre (Thomson did), and with five years of iteration could solve rim-attachment and puncture repair. The "practical" qualification requires a suitable host vehicle; the straightforward window opens once velocipedes and high-wheelers create demand (1870s). The team can build the artifact a generation early, but commercial viability waited for the bicycle market."""
    }
]

with open(CHECKPOINT, 'a') as f:
    for entry in entries:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Wrote {len(entries)} entries to checkpoint.")

with open(CHECKPOINT) as f:
    total = sum(1 for _ in f)
print(f"Total entries now: {total}")
