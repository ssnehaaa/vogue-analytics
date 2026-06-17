import streamlit as st
import pickle
import numpy as np
import pandas as pd
import time
import os

# 1. Load the trained model and your dataset
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

df = pd.read_csv('fashion_trends_lifecycle_analysis.csv')

# Page Configuration for a Premium Visual Studio look
st.set_page_config(
    page_title="VogueAnalytics // Trend Portfolio Engine", 
    page_icon="✨", 
    layout="wide"
)

# Custom High-End Styling Injection
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .brand-header {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #FF2E93, #FF8A00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .brand-sub {
        color: #666666;
        font-size: 1rem;
        margin-bottom: 2rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .attribute-tag {
        background-color: #1a1a1a;
        border: 1px solid #333333;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 0.9rem;
        color: #ffffff;
        display: inline-block;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .attribute-label {
        color: #666666;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.2rem;
    }
    
    .prediction-card {
        background: #0d0d0d;
        border: 1px solid #FF2E93;
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Top Brand Headers
st.markdown('<h1 class="brand-header">VOGUEANALYTICS</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-sub">Predictive Lifecycle & Trend Inventory Matrix</p>', unsafe_allow_html=True)
st.markdown("---")

# Dropdown Selection Menu
st.markdown("### 🔍 Quick Load From Dataset Portfolio")
selected_trend = st.selectbox(
    "Choose a pre-saved trend to pre-fill all configuration diagnostics:", 
    options=["-- Custom Entry --"] + list(df['trend_name'].unique())
)

# Configuration States Logic
if selected_trend != "-- Custom Entry --":
    trend_data = df[df['trend_name'] == selected_trend].iloc[0]
    default_name = str(trend_data['trend_name'])
    default_category = str(trend_data['category'])
    default_platform = str(trend_data['primary_platform'])
    default_material = str(trend_data['primary_fabric_material'])
    default_peak = int(float(trend_data['peak_value']))
    default_velocity = float(trend_data['peak_value'] / trend_data['weeks_to_peak'])
    default_spike = float(trend_data['peak_value'] / trend_data['avg_before_peak'])
    
    # LOCAL PATH BUILDER: Direct look-up inside the images folder
    local_image_path = os.path.join("images", f"{selected_trend}.jpg")
else:
    default_name = "Custom Silhouette"
    default_category = "Apparel"
    default_platform = "TikTok"
    default_material = "Synthetic (Polyester/Nylon)"
    default_peak = 85
    default_velocity = 12.4
    default_spike = 4.5
    local_image_path = None

st.markdown("---")

# Split Screen Dashboard Framework
col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    st.markdown("### 🎛️ Trend Diagnostic Controls")
    trend_input_name = st.text_input("Trend Identifier Label", value=default_name)
    
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        p_opts = ["TikTok", "Instagram", "Pinterest"]
        platform = st.selectbox("Source Driver Platform", p_opts, index=p_opts.index(default_platform) if default_platform in p_opts else 0)
        
        m_opts = ["Synthetic (Polyester/Nylon)", "Natural (Cotton/Linen)", "Mixed Blends"]
        current_m_idx = 0
        if "synthetic" in default_material.lower() or "polyester" in default_material.lower() or "nylon" in default_material.lower() or "spandex" in default_material.lower():
            current_m_idx = 0
        elif "cotton" in default_material.lower() or "linen" in default_material.lower() or "silk" in default_material.lower():
            current_m_idx = 1
        else:
            current_m_idx = 2
        fabric = st.selectbox("Material DNA", m_opts, index=current_m_idx)
        
    with sub_col2:
        peak_value = st.slider("Peak Interest Capacity", 10, 100, default_peak)
        rise_velocity = st.slider("Rise Velocity Index", 0.5, 50.0, default_velocity, step=0.1)
        
    spike_ratio = st.slider("Spike Sharpness Co-efficient (Peak / Baseline)", 1.0, 20.0, default_spike, step=0.1)
    
    platform_enc = {"TikTok": 3, "Instagram": 2, "Pinterest": 1}[platform]
    fabric_enc = 1 if fabric == "Synthetic (Polyester/Nylon)" else 0
    
    # 🖼️ Render Local Offline Image File
    if local_image_path and os.path.exists(local_image_path):
        st.markdown(" ")
        st.markdown("#### 🖼️ Loaded Trend Visual Identity")
        #  NEW CORRECT SYNTAX
        st.image(local_image_path, use_container_width=True, caption=f"Local Verification Asset: {trend_input_name}")
    elif selected_trend != "-- Custom Entry --":
        st.markdown(" ")
        st.info(f"ℹ️ Image placeholder: Place your file at 'images/{selected_trend}.jpg' to render it automatically.")

with col_right:
    st.markdown("### 📊 Predictive Intelligence Output")
    
    if selected_trend != "-- Custom Entry --":
        st.markdown("#### 🏷️ Current Profile Metadata")
        meta_1, meta_2, meta_3 = st.columns(3)
        with meta_1:
            st.markdown('<p class="attribute-label">Category</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="attribute-tag">📂 {default_category}</div>', unsafe_allow_html=True)
        with meta_2:
            st.markdown('<p class="attribute-label">Platform Engine</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="attribute-tag">📱 {platform}</div>', unsafe_allow_html=True)
        with meta_3:
            st.markdown('<p class="attribute-label">Material Composition</p>', unsafe_allow_html=True)
            st.markdown(f'<div class="attribute-tag">🧵 {default_material}</div>', unsafe_allow_html=True)
        st.markdown("---")

    calculate_btn = st.button("Run Predictive Engine →", type="primary", use_container_width=True)
    
    if calculate_btn:
        with st.spinner("Processing trend variables through XGBoost pipeline..."):
            time.sleep(0.4)
            
        input_features = np.array([[rise_velocity, spike_ratio, platform_enc, fabric_enc, peak_value]])
        predicted_weeks = float(model.predict(input_features)[0])
        predicted_weeks = max(0.1, predicted_weeks)
        
        st.markdown(f"""
            <div class="prediction-card">
                <span style="color: #666666; font-size: 0.8rem; text-transform: uppercase; font-weight: 600;">Systemic Shelf Life Remaining</span>
                <h2 style="font-size: 3rem; margin: 0.2rem 0; color: #FF2E93; font-weight: 700;">{predicted_weeks:.1f} <span style="font-size: 1.5rem; color: #ffffff; font-weight: 300;">Weeks Remaining</span></h2>
                <p style="color: #444444; margin: 0; font-size: 0.8rem;">Historical Root Mean Squared Error Bounds: +/- 4.48 weeks</p>
            </div>
        """, unsafe_allow_html=True)
        
        buffer_week = int(max(1, np.floor(predicted_weeks - 2)))
        st.warning(
            f"🚨 **Procurement Alert:** Trend '{trend_input_name}' is displaying structural lifecycle degradation. "
            f"Halt factory supply pipelines and clear material loops by **Week {buffer_week}** to eliminate deadstock surplus risk."
        )
    else:
        st.info("Adjust the diagnostic sliders on the left panel or load a pre-saved profile, then click 'Run Predictive Engine' to compile the real-time decay report.")