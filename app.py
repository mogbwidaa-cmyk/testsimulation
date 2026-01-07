import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت (بيانات المنصة والمهندس مجاهد بشير) ---
NAME = "Mogahed Bashir"
PLATFORM_NAME = "ثوابت"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"

# إعدادات الصفحة
st.set_page_config(page_title=f"محاكاة رسومية - {PLATFORM_NAME}", layout="wide")

# --- التنسيق الجانبي ---
st.sidebar.title(f"منصة {PLATFORM_NAME}")
st.sidebar.markdown(f"**المهندس:** {NAME}")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/{PHONE})")

# --- المحتوى الأساسي ---
st.title("📊 محاكاة هندسية مرئية لحركة البوابة الحرارية")
temp = st.slider("تحكم في درجة الحرارة (°C)", 20, 60, 25)

target_temp = 35

# حساب زاوية الفتح (من 0 إلى 90 درجة)
if temp >= target_temp:
    angle = min(90, (temp - target_temp) * 4.5)
else:
    angle = 0

# --- الرسم الهندسي (Simulation Drawing) ---
fig, ax = plt.subplots(figsize=(6, 6))

# رسم الإطار الثابت (الجدار)
ax.plot([0, 0], [0, 10], color='black', linewidth=5, label='Fixed Frame')

# حساب إحداثيات البوابة بناءً على زاوية الفتح
# نستخدم التحويل من قطبي إلى ديكارتي: x = L*sin(theta), y = L*cos(theta)
theta_rad = np.radians(angle)
x_gate = [0, 8 * np.sin(theta_rad)]
y_gate = [5, 5 + 8 * np.cos(theta_rad)]

# رسم البوابة (Gate)
ax.plot(x_gate, y_gate, color='red', linewidth=4, label='Thermal Gate')

# رسم الشريحة ثنائية المعدن (Bimetallic Strip) تمثيلياً
ax.annotate('Bimetallic Strip', xy=(0, 5), xytext=(3, 2),
            arrowprops=dict(facecolor='blue', shrink=0.05))

# إعدادات الرسم
ax.set_xlim(-2, 12)
ax.set_ylim(-2, 15)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f"Gate Angle: {angle:.1f}° | Temp: {temp}°C")

# عرض الرسم في Streamlit
st.pyplot(fig)



# --- بيانات الحالة ---
col1, col2 = st.columns(2)
with col1:
    st.metric("درجة الحرارة", f"{temp} °C")
with col2:
    status = "مفتوحة" if angle > 0 else "مغلقة"
    st.metric("حالة البوابة", status)

st.write("---")
st.info(f"هذه المحاكاة تعكس تمدد المعادن الفيزيائي. تم التصميم بواسطة المهندس {NAME} لتعزيز أنظمة التحكم الذاتي.")
