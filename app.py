import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- ثوابت المنصة والمهندس مجاهد بشير ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
PHONE = "+966501318054"

st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- الشريط الجانبي الثابت ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- واجهة المحاكاة ---
st.title("☀️ نظام التبريد الذاتي للخلايا الشمسية (Solar PV Self-Cooling)")
st.write("محاكاة ميكانيكية لفتح بوابات التهوية الخلفية باستخدام تمدد لوح الألمنيوم.")

temp = st.slider("درجة حرارة الخلية الشمسية (°C)", 20, 60, 25)

# الحسابات الفيزيائية
threshold = 35
# معامل تمدد الألمنيوم لرفع ذراع البوابة
expansion_factor = max(0, temp - threshold)
angle = min(90, expansion_factor * 6) # زاوية الفتح

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(10, 5))

# رسم الخلية الشمسية (Solar Panel)
ax.add_patch(plt.Rectangle((1, 8), 10, 1, color='navy', label='Solar PV Panel'))

# رسم البوابة الخلفية (Cooling Gate)
rad = np.radians(angle)
ax.plot([1, 1 + 4*np.cos(rad)], [8, 8 - 4*np.sin(rad)], color='red', linewidth=5, label='Mechanical Gate')

# رسم لوح الألمنيوم المشغل
ax.plot([1, 11], [7.5, 7.5], color='silver', linewidth=8, label='Aluminum Actuator')

# أسهم تدفق الهواء (Airflow)
if angle > 10:
    ax.arrow(3, 2, 0, 4, head_width=0.3, fc='skyblue', ec='skyblue')
    ax.text(3.5, 4, "Cold Air Inflow", color='blue', fontsize=10)

ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.axis('off')
st.pyplot(fig)



st.divider()
st.info(f"عند درجة {temp}°C، النظام في حالة {'تبريد نشط' if temp > 35 else 'سكون'}. تم التصميم بواسطة {ENGINEER_NAME}.")
