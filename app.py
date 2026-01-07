import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت المهنية (ثوابت منصة محاكاة براءة الاختراع) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = "https://wa.me/966501318054"

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- القائمة الجانبية الثابتة ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- الواجهة الرئيسية ---
st.title("☀️ Autonomous Thermal Cooling System Simulation")
st.write("Mechanical simulation of the self-cooling system: Gates actuated by Thermal Bimetallic Strips at 35°C.")

temp = st.slider("Solar Cell Temperature (°C)", 20, 60, 25)

# منطق الفيزياء: الشريحة الحرارية (Thermal Bimetallic Actuator)
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. Solar PV Panel
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f', label='Solar PV Panel'))
ax.text(8, 10.8, "SOLAR PV PANEL", color='black', fontweight='bold', ha='center')

# 2. Side Yellow Gates (Actuated by Bimetallic Strip)
# Left Side Gate
side_x_l = 2 - 1.5 * np.sin(rad)
side_y_l = 10 - 2 * np.cos(rad)
ax.plot([2, side_x_l], [10, side_y_l], color='yellow', linewidth=6, label='Bimetallic Side Gates')
ax.text(0.5, 9.5, "SIDE GATE\n(BIMETALLIC)", color='#d4af37', fontsize=8, fontweight='bold', ha='right')

# Right Side Gate
side_x_r = 14 + 1.5 * np.sin(rad)
side_y_r = 10 - 2 * np.cos(rad)
ax.plot([14, side_x_r], [10, side_y_r], color='yellow', linewidth=6)
ax.text(15.5, 9.5, "SIDE GATE\n(BIMETALLIC)", color='#d4af37', fontsize=8, fontweight='bold', ha='left')

# 3. Main Rear Gates (Actuated by Bimetallic Strip)
gate_length = 4.0 
gate_positions = [2, 6, 10]
ax.plot([2, 14], [8, 8], 'k--', alpha=0.2) # Base Line

for x_p in gate_positions:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6, label='Main Gates' if x_p==2 else "")
    ax.scatter(x_p, 8, color='black', zorder=5)

# Indication of Bimetallic Strip Activation
if angle > 0:
    ax.text(8, 7, "ACTUATED BY BIMETALLIC STRIPS", color='red', ha='center', fontweight='bold', fontsize=10)

# 4. Airflow Visualization
if angle > 15:
    for i in range(3):
        ax.arrow(4 + i*4, 4, 0, 3, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.4)
    ax.text(8, 5, "EXTERNAL COOL AIR INFLOW", color='blue', fontweight='bold', ha='center')

# Drawing settings
ax.set_xlim(-3, 19)
ax.set_ylim(3, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower left', fontsize='x-small')
st.pyplot(fig)



# --- البيانات التحليلية ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Temperature", f"{temp} °C")
with c2:
    st.metric("Opening Angle", f"{angle:.1f}°")
with c3:
    status = "Active Cooling" if temp > threshold else "System Closed"
    st.info(f"Status: {status}")

st.markdown(f"""
### ⚙️ Technical Specification (Multi-Gate Actuation):
- **Bimetallic Side Gates (Yellow):** These lateral gates open outward via a **Bimetallic Strip** to vent hot air trapped at the sides.
- **Bimetallic Main Gates (Red):** Located at the 5cm base line, these gates open via thermal expansion to scoop external air.
- **Thermal Actuation Logic:** No electricity is required. The **Bimetallic Strip** reacts to the panel's heat, bending at **{threshold}°C** to provide the mechanical force needed to open the entire cooling box.
""")

st.write(f"**Developed by Engineer: {ENGINEER_NAME} for {PLATFORM_NAME}**")
