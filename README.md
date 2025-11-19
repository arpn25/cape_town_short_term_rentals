[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Mapping Short-Term Rental Patterns and Housing Pressure Signals in Cape Town
This repository forms part of my personal **Urban Informatics & Data Science portfolio**.  
It demonstrates my ability to work with real-world spatial datasets, clean and model data, build a geospatial workflow end-to-end, and communicate findings clearly using maps and analytical visualizations.

The project highlights:
- Geospatial data cleaning and preprocessing  
- Exploratory spatial analysis (EDA)  
- Creating a neighbourhood-level Affordability Pressure Index  
- Static & interactive mapping (GeoPandas + Folium)  
- Model interpretation and feature importance

---

## Problem Statement
Cape Town is experiencing housing affordability crisis especially in the rental sector, and some neighborhoods are becoming less affordable for long-term residents. The growth of short-term rentals, such as Airbnb, may contribute to localized housing pressure by reducing long-term availability. This project analyzes Airbnb activity to identify neighborhoods with high listing density, turnover, and price patterns that may indicate potential housing affordability pressure zones.

## Research Questions
1. Which neighborhoods have the highest short term rental listing densities?
2. Which neighborhoods have high booking turnover, low availability, or high activity levels?
3. How does short term rental activity metrics like listing density, reviews, availability, and price contribute to a neighborhood-level Affordability Pressure Index?

## Tools & Libraries
- Python: Pandas, NumPy, Matplotlib, Seaborn
- Spatial Analysis: GeoPandas, Folium for static and interactive maps
- Machine Learning: scikit-learn (MinMaxScaler, Linear Regression, Random Forest)
- Workflow: Jupyter Notebooks, Git & GitHub

## Workflow Overview
1. Data Cleaning & Preprocessing: Load and clean Airbnb listings, calendar data, and neighborhood shapefiles.
2. Exploratory Data Analysis (EDA): Summarize metrics like average price, listing density, reviews per month, and availability.
3. Spatial Analysis: Map neighborhoods with high density and activity using GeoPandas (static) and Folium (interactive).
4. Affordability Pressure Index: Combine normalized metrics into a single index capturing affordability pressure driven by short term rental activity.
5. Modeling & Feature Analysis: Use Linear Regression and Random Forest to assess which factors most influence the pressure index.
6. Visualization & Insights: Identify high-pressure neighborhoods and provide actionable insights for policy, planning, or investment decisions.

## Key Insights
1. Listing Density & Turnover: High density and frequent bookings are the strongest drivers of housing pressure.
2. Price Influence: Price alone has minimal impact; expensive areas with few listings show low pressure.
3. High-Pressure Neighborhoods: Central and mid-range zones (e.g., Ward 115, Ward 54) exhibit the highest pressure.
4. Policy Implication: Short-term rentals reduce long-term housing availability, contributing to localized affordability stress regardless of price.

## Expected Outcomes
- Neighborhood ranking by Affordability Pressure Index
- Maps showing areas of high short-term rental activity and pressure
- Clear identification of key drivers of housing stress (density, turnover, availability)
- Static and interactive visualizations

---

## License & Usage
This project is released under the **MIT License**.  
You are free to use, adapt, and build upon this work for personal or academic purposes **as long as proper attribution is given**.

If you use or reference this project, please cite:
**Ar.Namita (2025). Mapping Short-Term Rental Patterns and Housing Pressure in Cape Town.**

## Author
**Ar.Namita**  
Urban Analytics | Spatial Data Science | Python | GeoPandas  
GitHub: https://github.com/arpn25  
LinkedIn: www.linkedin.com/in/namita-urbaninformatics
