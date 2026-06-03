---
tags: [NEST, Sprint, Simulation, KI, Schema]
projekt: "NEST Unit Sprint"
kapitel: "07"
titel: "AI Output Schema"
---

> ◀ [[05_calibration_history|← Calibration History]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[08_baseline_model|Baseline Model →]] ▶

---

# AI Output Schema

## Objective

Define a structured format for AI-generated calibration proposals.

The AI should generate physically plausible parameter improvement suggestions based on:

* [[05_calibration_history|calibration history]]
* [[10_calibration_insights|calibration insights]]
* [[03_parameter_catalog|parameter catalog]]
* [[09_schedules|schedules]]
* [[11_measured_energy_reference|measured energy reference]]
* [[08_baseline_model|baseline model]]

# General Rules

* Only propose 1–3 parameter changes at once
* Keep all values inside allowed parameter ranges
* Avoid unrealistic operational behavior
* Consider both temperature agreement and energy demand
* Avoid excessive HVAC operation
* Prefer stable improvements across multiple rooms

# Seasonal Focus

## Winter

Prioritize:

* reduction of underheating
* improved heating stability
* reduction of strong negative MBE
* realistic heating demand

## Summer

Prioritize:

* reduction of overheating
* realistic shading behavior
* low cooling demand
* stable peak temperatures

## Transition Periods

Prioritize:

* stable schedules
* smooth seasonal switching
* balanced heating/cooling behavior

# Energy Constraints

AI proposals should prefer:

* lower cooling demand
* lower ventilation energy
* stable heating demand
* realistic HVAC schedules

Avoid:

* permanent 24h operation
* excessive cooling compensation
* unrealistic seasonal shutdowns

# Output Format

```yaml
proposal_id: proposal_001
...
```

goal:
  primary: improve summer temperature agreement
  secondary: reduce cooling demand

target_rooms:
  - Office 172
  - Office 176
  - Office 185

target_periods:
  - Summer

current_problem:
  description: >
    Summer overheating remains visible during afternoon hours.

proposed_changes:

  - parameter: shading_threshold

    scope: all_offices

    old_value: 200
    new_value: 300

    unit: W/m²

    rationale: >
      Later shading activation may improve balance between solar gains and overheating protection.

    expected_temperature_effect: >
      Reduced summer overheating and improved MAE/RMSE.

    expected_energy_effect: >
      Possible increase in cooling demand but reduced over-shading.

    risks: >
      Some rooms may still overheat during peak solar periods.

priority: high

validation_plan:

  - Run new simulation
  - Compare MAE, MBE and RMSE
  - Compare heating, cooling and ventilation energy
  - Compare all focus rooms
  - Check seasonal consistency

# Proposal Priorities

## High Priority Parameters

* shading_schedule
* shading_threshold
* heating_capacity_offices
* cooling_capacity_offices
* ventilation_schedule

## Medium Priority Parameters

* heating_availability
* cooling_availability
* occupancy_schedule
* ventilation_flow_offices

## Lower Priority Parameters

* secondary fine-tuning parameters

# Notes

* AI proposals do not directly modify the IDA ICE model.
* The user remains responsible for evaluating all changes.
* Proposals should focus on physically plausible calibration improvements.
---

> ◀ [[05_calibration_history|← Calibration History]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[08_baseline_model|Baseline Model →]] ▶
