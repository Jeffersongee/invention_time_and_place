import json

CHECKPOINT = '/Users/jeffersongee/Documents/invention_time_and_place/analysis_checkpoint.jsonl'

entries = [
    {
        "invention": "Poudre B Smokeless powder",
        "year": "1884",
        "inventor": "Paul Vieille",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1846–1855",
        "earliest_straightforward": "1860–1875",
        "actual_location": "Paris, France",
        "possible_locations": "France; United Kingdom; Prussia/German states; Austria; Switzerland; Sweden; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Nitrocellulose chemistry was pursued vigorously across Western Europe immediately after Schönbein's 1845 disclosure (Austria's Lenk, Britain's Hall, France's powder service), and any of these well-resourced military-chemical establishments had the artisan base to iterate on gelatinization and flake geometry.",
        "confidence": "Medium",
        "full_text": """Invention: Poudre B smokeless powder
Year actually invented: 1884
Earliest plausible: 1846–1855
Earliest straightforward: 1860–1875
Confidence: Medium
Actual location: Paris, France
Possible locations at earliest plausible date: France, United Kingdom, Prussia/German states, Austria, Switzerland, Sweden, United States
Geographic note: ALIGNED. Nitrocellulose chemistry was pursued vigorously across Western Europe immediately after Schönbein's 1845 disclosure (Austria's Lenk, Britain's Hall, France's powder service), and any of these well-resourced military-chemical establishments had the artisan base to iterate on gelatinization and flake geometry.
Prerequisite technologies:
- Concentrated nitric acid + sulfuric acid mixed-acid nitration [pre-1845] — external
- Cleaned cotton/cellulose feedstock and washing/stabilization (boiling, neutralization) [1850s] — team-reachable
- Diethyl ether and ethanol in bulk industrial purity [pre-1845] — external
- Roll mills / calendering presses for thin-flake forming [1840s] — external
- Closed-vessel pressure gauges and chronographs for ballistic measurement [1850s] — team-reachable
- Stable storage/drying ovens for controlled solvent evaporation [pre-1845] — external
Scientific theories / key empirical observations:
- Nitrocellulose (guncotton) synthesis, Schönbein [1845] — external
- Solubility of partially-nitrated cellulose ("collodion") in ether-alcohol, Maynard [1847] — external
- Empirical observation that grain geometry / surface area controls burn rate [pre-1845] — external
- Stability achieved by thorough acid washing [empirically discoverable] — team-discoverable
Explanation: The binding barrier is not chemistry but stabilization-and-process know-how: once Schönbein (1845) and Maynard's collodion (1847) are public, every needed reagent, solvent, and forming machine already exists. A motivated team iterating empirically would converge on (a) thorough washing to remove residual acids that caused spontaneous detonation, (b) gelatinization in ether-alcohol to form a homogeneous colloid, and (c) rolling/cutting into flakes whose thickness tunes vivacity — all reachable within five years of focused empirical work after 1847. The single allowed precursor layer is the stabilization/washing protocol; everything else is straightforward extension of existing artillery and chemical practice. Earliest plausible lands 1846–1855 (immediately on the heels of Maynard's collodion), with a more comfortable "straightforward" window of 1860–1875 once mixed-acid nitration and washing were industrially routine. The thirty-year gap to Vieille (1884) reflects institutional caution after the catastrophic 1860s guncotton accidents rather than a missing technical prerequisite."""
    },
    {
        "invention": "Steam turbine",
        "year": "1884",
        "inventor": "Charles Parsons",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1875–1880",
        "earliest_straightforward": "1880–1885",
        "actual_location": "Newcastle, England",
        "possible_locations": "England; Germany; United States; France; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Britain's combination of advanced precision engineering workshops, high-quality steel manufacturing, and concentrated steam-power expertise made it the natural home for this invention; Newcastle in particular had strong marine engineering infrastructure that Parsons directly exploited.",
        "confidence": "High",
        "full_text": """Invention: Steam turbine (multi-stage compound reaction turbine)
Year actually invented: 1884
Earliest plausible: 1875–1880
Earliest straightforward: 1880–1885
Confidence: High
Actual location: Newcastle, England
Possible locations at earliest plausible date: England, Germany, United States, France, Belgium
Geographic note: ALIGNED. Britain's combination of advanced precision engineering workshops, high-quality steel manufacturing, and concentrated steam-power expertise made it the natural home for this invention; Newcastle in particular had strong marine engineering infrastructure that Parsons directly exploited.
Prerequisite technologies:
- Precision lathe and milling machinery (Whitworth standard screw threads, surface plate) [1840s–1850s] — external/team-reachable
- High-quality wrought iron and early steel for rotor and blade fabrication [1860s–1870s] — external/team-reachable
- Bessemer/open-hearth steel (consistent metallurgy for high-speed rotors) [1856–1870s] — external/team-reachable
- Reliable journal and thrust bearings for high-speed shafts [1860s–1870s] — external/team-reachable
- Labyrinth/gland sealing concepts for steam paths [1860s–1870s] — external/team-reachable
- High-pressure boiler technology producing superheated or dry steam [1850s–1870s] — external/team-reachable
- Dynamic balancing awareness for high-speed rotors [1860s–1870s] — external/team-reachable
- Earlier single-stage impulse turbine attempts [pre-1870s] — external/team-reachable
- Electrical generator design (dynamo) [1870s] — external/team-reachable
Scientific theories / key empirical observations:
- Thermodynamic understanding of steam expansion and pressure-drop staging (Rankine cycle) [1850s–1860s] — external/team-discoverable
- Observation that single-stage turbines require impractical rotor speeds — external/team-discoverable
- Empirical understanding that splitting pressure drop across many stages reduces per-stage velocity — external/team-discoverable
- Fluid dynamics of reaction blading — external/team-discoverable
Explanation: The binding constraint is the intersection of precision blade manufacture and reliable high-speed mechanical systems, both of which matured in Britain during the 1860s–1875s. Whitworth-standard precision machine tools of the 1850s–1860s could produce the thin, curved blade rows needed; Bessemer steel (post-1856) provided consistent material for high-speed rotors; and empirical bearing technology was adequate for shafts in the 10,000–20,000 RPM range by the early 1870s. The thermodynamic rationale for multi-staging was accessible via Rankine's published work (1859). A motivated team with one layer of precursor effort — specifically, empirically developing close-clearance labyrinth seals and dynamically balanced rotors — could plausibly have converged on a working multi-stage reaction turbine by roughly 1875–1880. The earliest straightforward window is 1880–1885, by which point all individual prerequisites were demonstrated and only their deliberate integration remained; Parsons's achievement was primarily one of engineering synthesis and persistent iteration."""
    },
    {
        "invention": "Closed core transformer",
        "year": "1884",
        "inventor": "Zipernowsky-Bláthy-Déri, \"ZBD\"",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1867–1872",
        "earliest_straightforward": "1878–1883",
        "actual_location": "Budapest, Austria-Hungary",
        "possible_locations": "United Kingdom (London/Manchester); France (Paris); Germany (Berlin); Austria-Hungary (Vienna/Budapest); United States (New York/Boston); Belgium (Liège)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Industrialized Europe and the US Northeast had the iron-working precision, insulated copper wire industry, and electrical instrument shops needed; Budapest in 1884 was within this cluster, and any of the listed cities could have hosted the same workshop a decade earlier.",
        "confidence": "Medium",
        "full_text": """Invention: Closed-core transformer
Year actually invented: 1884
Earliest plausible: 1867–1872
Earliest straightforward: 1878–1883
Confidence: Medium
Actual location: Budapest, Austria-Hungary
Possible locations at earliest plausible date: United Kingdom (London, Manchester), France (Paris), Germany (Berlin), Austria-Hungary (Vienna, Budapest), United States (New York, Boston), Belgium (Liège)
Geographic note: ALIGNED. Industrialized Europe and the US Northeast had the iron-working precision, insulated copper wire industry, and electrical instrument shops needed; Budapest in 1884 was within this cluster, and any of the listed cities could have hosted the same workshop a decade earlier.
Prerequisite technologies:
- Insulated copper magnet wire (silk/cotton/shellac) [pre-1840] — external
- Soft iron with controlled purity for cores [pre-1850] — external
- Induction coil with iron core (Ruhmkorff open-core) [1851] — external
- Faraday's electromagnetic induction (usable as external) [1831] — external
- Laminated iron core practice (to suppress eddy currents, post-Foucault 1855) [1850s–1860s] — external
- Practical AC generator / alternator (Wilde, Siemens-type) [1866–1867] — external (BINDING)
- Precision winding, varnishing, and insulation techniques from telegraph/induction-coil trade [1850s–1860s] — external
Scientific theories / key empirical observations:
- Faraday's law of induction [1831] — external (usable after 1831)
- Lenz's law [1834] — external
- Joule heating / I²R losses [1841] — external
- Foucault eddy-current losses in solid iron [1855] — external
- Empirical observation that closing the magnetic circuit increases mutual induction [1830s–1850s] — team-discoverable
- Empirical turns-ratio voltage relation in induction coils [1850s] — team-discoverable
Explanation: The binding prerequisite is a practical AC generator capable of sustained operation; before Wilde (1866) and Siemens (1867) no continuously running alternator existed, and the team cannot pre-build one because that would chain a second layer of precursor tech beyond the transformer itself. Every other ingredient — Faraday induction (external since 1831), Lenz's law, Joule heating, Foucault's 1855 eddy-current result, soft iron, insulated copper wire, Ruhmkorff-style coil-winding craft, and laminated-core practice — is in hand by the early 1860s. Once a Wilde/Siemens alternator is available off the shelf, a motivated inventor with a skilled workshop can, within five years, empirically iterate from open-core induction coils to a closed (toroidal or shell-type) laminated iron core, recognizing that closing the magnetic circuit reduces leakage and that lamination suppresses eddy losses; the turns-ratio voltage transformation is directly observable on a galvanometer. This places earliest plausible at 1867–1872. The earliest straightforward window of 1878–1883 reflects the period after Gaulard-Gibbs-style AC distribution made the economic motivation obvious."""
    },
    {
        "invention": "Safety bicycle",
        "year": "1885",
        "inventor": "John Kemp Starley",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1844–1855",
        "earliest_straightforward": "1865–1875",
        "actual_location": "Coventry, England",
        "possible_locations": "England; France; Germany; Belgium",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Britain and France led velocipede/cycle development through the mid-19th century, with strong precision metalworking and machine-tool industries; Coventry in particular had a watch and ribbon-weaving industry that transitioned into cycle manufacturing.",
        "confidence": "Medium",
        "full_text": """Invention: Safety bicycle (chain-drive rear-wheel bicycle)
Year actually invented: 1885
Earliest plausible: 1844–1855
Earliest straightforward: 1865–1875
Confidence: Medium
Actual location: Coventry, England
Possible locations at earliest plausible date: England, France, Germany, Belgium
Geographic note: ALIGNED. Britain and France led velocipede/cycle development through the mid-19th century, with strong precision metalworking and machine-tool industries; Coventry in particular had a watch and ribbon-weaving industry that transitioned into cycle manufacturing.
Prerequisite technologies:
- Wrought iron / steel bar and tube stock [by 1820s] — external/team-reachable
- Wire-drawing and wire-tensioning for spoked wheels [by 1808–1820s] — external/team-reachable
- Vulcanized rubber (solid tires) [Goodyear, 1844] — external/team-reachable (BINDING)
- Roller chain (block-chain variants in mill machinery; Galle 1871 — functional equivalents achievable earlier) — team-reachable
- Sprocket and gear reduction [by 1800] — external/team-reachable
- Ball or journal bearings [journal bearings extant; ball bearings patented 1869] — external/team-reachable
- Brazing and silver-soldering of metal frames [by 1840s] — external/team-reachable
- Velocipede / draisine frame geometry [Drais, 1817] — external/team-reachable
Scientific theories / key empirical observations:
- Bicycle stability (empirically achievable by iteration) [empirical by 1817+] — team-discoverable
- Mechanical advantage of chain-and-sprocket drive [understood by 1800] — external
- Diamond frame triangulation for rigidity [craft knowledge, available by 1840s] — team-discoverable
- Tension-spoke wheel load distribution (Cayley ∼1808) — external/team-reachable
Explanation: The binding constraint is vulcanized rubber (Goodyear 1844), which sets the lower bound: without it, iron-tired wooden wheels would produce an unrideable machine on any but the smoothest surfaces. Starting from 1844, a motivated team could wire-spoke the wheels (Cayley's tension wheel concept was public by 1808), fashion a block or plate chain from mill-chain technology (no Galle chain required — a simple block chain suffices for low-speed cycling), and apply sprocket gearing from textile machinery to drive the rear wheel, arriving at a functional if crude safety bicycle. The gap of roughly 30–40 years between earliest plausible and actual invention is explained by path dependency: the high-wheeler (penny-farthing) was a commercially successful dead end that absorbed industry attention through the 1870s, and the critical insight — that gear reduction via chain drive renders a large front drive-wheel unnecessary — was not pursued seriously until that path proved dangerous and limiting."""
    },
    {
        "invention": "Zinc-carbon dry cell",
        "year": "1886",
        "inventor": "Carl gassner",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1868–1872",
        "earliest_straightforward": "1872–1878",
        "actual_location": "Germany",
        "possible_locations": "France; United Kingdom; Germany; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. By the late 1860s, electrochemical engineering was active across Western Europe and the United States; the Leclanché cell was French in origin but rapidly disseminated, so Germany is entirely consistent with the improvement trajectory.",
        "confidence": "High",
        "full_text": """Invention: Zinc-carbon dry cell battery
Year actually invented: 1886
Earliest plausible: 1868–1872
Earliest straightforward: 1872–1878
Confidence: High
Actual location: Germany
Possible locations at earliest plausible date: France, United Kingdom, Germany, United States
Geographic note: ALIGNED. By the late 1860s, electrochemical engineering was active across Western Europe and the United States; the Leclanché cell was French in origin but rapidly disseminated, so Germany is entirely consistent with the improvement trajectory.
Prerequisite technologies:
- Voltaic pile / galvanic cell fundamentals [1800] — external
- Zinc as anode material in galvanic cells [1836, Daniell cell] — external
- Manganese dioxide as cathodic depolarizer [1866, Leclanché] — external
- Leclanché wet cell (zinc anode, MnO2 cathode, NH4Cl liquid electrolyte) [1866] — external
- Plaster of Paris as a setting/thickening binder [ancient] — external
- Ammonium chloride and zinc chloride as commercial chemicals [mid-19th century] — external
- Porous pot / separator technology [1836–1860s] — external
- Zinc sheet and rod fabrication [pre-1866] — external
Scientific theories / key empirical observations:
- Electrolyte conductivity requires ionic mobility [known empirically by 1840s] — external
- Pastes and gels retain sufficient ionic conductivity — team-discoverable
- MnO2 depolarization mechanism [Leclanché 1866, published] — external
- NH4Cl / ZnCl2 mixed electrolyte optimization — team-discoverable
Explanation: The binding constraint is the availability of the Leclanché cell chemistry, published in 1866. Once a motivated team knew that zinc/MnO2/NH4Cl produced a practical galvanic cell, the leap to paste immobilization required no new scientific framework — only the empirical insight that a thickened aqueous medium retains adequate ionic conductivity while eliminating spillage. All constituent materials were commercially available by 1866–1867. A skilled artisan team could have mixed electrolyte pastes, tested internal resistance and discharge curves, and iterated on binder ratios within one to two years, placing earliest plausible invention around 1868–1872. The straightforward window is wider (1872–1878) because paste optimization for shelf stability required additional empirical iteration. The gap between 1866 and 1886 is only twenty years and is explained largely by the absence of a clear commercial motivation until portable electrical devices created demand."""
    },
    {
        "invention": "Hall-Heroult process",
        "year": "1886",
        "inventor": "Charles Hall and Paul Heroult",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1856–1865",
        "earliest_straightforward": "1870–1880",
        "actual_location": "Oberlin, Ohio, USA (Hall); Paris, France (Héroult)",
        "possible_locations": "United Kingdom; Germany; France; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual inventors worked in France and the USA, both of which were among the leading industrial-chemical nations of the era and would have been plausible hosts for an earlier directed program given their electrochemical research communities.",
        "confidence": "Medium",
        "full_text": """Invention: Hall-Héroult process (electrolytic aluminum smelting)
Year actually invented: 1886
Earliest plausible: 1856–1865
Earliest straightforward: 1870–1880
Confidence: Medium
Actual location: Oberlin, Ohio, USA (Hall); Paris, France (Héroult)
Possible locations at earliest plausible date: United Kingdom, Germany, France, United States
Geographic note: ALIGNED. The actual inventors worked in France and the USA, both of which were among the leading industrial-chemical nations of the era and would have been plausible hosts for an earlier directed program given their electrochemical research communities.
Prerequisite technologies:
- Voltaic pile / sustained DC current source [1800] — external
- Large-scale battery banks / carbon-zinc cells capable of high current [1840s–1850s] — team-reachable
- Carbon electrode fabrication [1840s] — external/team-reachable
- Refractory crucible and high-temperature furnace technology (~1000°C) [pre-1800, improved 1820s–1840s] — external/team-reachable
- Isolation of pure alumina (Al₂O₃) [1827, Wöhler] — external/team-reachable
- Cryolite mineral (Na₃AlF₆) from Greenland [known by ∼1800] — external/team-reachable
- Sodium-reduction aluminum production (Deville process) [1854] — external
- Electrolytic deposition of metals from aqueous solution [1830s–1840s] — external/team-reachable
Scientific theories / key empirical observations:
- Faraday's laws of electrolysis [1833] — external
- Empirical knowledge that ionic/salt melts conduct electricity and yield metals at cathode (Davy 1807) — external
- Observation that cryolite dissolves alumina at ∼960°C — team-discoverable
- Understanding that aluminum oxide is not reducible from aqueous solution — team-discoverable
Explanation: The hard binding constraint is the empirical discovery that cryolite dissolves alumina to form a low-melting, electrically conducting melt suitable for electrolysis. All other prerequisites were in place by the mid-1850s. A motivated team in 1856–1865, aware of Deville's sodium-reduction work and the commercial value of cheap aluminum, could have systematically tested known mineral fluorides as alumina solvents and arrived at the cryolite melt within a five-year empirical program; the single layer of precursor technology (scaling battery banks to deliver the necessary current density) was team-reachable by iterating on existing Grove or Bunsen cell designs. The "earliest straightforward" range of 1870–1880 reflects the additional practical development of dynamo-based continuous DC power (Gramme dynamo, 1871), which makes sustained high-current electrolysis far more tractable."""
    },
    {
        "invention": "Petrol automobile",
        "year": "1886",
        "inventor": "Karl Benz",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "1877–1880",
        "earliest_straightforward": "1882–1886",
        "actual_location": "Mannheim, Germany",
        "possible_locations": "Germany; United Kingdom; France; Belgium; United States",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The actual invention occurred in Germany, which was among the most industrially and technically capable nations in the 1870s–1880s. France, the UK, and Belgium were equally plausible hosts given their comparable industrial infrastructure.",
        "confidence": "High",
        "full_text": """Invention: Petrol automobile (gasoline-powered motor vehicle)
Year actually invented: 1886
Earliest plausible: 1877–1880
Earliest straightforward: 1882–1886
Confidence: High
Actual location: Mannheim, Germany
Possible locations at earliest plausible date: Germany, United Kingdom, France, Belgium, United States
Geographic note: ALIGNED. The actual invention occurred in Germany, which was among the most industrially and technically capable nations in the 1870s–1880s. France, the UK, and Belgium were equally plausible hosts given their comparable industrial infrastructure.
Prerequisite technologies:
- Four-stroke internal combustion engine (Otto cycle) [1876] — external
- Reliable electric ignition coil (Ruhmkorff-type induction coil) [1851] — external
- Wire-spoked tension wheel [1869] — external
- Vulcanized rubber for wheels/seals [1844] — external
- Petrol/naphtha fuel (coal-tar distillation) [∼1850] — external
- Steel tube and sheet fabrication for lightweight chassis [∼1860s] — external
- Differential gear mechanism [1827] — external
- Leather/rubber belt drive transmission [∼1850s] — external
- Vaporizer/surface carburetor concept (Lenoir-type) [1860] — external
Scientific theories / key empirical observations:
- Thermodynamic cycle efficiency (empirical, no formal theory required) [1820s–1860s] — external
- Petroleum chemistry: fractional distillation [∼1850s] — external
- Empirical observation that volatile petroleum fractions ignite reliably under compression-timed spark [pre-1876] — external
- Air-fuel mixture ratio for reliable combustion — team-discoverable
Explanation: The binding item is Otto's four-stroke engine patent of 1876. Every other prerequisite was available by the mid-1860s at the latest. A motivated team starting in 1877 with access to Otto's published design could, within the five-year window, mount a refined four-stroke engine on a purpose-built lightweight chassis, adapt a surface carburetor for petrol vaporization, and implement timed electric ignition using off-the-shelf Ruhmkorff coil technology. The gap between the 1870 Marcus vehicle and the 1886 Benz Patent-Motorwagen is one of engineering refinement, not scientific discovery: reliable carburetion, consistent ignition timing, and a purpose-designed chassis were all within the empirical reach of a skilled mechanical workshop. The actual 1886 date reflects incremental development pace, not a hard technical barrier; a well-resourced team could plausibly have achieved a functionally equivalent vehicle by 1879–1880."""
    }
]

with open(CHECKPOINT, 'a') as f:
    for entry in entries:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')

print(f"Wrote {len(entries)} entries to checkpoint.")

with open(CHECKPOINT) as f:
    total = sum(1 for _ in f)
print(f"Total entries now: {total}")
