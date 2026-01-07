import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Platform Constants (ثوابت المنصة) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = f"https://wa.me/{PHONE.replace(' ', '').replace('+', '')}"

st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- Sidebar (بيانات التواصل الثابتة) ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**Engineer:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **Contact:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- Main Simulation ---
st.title("🏗️ Thermal Expansion System Simulation")
temp = st.slider("Aluminum Plate Temperature (°C)", 20, 60, 25)

# Engineering Logic
threshold = 35
alpha_al = 23e-6 
expansion = 1000 * alpha_al * max(0, temp - threshold)
angle = min(90, expansion * 60) if temp > threshold else 0

# Drawing the Simulation
fig, ax = plt.subplots(figsize=(10, 6))

# 1. Aluminum Plate (Sensing Element)
ax.barh(2, 10 + expansion, color='silver', height=0.6, label='Aluminum Actuator Plate')
ax.text(5, 2.8, "ALUMINUM ACTUATOR PLATE", fontweight='bold', color='darkgrey')

# 2. Fixed Frame
ax.plot([10, 10], [0, 10], 'k-', linewidth=6, label='Fixed Support Frame')
ax.text(10.2, 2, "FIXED FRAME", rotation=90)

# 3. Moving Gate
theta = np.radians(angle)
gate_x = [10, 10 + 6 * np.sin(theta)]
gate_y = [8, 8 + 6 * np.cos(theta)]
ax.plot(gate_x, gate_y, color='red', linewidth=5, label='Ventilation Gate')
ax.text(gate_x[1], gate_y[1], "VENTILATION GATE", color='red', fontweight='bold')

# 4. Mechanical Linkage (Pivot)
ax.scatter(10, 8, color='black', s=100, zorder=5) # Pivot Point
ax.text(9, 8.2, "PIVOT JOINT")

# 5. Airflow Indicators
if angle > 10:
    ax.arrow(13, 12, 0, -5, head_width=0.4, fc='blue', ec='blue')
    ax.text(12.5, 13, "AIRFLOW", color='blue', fontweight='bold')

# Final Plot Adjustments
ax.set_xlim(0, 20)
ax.set_ylim(-2, 15)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower left')
st.pyplot(fig)



st.divider()
st.success(f"This simulation is registered under **{PLATFORM_NAME}** - Mechanical Analysis by {ENGINEER_NAME}.")
