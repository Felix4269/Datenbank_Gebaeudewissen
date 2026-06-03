---
tags: [NEST, Sprint, Simulation, Kalibrierung]
projekt: "NEST Unit Sprint"
kapitel: "01"
titel: "Project Goal"
---

> [[_NEST_Sprint_MOC|↑ MOC]] · [[02_building_model_overview|Building Model Overview →]] ▶

---

# Project Goal

## Main Objective

Calibrate an IDA ICE model of the NEST Unit Sprint (1st floor) so that simulation results match measured data as closely as possible while maintaining physically plausible HVAC behavior and energy demand.

## Background

The goal of this project is to support the development of an AI-assisted workflow for building simulation calibration in IDA ICE.

The AI will use structured Markdown knowledge files to:

* understand the building model
* understand important calibration parameters
* understand calibration logic and dependencies
* analyze previous calibration results
* suggest physically plausible parameter modifications

## Calibration Philosophy

The calibration process should prioritize:

* physically realistic parameter values
* plausible HVAC operation
* seasonal consistency
* stable behavior across multiple rooms

Pure numerical fitting without physical plausibility should be avoided.

## Approach

### Step 1 – Baseline Model

* Create a realistic IDA ICE model
* Use measured weather data for 2022
* Define schedules, HVAC systems, and internal loads
* Establish a stable baseline configuration

### Step 2 – Calibration

* Change selected parameters step by step
* Compare simulation outputs with measured data
* Evaluate:

  * room temperatures
  * seasonal behavior
  * annual HVAC energy demand

Main temperature metrics:

* MAE
* MBE
* RMSE

### Step 3 – Sensitivity Analysis

* Test one parameter or one schedule modification at a time
* Analyze effects on:

  * winter behavior
  * summer overheating
  * transition periods
  * HVAC energy demand

Identify:

* sensitive parameters
* weak parameters
* problematic parameter interactions
* energetically inefficient control strategies

### Step 4 – AI Integration

Store all calibration knowledge in structured Markdown files.

The AI should be able to:

* interpret calibration results
* identify promising parameter changes
* generate structured improvement proposals
* consider seasonal effects
* consider HVAC energy implications
* propose schedule modifications

## Final Goal

The final objective is to create an AI-supported calibration framework capable of:

* understanding the simulation model
* interpreting calibration results
* proposing realistic parameter combinations
* improving agreement between measured and simulated data
* supporting future IDA ICE users during calibration tasks

---

> [[_NEST_Sprint_MOC|↑ MOC]] · [[02_building_model_overview|Building Model Overview →]] ▶