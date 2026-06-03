---
tags: [Lüftung, Raumlufttechnik, Klimaanlage, Gebäudetechnik]
skript: "Lüftungstechnik"
autor: "Prof. Markus Hubbuch"
version: "2022"
kapitel: "5.1"
titel: "Filter"
---

> ◀ [[04_2_kombinierte_anlagen|← Kombinierte Anlagen Luft/Wasser]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[05_2_ventilatoren|Ventilatoren →]] ▶

---

# Lüftungstechnik – Kap. 5.1: Filter

## 5 Komponenten der Lüftungs- und Klimatechnik

### 5.1 Filter
> 📖 Kontext: [[02_1_schadstoffabfuhr_luftfuehrung|Lüftung Kap. 2.1 – Schadstofftabelle & Filteranforderungen IAQ]]  ·  Simulation: [[03_2_3_air_handling|IDA ICE Manual Kap. 3.2 – Air Handling Unit (Filter im Modell)]]

Luftfilter sind Geräte resp. Komponenten der Luftaufbereitung, mit denen teilchen- und teilweise auch gasförmige Verunreinigungen aus der Luft gefiltert und abgeschieden werden. Die Aussenluft ist durch Staub unterschiedlicher Teilchengrösse und unterschiedlichen Materials verunreinigt. Ebenfalls sind gasförmige Verunreinigungen vorhanden. Saubere Luft ist in ländlichen Gegenden und nach Regen zu finden, stark verschmutzte Luft nach windstillen Tagen im Winter und in verkehrsreichen sowie städtischen Gebieten und Industriegebieten.

Die teilchenförmigen Verunreinigungen bilden ein disperses Gemisch, der Durchmesser liegt in der Grösse zwischen 0,001 und ca. 500 Mikrometer (µm). Für die Abscheidung dieses grossen Teilchenspektrums kommen verschiedene physikalische Effekte zum Tragen. Die Aussenluft weist Verunreinigungen mit einer Konzentration in der Grössenordnung zwischen 0,05 und 3 mg/m³ auf. Der grösste Teil des Gewichtes rührt dabei vom zahlenmässig sehr kleinen Teil der grossen Partikel her. Dagegen trägt die viel grössere Anzahl der kleinen und kleinsten Partikel nur wenig zur Gewichts-Konzentration der Verunreinigung bei.

Bei sehr hohem Staubgehalt, d. h. ab ca. 20 mg/m³ Partikelkonzentration, müssen andere Abscheidetechniken als Filter angewendet werden (z. B. Luftwäscher, Zentrifugen). Man spricht dann von Entstaubung (Beispiele: Textilfabriken, Mühlen).

Gasförmige Verunreinigungen (schädliche oder störende Gase) müssen durch chemische oder physikalische Sorptionsvorgänge abgeschieden werden. Die Gase werden an das Sorptionsmaterial (oft Aktivkohle) gebunden.

#### Filtertheorie

Die Abscheidung von Teilchen in Filtern beruht hauptsächlich auf folgenden Effekten:

- **Diffusionseffekt:** Das sich bewegende, sehr kleine Teilchen wird an einer Filterfaser abgeschieden, wenn es genügend nahe und während genügend langer Zeit an die Faseroberfläche gelangt.

- **Elektrostatik:** Je nach Ladungszustand der Filterfasern und der Partikel werden diese von den Fasern elektrostatisch angezogen und abgeschieden.

- **Trägheitseffekt:** Ein (grösseres) Teilchen wird dann an einer Faser abgeschieden, wenn es auf seiner Strömungslinie direkt auf eine Faser trifft (und infolge des Trägheitseffektes die Faser nicht umgeht).

- **Sperreffekt:** Dieser Effekt tritt auf, wenn ein kleines Teilchen auf seiner Flugbahn (Stromlinie) auf eine Faser trifft und die Faser seinen Weiterflug verhindert.

- **Siebeffekt:** Dieser Effekt tritt ein, wenn der Teilchendurchmesser grösser als der Faserabstand (Porenweite) ist.

Es werden in einem Filter also auch Teilchen abgeschieden, welche wesentlich kleiner als die Porenweite resp. der Faserdurchmesser sind (Sperrwirkung und Diffusionseffekt). Ein Teil dieser Teilchen kann den Filter auch durchdringen und wird nicht abgeschieden. Grössere Teilchen werden durch Sperrwirkung und Trägheitseffekt abgeschieden, grosse Teilchen werden durch den Trägheitseffekt und die Siebwirkung vollständig zurückgehalten.

