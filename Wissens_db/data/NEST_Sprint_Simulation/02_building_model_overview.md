---
tags: [NEST, Sprint, Simulation, Gebäudemodell, HVAC]
projekt: "NEST Unit Sprint"
kapitel: "02"
titel: "Building Model Overview"
---

> ◀ [[01_project_goal|← Project Goal]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[03_parameter_catalog|Parameter Catalog →]] ▶

---

# Building Model Overview

## Building

* Name: NEST
* Unit: Sprint
* Floor: 1st floor
* Location: Switzerland (Empa Dübendorf)

## Simulation Tool

* Software: IDA ICE 5.1.1 

## Focus Zones

* Office 172
* Office 176
* Office 185

Additional zones:

* Corridor zones
* Technical rooms

## HVAC System

### Offices

* Heating and cooling via active ceiling system
* Temperature setpoints


### Ventilation

* Mechanical ventilation system
* Supply and exhaust air
* Heat recovery system

### Other zones

* Corridors and technical rooms:

  * Ideal heaters
  * No active cooling

## Weather Data

* Source: MeteoSwiss
* Station: Zurich Fluntern (SMA)
* Year: 2022
* Format: EPW (converted for IDA ICE)

## Measured Data

### Temperature

* Room air temperature from sensors in offices
* Data resolution: typically hourly (aggregated)

### Energy

* Thermal energy and power from building system
* Measured via energy valve (Belimo)

## Simulation Outputs

Main outputs used for comparison:

* Room air temperature (hourly)
* Heating energy
* Cooling energy
* Ventilation energy

## Comparison Approach

* Time resolution: hourly


## Notes

* Focus is on matching measured room temperatures for 2022
* Special attention to:

  * weekend behavior
  * weekday heating patterns
  * midday temperature peaks
  * seasonal differences

---

> ◀ [[01_project_goal|← Project Goal]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[03_parameter_catalog|Parameter Catalog →]] ▶
