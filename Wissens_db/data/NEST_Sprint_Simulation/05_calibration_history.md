---
tags: [NEST, Sprint, Simulation, Kalibrierung, Ergebnisse]
projekt: "NEST Unit Sprint"
kapitel: "05"
titel: "Calibration History – Parameter Range Tests"
---

> ◀ [[04_calibration_rules|← Calibration Rules]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[07_ai_output_schema|AI Output Schema →]] ▶

---

# Parameter Range Tests

## Evaluation Approach

The simulation results are evaluated based on a temperature comparison between simulated and measured data.

The analysis focuses on three selected office rooms:

* Office 172
* Office 176
* Office 185

These rooms are used as representative zones for the thermal behavior of the building.

For each simulation run, the air temperature of these rooms is compared against measured data.

The evaluation is performed for three time periods:

* Winter (December – February)
* Summer (June – August)
* Transition periods (March – May, September – November)

For each period, the following performance metrics are calculated:

* MAE (Mean Absolute Error)
* MBE (Mean Bias Error)
* RMSE (Root Mean Square Error)

Lower MAE, MBE and RMSE values indicate better agreement between simulation and measured data.

## Data Basis

> Parameter definitions: [[03_parameter_catalog]] · Schedule definitions: [[09_schedules]] · Energy reference: [[11_measured_energy_reference]]

### Simulation Data

* Source: IDA ICE output
* Variable: Room air temperature
* Time resolution: hourly

### Measured Data

* Source: building sensors (2022)
* Variable: Room air temperature
* Aggregation: hourly average

## Time Alignment

* Simulation starts at: 2022-01-01 00:00
* Measured data timestamps aligned to full hours
* All comparisons performed on synchronized timestamps

## Energy Evaluation

In addition to the temperature comparison, building-level HVAC energy values are evaluated for each simulation run.

The reported energy values represent the total simulated annual energy demand of the complete model and are therefore identical for all evaluated office rooms within the same run.

The following values are considered:

* Heating energy \[kWh]
* Cooling energy \[kWh]
* Ventilation energy \[kWh]

This approach ensures a consistent and comparable assessment of all simulation runs.



# Office 172

## Baseline Reference

#### Winter

* MAE:0.862659
* MBE:-0.183246
* RMSE:1.099989

#### Summer

* MAE:1.005772
* MBE:-0.825942
* RMSE:1.332896

#### Transition

* MAE:1.087789
* MBE:-0.307654
* RMSE:1.420514

### Energy Evaluation

* Heating energy \[kWh]:15238.7
* Cooling energy \[kWh]:3134.5
* Ventilation energy \[kWh]:2605.6



## Run 001 office 172 – ventilation\_flow\_offices

### Parameter Setup

* Baseline: 0.6
* Min value: 0.1
* Max value: 3.0

### Evaluation min value

#### Winter

* MAE:0.837148
* MBE:-0.248844
* RMSE:1.075429

#### Summer

* MAE:1.002226
* MBE:-0.813616
* RMSE:1.329420

#### Transition

* MAE:1.086655
* MBE:-0.317127
* RMSE:1.419513

### Energy Evaluation

* Heating energy \[kWh]:15513.1
* Cooling energy \[kWh]:3183
* Ventilation energy \[kWh]:1924.6

### Evaluation max value

#### Winter

* MAE: 0.942129
* MBE:-0.020949
* RMSE:1.187226

#### Summer

* MAE:1.026988
* MBE:-0.867877
* RMSE:1.356006

#### Transition

* MAE:1.090635
* MBE:-0.273460
* RMSE:1.420386

### Energy Evaluation

* Heating energy \[kWh]:13985.7
* Cooling energy \[kWh]:2921.6
* Ventilation energy \[kWh]:5800.4

### Observations

* Lower ventilation flow slightly improved winter MAE and reduced ventilation energy demand       significantly.
* Higher ventilation flow reduced winter underheating but increased ventilation energy strongly.
* Summer and transition periods were only moderately affected by airflow changes.

### Interpretation

* Ventilation flow mainly influences winter heat losses and HVAC energy demand.
* Higher airflow stabilizes indoor temperatures but creates energetically inefficient operation.
* The parameter has limited influence on summer overheating behavior.



## Run 002 office 172 – cooling\_capacity\_offices

### Parameter Setup

* Baseline: 500 W
* Min value: 100 W
* Max value: 1200 W

### Evaluation min value

#### Winter

* MAE:0.862843
* MBE:-0.183264
* RMSE:1.100228

#### Summer

* MAE:1.250454
* MBE:0.587386
* RMSE:1.632937

#### Transition

* MAE:1.085660
* MBE:-0.190161
* RMSE:1.417916

### Energy Evaluation

* Heating energy \[kWh]:15235.7
* Cooling energy \[kWh]:2258.9
* Ventilation energy \[kWh]:2658.9

### Evaluation max value

#### Winter

* MAE:0.862885
* MBE:-0.183259
* RMSE:1.100262

#### Summer

* MAE:1.015598
* MBE:-0.828542
* RMSE:1.348229

#### Transition

* MAE:1.086012
* MBE:-0.305931
* RMSE:1.418737

### Energy Evaluation

* Heating energy \[kWh]:15235.5
* Cooling energy \[kWh]:3115.4
* Ventilation energy \[kWh]:2606.1

### Observations

* Very low cooling capacity strongly worsened summer performance and caused clear overheating effects.
* Increasing cooling capacity above the baseline produced only small additional improvements.
* Winter behavior remained nearly unchanged for all tested cooling capacities.

### Interpretation

* Insufficient cooling capacity causes visible summer overheating.
* Increasing cooling capacity alone does not solve the underlying overheating problem.
* Summer behavior appears to depend more strongly on solar gains and shading control.



## Run 003 office 172 – heating\_capacity\_offices

### Parameter Setup

* Baseline: 500 W
* Min value: 100 W
* Max value: 1200 W

### Evaluation min value

#### Winter

* MAE:7.545477
* MBE:-7.545039
* RMSE:7.720464

#### Summer

* MAE:1.005982
* MBE:-0.824003
* RMSE:1.334655

#### Transition

* MAE:3.258789
* MBE:-3.152147
* RMSE:4.024406

### Energy Evaluation

* Heating energy \[kWh]:7810.5
* Cooling energy \[kWh]:3113.9
* Ventilation energy \[kWh]:3185.9

### Evaluation max value

#### Winter

* MAE:1.370943
* MBE:1.043189
* RMSE:1.614030

#### Summer

* MAE:1.007139
* MBE:-0.826778
* RMSE:1.335597

#### Transition

* MAE:1.172574
* MBE:-0.023114
* RMSE:1.501569

### Energy Evaluation

* Heating energy \[kWh]:15214.3
* Cooling energy \[kWh]:3135.5
* Ventilation energy \[kWh]:2609.6

### Observations

* Very low heating capacity caused significant winter underheating and strongly worsened transition periods behavior.
* Increasing heating capacity above the baseline improved winter bias but produced limited overall improvement.
* Summer performance remained almost unchanged.