Für das Haften der Teilchen an der Faseroberfläche sind die elektrostatischen Kräfte verantwortlich. Der Abscheidegrad eines Filters ist daher vom Fasermaterial, dem Partikelmaterial sowie vom Oberflächenzustand der Faser (verschmutzt, feucht etc.) abhängig. Dazu kommen die Strömungsgeschwindigkeit und weitere Grössen. Deshalb ist der Abscheidegrad nicht konstant.

Der mittlere Abscheidegrad $A_m$ eines Filters ist wie folgt definiert:

$$A_m = \frac{\text{abgeschiedene Staubmasse}}{\text{angebotene Staubmasse}} = \frac{g_{roh} - g_{rein}}{g_{roh}} \cdot 100\,\%$$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $A_m$ | Abscheidegrad | % |
| $g_{roh}$ | Staubgehalt der Rohluft (vor dem Filter) | mg/m³ |
| $g_{rein}$ | Staubgehalt der Reinluft (nach dem Filter) | mg/m³ |

Der Durchlassgrad: $D_g = 100 - A_m \; [\%]$

Der mittlere Wirkungsgrad *E*m wird mit Prüfstaub gemessen; es werden die abgeschiedenen Partikelzahlen mit einer Partikelgrösse von 0,4 μm in Prozent nach SN EN 779 bestimmt (Tabelle 9).

**Tabelle 8: Einteilung Staubfilter nach SN EN 779, 2012 (seit 2018 nicht mehr in Kraft)**

| Filterklasse EN 779 | Abscheidegrad Gew. *A*m | Mittlerer Wirkungsgr. *E*m | Enddruckdiff. | Bezeichnung |
|---|---|---|---|---|
| G1 | 50–65 % | | 250 Pa | Grobstaubfilter |
| G2 | 65–80 % | | | |
| G3 | 80–90 % | | | |
| G4 | 90–95 % | | | |
| M5 | | 40–60 % | 450 Pa | Mediumfilter |
| M6 | | 60–80 % | | |
| F7 | | 80–90 % | 450 Pa | Feinstaubfilter |
| F8 | | 90–95 % | | |
| F9 | | > 95 % | | |

**Tabelle 9: Einteilung Schwebstoff-Filter nach SN EN 1822 und ISO 29463 (2018)**

| Filterklasse EN 1822 | Filterklasse ISO 29463 | Abscheidegrad bei MPPS (Integralwert) | Bezeichnung |
|---|---|---|---|
| E10 | – | > 85 % | Schwebstofffilter E |
| E11 | ISO 15 E | > 95 % | EPA-Filter |
| E12 | ISO 25 E | > 99,5 % | |
| H13 | ISO 35 E | > 99,95 % | Schwebstofffilter H |
| H14 | ISO 45 E | > 99,995 % | HEPA-Filter |
| U15 | ISO 55 E | > 99,9995 % | Reinraumfilter U |
| U16 | ISO 65 E | > 99,999 95 % | ULPA-Filter |
| U17 | ISO 75 E | > 99,999 995 % | |

Ab E10 erfolgen Messverfahren nach EN 1822, 2009, resp. neu nach ISO 29463 (2018). Es wird mit feineren Partikeln gemessen (Tabelle 10). Diese Prüfpartikel werden als «Most Penetrating Particle Size» (MPPS) bezeichnet. Solche Filter werden als Endfilter direkt vor dem Einblasen der Luft in den Reinraum verwendet. Es muss zusätzlich sichergestellt und ab HEPA-Filtern geprüft werden, dass es keine Leckluft gibt, welche neben den Filtern durchströmt.

**Staubfilter-Klassen nach SN EN ISO 16890 (2017):**

Seit 2018 werden die Staubfilter nach der SN EN ISO 16890 eingeteilt. Diese Norm richtet sich nach 3 Grössen von Partikeln: PM10, PM2,5 und PM1 (Abbildung 19).

![[abb19_vergleich_grossen_und_beispiele_der_partik.jpg]]
*Abbildung 19: Vergleich Grössen und Beispiele der Partikel ⁸*

Grobstaubfilter werden in eine Klasse eingeteilt und Coarse-Filter genannt. Die Medium- und Feinstaubfilter werden in drei Klassen entsprechend der Partikelgrössen PM10, PM2,5 und PM1 eingeteilt. Es wird die «Effizienz» gemessen, d. h. der Abscheidegrad der entsprechenden Prüfpartikel. Dieser muss immer mind. 50 % betragen, und kann bei den besten Filtern max. 95 % erreichen. Die Filterbezeichnung ist entsprechend: ISO ePM10, 2,5 oder 1 und die Abscheiderate in Prozent. Das kleine e steht dabei für Effizienz.

