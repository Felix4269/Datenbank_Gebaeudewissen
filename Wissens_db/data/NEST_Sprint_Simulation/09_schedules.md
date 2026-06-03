---
tags: [NEST, Sprint, Simulation, Zeitpläne, HVAC]
projekt: "NEST Unit Sprint"
kapitel: "09"
titel: "Schedules"
---

> ◀ [[08_baseline_model|← Baseline Model]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[10_calibration_insights|Calibration Insights →]] ▶

---

# Schedules

## Objective

This file contains all relevant schedules used in the IDA ICE model.
Schedules define temporal behavior of loads and systems and are referenced in the parameter catalog.



## schedule_office

* Name in IDA ICE: 08-17 wochentags1 (Sprint)

### Weekdays

* 08:00 – 12:00 → 1
* 12:00 – 13:00 → 0
* 13:00 – 17:00 → 1
* Rest of day → 0

### Weekend & Holidays

* Saturday → 0
* Sunday → 0
* Holidays → 0

### Applied to

* Occupancy
* Lighting
* Equipment

### Interpretation

* Typical office usage pattern
* No internal gains during weekends
* Midday break reduces internal gains



## schedule_ventilation_fans

* Name in IDA ICE: 06-18 wochentags

### Weekdays

* 06:00 – 18:00 → 1
* Rest of day → 0

### Weekend

* Off

### Applied to

* Ventilation fans

### Interpretation

* Ventilation active only during daytime
* No mechanical ventilation during night or weekends



## schedule_heat_recovery

* Name in IDA ICE: (implicit / always active)

### Behavior

* 24h active
* No schedule limitation

### Applied to

* Heat exchanger

### Interpretation

* Constant heat recovery
* Reduces heat losses in winter



## schedule_heating_availability

* Name in IDA ICE: HeizungSommer_inaktiv

### Behavior

* 1 June – 31 August → 0 (inactive)
* Rest of year → 1 (active)

### Applied to

* Heating system

### Interpretation

* Heating disabled in summer
* Prevents heating during warm months



## schedule_cooling_availability

* Name in IDA ICE: KühlungSommer_aktiv

### Behavior

* 1 October – 1 April → 0 (inactive)
* Rest of year → 1 (active)

### Applied to

* Cooling system

### Interpretation

* Cooling disabled in winter
* Active only in warmer periods



## schedule_shading

* Name in IDA ICE: Verschattung_Test2

### Baseline behavior

* Shading control in IDA ICE combines:
  * schedule activation
  * solar radiation threshold

* In the baseline configuration, no additional time-based shading restriction is active.
* Shading is therefore controlled primarily by the solar radiation threshold.

### Additional Condition

* Solar radiation >= 200 W/m²

### Applied to

* Window shading (lamellae)

### Control Logic

* Shading activates only if:

  * schedule = 1
    AND
  * solar radiation exceeds 200 W/m²

### Interpretation

* Solar radiation is the primary shading trigger in the baseline model
* Additional schedule restrictions can be introduced during calibration runs
* Different shading schedules may significantly affect summer overheating behavior



## schedule_temperature_control (implicit)

### Heating Setpoint

* Default: 21 °C
* 1 July – 31 August: 15 °C

### Cooling Setpoint

* June: 25 °C
* Rest of year: 24 °C

### Interpretation

* Seasonal adjustment of setpoints
* Heating effectively disabled in summer via low setpoint
* Cooling behavior varies slightly in June



## schedule_window_opening

* Name in IDA ICE: TBD

### Behavior

* Windows closed all year

### Applied to

* Window opening control

### Interpretation

* No natural ventilation
* Air exchange only via mechanical ventilation




## Notes

* Only schedules referenced in this file are considered part of the baseline configuration
* All schedules are linked to parameters defined in the [[03_parameter_catalog|parameter catalog]]




---

> ◀ [[08_baseline_model|← Baseline Model]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[10_calibration_insights|Calibration Insights →]] ▶
