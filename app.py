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
st.title("☀️ نظام التبريد الميكانيكي (صندوق مغلق بـ 5 بوابات)")
st.write("نظام متكامل يضم 3 بوابات خلفية وبوابتين جانبيتين تفتح بزاوية 90 درجة لتشكيل قناة تبريد عند 35°C.")

# منزلق الحرارة
temp = st.slider("درجة حرارة الخلية الشمسية (°C)", 20, 60, 25)

# منطق الفيزياء (العتبة 35 درجة)
threshold = 35
# الزاوية تبدأ من 90 (إغلاق الصندوق) وتميل نحو الصفر لفتح القناة
opening_offset = min(90, max(0, (temp - threshold) * 5))
current_angle = 90 - opening_offset 
rad = np.radians(current_angle)

# --- الرسم الهندسي (Simulation Graphics) ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية (طول 10 وحدات)
ax.add_patch(plt.Rectangle((3, 10), 10, 0.6, color='#001f3f', label='Solar PV Panel'))
ax.text(8, 10.8, "SOLAR PV PANEL", color='black', fontweight='bold', ha='center')

# 2. رسم البوابات الخلفية الـ 3 (طول كل واحدة يغطي جزء من اللوح)
gate_positions = [3, 6.3, 9.6] 
gate_length = 3.4 
for x_p in gate_positions:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 + gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6, solid_capstyle='round')
    ax.scatter(x_p, 8, color='black', zorder=5, s=80)

# 3. إضافة البوابات الجانبية (Side Gates) لتشكيل الصندوق
side_gate_len = 2.0 # تمثل الـ 5 سم ميكانيكياً
# البوابة الجانبية اليسرى (تغلق الجانب الأيسر للصندوق)
ax.plot([3, 3 - side_gate_len * np.cos(np.radians(opening_offset))], [8, 8 + side_gate_len * np.sin(np.radians(opening_offset))], color='orange', linewidth=6, label='Side Gates')
# البوابة الجانبية اليمنى (تغلق الجانب الأيمن للصندوق)
ax.plot([13, 13 + side_gate_len * np.cos(np.radians(opening_offset))], [8, 8 + side_gate_len * np.sin(np.radians(opening_offset))], color='orange', linewidth=6)

# 4. توضيح الفراغ الـ 5 سم (Air Gap)
ax.plot([3, 13], [8, 8], 'k--', alpha=0.1)
ax.text(13.5, 9, "5 cm Gap", color='gray', fontsize=9)

# 5. تدفق الهواء عند الفتح
if opening_offset > 15:
    ax.arrow(1, 9, 1.5, 0, head_width=0.3, fc='skyblue', ec='skyblue')
    ax.text(0, 9.5, "Air In", color='blue', fontsize=8)

# إعدادات المشهد
ax.set_xlim(0, 16)
ax.set_ylim(6, 12)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)



# --- البيانات التحليلية ---
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("الحرارة", f"{temp} °C")
with col2:
    st.metric("زاوية الميل", f"{opening_offset:.1f}°")
with col3:
    status = "صندوق مفتوح (تبريد)" if temp > threshold else "صندوق مغلق تماماً"
    st.info(f"حالة النظام: {status}")

st.markdown(f"""
### ⚙️ الإضافات الميكانيكية الجديدة:
- **نظام الصندوق المغلق:** تم إضافة بوابتين جانبيتين (باللون البرتقالي) تقفل جوانب الفراغ الـ 5 سم تماماً في حالة السكون.
- **التمدد الموحد:** عند التسخين، تتحرك البوابات الـ 5 (3 خلفية و 2 جانبية) في تناسق طولي لفتح مجرى الهواء.
""")

st.write(f"**تم التعديل بواسطة المهندس {ENGINEER_NAME} لمنصة {PLATFORM_NAME}.**")
