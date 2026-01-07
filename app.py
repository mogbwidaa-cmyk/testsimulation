import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

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

# --- واجهة المحاكاة الرئيسية ---
st.title("☀️ Autonomous Thermal Cooling System Simulation")
st.write("Dynamic simulation showing auto-actuation via Thermal Bimetallic Strips.")

# خيار التفعيل التلقائي
auto_mode = st.checkbox("تفعيل المحاكاة التلقائية (ارتفاع وانخفاض الحرارة)")

if auto_mode:
    t = time.time()
    temp = 35 + 10 * np.sin(2 * np.pi * t / 20) 
    st.info(f"المحاكاة نشطة: درجة الحرارة تتغير تلقائياً...")
else:
    temp = st.slider("Solar Cell Temperature (°C)", 20, 60, 25)

# منطق الفيزياء: الشريحة الحرارية
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. Solar PV Panel
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f'))
ax.text(8, 10.8, "SOLAR PV PANEL", color='black', fontweight='bold', ha='center')

# 2. Side Yellow Gates (Bimetallic)
side_x_l = 2 - 1.5 * np.sin(rad)
side_y_l = 10 - 2 * np.cos(rad)
ax.plot([2, side_x_l], [10, side_y_l], color='yellow', linewidth=6)
ax.text(0.5, 9.5, "SIDE GATE\n(BIMETALLIC)", color='#d4af37', fontsize=8, fontweight='bold', ha='right')

side_x_r = 14 + 1.5 * np.sin(rad)
side_y_r = 10 - 2 * np.cos(rad)
ax.plot([14, side_x_r], [10, side_y_r], color='yellow', linewidth=6)
ax.text(15.5, 9.5, "SIDE GATE\n(BIMETALLIC)", color='#d4af37', fontsize=8, fontweight='bold', ha='left')

# 3. Main Rear Gates (Red)
gate_length = 4.0 
gate_positions = [2, 6, 10]
ax.plot([2, 14], [8, 8], 'k--', alpha=0.2) # Base Line

for x_p in gate_positions:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6)
    ax.scatter(x_p, 8, color='black', zorder=5)

# --- تعريفات حالات البوابات بناءً على الحرارة ---
if temp < threshold:
    # حالة الإغلاق (أقل من 35)
    ax.text(8, 9, "GATES CLOSED: PREVENTING HEAT LOSS (TEMP < 35°C)", 
            color='gray', ha='center', fontweight='bold', bbox=dict(facecolor='white', alpha=0.5))
else:
    # حالة التبريد (أعلى من 35)
    ax.text(8, 9, "GATES OPEN: COOLING AIRFLOW INTAKE (TEMP > 35°C)", 
            color='green', ha='center', fontweight='bold', bbox=dict(facecolor='white', alpha=0.7))
    
    # أسهم دخول الهواء الجانبي
    ax.arrow(-0.5, 9, 1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.7)
    ax.arrow(16.5, 9, -1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.7)
    ax.text(-1, 8.5, "Side Air In", color='orange', fontsize=8, fontweight='bold')
    ax.text(17, 8.5, "Side Air In", color='orange', fontsize=8, fontweight='bold')
    
    # أسهم دخول الهواء السفلي
    for i in range(3):
        ax.arrow(4 + i*4, 4, 0, 3, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.4)
    ax.text(8, 5, "EXTERNAL COOL AIR INFLOW", color='blue', fontweight='bold', ha='center')

# إعدادات الرسم
ax.set_xlim(-3, 19)
ax.set_ylim(3, 12)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

if auto_mode:
    time.sleep(1)
    st.rerun()

# --- البيانات التحليلية وملخص المشروع ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Temperature", f"{temp:.1f} °C")
with c2:
    st.metric("Opening Angle", f"{angle:.1f}°")
with c3:
    status = "Active Cooling" if temp > threshold else "System Closed"
    st.info(f"Status: {status}")

st.markdown("""
### ⚙️ ملخص المشروع (Project Abstract):
يهدف هذا المشروع إلى تطوير نظام تبريد هوائي ميكانيكي ذاتي التشغيل للألواح الشمسية الكهروضوئية... (النص الكامل المعتمد مسبقاً)
""")

st.write(f"**Designed & Programmed by Engineer: {ENGINEER_NAME} for {PLATFORM_NAME}**")
