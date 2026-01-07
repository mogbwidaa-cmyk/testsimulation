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
st.title("☀️ نظام التبريد الميكانيكي (سحب الهواء الخارجي)")
st.write("محاكاة للبوابات التي تفتح باتجاه عكس اللوح (للخارج) لتوجيه الهواء البارد مباشرة إلى الخلية.")

temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25)

# منطق الفيزياء (العتبة 35 درجة)
threshold = 35
# الزاوية تتحرك للخارج (عكس اتجاه اللوح)
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية (طول 12 وحدة)
ax.add_patch(plt.Rectangle((2, 10), 12, 0.6, color='#001f3f', label='Solar PV Panel'))

# 2. رسم البوابات الجانبية الصفراء (Side Gates) - ثابتة كما هي
ax.plot([2, 2], [8, 10], color='yellow', linewidth=6, label='Side Gates (Fixed)')
ax.plot([14, 14], [8, 10], color='yellow', linewidth=6)

# 3. رسم البوابات الـ 3 الرئيسية (مجموعها يغطي طول اللوح وتفتح للخارج)
gate_length = 4.0 # 4 * 3 = 12 (طول اللوح بالكامل)
gate_positions = [2, 6, 10]

for x_p in gate_positions:
    # الفتح باتجاه الأسفل والخارج (عكس اللوح)
    # Pivot عند Y=10 (ملامسة للوح) والفتح لأسفل Y=8 وما دون
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 10 - gate_length * np.sin(rad)
    
    # رسم البوابة باللون الأحمر (تفتح للخارج)
    ax.plot([x_p, x_p + gate_length], [8, 8], color='red', alpha=0.3, linestyle='--') # وضع الإغلاق
    ax.plot([x_p, x_end], [10, y_end], color='red', linewidth=6, solid_capstyle='round')
    ax.scatter(x_p, 10, color='black', zorder=5, s=80) # المفصلة عند اللوح

# 4. تدفق الهواء من الخارج للداخل
if angle > 15:
    for i in range(3):
        ax.arrow(4 + i*4, 4, 0, 3, head_width=0.4, fc='skyblue', ec='skyblue', alpha=0.6)
    ax.text(8, 5, "EXTERNAL COOL AIR INFLOW", color='blue', fontweight='bold', ha='center')

# إعدادات الرسم
ax.set_xlim(0, 16)
ax.set_ylim(4, 12)
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
    status = "سحب هواء خارجي" if temp > threshold else "إغلاق حراري"
    st.info(f"الحالة: {status}")

st.markdown(f"""
### ⚙️ التحليل الميكانيكي للتعديل:
- **توجيه التدفق:** تفتح البوابات الحمراء الآن لأسفل وبعيداً عن اللوح، مما يعمل كمغرفة (Scoop) لسحب الهواء البارد من المحيط الخارجي.
- **تغطية كاملة:** تم ضبط طول البوابات الـ 3 لتعادل بالضبط طول اللوح (12 وحدة)، مما يضمن عدم وجود تسريب عند الإغلاق.
- **الهيكل الجانبي:** البوابات الصفراء تحافظ على ثبات "الصندوق" جانبياً لضمان توجيه الهواء عبر الفتحات الرئيسية فقط.
""")

st.write(f"**تم التطوير الهندسي بواسطة المهندس {ENGINEER_NAME} لدعم براءة الاختراع.**")
