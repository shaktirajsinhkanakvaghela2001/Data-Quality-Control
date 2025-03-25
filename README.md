# Data-Quality-Control
# Air Quality Data Quality Control 🏭🌫️📊

## Project Overview
Implementation of a **Data Quality Control (DQC)** framework for air quality (AQI) datasets to ensure accuracy, completeness, and reliability of pollution metrics (PM10, NO2, SO2, CO, etc.).  

## Key Components
- **Data Profiling**: Analyze AQI trends, missing values, and outliers  
- **Cleansing**: Handle duplicates, impute missing sensor data, standardize units  
- **Validation**: Check AQI health breakpoints & sub-index calculations  
- **Monitoring Dashboard**: Track real-time AQI anomalies and trends  
- **Automation**: Scripts for monthly AQI data updates  

## Technologies  
- **Data Tools**: Python (Pandas, OpenAQ API), Trifacta (for cleansing)  
- **Visualization**: Power BI (for AQI trend dashboards)  
- **Validation**: Automated checks for AQI index consistency  

## Dataset Notes  
- AQI is a **linear sub-index** of pollutants (PM10, NO2, etc.)  
- Health breakpoints define category thresholds (Good → Hazardous)  
