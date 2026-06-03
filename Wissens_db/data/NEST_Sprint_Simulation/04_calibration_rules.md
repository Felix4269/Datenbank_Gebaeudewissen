---
tags: [NEST, Sprint, Simulation, Kalibrierung, Regeln]
projekt: "NEST Unit Sprint"
kapitel: "04"
titel: "Calibration Rules"
---

> ◀ [[03_parameter_catalog|← Parameter Catalog]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[05_calibration_history|Calibration History →]] ▶

---

# Calibration Rules

## General Strategy

* Change only a small number of parameters at once
* Prefer physically explainable changes
* Avoid unrealistic parameter values
* Evaluate both temperature behavior and energy demand
* Do not optimize only one room while strongly worsening others

# Calibration Order

Recommended calibration sequence:

1. Schedules
2. Internal loads
3. Ventilation behavior
4. Heating and cooling control
5. System capacities
6. Solar and shading behavior
7. Advanced parameters

# Temperature Evaluation

The following metrics must always be evaluated:

* MAE
* MBE
* RMSE

Evaluation periods:

* Winter
* Summer
* Transition periods

Additional checks:

* weekday vs weekend behavior
* daily temperature peaks
* seasonal consistency

# Energy Evaluation

Temperature improvement alone is not sufficient.

Each proposal should additionally evaluate:

* Heating energy
* Cooling energy
* Ventilation energy

Avoid:

* unrealistic 24h operation
* strongly increased HVAC energy
* unrealistic seasonal behavior

# Heating Calibration

If winter temperatures are too low:

Check first:

* heating schedules
* ventilation schedules
* heating availability
* shading behavior
* internal gains

before increasing heating capacity.

Heating capacity should not be used as the main fitting parameter.

# Cooling Calibration

If summer temperatures are too high:

Check first:

* shading schedule
* shading threshold
* solar gains

before increasing cooling capacity.

Cooling capacity alone often does not solve overheating problems.

# Ventilation Calibration

Ventilation strongly affects:

* HVAC energy
* heat losses
* cooling potential

Continuous ventilation should only be used if physically justified.

Ventilation should not be used as the primary temperature correction parameter.


# Shading Calibration

Shading is one of the strongest summer calibration parameters.

Important considerations:

* shading timing
* shading threshold
* seasonal activation

Too much shading may:

* reduce useful solar gains
* increase heating demand
* create unrealistic cooling behavior


# Occupancy and Internal Loads

Internal loads strongly influence:

* summer overheating
* transition periods

Additional occupancy should only be introduced if operational behavior supports it.

Avoid unrealistic occupancy schedules.


# Seasonal Logic

## Winter

Prioritize:

* stable heating behavior
* realistic heat losses
* reduction of strong negative MBE values

## Summer

Prioritize:

* reduction of overheating
* realistic shading behavior
* low cooling demand

## Transition Periods

Prioritize:

* stable control behavior
* avoidance of simultaneous heating and cooling
* balanced seasonal schedules


# Documentation Rules

Every calibration run should document:

* changed parameter
* baseline value
* tested value or schedule
* seasonal results
* energy impact
* important observations

# AI Proposal Rules

AI-generated proposals should:

* remain within parameter ranges
* consider seasonal behavior
* consider HVAC energy impact
* avoid unrealistic operational strategies
* prioritize physically plausible solutions
---

> ◀ [[03_parameter_catalog|← Parameter Catalog]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[05_calibration_history|Calibration History →]] ▶
