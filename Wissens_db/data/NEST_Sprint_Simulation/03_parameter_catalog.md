---
tags: [NEST, Sprint, Simulation, Parameter, HVAC]
projekt: "NEST Unit Sprint"
kapitel: "03"
titel: "Parameter Catalog"
---

> ◀ [[02_building_model_overview|← Building Model Overview]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[04_calibration_rules|Calibration Rules →]] ▶

---

# Parameter Catalog



## ventilation\_flow\_offices

* Category: HVAC / Ventilation
* Location: Zone - Ventilation - Supply / Exhaust airflow
* Unit: l/(s\*m²)
* Baseline value: 0.6
* Allowed range: 0.1 – 3.0

### Influence

* affects heat loss in winter
* affects cooling potential in summer
* Priority: medium



## ventilation\_flow\_Technikräume\_Korridor

* Category: HVAC / Ventilation
* Location: Zone - Ventilation - Supply / Exhaust airflow
* Unit: l/(s\*m²)
* Baseline value: 2.0
* Allowed range: 0.1 – 3.0

### Influence

* affects heat loss in winter
* affects cooling potential in summer
* Priority: medium



## ventilation\_schedule

* Category: HVAC / Schedule
* Location: Ventilation control
* Unit: schedule
* Baseline value: schedule\_ventilation\_fans

### Influence

* defines when air exchange occurs
* affects heat loss and cooling potential

### Key effect in this model

* no ventilation during night
* no ventilation during weekends
* Priority: medium



## heat\_recovery\_efficiency

* Category: HVAC / Ventilation
* Location: Ventilation system - Heat exchanger
* Unit: schedule
* Baseline value: schedule\_heat\_recovery

### Influence

* reduces ventilation heat losses in winter
* affects supply air temperature
* impacts heating demand
* Priority: medium



## heating\_availability

* Category: HVAC / Control
* Location: Heating system - Availability schedule
* Unit: schedule
* Baseline value: schedule\_heating\_availability

### Influence

* determines when heating is allowed to operate
* prevents heating during summer

### Key effect in this model

* no heating during summer
* avoids simultaneous heating and cooling
* Priority: high



## heating\_setpoint\_offices

* Category: HVAC / Control
* Location: Zone - Setpoints
* Unit: °C
* Baseline value: schedule\_temperature\_control, Heating Setpoint

### Influence

* directly affects indoor temperature in heating periods
* determines minimum comfort temperature
* Priority: high



## cooling\_availability

* Category: HVAC / Control
* Location: Cooling system - Availability schedule
* Unit: schedule
* Baseline value: schedule\_cooling\_availability

### Influence

* determines when cooling is allowed to operate
* prevents cooling during winter

### Key effect in this model

* no cooling during winter
* avoids unrealistic winter cooling
* Priority: high



## cooling\_setpoint\_offices

* Category: HVAC / Control
* Location: Zone - Setpoints
* Unit: °C
* Baseline value: schedule\_temperature\_control, Cooling Setpoint

### Influence

* determines maximum indoor temperature
* defines cooling activation threshold
* Priority: high



## cooling\_capacity\_offices

* Category: HVAC / System
* Location: Zone - Cooling system
* Unit: W
* Baseline value: 500
* Allowed range: 100-1200

### Influence

* limits cooling performance
* affects peak temperature reduction
* Priority: high



## heating\_capacity\_offices

* Category: HVAC / System
* Location: Zone - Heating system
* Unit: W
* Baseline value: 500
* Allowed range: 100-1200

### Influence

* limits heating performance
* affects ability to maintain setpoint
* Priority: high



## occupancy\_schedule

* Category: Internal Loads
* Location: Zone - People
* Unit: schedule
* Baseline value: schedule\_office

### Influence

* affects internal heat gains
* Priority: medium



## lighting\_load

* Category: Internal Loads
* Location: Zone - Lighting
* Unit: schedule
* Baseline value: schedule\_office

### Influence

* contributes to internal heat gains
* Priority: medium



## equipment\_load

* Category: Internal Loads
* Location: Zone - Equipment
* Unit: schedule
* Baseline value: schedule\_office

### Influence

* contributes to internal heat gains
* Priority: medium



## shading\_threshold

* Category: Solar / Facade
* Location: Window - Shading control
* Unit: W/m²
* Baseline value: 200
* Allowed range: 100-600

### Influence

* Determines at which solar radiation level shading is activated
* lower threshold → earlier shading activation → reduced solar gains
* higher threshold → delayed shading → increased solar gains
* Priority: high



## shading\_schedule

* Category: Solar / Control
* Location: Window - Shading schedule
* Unit: schedule
* Baseline value: schedule\_shading (not activated)

### Influence

* defines when shading is allowed to activate
* restricts shading to specific time windows
* can prevent shading even if solar radiation is high

### Key effect in this model

* shading\_schedule is not activated
* Priority: high



## window\_opening\_schedule

* Category: Airflow / User Behavior
* Location: Window opening control
* Unit: schedule
* Baseline value: closed

### Influence

* affects natural ventilation
* affects indoor temperature
* can reduce overheating during summer

### Key effect in this model

* windows remain closed in the baseline model
* Priority: high


---

> ◀ [[02_building_model_overview|← Building Model Overview]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[04_calibration_rules|Calibration Rules →]] ▶
