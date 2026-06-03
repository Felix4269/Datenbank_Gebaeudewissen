---
tags: [NEST, Sprint, Simulation, Baseline, Modell]
projekt: "NEST Unit Sprint"
kapitel: "08"
titel: "Baseline Model"
---

> ◀ [[07_ai_output_schema|← AI Output Schema]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[09_schedules|Schedules →]] ▶

---

# Baseline Model (Best Current Configuration)

## Description

This file defines the structural setup of the baseline model.
All parameter values and schedules are defined in:

* [[03_parameter_catalog|Parameter Catalog]]
* [[09_schedules|Schedules]]

This file only describes the model structure and system configuration.


## General Model Information

* Project: NEST Unit Sprint
* Focus: 1st floor
* Simulation tool: IDA ICE 5.1.1


## Zones

### Offices

* Office 171 – 176
* Office 181 – 186

### Other zones

* Technical room 170
* Technical room 180
* Corridor 177
* Corridor 187

Total zones: 16


## Zone Geometry

### Office zones

- Typical room height: 3.21 m
- Typical floor area range: approx. 8.11 – 13.13 m²

Selected zones:
* Büro 185: 9.212 m², 3.21 m
* Büro 176: 12.88 m², 3.21 m
* Büro 172: 9.212 m², 3.21 m

### Other zones

* Technikraum 180: 10.61 m², 3.21 m
* Technikraum 170: 10.07 m², 3.21 m
* Gang 187: 19.44 m², 3.21 m
* Gang 177: 19.36 m², 3.21 m

### Total

* Total conditioned floor area: 172.9 m²
* Total zone volume: approx. 555 m³


## HVAC System

### Ventilation

* Central ventilation unit: Lüftungsgerät
* Connected zones: all zones
* Total supply airflow: 187 L/s
* Total exhaust airflow: 187 L/s

### Office Zones

* System type: KVS (active chilled ceiling system)
* Local heating/cooling elements (ceiling system)

### Technical Rooms & Corridors

* Ideal heating elements
* No active cooling


## Internal Loads

* Applied via schedule: "schedule_office"
* Includes:

  * occupancy
  * lighting
  * equipment


## HVAC Control

* Ventilation, heating and cooling operation controlled via schedules
* See [[09_schedules]]:

  * `schedule_ventilation_fans`
  * `schedule_heating_availability`
  * `schedule_cooling_availability`


## Solar & Shading

* Shading controlled by (→ [[03_parameter_catalog]]):

  * `schedule_shading`
  * `shading_threshold`

## Windows

* Windows remain closed in the baseline configuration
* No natural ventilation considered

## Parameter Reference

All adjustable model parameters are defined in:

* [[03_parameter_catalog]]


## Schedule Reference

All time-dependent behavior is defined in:

* [[09_schedules]]



## Current Model Characteristics

* Office-based internal loads
* Time-dependent ventilation
* Seasonal heating and cooling availability
* Radiation-based shading with schedule restriction
* Multi-zone thermal interaction


## Notes

* It serves as structural reference for the model



---

> ◀ [[07_ai_output_schema|← AI Output Schema]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[09_schedules|Schedules →]] ▶