### Interpretation

* Heating capacity is a critical parameter for stable winter operation.
* Extremely low capacities are physically unrealistic for the building operation.
* Additional heating capacity mainly compensates temperature deficits instead of solving operational mismatches.



## Run 004 office 172 – heating\_availability

### Scenarios

### Scenario A – Baseline

* 1 Jun – 31 Aug → 0
* Rest of year → 1

### Scenario B – Heating always available

* Whole year → 1

### Scenario C – Extended summer shutdown

* 1 May – 30 Sep → 0
* Rest of year → 1

## Results

### Scenario B – Heating always available

#### Winter

* MAE:0.862659
* MBE:-0.183246
* RMSE:1.099989

#### Summer

* MAE:0.961190
* MBE:-0.773555
* RMSE:1.259886

#### Transition

* MAE:1.087623
* MBE:-0.307703
* RMSE:1.420310

### Energy Evaluation

* Heating energy \[kWh]:15267.7
* Cooling energy \[kWh]:3160.1
* Ventilation energy \[kWh]:2621.4

### Scenario C – Extended summer shutdown

#### Winter

* MAE:0.862644
* MBE:-0.183262
* RMSE:1.099975

#### Summer

* MAE:1.010202
* MBE:-0.828962
* RMSE:1.342339

#### Transition

* MAE:1.566150
* MBE:-0.824020
* RMSE:2.224619

### Energy Evaluation

* Heating energy \[kWh]:14689.3
* Cooling energy \[kWh]:3096.5
* Ventilation energy \[kWh]:2468.3

## Observations

* Permanent heating availability slightly improved summer performance.
* Extended summer shutdown strongly worsened transition periods agreement.
* Winter results remained nearly identical between all scenarios.

## Interpretation

* Heating availability mainly affects seasonal stability during spring and autumn.
* Long heating shutdown periods create unrealistic underheating during transition periods.
* Moderate seasonal control appears more realistic than aggressive shutdown strategies.



## Run 005 office 172 – cooling\_availability

### Scenarios

### Scenario A – Baseline

* 1 Oct – 1 Apr → 0
* Rest of year → 1

### Scenario B – Cooling always available

* Whole year → 1

### Scenario C – Extended cooling period

* 1 Sep – 1 May → 1
* Rest → 0

## Results

### Scenario B – Cooling always available

#### Winter

* MAE:0.862775
* MBE:-0.183209
* RMSE:1.100236

#### Summer

* MAE:1.004758
* MBE:-0.823850
* RMSE:1.331801

#### Transition

* MAE:1.085445
* MBE:-0.308453
* RMSE:1.417544

### Energy Evaluation

* Heating energy \[kWh]:15242.3
* Cooling energy \[kWh]:3150.9
* Ventilation energy \[kWh]:2605.6

### Scenario C – Extended cooling period

#### Winter

* MAE:0.862658
* MBE:-0.183247
* RMSE:1.099989

#### Summer

* MAE:1.005507
* MBE:-0.824998
* RMSE:1.332637

#### Transition

* MAE:1.130476
* MBE:-0.192886
* RMSE:1.467947

### Energy Evaluation

* Heating energy \[kWh]:15215
* Cooling energy \[kWh]:2934
* Ventilation energy \[kWh]:2595.2

## Observations

* Cooling availability changes produced only small differences in overall performance.
* Extended cooling periods slightly improved transition periods bias.
* The influence on summer behavior remained relatively limited.

## Interpretation

* Cooling availability alone is not a dominant calibration parameter.
* Summer overheating appears to depend more strongly on solar behavior and shading control.
* Longer cooling periods may slightly stabilize transition season behavior.



## Run 006 office 172 – ventilation\_schedule

### Scenarios

### Scenario A – Baseline

* Weekdays: 06:00 – 18:00
* Night: OFF
* Weekend: OFF

### Scenario B – Extended operation (longer day)

* Weekdays: 05:00 – 20:00
* Night: OFF
* Weekend: OFF

### Scenario C – Continuous operation (24h weekdays)

* Weekdays: 00:00 – 24:00
* Weekend: OFF

### Scenario D – Always on (including weekend)

* 24h, all days

## Results

### Scenario B – Extended operation

#### Winter

* MAE:0.862456
* MBE:-0.141761
* RMSE:1.098211

#### Summer

* MAE:1.010365
* MBE:-0.834979
* RMSE:1.338291

#### Transition

* MAE:1.089916
* MBE:-0.293016
* RMSE:1.423529

### Energy Evaluation

* Heating energy \[kWh]:14984.9
* Cooling energy \[kWh]:3129.6
* Ventilation energy \[kWh]:3264.2

### Scenario C – Continuous weekdays

#### Winter

* MAE:0.874415
* MBE:-0.005561
* RMSE:1.103868

#### Summer

* MAE:1.028548
* MBE:-0.871767
* RMSE:1.357898

#### Transition

* MAE:1.091875
* MBE:-0.232334
* RMSE:1.427542

### Energy Evaluation

* Heating energy \[kWh]:14272
* Cooling energy \[kWh]:3043.6
* Ventilation energy \[kWh]:5159.1

### Scenario D – Always on

#### Winter

* MAE:0.869427
* MBE:0.186661
* RMSE:1.083848

#### Summer

* MAE:1.051740
* MBE:-0.907558
* RMSE:1.382557

#### Transition

* MAE:1.087434
* MBE:-0.169832
* RMSE:1.413903

### Energy Evaluation

* Heating energy \[kWh]:13433.7
* Cooling energy \[kWh]:2959.8
* Ventilation energy \[kWh]:7495.4

## Observations

* Longer ventilation operation reduced winter underheating.
* Continuous ventilation significantly increased ventilation energy demand.
* Permanent operation slightly improved winter bias but worsened summer performance.

## Interpretation

* Ventilation schedules strongly influence both thermal behavior and HVAC energy demand.
* Continuous operation stabilizes indoor temperatures but creates energetically unrealistic operation.
* Moderate operation periods appear more physically plausible than permanent ventilation.



## Run 007 office 172 – shading\_schedule

### Condition

* Shading activates only if:

  * schedule\_shading = 1
AND
  * solar radiation exceeds 200 W/m²

### Scenarios

### Scenario A – Daily shading window

* 1 Jun – 31 Aug
* 11:00 – 16:00
* Radiation threshold: 200 W/m²

### Scenario B – Longer daily shading window

* 1 Jun – 31 Aug
* 09:00 – 18:00
* Radiation threshold: 200 W/m²

### Scenario C – Radiation-based only, no daily time restriction

* 1 Jun – 31 Aug
* 00:00 – 24:00 allowed
* Radiation threshold: 200 W/m²

### Scenario D – Extended seasonal shading

* 1 May – 30 Sep
* 09:00 – 18:00
* Radiation threshold: 200 W/m²

## Results

### Scenario A – Daily shading window

