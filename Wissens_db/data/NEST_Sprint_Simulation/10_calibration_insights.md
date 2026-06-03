---
tags: [NEST, Sprint, Simulation, Kalibrierung, Erkenntnisse]
projekt: "NEST Unit Sprint"
kapitel: "10"
titel: "Calibration Insights"
---

> ◀ [[09_schedules|← Schedules]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[11_measured_energy_reference|Measured Energy Reference →]] ▶

---

# Calibration Insights

## Objective

This file summarizes the main insights from the completed parameter tests.  
It does not replace the detailed calibration history. Instead, it condenses the most important findings into practical calibration knowledge for future model improvements and AI-supported parameter suggestions.

The detailed numerical results are stored in [[05_calibration_history]].
This file focuses on:

* parameter sensitivity
* seasonal effects
* room-specific differences
* useful and problematic parameter changes
* recommended next calibration direction

## Evaluation Basis

The calibration was evaluated using temperature comparison between simulation and measured data for the three focus rooms:

* Office 172
* Office 176
* Office 185

The evaluation periods were:

* Winter: December – February
* Summer: June – August
* Transition: March – May and September – November

The main temperature metrics were:

* MAE: average absolute deviation
* MBE: systematic bias between simulation and measurement
* RMSE: stronger weighting of larger deviations and peaks

In addition, simulated annual HVAC energy values were added as a second evaluation layer.

## Overall Model Behavior

### General temperature tendency

The baseline model generally tends to underestimate measured temperatures in many periods, especially in winter and transition periods. This is visible through mostly negative MBE values.

### Room-specific behavior

The three focus rooms do not react identically to parameter changes. Some parameters improve one room while worsening another. This means that a single global parameter change may not always improve the complete model.

### Seasonal behavior

Different seasons are controlled by different dominant effects:

* Winter is mainly influenced by heating capacity, heating control, ventilation, and heat losses.
* Summer is mainly influenced by solar gains, shading behavior, cooling capacity, and internal loads.
* Transition periods are the most difficult because heating, cooling, solar gains, and schedules can all interact.

## Sensitivity Ranking

### Very high sensitivity

1. heating_capacity_offices
2. shading_schedule
3. shading_threshold
4. occupancy_schedule

### Medium sensitivity

5. cooling_capacity_offices
6. ventilation_schedule
7. heating_availability

### Low to moderate sensitivity

8. ventilation_flow_offices
9. cooling_availability

## Parameter Insights

## heating_capacity_offices

### Main insight

Heating capacity is one of the most critical parameters in winter.

### Observed behavior

Reducing the office heating capacity to 100 W caused very large winter errors in all focus rooms. This indicates that the model becomes unable to maintain realistic indoor temperatures when heating capacity is too low.

Increasing the heating capacity to 1200 W did not consistently improve the model. In some cases, it reduced the negative bias, but in others it led to overcompensation or higher errors.

### Interpretation

Heating capacity should not be used as a free fitting parameter. Too low values create unrealistic winter behavior. Too high values may mask other problems such as wrong schedules, internal gains, or boundary conditions.

### Calibration recommendation

* Keep 500 W as a physically reasonable baseline unless strong evidence suggests otherwise.
* Do not reduce heating capacity strongly.
* If winter temperatures remain too low, check schedules, setpoints, ventilation, and boundary assumptions before increasing capacity.

## cooling_capacity_offices

### Main insight

Cooling capacity mainly affects summer behavior.

### Observed behavior

Reducing cooling capacity to 100 W worsened summer behavior, especially in rooms with stronger solar influence. In Office 185, the low cooling capacity produced a strong positive summer bias, meaning the simulation became too warm.

Increasing cooling capacity to 1200 W did not produce a clear improvement in all rooms. The baseline value of 500 W often remained competitive.

### Interpretation

The cooling system is important for limiting summer peaks, but increasing capacity alone does not automatically improve the match. Solar gains and shading behavior appear to be more important calibration levers for summer.

### Calibration recommendation

* Do not reduce cooling capacity too much.
* Keep 500 W as baseline unless overheating remains clearly capacity-driven.
* Prioritize shading behavior before increasing cooling capacity.

## ventilation_flow_offices

### Main insight

Changing office ventilation flow has only a limited temperature effect compared with other parameters.

### Observed behavior

The temperature metrics changed only moderately when the office ventilation flow was varied between low and high values. Effects were room- and season-dependent, but no clear strong improvement was visible across all rooms.

### Interpretation

Ventilation flow is not the dominant parameter for temperature calibration in the current model. However, it still affects ventilation energy and heat exchange.

### Calibration recommendation

* Do not use ventilation flow as the first parameter for temperature calibration.
* Avoid unrealistic ventilation rates only to improve temperature fit.

