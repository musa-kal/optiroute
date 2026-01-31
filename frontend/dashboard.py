import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
import os

API_BASE_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(layout="wide")
st.title("🚛 OptiRoute: Logistics Optimization Engine")
st.caption("Operator-Engineer Project | Built with Python & Scikit-Learn")

# Sidebar for controls
with st.sidebar:
    st.header("Configuration")
    n_drivers = st.slider("Available Drivers", min_value=1, max_value=10, value=5)
    uploaded_file = st.file_uploader("Upload Orders CSV", type=["csv"])

# Main Logic
if uploaded_file is not None:
    # Prepare the file for the API request
    files = {'file': uploaded_file.getvalue()}
    params = {'n_drivers': n_drivers}
    
    # Call our local API (Microservices architecture!)
    try:
        response = requests.post(f"{API_BASE_URL}/optimize", files=files, params=params)
        
        if response.status_code == 200:
            data = response.json()['data']
            df_result = pd.DataFrame(data)
            
            # Metrics
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Orders", len(df_result))
            c2.metric("Drivers Utilized", n_drivers)
            c3.metric("Avg Orders/Driver", f"{len(df_result)/n_drivers:.1f}")

            # Map Visualization
            st.subheader("Geographic Clustering")
            m = folium.Map(location=[43.60, -79.75], zoom_start=10)
            
            # Color map for different drivers
            colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
            
            for _, row in df_result.iterrows():
                driver_idx = row['driver_id']
                folium.Marker(
                    [row['lat'], row['lon']],
                    popup=f"Order: {row['order_id']}\nDriver: {driver_idx}",
                    icon=folium.Icon(color=colors[driver_idx % len(colors)], icon="box", prefix='fa')
                ).add_to(m)
            
            st_folium(m, width=800, height=500)
            
            # Data Table
            st.dataframe(df_result)
            
        else:
            st.error("Error connecting to Optimization Engine.")
            
    except Exception as e:
        st.error(f"Make sure the FastAPI backend is running! Error: {e}")

else:
    st.info("Please upload `orders.csv` to begin optimization.")