#### Winter

* MAE:0.862216
* MBE:-0.181144
* RMSE:1.100339

#### Summer

* MAE:0.717530
* MBE:-0.278113
* RMSE:0.976109

#### Transition

* MAE:1.002893
* MBE:-0.074131
* RMSE:1.353058

### Energy Evaluation

* Heating energy \[kWh]:14047.8
* Cooling energy \[kWh]:7177.3
* Ventilation energy \[kWh]:2543.7

### Scenario B – Longer daily shading window

#### Winter

* MAE:0.862216
* MBE:-0.181144
* RMSE:1.100339

#### Summer

* MAE:0.859532
* MBE:-0.537157
* RMSE:1.122782

#### Transition

* MAE:1.003225
* MBE:-0.074606
* RMSE:1.353317

### Energy Evaluation

* Heating energy \[kWh]:14047.5
* Cooling energy \[kWh]:5752
* Ventilation energy \[kWh]:2522.7

### Scenario C – Radiation-based only

#### Winter

* MAE:0.862215
* MBE:-0.181144
* RMSE:1.100339

#### Summer

* MAE:1.068334
* MBE:-0.930983
* RMSE:1.395373

#### Transition

* MAE:1.003244
* MBE:-0.074937
* RMSE:1.353331

### Energy Evaluation

* Heating energy \[kWh]:14049
* Cooling energy \[kWh]:4082.5
* Ventilation energy \[kWh]:2506.1

### Scenario D – Extended seasonal shading

#### Winter

* MAE:0.862217
* MBE:-0.181142
* RMSE:1.100341

#### Summer

* MAE:0.866763
* MBE:-0.544521
* RMSE:1.134405

#### Transition

* MAE:1.032255
* MBE:-0.125544
* RMSE:1.378008

### Energy Evaluation

* Heating energy \[kWh]:14149.3
* Cooling energy \[kWh]:5066.8
* Ventilation energy \[kWh]:2533.7

## Observations

* Controlled summer shading significantly improved summer temperature agreement.
* Moderate daily shading windows produced better summer performance than unrestricted shading operation.
* Extended seasonal shading slightly worsened transition periods behavior.

## Interpretation

* Solar gains are one of the dominant causes of summer overheating.
* Time-restricted shading provides a better balance between solar protection and useful solar gains.
* Excessive shading outside summer periods may reduce beneficial passive heating effects.



## Run 008 office 172  – shading\_threshold

### Condition

* Shading activates only if:

  * solar radiation exceeds value in W/m²

### Parameter Setup

* Baseline: 200 W/m²
* Min value: 100 W/m²
* Max value: 300 W/m²

### Evaluation min value

#### Winter

* MAE:0.882484
* MBE:-0.209517
* RMSE:1.128113

#### Summer

* MAE:1.281103
* MBE:-1.186084
* RMSE:1.711149

#### Transition

* MAE:1.242875
* MBE:-0.645956
* RMSE:1.591556

### Energy Evaluation

* Heating energy \[kWh]:16363.6
* Cooling energy \[kWh]:1721.5
* Ventilation energy \[kWh]:2648.2

### Evaluation max value

#### Winter

* MAE:0.862117
* MBE:-0.181311
* RMSE:1.100410

#### Summer

* MAE:0.892793
* MBE:-0.597581
* RMSE:1.175729

#### Transition

* MAE:1.030954
* MBE:-0.162595
* RMSE:1.367605

### Energy Evaluation

* Heating energy \[kWh]:14675.4
* Cooling energy \[kWh]:4423.3
* Ventilation energy \[kWh]:2582.3

### Observations

* Very low shading thresholds strongly worsened summer and transition periods performance.
* Higher shading thresholds improved summer agreement significantly.
* Low thresholds increased heating demand noticeably.

### Interpretation

* Early shading activation removes useful solar gains and destabilizes the thermal balance.
* Moderate shading thresholds create more realistic solar control behavior.
* Shading control is one of the most influential calibration parameters in the model.



## Run 009 office 172 – occupancy\_schedule

### Scenarios

### Scenario A – Baseline

* Weekdays: 08:00 – 12:00 and 13:00 – 17:00
* Weekend: OFF

### Scenario B – No lunch break

* Weekdays: 08:00 – 17:00
* Weekend: OFF

### Scenario C – Extended working hours

* Weekdays: 07:00 – 18:00
* Weekend: OFF

### Scenario D – Weekend activity

* Weekdays: 08:00 – 12:00 and 13:00 – 17:00
* Saturday: 08:00 – 14:00
* Sunday: OFF

## Results

### Scenario B – No lunch break

#### Winter

* MAE:0.888200
* MBE:-0.194867
* RMSE:1.132850

#### Summer

* MAE:1.266960
* MBE:-1.166754
* RMSE:1.697949

#### Transition

* MAE:1.238672
* MBE:-0.625161
* RMSE:1.585622

### Energy Evaluation

* Heating energy \[kWh]:16178.9
* Cooling energy \[kWh]:1806.4
* Ventilation energy \[kWh]:2640.4

### Scenario C – Extended working hours

#### Winter

* MAE:0.900848
* MBE:-0.132083
* RMSE:1.143445

#### Summer

* MAE:1.226770
* MBE:-1.112465
* RMSE:1.654494

#### Transition

* MAE:1.232761
* MBE:-0.580789
* RMSE:1.576967

### Energy Evaluation

* Heating energy \[kWh]:15793.5
* Cooling energy \[kWh]:1955.9
* Ventilation energy \[kWh]:2623.8

### Scenario D – Weekend activity

#### Winter

* MAE:0.837401
* MBE:-0.391703
* RMSE:1.092814

#### Summer

* MAE:1.440014
* MBE:-1.370670
* RMSE:1.877453

#### Transition

* MAE:1.288069
* MBE:-0.794293
* RMSE:1.641708

### Energy Evaluation

* Heating energy \[kWh]:17673.6
* Cooling energy \[kWh]:1259.2
* Ventilation energy \[kWh]:2702.4

## Observations

* Increased occupancy generally worsened summer and transition periods performance.
* Weekend occupancy created strong thermal instability and increased heating demand.
* Winter improvements remained limited despite higher internal gains.

## Interpretation

* Additional occupancy increases internal heat gains and summer overheating.
* Unrealistic occupancy schedules destabilize the thermal behavior of the model.
* Occupancy assumptions should remain operationally realistic.



## Run 010 office 172 – window_opening_schedule

### Scenarios

### Scenario A – Closed windows (Baseline)

* Windows closed all year
* No natural ventilation

### Scenario B – Moderate daytime opening

* June – August
* 14:00 – 16:00 → windows open
* Rest of time → closed

### Scenario C – Moderate night ventilation

* June – August
* 00:00 – 05:00 → window opening factor = 0.5
* Rest of time → closed

### Scenario D – Occupancy-based opening

* June – August
* Weekdays only
* 09:00 – 12:00 → windows opening factor = 0.25
* 13:00 – 16:00 → windows opening factor = 0.25
* Weekend → closed