## ventilation_schedule

### Main insight

Ventilation schedule has a moderate effect on temperature but a strong effect on ventilation-related energy.

### Observed behavior

Extending ventilation operation or running ventilation continuously improved some winter bias values, especially in rooms where the model was too cold. However, it often worsened summer behavior and increased ventilation-related energy significantly.

### Interpretation

Ventilation schedule is not only a temperature parameter. It strongly affects energy and should be evaluated together with HVAC operation.

### Calibration recommendation

* Do not select a ventilation schedule based only on temperature metrics.
* Continuous ventilation should only be used if supported by real operation data.


## heating_availability

### Main insight

Heating availability has little effect in winter but can influence summer and transition periods.

### Observed behavior

Making heating available all year slightly improved summer values in some rooms. Extending the summer heating shutdown to May–September strongly worsened the transition period.

### Interpretation

The model still needs heating availability during parts of the transition season. Removing heating too early or enabling shutdown too long leads to underheating in transition months.

### Calibration recommendation

* Keep the baseline heating availability unless real operation indicates otherwise.
* Do not extend the heating shutdown into May or September without evidence.
* Heating availability should be treated as a seasonal control parameter, not as a general tuning parameter.


## cooling_availability

### Main insight

Cooling availability has a relatively small effect compared with shading and cooling capacity.

### Observed behavior

Making cooling always available caused only small changes in most periods. Extending the cooling period did not consistently improve the transition period and sometimes worsened it.

### Interpretation

Cooling availability is not currently the main reason for the remaining mismatch. The cooling setpoint, shading, and solar gains are likely more relevant.

### Calibration recommendation

* Keep baseline cooling availability unless measured operation proves a different cooling season.
* Do not prioritize cooling availability for early calibration.

## shading_schedule

### Main insight

Shading schedule is one of the strongest summer parameters, but its effect is highly room-specific.

### Observed behavior

Activating or modifying shading schedules strongly changed summer accuracy. Office 172 and Office 176 generally improved with shading scenarios. Office 185 reacted differently, with some shading scenarios worsening transition behavior.

### Interpretation

Solar gains are a major driver of summer temperature behavior. However, because rooms have different orientations and solar exposure, a single global shading schedule may not be ideal for all rooms.

### Calibration recommendation

* Treat shading as a high-priority summer calibration parameter.
* Do not assume one shading strategy fits all rooms equally well.
* Consider orientation-specific shading logic if IDA ICE model setup allows it.
* Compare shading improvements against cooling energy demand.

## shading_threshold

### Main insight

The solar radiation threshold strongly affects summer and transition behavior.

### Observed behavior

A lower threshold of 100 W/m² often led to too much shading and worsened the temperature match. A higher threshold of 300 W/m² often improved summer or transition values in several rooms, although the effect remained room-dependent.

### Interpretation

Too early shading can remove useful solar gains and make the simulation too cold. Too late shading can increase overheating. The threshold must therefore balance overheating protection and useful solar gains.

### Calibration recommendation

* Avoid very low shading thresholds unless real shading behavior confirms early activation.
* The tested 300 W/m² threshold appears promising and should be considered for further evaluation.
* Shading threshold should be evaluated together with shading schedule and solar orientation.

## occupancy_schedule

### Main insight

Occupancy schedule has a strong effect on summer and transition periods and can easily worsen the model.

### Observed behavior

Removing the lunch break, extending working hours, or adding weekend occupancy often increased errors, especially in summer and transition periods. Weekend activity sometimes improved winter values slightly in one room but worsened summer and transition behavior.

### Interpretation

Adding internal gains does not automatically improve the model. In the current setup, additional occupancy-related gains often make the model too warm or increase seasonal mismatch.

### Calibration recommendation

* Do not use occupancy schedule as a pure temperature-fitting parameter.

## heat_recovery_efficiency

### Main insight

Heat recovery is active continuously in the baseline model and mainly influences winter heat losses and supply air temperature.

### Interpretation

Because heat recovery affects the thermal effect of ventilation, it should not be changed without checking the ventilation system assumptions. It is a relevant parameter, but it was not the primary sensitivity focus in the completed tests.

### Calibration recommendation

* Keep as baseline unless measured ventilation/supply air data indicates otherwise.
* If ventilation behavior is analyzed deeper, heat recovery should be included.

## Cross-Parameter Insights

### 1. Temperature accuracy alone is not sufficient

Some scenarios improve temperature metrics but may increase energy demand or create unrealistic operation. Therefore, final model selection should consider both temperature agreement and HVAC energy.

### 2. Heating capacity and shading are the strongest physical levers

Heating capacity dominates winter stability. Shading dominates summer solar behavior. These two parameter groups should receive the most attention in interpretation and final discussion.

