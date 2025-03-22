# Aviation Risk Analysis for Aircraft Acquisition

## Overview
This repository contains the analysis and insights for determining the lowest-risk aircraft for commercial and private operations. The goal is to support the company's expansion into the aviation industry by identifying aircraft with the lowest risk profiles based on historical accident data. The findings are presented through data analysis, visualizations, and actionable insights to guide the aviation division's purchasing decisions.

---

## Business Understanding
### Stakeholder
- **Head of the New Aviation Division**: Responsible for deciding which aircraft to purchase and operate.

### Key Business Questions
1. Which aircraft models have the lowest historical accident rates?
2. What factors contribute to the risk profile of an aircraft (e.g., age, manufacturer, usage type)?
3. How can the company minimize operational risks when entering the aviation industry?

---

## Data Understanding and Analysis
### Source of Data
The dataset used is from the **National Transportation Safety Board (NTSB)**, containing civil aviation accident and incident data from **1962 to 2023** in the United States and international waters. The dataset includes details such as aircraft type, manufacturer, accident severity, and contributing factors.

### Description of Data
The dataset includes the following key columns:
- **Aircraft Type**: Model and type of aircraft.
- **Manufacturer**: Company that produced the aircraft.
- **Accident Date**: Date of the accident.
- **Injury Severity**: Level of injury or fatality.
- **Phase of Flight**: Phase during which the accident occurred (e.g., takeoff, landing).
- **Contributing Factors**: Factors that led to the accident (e.g., mechanical failure, weather).

### Data Preprocessing
- Handled missing values by imputing or removing incomplete records.
- Aggregated data by aircraft model and manufacturer to calculate accident rates.
- Filtered data to focus on commercial and private aircraft.

---

## Visualizations
### 1. **Accident Rates by Aircraft Model**
![Accident Rates by Aircraft Model](visualizations/accident_rates_by_model.png)  
*This bar chart shows the accident rates for the top 20 aircraft models, highlighting the lowest-risk models.*

### 2. **Accident Severity by Phase of Flight**
![Accident Severity by Phase of Flight](visualizations/accident_severity_by_phase.png)  
*This heatmap visualizes the severity of accidents during different phases of flight, helping identify high-risk operational phases.*

### 3. **Contributing Factors to Accidents**
![Contributing Factors](visualizations/contributing_factors.png)  
*This pie chart breaks down the primary contributing factors to accidents, such as mechanical failure, human error, and weather conditions.*

---

## Conclusion
### Summary of Findings
1. **Lowest-Risk Aircraft Models**: Aircraft models from manufacturers like [Manufacturer Name] consistently show lower accident rates, making them ideal candidates for acquisition.
2. **High-Risk Phases of Flight**: Accidents are most frequent during takeoff and landing, suggesting the need for enhanced training and safety protocols during these phases.
3. **Primary Contributing Factors**: Mechanical failures and human error are the leading causes of accidents, emphasizing the importance of rigorous maintenance and pilot training programs.

### Actionable Insights
- Prioritize purchasing aircraft models with the lowest historical accident rates.
- Invest in advanced training programs for pilots, particularly for high-risk phases of flight.
- Implement strict maintenance schedules to minimize mechanical failures.

---

This analysis provides a data-driven foundation for the company's entry into the aviation industry, ensuring informed and risk-averse decision-making.