## Results

### Scenario B – Moderate daytime opening

#### Winter

* MAE:0.862656
* MBE:-0.183250
* RMSE:1.099987

#### Summer

* MAE:1.311017
* MBE:-1.038454
* RMSE:1.819138

#### Transition

* MAE:1.087702
* MBE:-0.308290
* RMSE:1.420038

### Energy Evaluation

* Heating energy [kWh]:15243.2
* Cooling energy [kWh]:3327.6	
* Ventilation energy [kWh]:2620.3

### Scenario C – Moderate night ventilation

#### Winter

* MAE:0.862655
* MBE:-0.183252
* RMSE:1.099986

#### Summer

* MAE:2.595077
* MBE:-2.566693
* RMSE:3.314973

#### Transition

* MAE:1.088588
* MBE:-0.309078
* RMSE:1.420496

### Energy Evaluation

* Heating energy [kWh]:15348.2
* Cooling energy [kWh]:1839.2
* Ventilation energy [kWh]:2565.4

### Scenario D – Occupancy-based opening

#### Winter

* MAE:0.862655
* MBE:-0.183251
* RMSE:1.099987

#### Summer

* MAE:1.358270
* MBE:-1.212994
* RMSE:1.814217

#### Transition

* MAE:1.087257
* MBE:-0.307591
* RMSE:1.419712

### Energy Evaluation

* Heating energy [kWh]:15238.8	
* Cooling energy [kWh]:2723.6
* Ventilation energy [kWh]:2604.8

## Observations

* Window opening scenarios generally worsened summer agreement.
* Night ventilation caused strong thermal instability and large summer deviations.
* Moderate occupancy-based opening produced smaller impacts than aggressive ventilation strategies.

## Interpretation

* The model reacts strongly to natural ventilation assumptions.
* Aggressive window opening creates unrealistic cooling effects and unstable indoor temperatures.
* Real building operation likely involves more limited window opening behavior than assumed in the tested scenarios.
















































# Office 176

## Baseline Reference

#### Winter

* MAE:1.097823
* MBE:-0.762125
* RMSE:1.277335

#### Summer

* MAE:0.679206
* MBE:-0.395367
* RMSE:0.923687

#### Transition

* MAE:0.996499
* MBE:-0.688047
* RMSE:1.217512



## Run 001 office 176 – ventilation\_flow\_offices

### Parameter Setup

* Baseline: 0.6
* Min value: 0.1
* Max value: 3.0

### Evaluation min value

#### Winter

* MAE:1.097660
* MBE:-0.765430
* RMSE:1.278604

#### Summer

* MAE:0.673740
* MBE:-0.370544
* RMSE:0.916498

#### Transition

* MAE:1.000539
* MBE:-0.689617
* RMSE:1.222095

### Evaluation max value

#### Winter

* MAE:1.090829
* MBE:-0.744732
* RMSE:1.262906

#### Summer

* MAE:0.710245
* MBE:-0.481153
* RMSE:0.960586

#### Transition

* MAE:0.977702
* MBE:-0.665566
* RMSE:1.192279

### Observations

* Lower ventilation flow slightly improved summer performance but had limited influence on winter behavior.
* Higher ventilation flow slightly improved winter and transition periods agreement.
* Overall sensitivity to airflow changes remained relatively moderate.

### Interpretation

* Ventilation flow influences both thermal stability and HVAC energy demand.
* Increased airflow slightly stabilizes winter behavior but may increase unnecessary ventilation losses.
* The room appears less sensitive to airflow changes than to solar or shading effects.



## Run 002 office 176 – cooling\_capacity\_offices

### Parameter Setup

* Baseline: 500 W
* Min value: 100 W
* Max value: 1200 W

### Evaluation min value

#### Winter

* MAE:1.097792
* MBE:-0.762085
* RMSE:1.277300

#### Summer

* MAE:0.844155
* MBE:0.379458
* RMSE:1.140119

#### Transition

* MAE:1.020527
* MBE:-0.643476
* RMSE:1.235279

### Evaluation max value

#### Winter

* MAE:1.097805
* MBE:-0.762098
* RMSE:1.277322

#### Summer

* MAE:0.675765
* MBE:-0.383871
* RMSE:0.921878

#### Transition

* MAE:0.996278
* MBE:-0.686387
* RMSE:1.217453

### Observations

* Very low cooling capacity strongly worsened summer performance and produced clear overheating effects.
* Increasing cooling capacity above the baseline produced only small improvements.
* Winter behavior remained almost unchanged for all scenarios.

### Interpretation

* Insufficient cooling capacity leads directly to summer overheating.
* Increasing cooling capacity alone does not significantly improve the thermal balance.
* Solar gains and shading behavior appear more influential than pure cooling power.



## Run 003 office 176 – heating\_capacity\_offices

### Parameter Setup

* Baseline: 500 W
* Min value: 100 W
* Max value: 1200 W

### Evaluation min value

#### Winter

* MAE:8.363387
* MBE:-8.359449
* RMSE:8.528095

#### Summer

* MAE:0.678827
* MBE:-0.392340
* RMSE:0.924758

#### Transition

* MAE:3.208567
* MBE:-3.111806
* RMSE:3.937384

### Evaluation max value

#### Winter

* MAE:1.104878
* MBE:-0.723319
* RMSE:1.272020

#### Summer

* MAE:0.680412
* MBE:-0.395803
* RMSE:0.926344

#### Transition

* MAE:1.006197
* MBE:-0.702487
* RMSE:1.229529

### Observations

* Very low heating capacity caused severe winter underheating and strongly worsened transition periods behavior.
* Increasing heating capacity above the baseline produced only limited improvements.
* Summer behavior remained nearly unaffected.

### Interpretation

* Heating capacity is essential for stable winter operation.
* Extremely low capacities are physically unrealistic for the office zones.
* Larger heating capacities mainly compensate deficits instead of improving operational behavior.



## Run 004 office 176 – heating\_availability

### Scenarios

### Scenario A – Baseline

* 1 Jun – 31 Aug → 0
* Rest of year → 1

### Scenario B – Heating always available

* Whole year → 1

### Scenario C – Extended summer shutdown

* 1 May – 30 Sep → 0
* Rest of year → 1

## Results

### Scenario B – Heating always available

#### Winter

* MAE:1.097823
* MBE:-0.762125
* RMSE:1.277335

#### Summer

* MAE:0.664657
* MBE:-0.369240
* RMSE:0.892377

#### Transition

* MAE:0.996717
* MBE:-0.688084
* RMSE:1.217707

### Scenario C – Extended summer shutdown

#### Winter

* MAE:1.097822
* MBE:-0.762127
* RMSE:1.277334

#### Summer

* MAE:0.684921
* MBE:-0.400231
* RMSE:0.937444

#### Transition

* MAE:1.401080
* MBE:-1.102096
* RMSE:1.986204

## Observations

