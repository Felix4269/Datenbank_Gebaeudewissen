---
tags: [NEST, Sprint, Simulation, Kalibrierung, MOC]
projekt: NEST Unit Sprint
version: "2025"
---

# NEST Sprint – IDA ICE Kalibrierungsstudie (MOC)

Kalibrierungsstudie einer Büroetage im NEST-Gebäude (Empa Dübendorf)  
Simuliert mit IDA ICE 5.1.1 | Messjahr 2022 | Wetter: MeteoSchweiz Zürich Fluntern

---

## Dokumente

| Datei | Inhalt |
|---|---|
| [[01_project_goal\|Projektziel]] | Ziel, Kalibrierungsphilosophie, Vorgehensweise |
| [[02_building_model_overview\|Gebäudemodell]] | Zonen, HVAC, Wetterdaten, Messdaten |
| [[03_parameter_catalog\|Parameterkatalog]] | 16 Simulationsparameter mit Basiswerten und Einfluss |
| [[04_calibration_rules\|Kalibrierungsregeln]] | Strategie, Reihenfolge, saisonale Logik |
| [[05_calibration_history\|Kalibrierungshistorie]] | Run 001–010 für Büro 172, 176, 185 (MAE, MBE, RMSE, Energie) |
| [[07_ai_output_schema\|AI-Output-Schema]] | Format für KI-generierte Kalibrierungsvorschläge |
| [[08_baseline_model\|Baseline-Modell]] | Modellstruktur, Zonen, HLK-System |
| [[09_schedules\|Zeitpläne]] | 7 Steuerungszeitpläne (Belegung, Lüftung, Heizung, Kühlung, Verschattung) |
| [[10_calibration_insights\|Kalibrierungserkenntnisse]] | Parametersensitivität, Empfehlungen, beste Kalibrierrichtung |
| [[11_measured_energy_reference\|Gemessene Energiereferenz]] | Gemessene Heiz-, Kühl- und Lüftungsenergie 2022 (Belimo) |

---

## Fokuszonen

* [[05_calibration_history|Büro 172]] – 9,212 m²
* [[05_calibration_history|Büro 176]] – 12,88 m²
* [[05_calibration_history|Büro 185]] – 9,212 m²

## Bewertungsperioden

* **Winter**: Dezember – Februar
* **Sommer**: Juni – August
* **Übergang**: März – Mai, September – November

## Metriken

* MAE – Mean Absolute Error
* MBE – Mean Bias Error
* RMSE – Root Mean Square Error

## Getestete Parameter (Run 001–010)

| Run | Parameter | Kategorie |
|---|---|---|
| 001 | ventilation_flow_offices | Lüftung |
| 002 | cooling_capacity_offices | Kühlung |
| 003 | heating_capacity_offices | Heizung |
| 004 | heating_availability | Steuerung |
| 005 | cooling_availability | Steuerung |
| 006 | ventilation_schedule | Zeitplan |
| 007 | shading_schedule | Verschattung |
| 008 | shading_threshold | Verschattung |
| 009 | occupancy_schedule | Interne Lasten |
| 010 | window_opening_schedule | Natürliche Lüftung |

## Gemessene Energiereferenz (2022)

| Energietyp | Gemessen |
|---|---|
| Heizenergie | 9 632 kWh/a |
| Kühlenergie | 2 850 kWh/a |
| Lüftungsenergie | 2 119 kWh/a |

---

## Verwandte Themen

| Thema | Link |
|---|---|
| Software-Referenz IDA ICE | [[_IDAICE_Manual_MOC\|IDA ICE Manual v4.8]] |
| IDA ICE Modell aufbauen & kalibrieren | [[01_2d_Kalibrieren\|IDA ICE Tutorial – Modell kalibrieren]] |
| Theorie: Interne Wärmegewinne (Belegung) | [[03_1_interne_waermegewinne\|Skript Energie Kap. 3.1 – Interne Wärmegewinne]] |

---

*Zurück zum Hauptindex: [[00_Wissensbank_Index]]*