Für Lüftungsanlagen für normale Anforderungen wie Büroräume muss in der letzten oder einzigen Filterstufe ein Filter ISO ePM1 > 50 % eingesetzt werden.

Bei stark mit Feinstaub belasteter Aussenluft oder/und bei hohen Anforderungen an die Reinheit der Raumluft muss eine 2-stufige Filtrierung vorgesehen werden. Die erste Filterstufe ist gleich nach der Jalousieklappe Richtung Aussenluft zu empfehlen, um die nachfolgenden Einbauten im Monoblock zu schützen. Die zweite Filterstufe sollte im Monoblock ganz am Schluss montiert sein, sicher nach dem Ventilator (druckseitig). So kann keine ungefilterte Leckluft mehr eintreten und allfällige Verschmutzungen, die im Monoblock selbst auftreten (z. B. vom Befeuchter, Abrieb von Keilriemen, Fasern vom Schalldämpfer) werden ebenfalls abgefiltert. Zu empfehlen ist eine Filtrierung mit einem Vorfilter ISO ePM2,5 > 50 % oder > 65 % (entsprechend etwa F6 oder F7) und dann einem Filter ISO ePM1 > 80 % (entsprechend etwa F9).

> ⁸ Abbildung: Unifil AG, Filtertechnik, https://www.unifil.ch/de_CH/normen-richtlinien/p/3077

#### Aktivkohlefilter

Zur Abscheidung von Gasen und Gerüchen werden Aktivkohlefilter eingesetzt. Diese Filter benötigen einen Feinstaubfilter als Vorfilter (min. ISO ePM2,5 > 65 % oder ISO ePM1 ≥ 50 %). Aktivkohlefilter scheiden gasförmige Moleküle ab aufgrund ihrer sehr grossen Oberfläche (1000 bis 1500 m²/g). Diese Oberfläche entsteht durch Aktivierung organischer Rohstoffe wie Kohle, Kokosnussschalen, Holz, Harz oder Torf. Makroporen (> 50 nm) in der Oberfläche dienen dem Transport der Schadstoffe ins Innere der Kohleteilchen. Dort sind Mesoporen (2 bis 50 nm) und Mikroporen (< 2 nm) vorhanden, welche die Schadstoffmoleküle adsorbieren.

Aktivkohlefilter werden in verschiedenen Bauarten angeboten. Früher wurden zylinderförmige Elemente im Luftstrom angeordnet, in welchen rohrförmige Aktivkohlepatronen enthalten sind und durch welche die Luft strömen musste. Solche Aktivkohlepatronen müssen nach Erreichen der Sättigung ausgewechselt werden. Heute werden Aktivkohlefilter in Zellenbauweise angeboten, deren Aktivkohleplatten ebenfalls ausgewechselt werden können. Bei Aktivkohle-Einwegfiltern sind an ein Filtermedium angeklebte Aktivkohlekügelchen enthalten. Die Entwicklung geht hin zu wirksameren Filtern mit weniger Gewicht, einfacher Wartung und wenig Druckverlust (Energieeinsparung). Verhindert wird bei den neuen Typen auch der Abrieb von Aktivkohleteilchen.

Die Erschöpfung eines Aktivkohlefilters zeigt sich nicht im Druckverlust. Nur die Luftqualität nach dem Filter zeigt an, ob der Aktivkohlefilter gewechselt werden muss.

#### Elektrofilter

Für spezielle Anwendungen (z. B. Ölnebelabscheidung in der Industrie) gibt es Elektrofilter. Die Luft muss zwischen elektrostatisch aufgeladenen Platten hindurchströmen. Die geladenen Platten ziehen alle Partikel an, wo sie haften bleiben. Von Zeit zu Zeit müssen diese Platten gereinigt werden (manuell oder automatisch).

#### Bauarten von Faserfiltern

Filter aus Faservliesen werden nach Material, Einbauart, Filterklasse, Wirkungsweise etc. unterschieden. In der Klimatechnik werden meist Grob- und Feinstaubfilter (bis F9 resp. ISO ePM1 > 80 %) verwendet, in selteneren Fällen Aktivkohlefilter. In Spitälern oder Industriebetrieben werden auch Schwebestofffilter benötigt (Reinräume, Operation, Labors). Die Filter werden üblicherweise im Lüftungsgerät eingebaut. Für Grobstaubfilter werden Taschenfilter verwendet, oft Zellulosefilter. Nachteil ist deren Empfindlichkeit auf hohe Feuchte.

Für Feinstaubfilter werden oft Kassettenfilter (Abbildung 20) verwendet. Letztere haben eine grössere Filteroberfläche dank der speziellen Faltung der Filterelemente in den Kassetten. Das Filtervlies besteht meist aus Mikroglasfasern.

