---
tags: [Norm, Trinkwarmwasser, Sanitär, SIA385-2, Gebäudetechnik, Warmwasser]
normnummer: SN 546385/2:2025
gueltig_ab: "2025-02-01"
kapitel: "Anhang E"
titel: "Ausstosswärmeverluste"
anhang: normativ
---
> ◀ [[Anhang_D_Warmgehaltene_Leitungen|Anhang D]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_F_Stundenbedarfsverteilung|Anhang F]] ▶

---

# Anhang E (normativ) – Ausstosswärmeverluste $Q_{W,em,ls}$

---

E.1 Die Wärmeverluste der Ausstossleitungen einer Warmwasserversorgung werden bei der Feinplanung als Summe der Ausstosswärmeverluste in jeder Nutzungseinheit berechnet. Die dazu benötigten Daten werden der [[#Tabelle 4|Tabelle 4]] entnommen.

$$Q_{W,em,ls} = \sum_i n_{em,i} \cdot Q_{W,em,ls,ind,i} \tag{23}$$

| Symbol | Bedeutung |
|---|---|
| $Q_{W,em,ls}$ | Ausstosswärmeverluste der Warmwasserversorgung, in kWh/d |
| $n_{em,i}$ | Anzahl der Warmwasserentnahmen pro Tag in der Nutzungseinheit $i$ |
| $Q_{W,em,ls,ind,i}$ | Ausstosswärmeverluste einer einzelnen Entnahme in der Nutzungseinheit $i$, in kWh |

E.2 Bei der Anwendung der Tabelle 4 bezieht sich die Personenzahl bzw. Mahlzeiten- oder Bettenzahl immer auf eine Gruppe von Räumen gleicher Nutzung, die einer bestimmten Warmwasserversorgung zugeordnet sind. Sie muss keine ganze Zahl sein.

E.3 In Tabelle 4 gelten die angegebenen Wärmeverluste für Ausstossleitungen aus Kunststoff, welche die maximale Ausstosszeit $t_{em}$ gemäss SIA 385/1 aufweisen. Dabei unterscheidet man zwischen Warmwasserversorgungen mit ($t_{em}$ = 10 s) oder ohne ($t_{em}$ = 15 s) warmgehaltene Leitungen.

E.4 Ist die Ausstosszeit einer Leitung grösser als die maximale Ausstosszeit gemäss SIA 385/1, werden ihre Wärmeverluste $Q_{W,em,ls,ind,i}$ entsprechend proportional erhöht.

E.5 Ist die Ausstosszeit einer Leitung kleiner als die maximale Ausstosszeit gemäss SIA 385/1, können ihre Wärmeverluste $Q_{W,em,ls,ind,i}$ entsprechend proportional reduziert werden.

E.6 Erläuterungen zur Ausstosszeit und zu den Ausstosswärmeverlusten finden sich in [[Anhang_H_Erlaeuterungen_Ausstosszeit|Anhang H]].

---

##### Tabelle 4 – Anzahl der Warmwasserentnahmen pro Tag $n_{em,i}$ in der Nutzungseinheit $i$ und Ausstosswärmeverluste $Q_{W,em,ls,ind,i}$ einer einzelnen Entnahme in der Nutzungseinheit $i$, für Kunststoffleitungen, bei der Standardnutzung

| Nutzungseinheit $i$ | Beispiele | Entnahmen/Tag $n_{em,i}$ | $Q_{W,em,ls,ind,i}$ bei $t_{em}$ = 10 s (mit WHL) [kWh] | $Q_{W,em,ls,ind,i}$ bei $t_{em}$ = 15 s (ohne WHL) [kWh] |
|---|---|:---:|:---:|:---:|
| Wohneinheit mit $n_{P,i}$ Personen | | $2 + 5\,n_{P,i}$ | 0,10 | 0,14 |
| Verwaltungseinheit mit $n_{P,i}$ Personen | Büros, Schalterhalle, Arztpraxis, Bibliothek, Ateliers, Ausstellungsräumlichkeiten, Kulturzentrum, Rechenzentrum, Fernmelderaum, Fernsehraum, Filmstudio | $2\,n_{P,i}$ | 0,05 | 0,08 |
| Schuleinheit mit $n_{P,i}$ Personen | Schulräume, Kindergärten und -horte, Ausbildungsräume, Kongresszentren, Labors, Forschungsinstitut, Gemeinschaftsräume, Freizeitanlagen | $1{,}5\,n_{P,i}$ | 0,05 | 0,08 |
| Verkaufseinheit mit $n_{P,i}$ Mitarbeitenden | Verkaufsräume aller Art inkl. Einkaufszentren, Messegebäude | $2\,n_{P,i}$ | 0,10 | 0,14 |
| Restauranteinheit bei $n_{M,i}$ servierten Mahlzeiten pro Tag | Restaurants (inkl. Küchen), Cafeterias, Kantinen, Dancings, Diskotheken | $n_{M,i}$ | 0,10 | 0,14 |
| Versammlungslokaleinheit mit $n_{P,i}$ Besuchern | Theater, Konzertsäle, Kinos, Kirchen, Abdankungshallen, Aulas, Sporthallen mit viel Publikum | $0{,}5\,n_{P,i}$ | 0,05 | 0,08 |
| Spital / Hotel mit $n_{B,i}$ Betten | Spitäler, psychiatrische Kliniken, Krankenheime, Altersheime, Rehabilitationszentren, Behandlungsräume, Hotels (nur Beherbergung) | $3\,n_{B,i}$ | 0,10 | 0,14 |
| Industrieraumeinheit mit $n_{P,i}$ Mitarbeitenden | Fabrikationsräume, Gewerberäume, Werkstätten, Servicestationen, Werkhöfe, Bahnhöfe, Feuerwehrgebäude | $2\,n_{P,i}$ | 0,10 | 0,14 |
| Lagereinheit mit $n_{P,i}$ Mitarbeitenden | Lagerhallen, Verteilzentren | $2\,n_{P,i}$ | 0,05 | 0,08 |
| Sportanlage mit $n_{P,i}$ Besuchern | Turn- und Sporthallen, Gymnastikräume, Tennishallen, Kegelbahnen, Fitnesszentren, Sportgarderoben | $2\,n_{P,i}$ | 0,10 | 0,14 |
| Hallenbad mit $n_{P,i}$ Besuchern | Hallenbäder, Lehrschwimmbecken, Saunagebäude, Heilbäder | $2\,n_{P,i}$ | 0,10 | 0,14 |

$n_{P,i}$: Anzahl Personen für die Nutzung $i$  
$n_{M,i}$, $n_{B,i}$: Anzahl Bezugseinheiten für die Nutzung $i$

---

> ◀ [[Anhang_D_Warmgehaltene_Leitungen|Anhang D]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_F_Stundenbedarfsverteilung|Anhang F]] ▶

---