* Permanent heating availability slightly improved summer performance.
* Extended summer shutdown strongly worsened transition periods agreement.
* Winter performance remained nearly identical between all scenarios.

## Interpretation

* Heating availability mainly affects seasonal stability outside the winter period.
* Long shutdown periods create unrealistic underheating during spring and autumn.
* Moderate seasonal control appears more plausible than aggressive heating shutdowns.



## Run 005 office 176 – cooling\_availability

### Scenarios

### Scenario A – Baseline

* 1 Oct – 1 Apr → 0
* Rest of year → 1

### Scenario B – Cooling always available

* Whole year → 1

### Scenario C – Extended cooling period

* 1 Sep – 1 May → 1
* Rest → 0

## Results

### Scenario B – Cooling always available

#### Winter

* MAE:1.097794
* MBE:-0.762086
* RMSE:1.277316

#### Summer

* MAE:0.678172
* MBE:-0.392543
* RMSE:0.922151

#### Transition

* MAE:0.995861
* MBE:-0.687229
* RMSE:1.216797

### Scenario C – Extended cooling period

#### Winter

* MAE:1.097823
* MBE:-0.762125
* RMSE:1.277335

#### Summer

* MAE:0.678577
* MBE:-0.394102
* RMSE:0.923399

#### Transition

* MAE:1.075752
* MBE:-0.594344
* RMSE:1.303083

## Observations

* Cooling availability changes produced only small differences in all seasons.
* Extended cooling periods slightly improved transition periods behavior.
* Summer sensitivity remained relatively low.

## Interpretation

* Cooling availability alone is not a dominant calibration parameter.
* Summer behavior appears to depend more strongly on solar gains and shading strategies.
* Extended cooling operation may slightly stabilize transition periods.



## Run 006 office 176 – ventilation\_schedule

### Scenarios

### Scenario A – Baseline

* Weekdays: 06:00 – 18:00 
* Night: OFF
* Weekend: OFF

### Scenario B – Extended operation (longer day)

* Weekdays: 05:00 – 20:00
* Night: OFF
* Weekend: OFF

### Scenario C – Continuous operation (24h weekdays)

* Weekdays: 00:00 – 24:00
* Weekend: OFF

### Scenario D – Always on (including weekend)

* 24h, all days

## Results

### Scenario B – Extended operation

#### Winter

* MAE:1.098126
* MBE:-0.759178
* RMSE:1.276546

#### Summer

* MAE:0.683732
* MBE:-0.405254
* RMSE:0.931187

#### Transition

* MAE: 0.995099
* MBE:-0.687053
* RMSE:1.216100

### Scenario C – Continuous weekdays

#### Winter

* MAE:1.098434
* MBE:-0.750070
* RMSE:1.273769

#### Summer

* MAE:0.701372
* MBE:-0.444430
* RMSE:0.950538

#### Transition

* MAE:0.992137
* MBE:-0.684468
* RMSE:1.212332

### Scenario D – Always on

#### Winter

* MAE:1.102077
* MBE:-0.730687
* RMSE:1.271116

#### Summer

* MAE:0.724368
* MBE:-0.488755
* RMSE:0.983981

#### Transition

* MAE:0.984910
* MBE:-0.677530
* RMSE:1.200672

## Observations

* Longer ventilation operation slightly improved winter and transition periods agreement.
* Continuous ventilation gradually worsened summer performance.
* Permanent operation created the strongest overall ventilation impact.

## Interpretation

* Ventilation schedules influence both indoor stability and operational realism.
* Longer operation reduces winter underheating but increases unnecessary HVAC activity.
* Permanent ventilation operation appears energetically unrealistic.



## Run 007 office 176 – shading\_schedule

### Condition

* Shading activates only if:

  * schedule\_shading = 1
AND
  * solar radiation exceeds 200 W/m²

### Scenarios

### Scenario A – Daily shading window

* 1 Jun – 31 Aug
* 11:00 – 16:00
* Radiation threshold: 200 W/m²

### Scenario B – Longer daily shading window

* 1 Jun – 31 Aug
* 09:00 – 18:00
* Radiation threshold: 200 W/m²

### Scenario C – Radiation-based only, no daily time restriction

* 1 Jun – 31 Aug
* 00:00 – 24:00 allowed
* Radiation threshold: 200 W/m²

### Scenario D – Extended seasonal shading

* 1 May – 30 Sep
* 09:00 – 18:00
* Radiation threshold: 200 W/m²

## Results

### Scenario A – Daily shading window

#### Winter

* MAE:1.097758
* MBE:-0.762061
* RMSE:1.277275

#### Summer

* MAE:0.614331
* MBE:-0.012840
* RMSE:0.815295

#### Transition

* MAE:0.894864
* MBE:-0.439541
* RMSE:1.109446

### Scenario B – Longer daily shading window

#### Winter

* MAE:1.097758
* MBE:-0.762061
* RMSE:1.277275

#### Summer

* MAE:0.622386
* MBE:-0.150047
* RMSE:0.815367

#### Transition

* MAE:0.894941
* MBE:-0.440108
* RMSE:1.109459

### Scenario C – Radiation-based only

#### Winter

* MAE:1.097758
* MBE:-0.762061
* RMSE:1.277275

#### Summer

* MAE:0.682326
* MBE:-0.417610
* RMSE:0.915072

#### Transition

* MAE:0.895099
* MBE:-0.440578
* RMSE:1.109536

### Scenario D – Extended seasonal shading

#### Winter

* MAE:1.097758
* MBE:-0.762061
* RMSE:1.277275

#### Summer

* MAE:0.630172
* MBE:-0.155579
* RMSE:0.827779

#### Transition

* MAE:0.919374
* MBE:-0.486553
* RMSE:1.136083

## Observations

* Controlled summer shading produced some of the strongest improvements among all tested parameters.
* Daily shading windows significantly improved summer agreement.
* Extended seasonal shading slightly worsened transition periods behavior.

## Interpretation

* Solar gains are one of the dominant causes of overheating in Office 176.
* Time-controlled shading creates a better balance between solar protection and useful daylight gains.
* Excessive shading outside summer periods may reduce beneficial passive solar gains.



## Run 008 office 176  – shading\_threshold

### Condition

* Shading activates only if:

  * solar radiation exceeds value in W/m²

### Parameter Setup

* Baseline: 200 W/m²
* Min value: 100 W/m²
* Max value: 300 W/m²

### Evaluation min value

#### Winter

* MAE:1.100309
* MBE:-0.764758
* RMSE:1.281260

#### Summer

* MAE:0.923817
* MBE:-0.770649
* RMSE:1.294762

#### Transition

* MAE:1.124728
* MBE:-0.926359
* RMSE:1.372293

### Evaluation max value

#### Winter

* MAE:1.097867
* MBE:-0.762227
* RMSE:1.277406

#### Summer

* MAE:0.623036
* MBE:-0.172132
* RMSE:0.813909

#### Transition

