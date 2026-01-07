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
st.title("☀️ نظام التبريد الديناميكي الشامل (فتح كافة البوابات)")
st.write("محاكاة لنظام تبريد تفتح فيه البوابات الجانبية (الصفراء) والقاعدية (الحمراء) معاً عند 35°C لسحب الهواء من كل الاتجاهات.")

temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25)

# منطق الفيزياء (العتبة 35 درجة)
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية (المستوى العلوي Y=10)
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f', label='Solar PV Panel'))

# 2. رسم البوابات الجانبية الصفراء (Side Gates) - تفتح الآن للخارج
# المفصلات الجانبية عند نقاط التقاء اللوح (Y=10)
# بوابة يسار
side_x_l = 2 - 1.5 * np.sin(rad)
side_y_l = 10 - 2 * np.cos(rad)
ax.plot([2, side_x_l], [10, side_y_l], color='yellow', linewidth=6, label='Active Side Gates')
ax.scatter(2, 10, color='black', zorder=6, s=50)

# بوابة يمين
side_x_r = 14 + 1.5 * np.sin(rad)
side_y_r = 10 - 2 * np.cos(rad)
ax.plot([14, side_x_r], [10, side_y_r], color='yellow', linewidth=6)
ax.scatter(14, 10, color='black', zorder=6, s=50)

# 3. رسم البوابات الحمراء الـ 3 (عند مستوى القاعدة Y=8)
gate_length = 4.0 
gate_positions = [2, 6, 10]
ax.plot([2, 14], [8, 8], 'k--', alpha=0.2) # خط القاعدة المرجعي

for x_p in gate_positions:
    # الفتح من مستوى القاعدة (Y=8) باتجاه الخارج
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    
    # رسم البوابة الحمراء
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6, solid_capstyle='round')
    ax.scatter(x_p, 8, color='black', zorder=5, s=80)

# 4. تدفق الهواء الشامل (من الجوانب والأسفل)
if angle > 15:
    # هواء من الأسفل
    for i in range(3):
        ax.arrow(4 + i*4, 4, 0, 3, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.4)
    # هواء من الجوانب
    ax.arrow(0, 9, 1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.4)
    ax.arrow(16, 9, -1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.4)
    ax.text(8, 5, "MULTI-DIRECTIONAL AIR INTAKE", color='blue', fontweight='bold', ha='center')

# إعدادات الرسم
ax.set_xlim(-2, 18)
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
    st.metric("زاوية الفتح الموحدة", f"{angle:.1f}°")
with c3:
    status = "تبريد شامل (جوانب + قاعدة)" if temp > threshold else "صندوق محكم الإغلاق"
    st.info(f"حالة النظام: {status}")

st.markdown(f"""
### ⚙️ مميزات النظام الديناميكي المتكامل:
- **تحرر الجوانب:** تفتح البوابات الصفراء جانبياً لتقليل الضغط الداخلي والسماح بمرور تيار هواء عرضي.
- **تأثير المغرفة (Scooping Effect):** البوابات الحمراء في القاعدة تسحب الهواء الصاعد للأعلى باتجاه اللوح.
- **التزامن الميكانيكي:** كافة البوابات تعمل بمشغل حراري واحد يضمن تفتحها المتزامن عند **{threshold}°C**.
""")

st.write(f"**تم التطوير الهندسي والبرمجة بواسطة المهندس {ENGINEER_NAME}.**")
