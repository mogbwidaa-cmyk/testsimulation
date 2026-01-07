import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت (بيانات المهندس مجاهد بشير ومنصة محاكاة براءة الاختراع) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = f"https://wa.me/{PHONE.replace(' ', '').replace('+', '')}"

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- التنسيق الجانبي (ثوابت التواصل) ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- واجهة المحاكاة ---
st.title(f"⚙️ محاكاة براءة الاختراع: نظام التهوية الحراري الذاتي")
st.write("محاكاة ميكانيكية توضح استجابة البوابة لتمدد الشريحة ثنائية المعدن (Bimetallic Strip).")

# منزلق درجة الحرارة
temp = st.slider("درجة الحرارة المحيطة (°C)", 20, 60, 25)

# منطق الفيزياء (Logic)
threshold = 35
if temp > threshold:
    # زاوية الفتح تزداد تدريجياً (محاكاة لسوليد وورك)
    angle = min(90, (temp - threshold) * 4) 
    status = "OPENING / تمدد حراري"
    color = "green"
else:
    angle = 0
    status = "CLOSED / انكماش"
    color = "red"

# --- الرسم الهندسي (Simulation Graphics) ---
fig, ax = plt.subplots(figsize=(7, 7))

# 1. رسم الإطار الثابت (Fixed Structure)
ax.plot([-1, -1], [0, 10], 'k-', linewidth=10) # الجدار الأيسر
ax.plot([10, 10], [0, 10], 'k-', linewidth=10) # الجدار الأيمن
ax.plot([-1, 10], [10, 10], 'k-', linewidth=5)  # السقف

# 2. حساب حركة البوابة (تفتح من المنتصف أو كبوابة علوية)
rad = np.radians(angle)
x_gate = [0, 8 * np.cos(rad)]
y_gate = [10, 10 - 8 * np.sin(rad)]

# 3. رسم البوابة (The Flap)
ax.plot(x_gate, y_gate, color=color, linewidth=6, label='Ventilation Gate')

# 4. رسم سهم تدفق الهواء (Airflow) عند الفتح
if angle > 10:
    ax.arrow(4, -2, 0, 5, head_width=0.5, head_length=1, fc='blue', ec='blue', label='Airflow')
    ax.text(4.5, 0, "دخول الهواء", color='blue', fontsize=12)

# تنسيق المشهد الرسومي
ax.set_xlim(-5, 15)
ax.set_ylim(-5, 15)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f"الحرارة: {temp}°C | الزاوية: {angle:.1f}°", fontsize=14, fontweight='bold')

# عرض الرسم في Streamlit
st.pyplot(fig)



# --- لوحة البيانات ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"### الحالة الحالية: :{color}[{status}]")
with c2:
    st.markdown("### المبدأ الفيزيائي")
    st.write("تحويل الطاقة الحرارية إلى شغل ميكانيكي عبر اختلاف معامل التمدد الطولي للمركبات المعدنية.")

st.info(f"تم تطوير هذه المحاكاة لتعزيز ملف براءة الاختراع الخاص بالمهندس {ENGINEER_NAME} في تطبيقات الصيانة التنبؤية.")
