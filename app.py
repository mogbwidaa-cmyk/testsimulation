import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- ثوابت المهندس (من السيرة الذاتية) ---
NAME = "Mogahed Bashir" [cite: 1]
LOCATION = "Madinah, Saudi Arabia" [cite: 2]
PHONE = "+966 50 131 8054" [cite: 3]
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/" [cite: 5]
PLATFORM_NAME = "محاكاة براءة الاختراع"

st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- الشريط الجانبي الثابت ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {NAME}") [cite: 1]
st.sidebar.info(f"📍 {LOCATION}") [cite: 2]
st.sidebar.divider()
st.sidebar.markdown(f"📞 {PHONE}") [cite: 3]
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})") [cite: 5]
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/966501318054)")

# --- واجهة المحاكاة ---
st.title("☀️ نظام التبريد الذاتي للخلايا الشمسية (فراغ 5 سم)")
temp = st.slider("درجة حرارة الخلية (°C)", 20, 65, 25)

# منطق الفتح عند 35 درجة
threshold = 35
angle = min(90, max(0, (temp - threshold) * 4))

# --- الرسم الميكانيكي ---
fig, ax = plt.subplots(figsize=(10, 5))

# رسم الخلية الشمسية
ax.add_patch(plt.Rectangle((1, 10), 10, 0.5, color='#1a237e', label='Solar Panel'))

# رسم فراغ الـ 5 سم (Air Gap)
ax.text(11.5, 8.5, "5 cm Air Gap", color='gray', fontsize=10)
ax.plot([11.2, 11.2], [10, 7.5], 'k--', alpha=0.3)

# رسم البوابات الميكانيكية (خلف الفراغ)
rad = np.radians(angle)
# البوابة الأولى
ax.plot([1, 1 + 3*np.cos(rad)], [7.5, 7.5 - 3*np.sin(rad)], color='red', linewidth=4, label='Mechanical Flaps')
# البوابة الثانية
ax.plot([5, 5 + 3*np.cos(rad)], [7.5, 7.5 - 3*np.sin(rad)], color='red', linewidth=4)

# تدفق الهواء (Airflow)
if temp > threshold:
    for i in range(3):
        ax.arrow(2 + i*3, 2, 0, 4, head_width=0.3, fc='skyblue', ec='skyblue')
    ax.text(5, 4, "Natural Convection Flow", color='blue', fontweight='bold')

ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.axis('off')
st.pyplot(fig)


st.divider()
st.success(f"تم حساب التمدد الميكانيكي بناءً على معايير الهندسة الميكانيكية - المهندس {NAME}") [cite: 1]
