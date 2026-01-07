import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت المهنية (ثوابت المنصة) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = "https://wa.me/966501318054"

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- القائمة الجانبية ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- الواجهة الرئيسية ---
st.title("☀️ نظام التبريد المتكامل (خلفي + جانبي)")
st.write("محاكاة لنظام تبريد بـ 3 بوابات خلفية وبوابتين جانبيتين (5 سم) تفتح جميعاً عند 35°C.")

temp = st.slider("درجة حرارة الخلية الشمسية (°C)", 20, 60, 25)

# منطق الفيزياء
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية (العرض 10 وحدات)
panel_width = 10
ax.add_patch(plt.Rectangle((3, 10), panel_width, 0.6, color='#001f3f', label='Solar PV Panel'))

# 2. رسم البوابات الجانبية (Side Gates) - 5 سم (0.5 وحدة افتراضية)
side_gate_len = 1.5 
# البوابة الجانبية اليسرى
ax.plot([3, 3 - side_gate_len * np.cos(rad)], [10, 10 - side_gate_len * np.sin(rad)], color='orange', linewidth=4, label='Side Gates (5cm)')
# البوابة الجانبية اليمنى
ax.plot([13, 13 + side_gate_len * np.cos(rad)], [10, 10 - side_gate_len * np.sin(rad)], color='orange', linewidth=4)

# 3. رسم البوابات الخلفية الـ 3 (Rear Gates)
gate_positions = [3, 6.3, 9.6] 
gate_length = 3.4 # لتغطية طول اللوح
for x_p in gate_positions:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=5)
    ax.scatter(x_p, 8, color='black', zorder=5)

# 4. توضيح الفراغ الخلفي (5 cm Gap)
ax.plot([3, 13], [8, 8], 'k--', alpha=0.1)
ax.text(13.5, 9, "5 cm Rear Gap", color='gray', fontsize=9, va='center')

# 5. تدفق الهواء الشامل
if angle > 10:
    # هواء من الخلف
    for i in range(4):
        ax.arrow(4 + i*2.5, 2, 0, 4, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.4)
    # هواء من الجوانب
    ax.arrow(1, 10, 1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.4)
    ax.arrow(15, 10, -1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.4)

# إعدادات الرسم
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower left')
st.pyplot(fig)



# --- التحليل الفني ---
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.metric("درجة الحرارة", f"{temp} °C")
    st.write(f"**الحالة:** {'تبريد شامل نشط' if temp > threshold else 'نظام مغلق'}")
with col2:
    st.metric("زاوية الفتح", f"{angle:.1f}°")
    st.write("**التكوين:** 3 بوابات خلفية + 2 بوابة جانبية")

st.info(f"هذا التصميم المسجل في منصة **{PLATFORM_NAME}** يضمن طرد الحرارة من جميع الاتجاهات المحيطة بالخلية الشمسية.")
st.write(f"**بواسطة المهندس: {ENGINEER_NAME}**")
