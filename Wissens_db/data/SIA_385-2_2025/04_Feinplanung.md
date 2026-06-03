---
tags: [Norm, Trinkwarmwasser, Sanitär, SIA385-2, Gebäudetechnik, Warmwasser]
normnummer: SN 546385/2:2025
gueltig_ab: "2025-02-01"
kapitel: "Kap. 4"
titel: "Feinplanung – Auslegung der Warmwasserversorgung"
---
> ◀ [[03_Grobauslegung|Kap. 3 Grobauslegung – Vorprojektphase]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[05_Waermebedarf_Hilfsenergie|Kap. 5 Wärmebedarf und Hilfsenergie]] ▶

---

# Kap. 4 – Feinplanung – Auslegung der Warmwasserversorgung

---

### 4.1 Vorgehensweise

4.1.1 Ausgehend vom Ergebnis der Grobauslegung wird die Warmwasserversorgung in Einzelheiten geplant. In Figur 4 ist der Ablauf ersichtlich.

4.1.2 Bauherrschaft und Planer bzw. ausführender Installateur klären die letzten Details der Gebäudenutzung und des gewünschten Nutzungskomforts ab und aktualisieren die Nutzungsvereinbarung. Ist die Nutzungsvereinbarung von beiden Parteien unterzeichnet, kann die Feinplanung beginnen.

4.1.3 Der Wärmebedarf für Warmwasser $Q_W$ wird auf der Basis der Nutzungsvereinbarung gemäss A.3 und A.4 neu bestimmt. Dabei wird eine allfällige Wärmerückgewinnung aus Duschwasser vorerst nicht berücksichtigt.

#### 4.1.4 Warmgehaltene Leitungen (wenn vorhanden)

4.1.4.1 Die warmgehaltenen Leitungen werden gemäss D.1 unter Einhaltung sämtlicher Anforderungen von SIA 385/1 detailliert ausgelegt.

4.1.4.2 Die täglichen Wärmeverluste $Q_{W,hl,ls}$ der warmgehaltenen Leitungen werden gemäss D.2 neu bestimmt.

#### 4.1.5 Ausstossleitungen

4.1.5.1 Die Ausstossleitungen werden unter Einhaltung der Anforderungen von SIA 385/1:2020, Ziffern 5.4 und 5.5, detailliert geplant.

4.1.5.2 Die täglichen Wärmeverluste $Q_{W,em,ls}$ der Ausstossleitungen werden gemäss Anhang E bestimmt.

#### 4.1.6 Speicher

4.1.6.1 Die Anforderungen von SIA 385/1:2020, Ziffer 5.2 (Speicherdämmung, Schichtung, Wärmesiphons) sind einzuhalten.

4.1.6.2 Das Volumen des Speichers – insbesondere sein Bereitschaftsvolumen $V_{W,sto,cont}$ – und der Wärmeleistungsbedarf der Wassererwärmungsanlage $\Phi_{W,gen}$ werden gemäss [[04_Feinplanung|4.2]] ermittelt. Dabei kann ein iteratives Vorgehen mit der Erarbeitung sukzessiver Varianten nötig sein (siehe 4.2.3.5 und Anhang F). Bei der Berechnung des Speichervolumens werden für das Steuervolumen und das Spitzendeckungsvolumen unterschiedliche Verfahren angewendet. Eine entscheidende Grösse ist die Anzahl der Ladezyklen pro Tag $n_z$. Das so bestimmte Speichervolumen umfasst keine allfälligen vorgeschalteten Vorwärm- und Mitteltemperaturzonen, welche gemäss ihren eigenen, von der Anlageart abhängigen Regeln dimensioniert werden.

4.1.6.3 Ist im Speicher eine Vorwärmzone, die Trinkwasser (auch nur teilweise) enthält, sowie allenfalls eine Mitteltemperaturzone vorhanden, sind alle Anforderungen von SIA 385/1:2020, Ziffer 3.2.6, aus hygienischen Gründen einzuhalten. Insbesondere ist in Vorwärm- sowie allenfalls Mitteltemperaturzonen vorzugsweise Betriebswasser vorzusehen und die Dimensionierungsregeln sind zu beachten.

4.1.6.3.1 Bei der Dimensionierung einer Mitteltemperaturzone sind die Anforderungen von SIA 384/1:2022, Kapitel 4 einzuhalten.

4.1.6.3.2 Bei Kombispeichern gemäss Figur 2e ist das Spitzendeckungsvolumen gleich dem Volumen des Trinkwassers, das auf Soll-Temperatur gehalten wird.