* MAE:0.919071
* MBE:-0.546084
* RMSE:1.129329

### Observations

* Low shading thresholds strongly worsened summer and transition periods performance.
* Higher shading thresholds produced clear improvements in summer agreement.
* Winter behavior remained nearly unchanged.

### Interpretation

* Early shading activation reduces useful solar gains and destabilizes thermal behavior.
* Moderate shading thresholds provide more realistic solar control.
* Shading threshold is one of the most influential summer calibration parameters.



## Run 009 office 176 – occupancy\_schedule

### Scenarios

### Scenario A – Baseline

* Weekdays: 08:00 – 12:00 and 13:00 – 17:00
* Weekend: OFF

### Scenario B – No lunch break

* Weekdays: 08:00 – 17:00
* Weekend: OFF

### Scenario C – Extended working hours

* Weekdays: 07:00 – 18:00
* Weekend: OFF

### Scenario D – Weekend activity

* Weekdays: 08:00 – 12:00 and 13:00 – 17:00
* Saturday: 08:00 – 14:00
* Sunday: OFF

## Results

### Scenario B – No lunch break

#### Winter

* MAE:1.100249
* MBE:-0.764107
* RMSE:1.280919

#### Summer

* MAE:0.907103
* MBE:-0.744151
* RMSE:1.274826

#### Transition

* MAE:1.113882
* MBE:-0.908489
* RMSE:1.361362

### Scenario C – Extended working hours

#### Winter

* MAE:1.100866
* MBE:-0.760403
* RMSE:1.279966

#### Summer

* MAE:0.865753
* MBE:-0.683324
* RMSE:1.222593

#### Transition

* MAE:1.098572
* MBE:-0.881313
* RMSE:1.346451

### Scenario D – Weekend activity

#### Winter

* MAE:1.095804
* MBE:-0.776057
* RMSE:1.282692

#### Summer

* MAE:1.121144
* MBE:-1.019971
* RMSE:1.504426

#### Transition

* MAE:1.213530
* MBE:-1.033092
* RMSE:1.444798

## Observations

* Increased occupancy generally worsened summer and transition periods behavior.
* Weekend occupancy produced the strongest thermal instability.
* Longer weekday occupancy increased internal heat gains noticeably.

## Interpretation

* Additional occupancy increases internal gains and summer overheating risk.
* Unrealistic occupancy assumptions destabilize the thermal balance of the model.
* Operational schedules should remain physically plausible.



## Run 010 office 176 – window_opening_schedule

### Scenarios

### Scenario A – Closed windows (Baseline)

* Windows closed all year
* No natural ventilation

### Scenario B – Moderate daytime opening

* June – August
* 14:00 – 16:00 → windows open
* Rest of time → closed

### Scenario C – Moderate night ventilation

* June – August
* 00:00 – 05:00 → window opening factor = 0.5
* Rest of time → closed

### Scenario D – Occupancy-based opening

* June – August
* Weekdays only
* 09:00 – 12:00 → windows opening factor = 0.25
* 13:00 – 16:00 → windows opening factor = 0.25
* Weekend → closed

## Results

### Scenario B – Moderate daytime opening

#### Winter

* MAE:1.097824
* MBE:-0.762124
* RMSE:1.277335

#### Summer

* MAE:1.050034
* MBE:-0.700345
* RMSE:1.513363

#### Transition

* MAE:0.998684
* MBE:-0.693455
* RMSE:1.219342

### Scenario C – Moderate night ventilation

#### Winter

* MAE:1.097824
* MBE:-0.762124
* RMSE:1.277335

#### Summer

* MAE:2.663480
* MBE:-2.639482
* RMSE:3.338576

#### Transition

* MAE:1.000146
* MBE:-0.696081
* RMSE:1.220482

### Scenario D – Occupancy-based opening

#### Winter

* MAE:1.097824
* MBE:-0.762124
* RMSE:1.277335

#### Summer

* MAE:1.069586
* MBE:-0.875739
* RMSE:1.450244

#### Transition

* MAE:0.996100
* MBE:-0.688129
* RMSE:1.217154

## Observations

* Window opening scenarios generally worsened summer agreement.
* Night ventilation caused very large summer deviations and unstable behavior.
* Occupancy-based opening produced smaller impacts than unrestricted ventilation strategies.

## Interpretation

* The room reacts strongly to natural ventilation assumptions.
* Aggressive window opening strategies create unrealistic cooling behavior.
* Real user window operation is likely more limited than assumed in the tested schedules.
















































# Office 185

## Baseline Reference

#### Winter

* MAE:1.006192
* MBE:-0.536039
* RMSE:1.242702

#### Summer

* MAE:0.656990
* MBE:-0.056468
* RMSE:0.889339

#### Transition

* MAE:1.058456
* MBE:-0.573516
* RMSE:1.287629



## Run 001 office 185 – ventilation\_flow\_offices

### Parameter Setup

* Baseline: 0.6
* Min value: 0.1
* Max value: 3.0

### Evaluation min value

#### Winter

* MAE:1.004155
* MBE:-0.591068
* RMSE:1.239218

#### Summer

* MAE:0.658492
* MBE:-0.044613
* RMSE:0.890649

#### Transition

* MAE:1.066785
* MBE:-0.579681
* RMSE:1.296665

### Evaluation max value

#### Winter

* MAE:1.020801
* MBE:-0.395399
* RMSE:1.266851

#### Summer

* MAE:0.659240
* MBE:-0.098593
* RMSE:0.893857

#### Transition

* MAE:1.029714
* MBE:-0.546753
* RMSE:1.258742

### Observations

* Lower ventilation flow slightly improved summer performance and reduced ventilation energy demand.
* Higher ventilation flow improved winter stability but increased ventilation energy significantly.
* Transition periods reacted moderately to airflow changes.

### Interpretation

* Ventilation flow mainly influences winter heat losses and HVAC energy demand.
* Higher airflow stabilizes indoor temperatures but creates energetically inefficient operation.
* The parameter has only limited influence on summer overheating.



## Run 002 office 185 – cooling\_capacity\_offices

### Parameter Setup

* Baseline: 500 W
* Min value: 100 W
* Max value: 1200 W

### Evaluation min value

#### Winter

* MAE:1.006348
* MBE:-0.536123
* RMSE:1.243057

#### Summer

* MAE:1.813362
* MBE:1.549781
* RMSE:2.246012

#### Transition

* MAE:1.148210
* MBE:-0.405434
* RMSE:1.397634

### Evaluation max value

#### Winter

* MAE:1.006040
* MBE:-0.535855
* RMSE:1.242529

#### Summer

* MAE:0.677767
* MBE:-0.066559
* RMSE:0.906217

#### Transition

* MAE:1.058913
* MBE:-0.572023
* RMSE:1.287846

### Observations

* Very low cooling capacity strongly worsened summer performance and caused visible overheating.
* Increasing cooling capacity above the baseline produced only limited improvements.
* Winter behavior remained almost unaffected.

### Interpretation

