import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت (بيانات المهندس والمنصة) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = "https://wa.me/966501318054"

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# --- القائمة الجانبية (ثوابت التواصل) ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- واجهة المحاكاة ---
st.title("☀️ نظام التبريد الميكانيكي للخلايا الشمسية")
st.write("تصميم يعتمد على وجود فراغ 5 سم خلف الخلية مع بوابات تفتح آلياً عند 35°C.")

temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25)

# منطق الفيزياء
threshold = 35
# زاوية الفتح
angle = min(90, max(0, (temp - threshold) * 5))

# --- الرسم الهندسي للمحاكاة ---
fig, ax = plt.subplots(figsize=(10, 6))

# 1. رسم الخلية الشمسية (Solar Panel)
ax.add_patch(plt.Rectangle((2, 10), 10, 0.6, color='#001f3f', label='Solar PV Panel'))
ax.text(5.5, 10.8, "SOLAR PANEL", color='black', fontweight='bold', ha='center')

# 2. تحديد الفراغ (5 cm Gap)
ax.plot([2, 12], [8, 8], 'k--', alpha=0.2) # خط وهمي يمثل نهاية الفراغ
ax.annotate('', xy=(13, 8), xytext=(13, 10),
            arrowprops=dict(arrowstyle='<->', color='gray'))
ax.text(13.2, 9, "5 cm Gap", color='gray', va='center')

# 3. رسم البوابات الميكانيكية (Mechanical Gates) خلف الفراغ
rad = np.radians(angle)
# سنرسم بوابتين لتوضيح النظام
for x_pos in [4, 9]:
    # نقطة الارتكاز (Pivot) عند Y=8 (بعد الفراغ بـ 5 سم افتراضاً)
    gate_x = [x_pos, x_pos + 3 * np.cos(rad)]
    gate_y = [8, 8 - 3 * np.sin(rad)]
    ax.plot(gate_x, gate_y, color='red', linewidth=5, label='Mechanical Gate' if x_pos==4 else "")
    ax.scatter(x_pos, 8, color='black', zorder=5) # المفصلة

# 4. تدفق الهواء (Airflow)
if angle > 10:
    for i in range(3):
        ax.arrow(5 + i*2, 2, 0, 4, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.6)
    ax.text(1, 4, "Natural Airflow", color='blue', fontweight='bold', rotation=90)

# إعدادات المشهد
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower left')
st.pyplot(fig)



# --- البيانات التحليلية ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.info(f"الحالة الحالية: {'نظام تبريد نشط' if temp > threshold else 'نظام مغلق'}")
with c2:
    st.success(f"زاوية فتح البوابة: {angle:.1f} درجة")

st.write(f"**تم إعداد هذه المحاكاة بواسطة المهندس {ENGINEER_NAME} لدعم ملف براءة الاختراع.**")