4.1.7 Ab diesem Schritt der Feinplanung werden die unterschiedlichen Anforderungen gemäss SIA 384/1 bzw. SIA 385/1 berücksichtigt, siehe Figur 1 der vorliegenden Norm. Wasser-Wärmespeicher sowie Leitungen und Wärmeübertrager der Warmwasserversorgung, die ausschliesslich Betriebswasser enthalten, werden nach SIA 384/1 gedämmt und ihre Wärmeverluste gemäss SIA 384/3 berechnet. Alle Komponenten, die Trinkwasser enthalten, werden gemäss SIA 385/1 und SIA 385/2 ausgelegt.

#### 4.1.8 Wärmeerzeugung

4.1.8.1 Wenn die Wärmeerzeugung der Warmwasserversorgung mit derjenigen der Heizung und/oder der Lüftung kombiniert ist, wird sie gemäss SIA 384/1 in Absprache mit dem Heizungsplaner ausgelegt.

4.1.8.2 Bei Wärmepumpen, die nur der Wassererwärmung dienen, müssen alle Anforderungen von SIA 385/1:2020, Ziffer 5.7.1, eingehalten werden. Bei der Berechnung der Leistungszahl muss der Stromverbrauch eines allfälligen Widerstandsheizelements mitberücksichtigt werden.

4.1.9 Der Wärmebedarf der Warmwasserversorgung $Q_{W,gen,out}$ und die Hilfsenergie $E_{W,aux}$ werden schliesslich gemäss Kapitel 5 als Beiträge zur Gebäudeenergiebilanz berechnet.

**Figur 4** – Schematische Darstellung des Ablaufs der Feinplanung

![[Figur_4_Feinplanung.png]]

---

### 4.2 Speichervolumen und Wärmeleistungsbedarf der Wassererwärmungsanlage

#### 4.2.1 Grundlegendes

4.2.1.1 Speichervolumen und Wärmeleistungsbedarf der Wassererwärmungsanlage[^8] sind von den Eigenschaften der Wärmeerzeugung und der Systemwahl der Warmwasserversorgung abhängig. Dabei sind insbesondere folgende Einflussgrössen massgebend:

- der eingesetzte Energieträger des Wärmeerzeugers;
- die zeitliche Verfügbarkeit des Wärmeerzeugers für die Wassererwärmung;[^9] sie bestimmt die Anzahl der Ladezyklen und deren maximale Dauer;
- die Temperatur, für welche der Wärmeerzeuger die Wärme bereitstellen soll;
- die Vorlaufzeit des Wärmeerzeugers (bis Wärme abgegeben werden kann);
- die Mindestlaufzeit des Wärmeerzeugers, die nach dessen Einschaltung eingehalten werden soll;
- die grösste kurzfristig zu erwartende Spitze des Warmwasserverbrauchs;
- die thermische Trägheit des Gebäudes; es ist festzulegen, ob die Heizung − bei Wassererwärmung und Heizung mit einem gemeinsamen Wärmeerzeuger − während der Wassererwärmung unterbrochen werden darf oder ob sie parallel betrieben werden soll;
- die Abmessungen des Speichers und der Einbringungsöffnungen;
- bei Fernwärme und Wärmepumpen: die höchste zulässige Rücklauftemperatur.

4.2.1.2 Anhand dieser Einflussgrössen wird in Koordination mit dem Heizungsplaner entschieden, wie viele Ladezyklen des Speichers pro Tag vorzusehen sind. Zusätzliche Hinweise siehe SIA 384/1.

4.2.1.3 Das Berechnungsverfahren von 4.2.2 gilt auch, wenn der Speicher ein Wasser-Wärmespeicher (z. B. bei Durchflusswassererwärmern) ist.

#### 4.2.2 Berechnungsgang Speichervolumen und Wärmebedarf

4.2.2.1 Die Speicherwärmeverluste $Q_{W,sto,ls}$ werden auf der Basis des Wärmebedarfs für Warmwasser $Q_W$ gemäss Anhang B berechnet.

4.2.2.2 Der Wärmebedarf $Q_{W,gen,out}$ der Warmwasserversorgung wird berechnet:

$$Q_{W,gen,out} = Q_W + Q_{W,sto,ls} + Q_{W,hl,ls} + Q_{W,em,ls} \tag{5}$$

| Symbol | Bedeutung |
|---|---|
| $Q_{W,gen,out}$ | Wärmebedarf der Warmwasserversorgung, in kWh/d |
| $Q_W$ | Wärmebedarf für Warmwasser gemäss A.3 und A.4, in kWh/d |
| $Q_{W,sto,ls}$ | Speicherwärmeverluste gemäss Anhang B, in kWh/d |
| $Q_{W,hl,ls}$ | Wärmeverluste der warmgehaltenen Leitungen gemäss D.2, in kWh/d |
| $Q_{W,em,ls}$ | Ausstosswärmeverluste gemäss Anhang E, in kWh/d |

Bei einer Warmhaltung mit Warmhaltebändern werden – analog zu 3.3.3.6.2, Gleichung 4 – die Wärmeverluste der warmgehaltenen Leitungen um zwei Drittel reduziert:

$$Q_{W,gen,out} = Q_W + Q_{W,sto,ls} + 0{,}333 \cdot Q_{W,hl,ls} + Q_{W,em,ls} \tag{6}$$

Ist in der Warmwasserversorgung eine Wärmerückgewinnung aus Duschwasser vorhanden, reduziert sich der Wärmebedarf der Warmwasserversorgung gemäss Gleichung 40 im Anhang K.

4.2.2.3 Die in jedem Ladezyklus bereitzustellende Wärmemenge wird berechnet:

$$Q_{W,gen,out,z} = \frac{Q_{W,gen,out}}{n_z} \tag{7}$$

| Symbol | Bedeutung |
|---|---|
| $Q_{W,gen,out,z}$ | in einem Ladezyklus bereitzustellende Wärmemenge, in kWh |
| $Q_{W,gen,out}$ | täglicher Wärmebedarf der Warmwasserversorgung gemäss Gl. 5 bzw. 6, in kWh/d |
| $n_z$ | Anzahl der Speicherladezyklen pro Tag, gemäss [[04_Feinplanung\|4.2.1.2]] |

4.2.2.4 Der Wärmebedarf $Q_{W,pk}$ für die Deckung der grössten Stundenspitze des Warmwasserbedarfs wird gemäss A.5 berechnet.

4.2.2.5 Der Wärmeinhalt des Bereitschaftsvolumens des Speichers wird berechnet:

$$Q_{W,sto,cont} = Q_{W,pk} + Q_{W,gen,out,z} \tag{8}$$

| Symbol | Bedeutung |
|---|---|
| $Q_{W,sto,cont}$ | Wärmeinhalt des Bereitschaftsvolumens des Speichers, in kWh |
| $Q_{W,pk}$ | Wärmebedarf für die Deckung der grössten Stundenspitze gemäss A.5, in kWh |
| $Q_{W,gen,out,z}$ | in jedem Ladezyklus bereitzustellende Wärmemenge gemäss [[04_Feinplanung\|4.2.2.3]], in kWh |

4.2.2.6 Die Temperatur $\theta_{W,sto,out}$, welche am Austritt des Speichers nötig ist, um die Mindesttemperaturen im Warmwasserverteilnetz gemäss SIA 385/1:2020, Ziffern 3.2.3 und 3.2.5 einzuhalten, wird bestimmt.

4.2.2.7 Der Anfangswert des Bereitschaftsvolumens des Speichers wird berechnet:

$$V_{W,sto,cont,1} = \frac{Q_{W,sto,cont}}{(\theta_{W,sto,out} - \theta_{W,c}) \cdot \rho \cdot C_p} \tag{9}$$

| Symbol | Bedeutung |
|---|---|
| $V_{W,sto,cont,1}$ | Anfangswert des Bereitschaftsvolumens des Speichers, in Liter |
| $Q_{W,sto,cont}$ | Wärmeinhalt des Bereitschaftsvolumens gemäss [[04_Feinplanung\|4.2.2.5]], in kWh |
| $\theta_{W,sto,out}$ | erforderliche Temperatur am Speicheraustritt gemäss [[04_Feinplanung\|4.2.2.6]], in °C |
| $\theta_{W,c}$ | Temperatur des Kaltwassers am Speichereintritt, fix 10 °C |
| $\rho \cdot C_p$ | $= 1{,}16 \cdot 10^{-3}$ kWh/(K·l) |

4.2.2.8 Das Speichervolumen wird wie folgt berechnet.

##### 4.2.2.8.1 Anfangswert des Speichervolumens

$$V_{W,sto,1} = V_{W,sto,cont,1} \cdot f_{sto} \tag{10}$$

| Symbol | Bedeutung |
|---|---|
| $V_{W,sto,1}$ | Anfangswert des Speichervolumens, in Liter |
| $V_{W,sto,cont,1}$ | Anfangswert des Bereitschaftsvolumens gemäss [[04_Feinplanung\|4.2.2.7]], in Liter |
| $f_{sto}$ | von der Speicherkonfiguration abhängiger Faktor (siehe unten) |

| $f_{sto}$ | Bedingung |
|---|---|
| 1,25 | wenn eine Mischzone und eine Kaltzone vorhanden sind, in denen die Solltemperatur des Warmwassers nicht erreicht wird (z. B. Speicherladung mit innenliegendem Wärmeübertrager) |
| 1,1 | wenn nur eine Mischzone vorhanden ist (z. B. Speicherladung mit aussenliegendem Wärmeübertrager) |
| 1,0 | wenn weder eine Mischzone noch eine Kaltzone vorhanden ist, oder wenn eine zusätzliche Vorwärmzone sowie evtl. eine Mitteltemperaturzone vorhanden ist[^10] |

