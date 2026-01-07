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

# --- الواجهة الرئيسية ---
st.title("☀️ نظام التبريد الطولي المتكامل للخلايا الشمسية")
st.write("محاكاة لنظام تبريد يعتمد على التمدد الطولي الموحد للبوابات الخلفية والجانبية بمجرد وصول الحرارة إلى 35°C.")

temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25)

# منطق الفيزياء
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي (Simulation Graphics) ---
fig, ax = plt.subplots(figsize=(14, 7))

# 1. رسم الخلية الشمسية (Solar PV Panel)
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f', label='Solar PV Panel'))

# 2. رسم مسار التمدد الطولي (Longitudinal Actuator Path)
ax.plot([2, 14], [8, 8], 'k--', alpha=0.3, label='5cm Air Gap Path')

# 3. رسم البوابات الميكانيكية (3 خلفية + 2 جانبية في الاتجاه الطولي)
# توزيع 5 بوابات على طول المسار لضمان فتح القناة بالكامل
gate_length = panel_length / 3  # طول البوابات الخلفية
side_gate_len = 1.5           # طول البوابات الجانبية الطولية

# البوابات الخلفية (تفتح في الاتجاه الطولي)
for x_p in [2, 6, 10]:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6)
    ax.scatter(x_p, 8, color='black', zorder=5)

# البوابات الجانبية (ممتدة طولياً عند الحواف 5 سم)
# جانب أيسر
ax.plot([2, 2 - side_gate_len * np.cos(rad)], [8, 8 - side_gate_len * np.sin(rad)], color='orange', linewidth=5, label='Side Longitudinal Gates')
# جانب أيمن
ax.plot([14, 14 + side_gate_len * np.cos(rad)], [8, 8 - side_gate_len * np.sin(rad)], color='orange', linewidth=5)

# 4. محاكاة تدفق الهواء الطولي (Airflow)
if angle > 10:
    # أسهم تمثل دخول الهواء من الجوانب وتدفقه تحت اللوح
    ax.arrow(0, 8, 1.5, 0, head_width=0.3, fc='orange', ec='orange')
    ax.arrow(16, 8, -1.5, 0, head_width=0.3, fc='orange', ec='orange')
    for i in range(5):
        ax.arrow(3 + i*2.2, 1, 0, 4, head_width=0.4, fc='skyblue', ec='skyblue', alpha=0.5)

# إعدادات الرسم
ax.set_xlim(-2, 18)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower center', ncol=3)
st.pyplot(fig)



# --- لوحة التحكم والبيانات ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("درجة الحرارة", f"{temp} °C")
with c2:
    st.metric("زاوية الفتح الطولي", f"{angle:.1f}°")
with c3:
    status = "تبريد طولي نشط" if temp > threshold else "وضع الاستعداد"
    st.info(f"الحالة: {status}")

st.markdown(f"""
### ⚙️ الوصف الفني للابتكار:
يعتمد هذا النظام على **التمدد الطولي** المتزامن للبوابات الخلفية والجانبية. تم تصميم البوابات لتغطي كامل طول الخلية الشمسية، مع وجود بوابات جانبية إضافية تفتح في نفس الاتجاه الطولي لتوجيه تيار الهواء داخل الفراغ الـ 5 سم، مما يحقق تبريداً انسيابياً يقلل من مقاومة الهواء (Air Drag) ويزيد من كفاءة تبديد الحرارة.
""")

st.write(f"**تم التطوير والبرمجة بواسطة المهندس: {ENGINEER_NAME}**")
