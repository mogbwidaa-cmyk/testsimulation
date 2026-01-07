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

# --- واجهة المحاكاة الرئيسية ---
st.title("☀️ نظام التبريد الميكانيكي بـ 3 بوابات متصلة")
st.write("محاكاة لنظام تبريد خلفي بمسافة 5 سم، حيث تفتح 3 بوابات تغطي كامل طول اللوح عند 35°C.")

# منزلق الحرارة
temp = st.slider("درجة حرارة الخلية الشمسية (°C)", 20, 60, 25)

# منطق الفيزياء (العتبة 35 درجة)
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))

# --- الرسم الهندسي (Simulation Graphics) ---
fig, ax = plt.subplots(figsize=(12, 6))

# 1. رسم الخلية الشمسية (طول اللوح 12 وحدة افتراضية)
ax.add_patch(plt.Rectangle((2, 10), 12, 0.6, color='#001f3f', label='Solar PV Panel'))
ax.text(8, 10.8, "SOLAR PV PANEL (TOP VIEW)", color='black', fontweight='bold', ha='center')

# 2. توضيح فراغ الـ 5 سم خلف الخلية
ax.annotate('', xy=(14.5, 8), xytext=(14.5, 10),
            arrowprops=dict(arrowstyle='<->', color='gray'))
ax.text(14.7, 9, "5 cm Air Gap", color='gray', va='center', fontsize=10)

# 3. رسم 3 بوابات ميكانيكية (Mechanical Gates)
# طول اللوح الكلي 12، لذا كل بوابة طولها 4 وحدات لتغطي كامل الطول
gate_positions = [2, 6, 10] # نقاط الارتكاز (Pivots)
gate_length = 4
rad = np.radians(angle)

for x_p in gate_positions:
    # حساب إحداثيات البوابة المتحركة
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    
    # رسم البوابة
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6, solid_capstyle='round')
    # رسم المفصلة (Pivot)
    ax.scatter(x_p, 8, color='black', zorder=5, s=100)

# تسمية البوابات
ax.text(8, 6.5, "3RD GENERATION MECHANICAL VENTILATION GATES", color='red', ha='center', fontweight='bold', fontsize=9)

# 4. تدفق الهواء عند الفتح
if angle > 10:
    for i in range(5):
        ax.arrow(3 + i*2.2, 1, 0, 4, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.5)
    ax.text(1, 3, "COOLING AIRFLOW", color='blue', fontweight='bold', rotation=90)

# إعدادات المشهد الرسومي
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)



# --- البيانات التحليلية ---
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("درجة الحرارة الحالية", f"{temp} °C")
with col2:
    st.metric("زاوية الفتح الميكانيكي", f"{angle:.1f}°")
with col3:
    status = "تبريد فعال" if temp > threshold else "وضع الاستعداد"
    st.info(f"حالة النظام: {status}")

st.markdown(f"""
### ⚙️ المواصفات الفنية للابتكار:
- **المشغل:** لوح ألمنيوم حساس للحرارة (Thermal Actuator).
- **التصميم:** 3 بوابات متتابعة تغطي كامل مساحة سطح التبادل الحراري خلف الخلية.
- **آلية العمل:** تفتح البوابات بمجرد تمدد المعدن عند **{threshold}°C** للسماح بتدفق هواء طبيعي (Natural Convection).
""")

st.write(f"**تم إعداد هذا النموذج بواسطة المهندس {ENGINEER_NAME} لدعم ملف براءة الاختراع.**")
