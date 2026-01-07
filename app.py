import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت الأساسية ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
THRESHOLD_TEMP = 35

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, page_icon="💡", layout="wide")

# --- الشريط الجانبي (ثوابت التواصل) ---
st.sidebar.title(PLATFORM_NAME)
st.sidebar.markdown(f"**إشراف المهندس:**\n{ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **رقم التواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)](https://wa.me/{PHONE.replace(' ', '')})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- واجهة المحاكاة الرئيسية ---
st.title(f"🚀 {PLATFORM_NAME}")
st.subheader("نظام البوابة ذاتية الحركة بالتمدد الحراري")

# تحكم المستخدم في الحرارة
temp = st.select_slider("درجة الحرارة المحيطة (°C)", options=list(range(20, 61)), value=25)

# منطق فتح البوابة
if temp >= THRESHOLD_TEMP:
    # حساب زاوية الفتح (تزداد بزيادة الحرارة بحد أقصى 90 درجة)
    angle = min(90, (temp - THRESHOLD_TEMP) * 5)
    status_text = f"البوابة مفتوحة بزاوية {angle:.1f}°"
    status_color = "green"
else:
    angle = 0
    status_text = "البوابة مغلقة (درجة الحرارة منخفضة)"
    status_color = "red"

# --- رسم السيموليشن (Visual Simulation) ---
fig, ax = plt.subplots(figsize=(8, 6))

# رسم الإطار الثابت (Fixed Frame)
ax.plot([0, 0], [0, 10], color='black', linewidth=8, label='إطار ثابت')

# حساب حركة البوابة (تتحرك المفصلة عند النقطة 0,5)
theta_rad = np.radians(angle)
# إحداثيات نهاية البوابة بناءً على الزاوية
x_end = 8 * np.sin(theta_rad)
y_end = 5 + 8 * np.cos(theta_rad)

# رسم البوابة المتحركة
ax.plot([0, x_end], [5, y_end], color='red', linewidth=6, label='البوابة المتحركة')

# إضافة مؤشر للشريحة ثنائية المعدن
if angle > 0:
    ax.annotate('تمدد حراري!', xy=(x_end/2, (5+y_end)/2), xytext=(5, 8),
                arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=12, color='orange')

# تنسيق الرسم البياني
ax.set_xlim(-2, 12)
ax.set_ylim(-2, 15)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f"حالة النظام عند {temp}°C", fontsize=15)

# عرض الرسم
st.pyplot(fig)

# --- تفاصيل الحالة ---
st.markdown(f"### الحالة الحالية: :{status_color}[{status_text}]")

st.divider()
st.info(f"هذا المشروع مسجل ضمن منصة **{PLATFORM_NAME}** كنموذج أولي لابتكار ميكانيكي يعتمد على الفيزياء التطبيقية في الصيانة التنبؤية.")
