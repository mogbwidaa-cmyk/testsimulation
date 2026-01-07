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

# --- واجهة المحاكاة الرئيسية ---
st.title("☀️ نظام التبريد الميكانيكي (موقع القاعدة السفلي)")
st.write("محاكاة للبوابات الموجودة عند مستوى القاعدة (5 سم خلف اللوح) وتفتح للخارج لسحب الهواء.")

temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25)

# منطق الفيزياء (العتبة 35 درجة)
threshold = 35
# الزاوية تفتح للخارج (لأسفل) لسحب الهواء
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية (المستوى العلوي Y=10)
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f', label='Solar PV Panel'))

# 2. رسم البوابات الجانبية الصفراء (Side Gates) - تربط بين اللوح والقاعدة
ax.plot([2, 2], [8, 10], color='yellow', linewidth=6, label='Side Support Gates')
ax.plot([14, 14], [8, 10], color='yellow', linewidth=6)

# 3. رسم البوابات الـ 3 (موقعها عند الخط المتقطع Y=8)
# طول البوابات الـ 3 يغطي كامل المسافة بين البوابات الصفراء
gate_length = 4.0 
gate_positions = [2, 6, 10]

# رسم الخط المتقطع (القاعدة) كمرجع خلف البوابات
ax.plot([2, 14], [8, 8], 'k--', alpha=0.3)

for x_p in gate_positions:
    # الفتح من مستوى القاعدة (Y=8) باتجاه الخارج (Y < 8)
    # المفصلات (Pivots) عند مستوى الخط المتقطع
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    
    # رسم البوابة باللون الأحمر (موقعها الأصلي على الخط المتقطع)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6, solid_capstyle='round')
    ax.scatter(x_p, 8, color='black', zorder=5, s=80) # المفصلة عند القاعدة

# 4. محاكاة سحب الهواء من الأسفل للداخل
if angle > 15:
    for i in range(4):
        ax.arrow(3 + i*2.7, 4, 0, 3.5, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.5)
    ax.text(8, 5, "EXTERNAL AIR INTAKE", color='blue', fontweight='bold', ha='center')

# إعدادات الرسم
ax.set_xlim(0, 16)
ax.set_ylim(3, 12)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# --- البيانات التحليلية ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("الحرارة", f"{temp} °C")
with c2:
    st.metric("زاوية الفتح للخارج", f"{angle:.1f}°")
with c3:
    status = "سحب هواء نشط" if temp > threshold else "صندوق مغلق"
    st.info(f"حالة النظام: {status}")

st.markdown(f"""
### ⚙️ الوصف الميكانيكي المحدث:
- **الموقع:** تم نقل مفصلات البوابات الـ 3 لتكون موازية لخط القاعدة (على بعد 5 سم من اللوح).
- **آلية الفتح:** تفتح البوابات للخارج لتعمل كـ "مغارف هواء" (Air Scoops) تسحب تيار الهواء المحيط وتوجهه لداخل الفراغ خلف الخلية.
- **التغطية:** البوابات الصفراء الجانبية تغلق الصندوق من الأطراف، بينما البوابات الحمراء تفتح وتغلق القاعدة بالكامل.
""")

st.write(f"**تم التعديل الهندسي بواسطة المهندس {ENGINEER_NAME} لدعم براءة الاختراع.**")