![[abb20_kassettenfilter_in_leftungsgerat.jpg]]
*Abbildung 20: Kassettenfilter in Lüftungsgerät*

#### Filteranordnung

Bis zu einem Filtergrad von max. ISO ePM2,5 ≥ 65 % oder ISO ePM1 ≥ 50 % (ca. F7) können Filter ohne Vorfilter eingesetzt werden. In staubigen Umgebungen oder bei Verwendung von Filtern ab F8 ist ein Vorfilter erforderlich, welcher idealerweise eine 2 bis 3 Stufen tiefere Güte hat. Die Vorfilter verlängern die Standzeit der teuren Feinstaubfilter. Schwebestofffilter benötigen immer eine mehrstufige Vorfiltrierung.

#### Filtereinbau

Die Filter müssen mit dichten Rahmen eingebaut werden, damit keine Luft ungefiltert den Filter umströmen kann. Vor dem ersten Wärmetauscher im Luftstrom (meist die Wärmerückgewinnung) muss mindestens ein Grobstaubfilter (mind. ISO ePM10 ≥ 50 %) eingebaut werden, um den Wärmetauscher vor Verschmutzung zu bewahren. Auf der Luftansaugseite wird der Filter damit von der kalten und je nach Witterung (Nebel) fast gesättigten Aussenluft durchströmt. Infolge des Druckabfalls im Filter (und zuvor schon im Wetterschutzgitter) sinkt auch die Temperatur der Luft (Gasgesetze). Demzufolge steigt die relative Feuchte und kann die Sättigung erreichen, so dass der Filter nass wird. Dies wiederum führt zum Wachstum von Schimmelpilzen sowie anderen Mikroorganismen und zu hygienischen Problemen. Deshalb werden für heikle Anwendungen (Spitäler etc.) dem ersten Filter Vorwärmer vorgeschaltet, welche dann aber nicht vor Verschmutzung geschützt sind und entsprechend häufig gereinigt werden müssen. Eine andere, bessere, aber teurere Variante ist das Nachschalten eines Feinstaubfilters nach dem Lufterhitzer.

Bei hohen Anforderungen ist eine zweistufige Filtrierung erforderlich. Der Feinstaubfilter soll nach dem Ventilator und nach der WRG angeordnet werden. Damit kann dieser Filter auch den Abrieb des oft vorhandenen Keilriemens auffangen und reinigt auch die Leckluft, welche saugseitig vom Ventilator ins Monoblocgehäuse dringen kann. Zudem ist der Filter dort im warmen und trockenen Luftstrom, was das Pilzwachstum verhindert.

Schwebestofffilter werden meist unmittelbar vor dem Luftauslass im Raum angeordnet, um auch eine Zuluftverschmutzung in den Kanälen noch auffangen zu können.

#### Wartung der Filter

Da Filter die Schadstoffe nur abscheiden, nicht aber umwandeln (vernichten), müssen sie regelmässig ausgewechselt werden.

Faserfilter werden üblicherweise mit Differenzdruckmanometern überwacht. Mit zunehmender Filterbelastung nimmt der Druckverlust zu. Damit ergibt sich ein Mass für den Filterzustand. Aus hygienischen Gründen sollte nicht bis zum Erreichen des Enddruckes gewartet werden, bis der Filter ausgewechselt wird. Untersuchungen zeigen, dass die sich in Filtern aufgrund der oft hohen Feuchtigkeit bildenden Schimmelpilze meist schon vor dem Erreichen des Enddrucks problematisch werden. Diese Pilze können durch das Filtermedium hindurch wachsen. Auf der Reinluftseite lösen sich dann Pilzsporen, welche mit der Zuluft in die Räume gelangen. Dort können sie Allergien auslösen. Deshalb muss der Filterwartung eine hohe Priorität eingeräumt werden.

Die Filterstandzeiten, das heisst die Wechselintervalle, sollten deswegen nicht nach dem Enddruck bemessen werden. Einstufige Grob- und Feinstaubfilter müssen aus hygienischen Gründen mindestens einmal jährlich, am besten im Frühsommer, gewechselt werden. Durch Vorfilter geschützte Feinstaubfilter, Schwebestofffilter und Aktivkohlefilter alle 2 Jahre ausgetauscht werden. Die Hygienerichtlinie RLT-Anlagen SWKI VA 104-01, 2019 resp. VDI 6022 sind zu beachten.

---

> ◀ [[04_2_kombinierte_anlagen|← Kombinierte Anlagen Luft/Wasser]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[05_2_ventilatoren|Ventilatoren →]] ▶

---