* Insufficient cooling capacity directly increases summer overheating.
* Increasing cooling power alone does not solve the underlying thermal imbalance.
* Solar gains and shading appear more influential than additional cooling capacity.



## Run 003 office 185 – heating\_capacity\_offices

### Parameter Setup

* Baseline: 500 W
* Min value: 100 W
* Max value: 1200 W

### Evaluation min value

#### Winter

* MAE:7.721965
* MBE:-7.717599
* RMSE:7.885286

#### Summer

* MAE:0.657591
* MBE:-0.055000
* RMSE:0.890370

#### Transition

* MAE:3.402012
* MBE:-3.150058
* RMSE:4.215258

### Evaluation max value

#### Winter

* MAE:1.129225
* MBE:0.546027
* RMSE:1.423341

#### Summer

* MAE:0.657868
* MBE:-0.057685
* RMSE:0.890546

#### Transition

* MAE:0.995566
* MBE:-0.357371
* RMSE:1.216889

### Observations

* Very low heating capacity caused severe winter underheating and unstable transition periods behavior.
* Higher heating capacity improved winter agreement slightly but did not solve all deviations.
* Summer behavior remained nearly unchanged.

### Interpretation

* Heating capacity is essential for maintaining stable winter temperatures.
* Extremely low capacities are physically unrealistic for office operation.
* Increasing heating capacity mainly compensates deficits instead of improving operational control.



## Run 004 office 185 – heating\_availability

### Scenarios

### Scenario A – Baseline

* 1 Jun – 31 Aug → 0
* Rest of year → 1

### Scenario B – Heating always available

* Whole year → 1

### Scenario C – Extended summer shutdown

* 1 May – 30 Sep → 0
* Rest of year → 1

## Results

### Scenario B – Heating always available

#### Winter

* MAE:1.006192
* MBE:-0.536039
* RMSE:1.242702

#### Summer

* MAE:0.625364
* MBE:-0.011820
* RMSE:0.831984

#### Transition

* MAE:1.058376
* MBE:-0.573816
* RMSE:1.287473

### Scenario C – Extended summer shutdown

#### Winter

* MAE:1.006178
* MBE:-0.536050
* RMSE:1.242694

#### Summer

* MAE:0.660763
* MBE:-0.058828
* RMSE:0.896123

#### Transition

* MAE:1.491320
* MBE:-1.041084
* RMSE:2.088674

## Observations

* Permanent heating availability slightly improved transition periods behavior.
* Extended summer shutdown worsened thermal stability during spring and autumn.
* Winter behavior remained largely unchanged between scenarios.

## Interpretation

* Heating availability mainly affects seasonal stability outside the main winter period.
* Aggressive seasonal shutdowns create unrealistic underheating during transition periods.
* Moderate seasonal control appears more physically plausible.



## Run 005 office 185 – cooling\_availability

### Scenarios

### Scenario A – Baseline

* 1 Oct – 1 Apr → 0
* Rest of year → 1

### Scenario B – Cooling always available

* Whole year → 1

### Scenario C – Extended cooling period

* 1 Sep – 1 May → 1
* Rest → 0

## Results

### Scenario B – Cooling always available

#### Winter

* MAE:1.006219
* MBE:-0.536043
* RMSE:1.242928

#### Summer

* MAE:0.657071
* MBE:-0.055461
* RMSE:0.889379

#### Transition

* MAE:1.049657
* MBE:-0.584946
* RMSE:1.274793

### Scenario C – Extended cooling period

#### Winter

* MAE:1.006192
* MBE:-0.536038
* RMSE:1.242702

#### Summer

* MAE:0.657542
* MBE:-0.056786
* RMSE:0.890312

#### Transition

* MAE:1.184960
* MBE:-0.417604
* RMSE:1.478643

## Observations

* Cooling availability changes produced only small overall differences.
* Extended cooling periods slightly stabilized transition periods behavior.
* Summer sensitivity remained relatively low.

## Interpretation

* Cooling availability alone is not one of the dominant calibration parameters.
* Summer behavior depends more strongly on solar gains and shading control.
* Extended cooling operation may slightly improve seasonal stability.



## Run 006 office 185 – ventilation\_schedule

### Scenarios

### Scenario A – Baseline

* Weekdays: 06:00 – 18:00
* Night: OFF
* Weekend: OFF

### Scenario B – Extended operation (longer day)

* Weekdays: 05:00 – 20:00
* Night: OFF
* Weekend: OFF

### Scenario C – Continuous operation (24h weekdays)

* Weekdays: 00:00 – 24:00
* Weekend: OFF

### Scenario D – Always on (including weekend)

* 24h, all days

## Results

### Scenario B – Extended operation

#### Winter

* MAE:0.992526
* MBE:-0.494794
* RMSE:1.230168

#### Summer

* MAE:0.658058
* MBE:-0.064282
* RMSE:0.891198

#### Transition

* MAE:1.049950
* MBE:-0.559692
* RMSE:1.280891

### Scenario C – Continuous weekdays

#### Winter

* MAE:0.963032
* MBE:-0.359620
* RMSE:1.202525

#### Summer

* MAE:0.657829
* MBE:-0.090190
* RMSE:0.890684

#### Transition

* MAE:1.017239
* MBE:-0.507126
* RMSE:1.251876

### Scenario D – Always on

#### Winter

* MAE:0.905433
* MBE:-0.182987
* RMSE:1.139946

#### Summer

* MAE:0.659690
* MBE:-0.124187
* RMSE:0.901986

#### Transition

* MAE:0.987765
* MBE:-0.465124
* RMSE:1.221639

## Observations

* Longer ventilation operation reduced winter underheating noticeably.
* Continuous ventilation caused a very large increase in ventilation energy demand.
* Permanent operation slightly worsened summer agreement.

## Interpretation

* Ventilation schedules strongly influence both thermal stability and HVAC energy demand.
* Longer operation improves winter stability but creates energetically unrealistic behavior.
* Moderate ventilation schedules appear more physically plausible than permanent operation.



## Run 007 office 185 – shading\_schedule

### Condition

* Shading activates only if:

  * schedule\_shading = 1
AND
  * solar radiation exceeds 200 W/m²

### Scenarios

### Scenario A – Daily shading window

* 1 Jun – 31 Aug
* 11:00 – 16:00
* Radiation threshold: 200 W/m²

### Scenario B – Longer daily shading window

* 1 Jun – 31 Aug
* 09:00 – 18:00
* Radiation threshold: 200 W/m²

### Scenario C – Radiation-based only, no daily time restriction

* 1 Jun – 31 Aug
* 00:00 – 24:00 allowed
* Radiation threshold: 200 W/m²

### Scenario D – Extended seasonal shading

* 1 May – 30 Sep
* 09:00 – 18:00
* Radiation threshold: 200 W/m²

## Results

### Scenario A – Daily shading window

#### Winter

* MAE:0.946981
* MBE:-0.249242
* RMSE:1.212291

#### Summer