### 3. Transition periods are the most difficult

Transition months react strongly to seasonal schedules, shading, and internal loads. This makes them a useful stress test for model realism.

### 4. Room-specific calibration may be necessary

Because Office 172, Office 176, and Office 185 react differently, one global parameter set may not optimize all rooms at the same time.

## Best Candidate Directions

### For winter improvement

* heating_capacity_offices
* ventilation_schedule
* heating_availability

### For summer improvement

* shading_schedule
* shading_threshold
* cooling_capacity_offices

### For transition improvement

* seasonal schedules
* shading behavior
* heating availability

## Parameters Not Recommended as First Calibration Levers

The following parameters should not be used first for temperature calibration:

* ventilation_flow_offices
* cooling_availability
* occupancy_schedule

Reason:

* ventilation flow had limited temperature impact,
* cooling availability showed small effects,
* occupancy changes often worsened temperature agreement

## Parameters Recommended for Further Focus

The following parameters are the most relevant for the next calibration step:

1. shading_threshold
2. shading_schedule
3. heating_capacity_offices

## Final Interpretation

The test results show that the model is most sensitive to parameters that directly affect the main physical drivers of each season:

* heating capacity in winter,
* solar shading in summer,
* seasonal control logic in transition periods.

The results also show that improving one season or room can worsen another. Therefore, the final calibrated model should not be selected based on one metric alone. A balanced decision should consider:

* temperature fit in all three focus rooms,
* seasonal MAE, MBE, and RMSE,
* simulated HVAC energy demand,
* physical plausibility of parameter values,
* consistency with real building operation.

## Recommended Use for AI-Supported Calibration

For future AI-supported parameter suggestions, the AI should:

* avoid extreme parameter values,
* prioritize physically interpretable changes,
* compare temperature and energy simultaneously,
* treat shading and heating capacity as high-impact parameters,
* consider room-specific differences before proposing a global change.



# Recommended Next Calibration Direction

## Winter Calibration Direction

### Main Problem

The model still tends to underestimate temperatures during winter and transition periods.

### Recommended Focus

Priority parameters:

* ventilation_schedule
* heating_availability
* heating_setpoint_offices

### Recommended Strategy

* avoid excessive ventilation during cold periods
* maintain stable heating availability during transition months
* avoid unrealistic heating shutdown extensions
* improve heating stability before increasing heating capacity

### Energy Consideration

Avoid solutions that strongly increase heating demand through permanent HVAC operation.

## Summer Calibration Direction

### Main Problem

Summer overheating remains strongly influenced by solar gains and shading behavior.

### Recommended Focus

Priority parameters:

* shading_schedule
* shading_threshold

### Recommended Strategy

* prioritize realistic shading schedules
* test moderate shading activation windows
* avoid aggressive permanent shading
* use shading before increasing cooling capacity

### Most Promising Observation

A shading threshold around 300 W/m² appears more promising than very low thresholds.

### Energy Consideration

Shading strategies should reduce overheating without strongly increasing cooling demand.

## Transition Period Calibration Direction

### Main Problem

Transition periods remain the most unstable and difficult calibration phase.

### Recommended Focus

Priority parameters:

* seasonal schedules
* heating availability
* shading behavior

### Recommended Strategy

* avoid aggressive seasonal shutdowns
* maintain stable heating behavior during spring and autumn
* avoid excessive shading outside summer periods

### Energy Consideration

Transition periods should avoid simultaneous heating and cooling behavior.

## HVAC Energy Insights

### Main Observation

Some scenarios improve temperature agreement while strongly worsening HVAC energy demand.

### Important Findings

* permanent ventilation operation creates large ventilation energy increase
* shading strongly influences cooling demand
* aggressive occupancy schedules can destabilize energy behavior
* cooling capacity alone is not the main solution for overheating

### Recommended Energy Strategy

Prefer solutions that:

* improve temperature agreement
* maintain realistic HVAC operation
* avoid excessive ventilation energy
* avoid unnecessary cooling compensation


## Most Promising Parameters

Based on the completed tests, the following parameters appear most influential:

### Summer

* shading_schedule
* shading_threshold

### Winter

* ventilation_schedule
* heating_availability

### Overall Stability

* balanced schedules
* realistic solar control
* moderate HVAC operation

## General Conclusion

The calibration results indicate that operational schedules and solar behavior are more important than extreme HVAC sizing changes.

The model reacts strongly to shading and seasonal control logic, while some capacity changes mainly compensate for deeper operational mismatches.

Future calibration steps should therefore prioritize:

* operational realism
* seasonal consistency
* energetically plausible behavior
* moderate and explainable parameter modifications
---

> ◀ [[09_schedules|← Schedules]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[11_measured_energy_reference|Measured Energy Reference →]] ▶
