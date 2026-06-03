---
tags: [NEST, Sprint, Simulation, Energie, Messdaten]
projekt: "NEST Unit Sprint"
kapitel: "11"
titel: "Measured Energy Reference"
---

> ◀ [[10_calibration_insights|← Calibration Insights]] · [[_NEST_Sprint_MOC|↑ MOC]]

---

# Measured Energy Reference

## Annual Measured Energy Values (2022)

### Energy Evaluation

* Heating energy [kWh/year]: 9632
* Cooling energy [kWh/year]: 2850
* Ventilation energy [kWh/year]: 2119



## Total System Reference

### Energy Evaluation

* Total heating energy [kWh/year]: 13641
* Total cooling energy [kWh/year]: 3873



# Description

This file contains measured thermal energy values used as reference for comparison with the IDA ICE simulation outputs.

The measured values are based on Belimo energy meters installed in the Sprint unit HVAC system.

The comparison is intended as a plausibility evaluation and not as an exact optimization target, since the real HVAC system and the simplified IDA ICE system are not fully identical.



# Evaluation Period

* Year: 2022

The annual energy values were calculated using:


Energy_2022 = Meter value (01.01.2023) - Meter value (01.01.2022)




# Heating Energy

## Measured Data Source

* System: U10Z1
* Datapoint: th. energy total heating
* Unit: kWh

## Calculation


9632 - 0 = 9632 kWh/year




# Cooling Energy

## Measured Data Source

* System: U10Z1
* Datapoint: th. energy total cooling
* Unit: kWh

## Calculation


2850 - 0 = 2850 kWh/year




# Ventilation Energy

## Measured Data Source

Ventilation-related energy is evaluated using the air conditioning subsystem U10L1.

The heating and cooling contributions are combined to obtain the total ventilation-related thermal energy.

### Heating contribution

* System: U10L1
* Datapoint: th. energy total heating
* Unit: kWh


1317 - 0 = 1317 kWh/year


### Cooling contribution

* System: U10L1
* Datapoint: th. energy total cooling
* Unit: kWh


802 - 0 = 802 kWh/year


## Total Ventilation Energy


1317 + 802 = 2119 kWh/year




# Total System Reference

## Total Heating Energy

### Measured Data Source

* System: U10M1
* Datapoint: th. energy total heating
* Unit: kWh

## Calculation


20641 - 7000 = 13641 kWh/year




## Total Cooling Energy

### Measured Data Source

* System: U10N1
* Datapoint: th. energy total cooling
* Unit: kWh

## Calculation


4626 - 753 = 3873 kWh/year




# Notes

* The measured values represent thermal energy measurements from the real building system.
* The IDA ICE model uses a simplified HVAC representation.
* Therefore, the comparison is mainly used to evaluate energetic plausibility and relative behavior between simulation scenarios.
* The total system values are used as an additional plausibility reference for the separated subsystem measurements.
---

> ◀ [[10_calibration_insights|← Calibration Insights]] · [[_NEST_Sprint_MOC|↑ MOC]]