Die Werte von $f_{sto}$ setzen voraus, dass die Kaltzone und die Mischzone möglichst klein sind.

##### 4.2.2.8.2 Definitives Speichervolumen

Mit dem gemäss Gleichung 10 berechneten Wert $V_{W,sto,1}$ ist ein nächstliegender Speicher des Markts auszuwählen. Dabei ist in Abhängigkeit von der Wärmeerzeugung auf eine ausreichende Wärmeübertragungsfläche zu achten. Die Koordination mit dem Heizungsplaner ist zu diesem Zeitpunkt besonders wichtig. Das definitive Volumen $V_{W,sto}$ des Speichers sowie seine Teilvolumen ergeben sich aus der Geometrie dieses konkreten Speichers inkl. Positionen von Rohranschlüssen und Steuerfühlern. Je nach dem Warmwasserversorgungstyp wird das Volumen einer vorgeschalteten Vorwärmzone (und allenfalls Mitteltemperaturzone) dem soeben bestimmten Volumen $V_{W,sto}$ hinzugefügt.

#### 4.2.3 Ermittlung des Wärmeleistungsbedarfs der Wassererwärmungsanlage (in Anlehnung an SN EN 12831-3)

4.2.3.1 Der Zusammenhang zwischen dem Wärmeleistungsbedarf der Wassererwärmungsanlage und der Dauer eines Ladezyklus ist durch Gleichung 11 gegeben:

$$\Phi_{W,gen} \cdot t_z = Q_{W,gen,out,z} \tag{11}$$

| Symbol | Bedeutung |
|---|---|
| $\Phi_{W,gen}$ | Wärmeleistungsbedarf der Wassererwärmungsanlage, in kW |
| $t_z$ | Dauer eines Ladezyklus (Planungswert), in Stunden |
| $Q_{W,gen,out,z}$ | in einem Ladezyklus bereitzustellende Wärmemenge gemäss [[04_Feinplanung\|4.2.2.3]], in kWh |

Die Dauer eines Ladezyklus wird unter Beachtung von 4.2.1.1 und 4.2.1.2 gewählt. Mit Gleichung 11 steht dann der Wärmeleistungsbedarf der Wassererwärmungsanlage fest.

4.2.3.2 Wenn der Wärmeerzeuger ausschliesslich der Trinkwassererwärmung dient und keine Feuerung umfasst, wird der gemäss [[04_Feinplanung|4.2.3.1]] bestimmte Wärmeleistungsbedarf der Wassererwärmungsanlage übernommen.

4.2.3.3 Wenn die Wärmeerzeugung der Wassererwärmung mit derjenigen der Heizung kombiniert ist, wird der Wärmeleistungsbedarf der Wassererwärmungsanlage gemäss SIA 384/1 auf der Basis des Wärmebedarfs der Warmwasserversorgung $Q_{W,gen,out}$ bestimmt. Dabei ergibt sich eventuell eine neue Anzahl der Speicherladezyklen pro Tag $n_z$.

4.2.3.4 Die Berechnungsschritte 4.2.2.3 bis 4.2.3.3 werden ggf. mit Anpassungen bei Ladezyklen und Wärmeerzeugerleistung wiederholt, bis das Resultat unter Berücksichtigung sämtlicher Randbedingungen befriedigt. Ein empfohlenes Hilfsmittel ist dabei das Summenliniendiagramm. Im Anhang F ist das Beispiel einer Bedarfskennlinie zu finden.

4.2.3.5 Bei der dynamischen Leistungsbedarfsberechnung nach SIA 380/2 werden die Werte für $Q_{W,gen,out,z}$ als stündliches Profil übertragen. Bei $t_z > 1$ h wird $Q_{W,gen,out,z}$ auf die erforderliche Anzahl Stunden aufgeteilt, wobei der letzten Stunde des Ladezyklus der allenfalls verbleibende Rest zugeordnet wird. Die Zeiten sind mit zu übertragen.

---

[^8]: Die Dimensionierung erfolgt hier ohne Berücksichtigung einer allfälligen Speicherladung durch Sonnenkollektoren oder Wärmerückgewinnung, da die Bereitstellung des Warmwassers jederzeit, d. h. auch ohne diese Zusatzladungen, sichergestellt werden muss.
[^9]: Elektrizität als Wärmequelle oder Antriebsenergie wird oft zu bestimmten Tageszeiten gesperrt.
[^10]: Das so berechnete Speichervolumen stellt die Verfügbarkeit des Warmwassers auch in Perioden sicher, in denen die Vorwärmung keine Wärmeenergie liefert.

---

> ◀ [[03_Grobauslegung|Kap. 3 Grobauslegung – Vorprojektphase]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[05_Waermebedarf_Hilfsenergie|Kap. 5 Wärmebedarf und Hilfsenergie]] ▶

---
