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
st.title("☀️ نظام التبريد الميكانيكي بالبوابات القائمة (90°)")
st.write("محاكاة لنظام تبريد بـ 5 بوابات (3 خلفية و2 جانبية) بطول 5 سم، تفتح جميعاً في اتجاه واحد عند 35°C.")

temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25)

# منطق الفيزياء
threshold = 35
# البوابة تبدأ من زاوية 90 (قائمة لسد الفراغ) وتميل للفتح عند التسخين
tilt = min(90, max(0, (temp - threshold) * 6))
current_angle = 90 - tilt 

# --- الرسم الهندسي (Simulation Graphics) ---
fig, ax = plt.subplots(figsize=(14, 7))

# 1. رسم الخلية الشمسية (Solar PV Panel)
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f', label='Solar PV Panel'))
ax.text(8, 10.8, "SOLAR PANEL", color='black', fontweight='bold', ha='center')

# 2. رسم مسار القناة (5cm Air Gap)
ax.plot([2, 14], [8, 8], 'k--', alpha=0.1)

# 3. رسم البوابات الـ 5 بطول 5 سم (1.5 وحدة رسم) في اتجاه واحد
gate_length = 1.5 
# توزيع البوابات بناءً على رسمك اليدوي (Pivots)
gate_positions = [2, 5, 8, 11, 14] 
rad = np.radians(current_angle)

for x_p in gate_positions:
    # البوابات تفتح من الأسفل (Y=8) باتجاه اللوح (Y=10)
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 + gate_length * np.sin(rad)
    
    # رسم البوابة باللون الأحمر
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=5)
    # رسم المفصلة (Pivot) كما في رسمك اليدوي
    ax.scatter(x_p, 8, color='black', zorder=5, s=80)

# 4. محاكاة تيار الهواء (Airflow)
if tilt > 15:
    ax.arrow(0, 9, 1.5, 0, head_width=0.3, fc='skyblue', ec='skyblue')
    for i in range(4):
        ax.arrow(3 + i*3, 7.5, 1.2, 0.8, head_width=0.2, fc='skyblue', ec='skyblue', alpha=0.4)
    ax.text(14.5, 9, "Air Out", color='blue', fontweight='bold')

# إعدادات الرسم
ax.set_xlim(-1, 17)
ax.set_ylim(5, 12)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)


# --- لوحة البيانات ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("الحرارة", f"{temp} °C")
with c2:
    status = "إغلاق تام (90°)" if temp <= threshold else "انفتاح انسيابي"
    st.write(f"**الوضعية:** {status}")
with c3:
    st.metric("زاوية الميل", f"{tilt:.1f}°")

st.info("تم ضبط طول البوابات بـ 5 سم لتتطابق تماماً مع مسافة الفراغ خلف اللوح، مما يضمن كفاءة ميكانيكية قصوى.")
st.write(f"**التطوير الهندسي: المهندس {ENGINEER_NAME}**")