* MAE:0.989073
* MBE:0.640052
* RMSE:1.465275

#### Transition

* MAE:1.308124
* MBE:0.273136
* RMSE:1.827221

### Scenario B – Longer daily shading window

#### Winter

* MAE:0.946982
* MBE:-0.249242
* RMSE:1.212291

#### Summer

* MAE:0.714439
* MBE:0.101811
* RMSE:0.997275

#### Transition

* MAE:1.308066
* MBE:0.272544
* RMSE:1.827420

### Scenario C – Radiation-based only

#### Winter

* MAE:0.946981
* MBE:-0.249242
* RMSE:1.212291

#### Summer

* MAE:0.671308
* MBE:-0.257934
* RMSE:0.940595

#### Transition

* MAE:1.308127
* MBE:0.272444
* RMSE:1.827351

### Scenario D – Extended seasonal shading

#### Winter

* MAE:0.946982
* MBE:-0.249242
* RMSE:1.212291

#### Summer

* MAE:0.727339
* MBE:0.100845
* RMSE:1.024815

#### Transition

* MAE:1.287544
* MBE:0.088416
* RMSE:1.796634

## Observations

* Controlled summer shading improved summer agreement significantly.
* Daily shading windows generally improved summer performance while maintaining more realistic operational control.
* Extended seasonal shading slightly worsened transition periods behavior.

## Interpretation

* Solar gains strongly influence summer overheating in Office 185.
* Time-controlled shading creates a better balance between overheating protection and useful solar gains.
* Excessive shading outside summer periods may reduce passive heating benefits.



## Run 008 office 185  – shading\_threshold

### Condition

* Shading activates only if:

  * solar radiation exceeds value in W/m²

### Parameter Setup

* Baseline: 200 W/m²
* Min value: 100 W/m²
* Max value: 300 W/m²

### Evaluation min value

#### Winter

* MAE:1.034695
* MBE:-0.587701
* RMSE:1.279353

#### Summer

* MAE:0.788515
* MBE:-0.498338
* RMSE:1.167923

#### Transition

* MAE:1.212889
* MBE:-0.921466
* RMSE:1.456047

### Evaluation max value

#### Winter

* MAE:0.986098
* MBE:-0.477203
* RMSE:1.222035

#### Summer

* MAE:0.650810
* MBE:0.090809
* RMSE:0.873203

#### Transition

* MAE:1.037699
* MBE:-0.408561
* RMSE:1.282822

### Observations

* Low shading thresholds strongly worsened overall thermal performance.
* Higher shading thresholds significantly improved summer behavior.
* Very early shading activation increased heating demand noticeably.

### Interpretation

* Early shading removes useful solar gains and destabilizes the thermal balance.
* Moderate shading thresholds provide more realistic solar control behavior.
* Shading threshold is one of the strongest summer calibration parameters.



## Run 009 office 185 – occupancy\_schedule

### Scenarios

### Scenario A – Baseline

* Weekdays: 08:00 – 12:00 and 13:00 – 17:00
* Weekend: OFF

### Scenario B – No lunch break

* Weekdays: 08:00 – 17:00
* Weekend: OFF

### Scenario C – Extended working hours

* Weekdays: 07:00 – 18:00
* Weekend: OFF

### Scenario D – Weekend activity

* Weekdays: 08:00 – 12:00 and 13:00 – 17:00
* Saturday: 08:00 – 14:00
* Sunday: OFF

## Results

### Scenario B – No lunch break

#### Winter

* MAE:1.035981
* MBE:-0.577337
* RMSE:1.282454

#### Summer

* MAE:0.784486
* MBE:-0.481812
* RMSE:1.159503

#### Transition

* MAE:1.206976
* MBE:-0.900995
* RMSE:1.448842

### Scenario C – Extended working hours

#### Winter

* MAE:1.025486
* MBE:-0.519486
* RMSE:1.273290

#### Summer

* MAE:0.763737
* MBE:-0.427846
* RMSE:1.129677

#### Transition

* MAE:1.188602
* MBE:-0.861409
* RMSE:1.432739

### Scenario D – Weekend activity

#### Winter

* MAE:1.050834
* MBE:-0.728972
* RMSE:1.293410

#### Summer

* MAE:0.877783
* MBE:-0.666828
* RMSE:1.283718

#### Transition

* MAE:1.272485
* MBE:-1.061065
* RMSE:1.512738

## Observations

* Increased occupancy worsened summer and transition periods behavior.
* Weekend occupancy caused strong thermal instability and increased energy demand.
* Winter improvements remained relatively limited.

## Interpretation

* Additional occupancy increases internal heat gains and overheating risk.
* Unrealistic occupancy schedules destabilize the thermal behavior of the model.
* Occupancy assumptions should remain operationally realistic.



## Run 010 office 185 – window_opening_schedule

### Scenarios

### Scenario A – Closed windows (Baseline)

* Windows closed all year
* No natural ventilation

### Scenario B – Moderate daytime opening

* June – August
* 14:00 – 16:00 → windows open
* Rest of time → closed

### Scenario C – Moderate night ventilation

* June – August
* 00:00 – 05:00 → window opening factor = 0.5
* Rest of time → closed

### Scenario D – Occupancy-based opening

* June – August
* Weekdays only
* 09:00 – 12:00 → windows opening factor = 0.25
* 13:00 – 16:00 → windows opening factor = 0.25
* Weekend → closed

## Results

### Scenario B – Moderate daytime opening

#### Winter

* MAE:1.006195
* MBE:-0.536042
* RMSE:1.242704

#### Summer

* MAE:0.923292
* MBE:-0.272420
* RMSE:1.396268

#### Transition

* MAE:1.058967
* MBE:-0.573696
* RMSE:1.288025

### Scenario C – Moderate night ventilation

#### Winter

* MAE:1.006195
* MBE:-0.536042
* RMSE:1.242704

#### Summer

* MAE:1.870303
* MBE:-1.664951
* RMSE:2.733009

#### Transition

* MAE:1.059135
* MBE:-0.575288
* RMSE:1.287977

### Scenario D – Occupancy-based opening

#### Winter

* MAE:1.006195
* MBE:-0.536042
* RMSE:1.242704

#### Summer

* MAE:0.889519
* MBE:-0.446975
* RMSE:1.295914

#### Transition

* MAE:1.058600
* MBE:-0.573021
* RMSE:1.287807

## Observations

* Window opening scenarios generally worsened summer agreement.
* Night ventilation produced strong instability and large summer deviations.
* Moderate occupancy-based opening had smaller effects than unrestricted ventilation strategies.

## Interpretation

* The model reacts strongly to natural ventilation assumptions.
* Aggressive window opening strategies create unrealistic cooling effects.
* Real occupant behavior likely involves more limited and irregular window opening patterns.



---

> ◀ [[04_calibration_rules|← Calibration Rules]] · [[_NEST_Sprint_MOC|↑ MOC]] · [[07_ai_output_schema|AI Output Schema →]] ▶
