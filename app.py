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
st.write("محاكاة نظام التبريد الذاتي: فتح البوابات عبر التمدد الميكانيكي للشريحة الحرارية عند 35°C.")

temp = st.slider("Solar Cell Temperature (°C)", 20, 60, 25)

# منطق الفيزياء: الشريحة الحرارية (Thermal Bimetallic Actuator)
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية (Solar PV Panel)
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f', label='Solar PV Panel'))
ax.text(8, 10.8, "SOLAR PV PANEL", color='black', fontweight='bold', ha='center')

# 2. البوابات الجانبية الصفراء (Active Side Gates)
# تفتح للخارج عبر الشريحة الحرارية
side_x_l = 2 - 1.5 * np.sin(rad)
side_y_l = 10 - 2 * np.cos(rad)
ax.plot([2, side_x_l], [10, side_y_l], color='yellow', linewidth=6, label='Side Gates (Yellow)')
ax.text(1, 11, "Side Gate", color='#d4af37', fontsize=9, fontweight='bold')

side_x_r = 14 + 1.5 * np.sin(rad)
side_y_r = 10 - 2 * np.cos(rad)
ax.plot([14, side_x_r], [10, side_y_r], color='yellow', linewidth=6)

# 3. البوابات الحمراء الـ 3 (Main Ventilation Gates)
gate_length = 4.0 
gate_positions = [2, 6, 10]
ax.plot([2, 14], [8, 8], 'k--', alpha=0.2) # Base Line

for x_p in gate_positions:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6, solid_capstyle='round')
    ax.scatter(x_p, 8, color='black', zorder=5)

# توضيح الشريحة الحرارية (Bimetallic Strip)
if angle > 0:
    ax.text(8, 7, "ACTUATED BY BIMETALLIC STRIP", color='red', ha='center', fontweight='bold', fontsize=10)

# 4. تدفق الهواء (Airflow Labels)
if angle > 15:
    for i in range(3):
        ax.arrow(4 + i*4, 4, 0, 3, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.4)
    ax.text(8, 5, "COOL EXTERNAL AIR INTAKE", color='blue', fontweight='bold', ha='center')

# إعدادات الرسم
ax.set_xlim(-2, 18)
ax.set_ylim(3, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower left', fontsize='small')
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
### ⚙️ Technical Mechanism (Bimetallic Actuation):
- **Thermal Actuator:** The gates are operated by a **Bimetallic Strip** (شريحة حرارية).
- **Function:** When the temperature reaches **{threshold}°C**, the thermal expansion difference between the two metals causes the strip to bend, mechanically pushing the gates open without any electrical power.
- **Cooling Path:** Once opened, the system allows for multi-directional airflow (Bottom and Sides) to reduce the panel's temperature and increase efficiency.
""")

st.write(f"**Designed & Programmed by Engineer: {ENGINEER_NAME}**")
