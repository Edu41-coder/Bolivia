import streamlit as st
# Description of the VECM model
st.title("VECM Model for Bolivia's Economic Data")
st.markdown("""
### Description
The Vector Error Correction Model (VECM) is a multivariate time series model used to capture the long-term equilibrium relationships between multiple time series that are cointegrated. In this app, we apply the VECM model to Bolivia's economic data, specifically focusing on the following variables:
- IPC promedio (Average Consumer Price Index)
- IPC fin de periodo (End of Period Consumer Price Index)
- Deflactor del PIB (GDP Deflator)

### Data
The data consists of annual observations from 2006 to 2023.
""")

# Display the image
st.image('imagenes/VECM_Bolivia.png', caption='VECM Forecast for Bolivia\'s Economic Data')

# Interpretation of the results
st.markdown("""
### Interpretation of the Results
The VECM model captures the long-term equilibrium relationships between the selected economic indicators. The forecasted values for the next 5 years (2024-2028) are shown in the graph above. The red dashed line indicates the start of the forecast period.

- **IPC promedio** and **IPC fin de periodo**: These indices show the general price level changes over time. The forecast suggests a continued increase in the price levels.
- **Deflactor del PIB**: This index measures the changes in the price level of all new, domestically produced, final goods and services in an economy. The forecast indicates a steady increase in the GDP deflator, suggesting inflationary pressures in the economy.

The VECM model helps in understanding the dynamic relationships between these variables and provides insights into future trends based on historical data.
""")