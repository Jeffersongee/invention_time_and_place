#!/usr/bin/env python3
"""Write batch 27 entries (indices 182-189) to analysis_checkpoint.jsonl"""
import json

CHECKPOINT = "analysis_checkpoint.jsonl"

entries = [
    # 182: Sputnik
    {
        "invention": "Sputnik artificial satellite",
        "year": 1957,
        "inventor": "USSR (Korolev and team / OKB-1)",
        "category": "Other",
        "category2": "",
        "earliest_plausible": "1948–1952",
        "earliest_straightforward": "1952–1955",
        "actual_location": "Baikonur, USSR (Kazakh SSR)",
        "possible_locations": "USSR (Moscow — OKB-1/Korolev, Kapustin Yar test site); USA (Huntsville AL — Redstone Arsenal/von Braun team, White Sands NM); UK (Royal Aircraft Establishment Farnborough); Germany (reconstituted Peenemünde team)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USSR is in the possible-locations list. Both the USSR and USA are equally strong candidates at the earliest plausible date — each had captured V-2 hardware and personnel. The Soviet program launched first due to strong state prioritization and the pre-war GIRD/Korolev rocketry tradition.",
        "confidence": "Medium",
        "full_text": """Invention: Sputnik artificial satellite
Year actually invented: 1957
Earliest plausible: 1948–1952
Earliest straightforward: 1952–1955
Confidence: Medium
Actual location: Baikonur, USSR (Kazakh SSR)
Possible locations at earliest plausible date: USSR (Moscow — OKB-1/Korolev, Kapustin Yar); USA (Huntsville AL — Redstone Arsenal/von Braun team, White Sands NM); UK (Royal Aircraft Establishment Farnborough); Germany (reconstituted Peenemünde team)
Geographic note: ALIGNED. The USSR is in the possible-locations list. Both the USSR and USA are equally strong candidates given captured V-2 hardware and personnel; the Soviet program launched first due to strong state prioritization and the Korolev/GIRD pre-war tradition.

Prerequisite technologies:
- Tsiolkovsky rocket equation [1903] — external knowledge; non-binding
- Goddard liquid-fueled rocket [1926] — external knowledge; non-binding
- V-2 turbopump-fed large liquid rocket [Peenemünde 1942] — external knowledge; binding lower bound for delta-v starting point
- Multi-stage rocket concept [Tsiolkovsky 1903; Oberth 1923] — external knowledge; essential for reaching orbital velocity
- Orbital mechanics (Newton/Kepler, refined by Gauss) [1687–1801] — external knowledge; non-binding
- Radio transmitter technology [Marconi era, 1895–1901] — external knowledge; non-binding
- Aluminum alloy aerospace fabrication [1930s] — external knowledge; non-binding
- Gyroscopic inertial guidance [V-2 era, 1940s] — external knowledge; non-binding
- High-energy liquid propellants (LOX/alcohol, LOX/kerosene) [1926–1942] — external knowledge; non-binding
- Scaling V-2 thrust 5–8× via engine clustering or enlargement — team-reachable (one precursor layer: hard turbopump engineering, no new science)

Scientific theories / key empirical observations:
- Newtonian orbital mechanics: circular orbit requires v = √(GM/r) ≈ 7.9 km/s at LEO — available from 1687
- Tsiolkovsky mass-ratio equation: quantifies propellant fraction needed; shows orbital velocity requires staging or very high mass ratio
- Specific impulse of LOX/kerosene (~310s) empirically measured by Peenemünde teams — available as external knowledge
- V-2 achieved ~1.6 km/s burnout; orbital velocity gap is a factor ~5× in delta-v — purely engineering, no new physics

Explanation:
The binding constraint for an artificial satellite is achieving ~7.9 km/s orbital velocity with sufficient payload mass. The V-2 (1942) achieved approximately 1.6 km/s burnout velocity; the gap to orbital velocity requires a ~5× increase in delta-v, achievable via multi-staging (Oberth's concept, published 1923) and/or engine scaling. Both the staging concept and the specific impulse data needed to calculate propellant mass ratios were published and available as external knowledge. A motivated team starting from the late 1940s with V-2-level knowledge and focused on a minimal orbital payload (Sputnik 1 weighed only 83.6 kg — far less than the several-tonne ICBM payload the R-7 was designed for) could reach orbit with a less capable rocket, substantially reducing thrust requirements.

The earliest plausible window of 1948–1952 reflects that: (1) V-2 hardware and documentation were captured by both the USSR and USA in 1945–1946; (2) the engineering gap from V-2 to orbit contains no scientific unknowns — turbopump scaling, propellant tank mass fractions, and guidance adequate for orbital insertion are all subject to empirical iteration; (3) a team focused solely on a minimum orbital launcher for an 80–100 kg payload could plausibly reach orbit within 5 years of intensive effort from ~1946. The earliest straightforward range of 1952–1955 reflects the genuine difficulty of turbopump reliability at higher thrust levels: failure modes are hard to predict analytically, and real programs (both US and Soviet) experienced many test failures at this stage.

Both the USSR and USA are essentially co-equal candidates at the earliest plausible date. The USSR benefited from Korolev's pre-war GIRD group and Tsander's rocket research tradition, as well as strong post-war state prioritization; the USA benefited from Operation Paperclip bringing von Braun and ~100 Peenemünde engineers with complete V-2 hardware. The UK and a reconstituted German team are plausible but secondary candidates given their smaller industrial base post-1945. The actual Soviet success is ALIGNED and geographically unsurprising given the confluence of captured talent, institutional memory, and state will."""
    },

    # 183: Integrated circuit
    {
        "invention": "Integrated circuit",
        "year": 1958,
        "inventor": "Jack Kilby (Texas Instruments); Robert Noyce (Fairchild Semiconductor)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1957–1958",
        "earliest_straightforward": "1959–1961",
        "actual_location": "Dallas TX (Kilby/TI); Mountain View CA (Noyce/Fairchild)",
        "possible_locations": "USA (Bell Labs Murray Hill NJ; Texas Instruments Dallas TX; Fairchild Semiconductor Mountain View CA; RCA Princeton NJ; Motorola Phoenix AZ); UK (Standard Telephones & Cables London; Mullard/Philips); Germany (Siemens Munich; Telefunken Berlin)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Both actual invention sites (TI Dallas and Fairchild Mountain View) are within the USA cluster, which leads due to its dominance in transistor technology, photolithography, and diffusion doping through the late 1950s.",
        "confidence": "High",
        "full_text": """Invention: Integrated circuit
Year actually invented: 1958
Earliest plausible: 1957–1958
Earliest straightforward: 1959–1961
Confidence: High
Actual location: Dallas TX (Kilby/Texas Instruments); Mountain View CA (Noyce/Fairchild Semiconductor)
Possible locations at earliest plausible date: USA (Bell Labs Murray Hill NJ; Texas Instruments Dallas TX; Fairchild Semiconductor Mountain View CA; RCA Princeton NJ; Motorola Phoenix AZ); UK (Standard Telephones & Cables; Mullard/Philips); Germany (Siemens Munich; Telefunken Berlin)
Geographic note: ALIGNED. Both actual sites (TI Dallas and Fairchild Mountain View) are within the USA cluster, dominant due to its lead in transistor technology, photolithography, and diffusion doping.

Prerequisite technologies:
- Bipolar transistor and semiconductor p-n junction physics [Bardeen/Brattain/Shockley, Bell Labs, 1947] — external knowledge
- Silicon single-crystal growth (Czochralski/float-zone) [Bell Labs 1950–1952] — external knowledge
- Diffusion doping for controlled junction formation [Sparks/Teal ~1954; Pfann zone refining] — external knowledge
- Photolithographic patterning of semiconductor surfaces [~1955–1956, Bell Labs/Texas Instruments] — external knowledge
- Thermal SiO2 growth and oxide masking (selective diffusion through oxide windows) [Frosch & Derick, Bell Labs, 1957] — external knowledge; BINDING LOWER BOUND
- Metal evaporation for ohmic contacts and interconnects [aluminum evaporation, routine by mid-1950s] — external knowledge
- Planar process (oxide-masked diffusion + metal interconnects in single photolithographic sequence) — team-reachable as ONE precursor layer from oxide masking

Scientific theories / key empirical observations:
- Semiconductor band theory and p-n junction rectification — published/external
- Minority carrier injection and transistor action — Shockley 1949; external
- Concept that resistors and capacitors can be formed from doped semiconductor regions and reverse-biased junctions — team-discoverable from transistor physics
- Oxide masking enabling selective area diffusion — Frosch & Derick 1957 (binding)

Explanation:
The integrated circuit represents the convergence of transistor technology, diffusion doping, photolithography, and the conceptual insight that multiple electronic components — transistors, resistors, and capacitors — can be fabricated and interconnected on a single semiconductor substrate. Jack Kilby's September 1958 demonstration at Texas Instruments used germanium with fine gold wire bonds connecting separately fabricated regions; Robert Noyce's 1959 planar IC at Fairchild Semiconductor used the planar process (Jean Hoerni, developed ~late 1958) to create all components and interconnections entirely through photolithographic patterning and metal deposition.

The binding external-knowledge prerequisite is the 1957 Frosch-Derick oxide masking paper (Journal of the Electrochemical Society, 1957). This publication established that thermally grown SiO2 could both passivate the silicon surface and serve as a selective diffusion mask — enabling different device regions to be defined photolithographically and doped independently. The team-reachable precursor layer is the planar process itself: given oxide masking (1957), a motivated team could develop the sequence of oxide growth, photolithographic window etching, diffusion, and metal interconnect deposition within 1–2 years of intensive work. This is precisely what Hoerni accomplished at Fairchild in 1958, working from the same published foundation.

Kilby's approach was slightly more primitive but required only diffusion-doped transistor technology (~1954) plus the conceptual insight to integrate components on one chip, without the planar process. The lower bound of 1957 therefore accommodates both: the earliest a Kilby-style wire-bond IC could be deliberately attempted (once silicon transistors and diffusion doping were mature, ~1955–1956) and the earliest a planar IC could be built (once oxide masking was published, 1957). The earliest straightforward date of 1959–1961 reflects when, once the planar process was published and silicon transistor technology widely distributed, any well-equipped semiconductor laboratory could systematically pursue integration. Confidence is High: the path from SiO2 oxide masking to integrated circuit is short, direct, and required no new scientific discovery."""
    },

    # 184: MOSFET
    {
        "invention": "MOSFET transistor",
        "year": 1959,
        "inventor": "Mohamed Atalla & Dawon Kahng (Bell Labs, Murray Hill NJ)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1958–1960",
        "earliest_straightforward": "1959–1961",
        "actual_location": "Murray Hill, New Jersey, USA (Bell Labs)",
        "possible_locations": "USA (Bell Labs Murray Hill NJ; RCA Princeton NJ); Germany (Siemens Munich); Netherlands (Philips Eindhoven)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Murray Hill NJ (Bell Labs) appears in the possible-locations list. Bell Labs was the uniquely positioned institution holding thermal SiO2 expertise, silicon crystal growth, photolithography, JFET theory, and surface physics knowledge simultaneously.",
        "confidence": "High",
        "full_text": """Invention: MOSFET transistor
Year actually invented: 1959
Earliest plausible: 1958–1960
Earliest straightforward: 1959–1961
Confidence: High
Actual location: Murray Hill, New Jersey, USA (Bell Labs)
Possible locations at earliest plausible date: USA (Bell Labs Murray Hill NJ; RCA Princeton NJ); Germany (Siemens Munich); Netherlands (Philips Eindhoven)
Geographic note: ALIGNED. Murray Hill NJ (Bell Labs) is in the possible-locations list. Bell Labs was uniquely positioned as the single institution holding thermal SiO2 passivation expertise, silicon crystal growth, photolithography infrastructure, JFET theory, and surface physics knowledge simultaneously.

Prerequisite technologies:
- Silicon single-crystal growth (Czochralski method) [Teal/Sparks/Little, Bell Labs, 1950; commercially available mid-1950s] — external
- p-n junction theory and diffused junctions [Shockley 1949; Pfann/Sparks diffusion ~1952–1954] — external
- Bipolar transistor [Bardeen/Brattain/Shockley, Bell Labs, 1947] — external
- JFET concept [Shockley 1952; Lilienfeld patent 1925 as prior art] — external
- Photolithography for semiconductor patterning [~1955, Frosch & Derick process] — external
- Thermal SiO2 growth as surface passivation (Frosch & Derick, Bell Labs, 1957) — BINDING PREREQUISITE; external
- Metal evaporation for gate contact deposition [standard by 1955] — external
- Surface state physics: Bardeen 1947 theory explaining why early FETs failed (surface traps pin Fermi level) — external published knowledge

Scientific theories / key empirical observations:
- Field-effect modulation concept [Lilienfeld 1925 patent; Heil 1935 patent; Shockley 1952 JFET analysis] — external
- Bardeen 1947 surface-state theory: interface traps screen gate field and prevent inversion — explains all 1940s–1950s FET failures
- Thermal SiO2 passivation: Frosch & Derick 1957 — thermally grown oxide reduces Si/SiO2 interface trap density by 2–3 orders of magnitude, enabling inversion layer formation
- Inversion layer concept and MOS capacitor threshold physics — consolidated 1955–1960 in Bell Labs research

Explanation:
The MOSFET is an instructive case where the conceptual idea — field-effect gating of a semiconductor channel — preceded actual realization by over three decades, and the gap was entirely explained by one specific, non-obvious technical barrier: surface state density. Lilienfeld's 1925 patent described a device topologically identical to a MOSFET. Shockley's team at Bell Labs actively attempted to build a working FET in 1945–1948 and failed; Bardeen's surface-state theory (1947) explained why. The Si/SiO2 interface, before controlled thermal oxidation, harbors a trap density of ~10¹²–10¹³ cm⁻², sufficient to screen any practical gate voltage and prevent inversion layer formation. This barrier could not be closed by empirical iteration alone — the team needed to understand why the device was failing, which required the published surface-state physics work of Bardeen, Brattain, and others through the late 1940s–1950s.

The binding prerequisite that unlocks the MOSFET is the 1957 Frosch-Derick result. Their thermally grown SiO2 reduced interface trap density by roughly two to three orders of magnitude, making the Si/SiO2 system qualitatively different from earlier oxide films — low enough to permit gate-induced inversion. A motivated team reading the 1957 paper could recognize its implications for FET fabrication and execute the MOSFET demonstration on essentially the same timeline as the actual inventors. The earliest plausible lower bound (~1958) reflects: one year to absorb the result, procure high-quality thermal oxide samples, design the gate geometry, pattern with photolithography, and measure. This is tight but not implausible for a focused team at a well-equipped facility.

The earliest straightforward window of 1959–1961 acknowledges that connecting the Frosch-Derick passivation specifically to MOS gate applications required non-trivial conceptual synthesis. Bell Labs' advantage was structural: Atalla and Kahng worked in the same building as the oxide growers and could iterate rapidly. An outside team at RCA Princeton, Philips Eindhoven, or Siemens Munich would need additional time to replicate the oxide quality and develop C-V characterization to confirm interface cleanliness. The MOSFET is not a serendipity case — once the Frosch-Derick passivation result existed in the literature, the device was a predictable engineering consequence for any team that understood both the 1947 surface-state barrier and the 1957 solution to it. Confidence is High."""
    },

    # 185: First working laser
    {
        "invention": "First working laser (pulsed ruby laser)",
        "year": 1960,
        "inventor": "Theodore Maiman (Hughes Research Laboratories, Malibu CA)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1956–1958",
        "earliest_straightforward": "1959–1961",
        "actual_location": "Malibu, California, USA (Hughes Research Laboratories)",
        "possible_locations": "USA (Bell Labs Murray Hill NJ; Columbia University NYC; MIT Cambridge MA; Hughes Research Labs Malibu CA; Westinghouse); USSR (Lebedev Physical Institute Moscow); UK (NPL Teddington; Clarendon Laboratory Oxford); Germany (university physics labs)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA (Hughes Research Labs, Malibu CA) is in the possible-locations list. The USA had the densest concentration of relevant capabilities: Bell Labs (maser tradition, mirror coatings), Columbia (Townes' maser group), and Linde/Union Carbide (synthetic ruby supply).",
        "confidence": "Medium",
        "full_text": """Invention: First working laser (pulsed ruby laser)
Year actually invented: 1960
Earliest plausible: 1956–1958
Earliest straightforward: 1959–1961
Confidence: Medium
Actual location: Malibu, California, USA (Hughes Research Laboratories)
Possible locations at earliest plausible date: USA (Bell Labs Murray Hill NJ; Columbia University NYC; MIT Cambridge MA; Hughes Research Labs Malibu CA; Westinghouse); USSR (Lebedev Physical Institute Moscow); UK (NPL Teddington; Clarendon Laboratory Oxford); Germany (university physics labs)
Geographic note: ALIGNED. The USA (Hughes Research Labs, Malibu CA) is in the possible-locations list. The USA had the densest concentration of relevant capabilities: Bell Labs (maser tradition, mirror coatings), Columbia (Townes' maser group), and Linde/Union Carbide's large synthetic ruby supply.

Prerequisite technologies:
- Einstein stimulated emission theory [1917] — external knowledge
- Population inversion concept and rate equations [1940s–1950s, Kastler optical pumping; Bloembergen three-level maser scheme 1956] — external knowledge; Bloembergen 1956 is BINDING LOWER BOUND
- Ammonia beam maser [Townes/Gordon/Zeiger, Columbia, 1953–1954] — external knowledge; demonstrates maser physics
- Fabry-Pérot optical resonant cavity concept — team-reachable once maser analogy is drawn; Fabry-Pérot etalons were mature 19th-century technology
- Verneuil-process synthetic ruby crystals [commercially available ~1902+] — external knowledge
- Large high-optical-quality synthetic ruby boules [Linde/Union Carbide, available ~1953–1955] — external knowledge
- Xenon flash lamps [Edgerton strobe ~1931; commercial high-intensity xenon flash, ~1950–1953] — external knowledge
- High-reflectivity dielectric mirror coatings [evaporated thin-film, mature by ~1950] — external knowledge
- Ruby Cr³⁺ R-line spectroscopy fully characterized [mid-1950s] — external knowledge

Scientific theories / key empirical observations:
- Einstein A and B coefficients; stimulated emission cross-section for ruby R-lines (~2.5 × 10⁻²⁰ cm²)
- Three-level energy scheme of Cr³⁺ in Al₂O₃: ground state, pump bands at ~550/400 nm, metastable ²E emitting at 694.3 nm
- Long fluorescence lifetime (~3 ms) enabling population inversion under pulsed pumping
- Bloembergen 1956 three-level maser paper: first quantitative publication making optical frequency extensions explicit
- Threshold condition: round-trip gain must exceed round-trip loss — straightforward calculation once optical resonator concept in hand

Explanation:
The binding constraint is not the maser (1953–54) per se but the conceptual leap of applying a Fabry-Pérot optical resonant cavity to an optically pumped medium — recognizing that coherent light amplification could work by the same stimulated-emission physics as the maser, using mirrors instead of a waveguide. This insight was implicit in Bloembergen's July 1956 paper (three-level solid-state maser), which explicitly discussed optical frequencies as a future extension, and was made fully explicit by Schawlow and Townes in their December 1958 Physical Review paper. A motivated team reading the 1956 Bloembergen paper carefully could plausibly have drawn the same conclusion 1–2 years earlier — approximately 1956–1957 — since every physical ingredient was already in hand: large synthetic ruby crystals, high-intensity xenon flash lamps, dielectric mirror coatings, and well-measured ruby spectroscopy.

The team-reachable layer is the optical resonator cavity design: choosing mirror separation, estimating threshold pump power, and deciding to use polished ruby end-faces as mirrors. Maiman's actual approach was remarkably simple — a helical flash lamp around a ruby rod with silvered ends — essentially an engineering calculation using published spectroscopic data and standard Fabry-Pérot theory. A skilled team in 1956–1957, armed with Bloembergen's paper and the ruby spectroscopic literature, could converge on the same configuration. The main empirical iteration — confirming that pump intensity from available flash lamps exceeded threshold — was a matter of weeks of lab work, not years.

The lower bound of 1956 is set by Bloembergen's three-level maser paper: below that date, the population inversion scheme for solid-state media was not published in actionable form. The upper bound of 1958 reflects that by the time Schawlow-Townes was published (summer 1958), only engineering remained; any competent team reading that paper should reach a working ruby laser within 1–2 years, consistent with Maiman's actual 1960 result. The Medium confidence reflects genuine uncertainty about whether the conceptual synthesis (from Bloembergen's maser discussion to optical cavity laser) was achievable without the specific context of Bell Labs' maser program and existing mirror-coating expertise."""
    },

    # 186: Electronic cigarette
    {
        "invention": "Electronic cigarette (e-cigarette)",
        "year": 1963,
        "inventor": "Herbert A. Gilbert (Beaver Falls, Pennsylvania, USA)",
        "category": "Electrical",
        "category2": "",
        "earliest_plausible": "1900–1910",
        "earliest_straightforward": "1920–1930",
        "actual_location": "Beaver Falls, Pennsylvania, USA",
        "possible_locations": "United Kingdom (London, Birmingham — electrical instrument trade); Germany (Berlin, Munich — precision engineering); United States (New York, New Jersey, Massachusetts — electrical manufacturing); France (Paris — instrument trade)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The United States appears in the possible-locations list. The 1963 actual date represents a ~40-year demand gap from earliest plausible; no technical barrier existed beyond the demand for such a device.",
        "confidence": "High",
        "full_text": """Invention: Electronic cigarette (e-cigarette)
Year actually invented: 1963
Earliest plausible: 1900–1910
Earliest straightforward: 1920–1930
Confidence: High
Actual location: Beaver Falls, Pennsylvania, USA
Possible locations at earliest plausible date: United Kingdom (London, Birmingham — electrical instrument trade); Germany (Berlin, Munich — precision engineering); United States (New York, New Jersey, Massachusetts — electrical manufacturing); France (Paris — instrument trade)
Geographic note: ALIGNED. The United States appears in the possible-locations list. The 1963 actual date represents a ~40-year demand gap from earliest plausible; all physical components were commercially available since the early 1900s.

Prerequisite technologies:
- Dry-cell primary batteries [Leclanché cell 1866; compact zinc-carbon cells widely available by 1890s] — external
- Nichrome resistance wire [patented 1906 by Albert Marsh; platinum/iron wire available earlier for same function] — external by ~1906; team-reachable before 1906 using platinum wire
- Propylene glycol / glycerine as carrier liquid [glycerine commercially available since 1800s; propylene glycol synthesized 1859, commercial early 1900s] — external
- Nicotine solution [nicotine isolated 1828, tobacco alkaloid chemistry well understood by 1890s] — external
- Porous wicking materials [cotton, felt, ceramic — universally available throughout period] — external
- Miniaturized metal tube housing [standard precision metalworking throughout period] — external
- Electrical insulation materials [rubber, shellac, mica — available throughout period] — external

Scientific theories / key empirical observations:
- Joule heating [Joule 1841]: resistance wire carrying current generates heat proportional to I²R
- Evaporation/aerosolization of low-volatility liquids at moderate temperatures (~100–250°C) — basic thermodynamics, no new science required
- Nicotine pharmacology and inhalation delivery — empirically understood through tobacco use for centuries; isolated and characterized by 1828

Explanation:
The electronic cigarette is a straightforwardly electromechanical device: a primary battery drives current through a resistance wire in contact with a liquid-saturated wick, generating enough heat to aerosolize the liquid drawn through a mouthpiece. Every element was independently mature well before Gilbert's 1963 conception. Compact zinc-carbon dry cells were available by the 1880s–1890s. Nichrome wire was patented in 1906, but iron or platinum resistance wire capable of the same Joule-heating function existed decades earlier. Glycerine — the simplest carrier liquid candidate — was a well-known, inexpensive byproduct of soap manufacture throughout the 19th century, and nicotine had been isolated and characterized since 1828. There is no physical phenomenon in a vaporizer that postdates 1850.

The earliest plausible bound of 1900–1910 reflects the point at which a motivated team could assemble all components without any bespoke fabrication challenge: compact dry cells, nichrome or iron resistance wire, glycerine solution, cotton wick, and a machined brass tube. The device requires no new science, no industrial scale, and no serendipitous observation — only the deliberate assembly of known components toward a defined goal (a non-combustion nicotine delivery device). A team with a clear specification could produce a functional prototype within weeks. The earliest straightforward bound of 1920–1930 reflects when all components were standard catalog items: by the 1920s, nichrome wire was widely commercially stocked, small primary batteries were standard, and precision metalworking for consumer devices was routine. The 1963 actual date therefore represents a ~40–50 year demand gap, not a technical barrier of any kind. Confidence is High."""
    },

    # 187: Shinkansen — FLAGGED
    {
        "invention": "Shinkansen high-speed rail system",
        "year": 1964,
        "inventor": "Japanese National Railways (JNR); chief engineer Hideo Shima; champion Shinji Sogō",
        "category": "Mechanical",
        "category2": "",
        "earliest_plausible": "Flag",
        "earliest_straightforward": "Flag",
        "actual_location": "Japan (Tokyo–Osaka corridor)",
        "possible_locations": "Flag",
        "geographic_flag": "Flag",
        "geographic_note": "Flag. Category (c): fundamentally social/organizational. The Shinkansen is a 515 km national public transport infrastructure system requiring national-scale land acquisition, World Bank financing, legislative authorization, and operational machinery that no small workshop team can provide. Individual component technologies (EMU trains, welded rail, ATC) were mature by the 1940s–1950s; the binding constraint is organizational and political, not technical.",
        "confidence": "Flag",
        "full_text": """Invention: Shinkansen high-speed rail system
Year actually invented: 1964
Earliest plausible: Flag — Category (c): fundamentally social/organizational
Earliest straightforward: Flag — Category (c): fundamentally social/organizational
Confidence: Flag
Actual location: Japan (Tokyo–Osaka corridor)
Possible locations at earliest plausible date: Flag
Geographic note: Flag. Category (c): fundamentally social/organizational.

Prerequisite technologies:
- Electric traction motors [1880s; external, commercially available]
- Electric multiple-unit (EMU) trains [1890s–1900s; external, commercial]
- Continuous welded rail [1930s; external, commercial]
- Aerodynamic profiling knowledge [1920s–1930s; external, published]
- Automatic Train Protection / cab signalling [1920s–1930s; external, commercial]
- Centralized Traffic Control (CTC) [1920s–1930s; external, commercial]
- Prestressed concrete for bridges/viaducts [1930s–1940s; external]
- High-capacity AC power distribution for rail [1910s–1930s; external]

Scientific theories / key empirical observations:
- Classical vehicle dynamics and hunting oscillation theory [Klingel 1883; published, 19th c. onward]
- Aerodynamic drag scaling with v² [published, early 20th c.]
- AC electric traction theory [published, 1880s–1900s]

Explanation:
Every individual technical component of the Shinkansen was commercially available or published prior to 1964: electric multiple units (1890s), continuous welded rail (1930s), aerodynamic bodyshells (1930s), automatic train protection (1920s), and centralized traffic control (1930s). Germany's Schienenzeppelin reached 230 km/h in 1931; the German Reichsbahn operated 160 km/h electric expresses in the 1930s; France's SNCF ran test runs at over 300 km/h in 1955. In the narrow technical sense, a design specification for a dedicated 200 km/h rail system could have been assembled from published knowledge by the mid-to-late 1950s.

However, the Shinkansen is not a device, a circuit, or a mechanical assembly — it is a system of systems at national infrastructure scale. Its core innovation is the political-institutional decision to build an entirely new, dedicated, standard-gauge right-of-way through 515 km of dense urban and mountainous terrain, separated from all existing traffic, with no grade crossings, purpose-engineered alignment, and a new operations organization built around it. The project required national land acquisition legislation, World Bank financing, JNR institutional commitment, the 1964 Tokyo Olympics as a hard political deadline, and the training of thousands of operating and maintenance staff. None of these factors are substitutable by a motivated small team, regardless of their technical access.

This is therefore a clear instance of Flag criterion (c): the invention is fundamentally social and organizational. A workshop team could design and prototype constituent technologies — an aerodynamic EMU running on a short test track — but that is not the Shinkansen. The Shinkansen's identity as an invention is inseparable from its being a complete, operationally reliable, commercially open, national-scale public transport system. The question of when a small team "could have built it" is not coherently applicable. The Shinkansen belongs to the same category as the Interstate Highway System, the London Underground, or the Panama Canal: technical knowledge sufficient for the engineering predated construction by decades, but the binding constraint was never the engineering per se."""
    },

    # 188: Kevlar — will be filled in below
    {
        "invention": "Kevlar (poly-paraphenylene terephthalamide, PPD-T)",
        "year": 1965,
        "inventor": "Stephanie Kwolek (DuPont Experimental Station, Wilmington DE)",
        "category": "Chemical",
        "category2": "",
        "earliest_plausible": "1957–1962",
        "earliest_straightforward": "1962–1966",
        "actual_location": "Wilmington, Delaware, USA (DuPont Experimental Station)",
        "possible_locations": "USA (DuPont Wilmington DE; Celanese; Monsanto; 3M); Germany (BASF, Bayer, Hoechst — IG Farben successor firms); UK (ICI, Courtaulds); Switzerland (Ciba)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. The USA (DuPont Wilmington DE) is in the possible-locations list. DuPont's unique combination of nylon/polyamide expertise, a systematic fiber research program, and Kwolek's expertise in low-temperature solution polymerization made it a natural leader, but German and UK chemical giants were plausible alternatives.",
        "confidence": "Medium",
        "full_text": """Invention: Kevlar (poly-paraphenylene terephthalamide, PPD-T)
Year actually invented: 1965
Earliest plausible: 1956–1962
Earliest straightforward: 1963–1968
Confidence: Medium
Actual location: Wilmington, Delaware, USA (DuPont Experimental Station)
Possible locations at earliest plausible date: USA (DuPont Wilmington DE; Celanese; Monsanto; 3M); Germany (BASF, Bayer, Hoechst); UK (ICI, Courtaulds); Switzerland (Ciba)
Geographic note: ALIGNED. The USA (DuPont Wilmington DE) is in the possible-locations list. DuPont's polyamide expertise and systematic fiber research program made it the natural leader, but German and UK chemical companies were plausible alternatives.

Prerequisite technologies:
- Carothers' polyamide chemistry and nylon synthesis [DuPont, 1930s] — external knowledge; binding foundation
- Aromatic amine synthesis (aniline derivatives, para-phenylenediamine) [19th c. organic chemistry] — external
- Acid chloride synthesis and Schotten-Baumann interfacial polymerization [early 20th c.] — external
- Low-temperature solution polymerization of aramids [available from Carothers framework; team-reachable] — external/team extension
- Wet/dry-jet-wet spinning of fiber from polymer solutions [nylon/rayon era, 1940s–1950s] — external
- Polymer solution viscometry and molecular weight characterization [1930s–1950s] — external
- Flory's theory of liquid crystalline polymer solutions [Flory 1956] — external; BINDING ENABLING FRAMEWORK

Scientific theories / key empirical observations:
- Amide bond polymerization and chain-growth control — Carothers 1930s
- Extended-chain vs. random-coil fiber morphology and its effect on tensile strength — Flory/Mark 1940s–1950s
- Flory 1956: rigid-rod polymers in solution can form anisotropic liquid crystalline phases at a critical concentration (Flory lattice theory)
- Recognition that para-oriented aromatic polyamides produce more rigid chains than meta-oriented counterparts
- Lyotropic liquid crystal behavior of PPD-T in sulfuric acid or DMAC/LiCl solutions — produces extended-chain fiber when spun

Explanation:
Kevlar's extraordinary strength (tensile strength ~3.6 GPa, five times stronger than steel by weight) arises from the combination of: (1) para-oriented aromatic polyamide repeat units forming a rigid, rod-like polymer backbone; (2) lyotropic liquid crystalline behavior in solution, enabling extended-chain ordering; and (3) spinning through a spinneret that preserves that order. Carothers' polyamide chemistry (1930s) established the amide bond foundation. The critical theoretical enabling framework was Flory's 1956 paper on liquid crystalline polymer solutions, which predicted that sufficiently stiff-chain polymers in solution would form anisotropic phases above a critical concentration — and explicitly noted that such phases would yield fibers with superior axial properties upon spinning.

A motivated team reading Flory's 1956 paper and armed with knowledge of aromatic polyamide synthesis (para-phenylenediamine + terephthaloyl chloride low-temperature solution polymerization — achievable from Carothers' published framework + standard acid chloride chemistry) could systematically explore para-oriented aromatic polyamides as candidates for liquid crystalline spinning. The synthesis steps involve no new scientific discoveries: both monomers were available and the low-temperature solution polymerization of aromatic polyamides was achievable by a team extending Carothers' methodology. The liquid crystal spinning behavior, once the polymer was synthesized, would be observable empirically through solution turbidity/birefringence measurements.

Kwolek's actual discovery involved noticing the turbid/opalescent solution that others had discarded — behavior characteristic of a liquid crystalline phase. While this has a serendipitous element, it is not irreducibly serendipitous: a team systematically guided by Flory's 1956 prediction would know to look specifically for anisotropic behavior in their spinning solutions and to test (rather than discard) cloudy solutions. The earliest plausible range of 1956–1962 reflects: lower bound set by Flory's 1956 theory (the necessary conceptual framework); upper bound reflecting that synthesizing a series of aromatic polyamides and systematically evaluating their spinning solutions requires 2–6 years of focused polymer chemistry work. The Medium confidence reflects the genuine uncertainty about how long the systematic search would take and whether a non-DuPont team would have both the polymer expertise and the spinning infrastructure needed to convert the discovery to a usable fiber."""
    },

    # 189: Packet-switched networks
    {
        "invention": "Packet-switched networking",
        "year": 1969,
        "inventor": "Paul Baran (RAND Corp); Donald Davies (NPL UK); BBN Technologies (ARPANET implementation)",
        "category": "Electronic",
        "category2": "",
        "earliest_plausible": "1955–1962",
        "earliest_straightforward": "1960–1965",
        "actual_location": "USA (RAND Corp Santa Monica CA; BBN Cambridge MA); independently UK (NPL Teddington)",
        "possible_locations": "USA (Bell Labs Murray Hill NJ; MIT Cambridge MA; IBM research; RAND Santa Monica CA; military computing centers); UK (NPL Teddington; University of Manchester; Cambridge); USSR (computing institutes Moscow/Leningrad); France (Institut Blaise Pascal Paris); West Germany (Munich, Göttingen academic computing, post-1955)",
        "geographic_flag": "ALIGNED",
        "geographic_note": "ALIGNED. Both actual invention sites (USA and UK) are the top-tier locations in the possible-locations list. The USA led the ARPANET implementation due to its large installed base of research computers and defense funding; the UK's NPL was a co-equal intellectual birthplace of the concept.",
        "confidence": "Medium",
        "full_text": """Invention: Packet-switched networking (concept and first implementation)
Year actually invented: 1969 (ARPANET first packet switch, Oct 29, 1969); concept developed 1961–1966 (Baran, Davies)
Earliest plausible: 1955–1962
Earliest straightforward: 1960–1965
Confidence: Medium
Actual location: USA (RAND Corp Santa Monica CA; BBN Cambridge MA); independently UK (NPL Teddington)
Possible locations at earliest plausible date: USA (Bell Labs Murray Hill NJ; MIT Cambridge MA; IBM research; RAND Santa Monica CA; military computing centers); UK (NPL Teddington; University of Manchester; Cambridge); USSR (computing institutes Moscow/Leningrad); France (Institut Blaise Pascal Paris); West Germany (Munich, Göttingen academic computing, post-1955)
Geographic note: ALIGNED. Both actual invention sites (USA and UK) are the top-tier locations in the possible-locations list. The USA led the ARPANET implementation; the UK's NPL was a co-equal intellectual birthplace of the concept.

Prerequisite technologies:
- Stored-program digital computer [Manchester Baby 1948; EDSAC 1949; commercial machines ~1951–1955] — external; BINDING LOWER BOUND
- Telecommunications transmission links (telephone/telegraph/leased lines) [1840s+] — external, non-binding
- Store-and-forward message switching (telegraph relay, Telex) [1850s–1930s] — external; non-binding; conceptual ancestor
- Time-sharing OS / multi-user computing [MIT CTSS 1961] — external; motivationally enabling but not technically binding for a two-node prototype
- Packet routing, queuing, and reassembly software — team-reachable within 5-year window once computers available and concept defined
- Shannon's information theory and channel capacity [Shannon 1948] — external; provides statistical multiplexing framework

Scientific theories / key empirical observations:
- Shannon's information theory [1948]: channel capacity theory and statistical multiplexing efficiency
- Store-and-forward switching principle — conceptual ancestor from telegraph tradition
- Statistical multiplexing efficiency vs. dedicated circuit allocation — team-discoverable through empirical utilization measurement
- Distributed routing survivability — team-discoverable through project-level failure-mode analysis
- Boolean algebra applied to digital circuits [Shannon 1937] — external, subsumed in computer prerequisite

Explanation:
The binding prerequisite for a working packet-switching prototype is the stored-program digital computer, available from 1948–1951. By ~1953–1955, multiple institutions in the USA, UK, and USSR had working machines; a team with access to two programmable computers and a leased telephone line could implement packet queuing and forwarding as a pure software engineering project within the 5-year window. Shannon's information theory (1948) provides the intellectual framework for thinking about shared channels; store-and-forward switching from telegraphy provides the conceptual ancestor; the key leap — breaking messages into independently routed blocks reassembled at the destination — is an engineering systems insight, not a scientific discovery, team-discoverable through iteration on a two-node prototype.

The earliest plausible range of 1955–1962 reflects: lower bound (1955) when enough stored-program computers existed for a two-node experiment to be physically assembled; upper bound (1962) when the motivation became sufficiently obvious that no "lucky guesses" are required. The earliest straightforward range of 1960–1965 reflects that by 1960–1961, the time-sharing era was beginning (MIT CTSS 1961), multiple computing centers had motivation to interconnect, and multiple independent teams did in fact converge between 1961 and 1966 (Baran and Davies independently). The ~6–8 year gap between earliest plausible (1955) and actual concept articulation (1961) reflects not a technical barrier but a demand/motivation barrier: few institutions had enough computers to make networking them a priority before the early 1960s.

The gap between the concept (1961–1966) and ARPANET implementation (1969) reflects institutional and organizational factors — DARPA procurement, IMP development at BBN, inter-university coordination — rather than any fundamental technical barrier. A motivated small team with two computers and a leased line could have demonstrated the core packet-switching mechanism years earlier; the ARPANET scale required organizational scaffolding beyond what the rubric team can provide. Both actual invention sites (RAND in the USA, NPL in the UK) are the most plausible locations: the USA dominated due to the sheer number of defense-funded computing installations; the UK was the natural second center given NPL's computing tradition and Davies' background."""
    },
]

# Read existing entries to find current count
with open(CHECKPOINT, 'r') as f:
    existing = f.readlines()
start_idx = len(existing)
print(f"Current checkpoint entries: {start_idx}")
assert start_idx == 182, f"Expected 182 entries, got {start_idx}"

with open(CHECKPOINT, 'a') as f:
    for i, entry in enumerate(entries):
        f.write(json.dumps(entry) + '\n')

with open(CHECKPOINT, 'r') as f:
    final = f.readlines()
print(f"Wrote {len(entries)} entries. Total: {len(final)}")
