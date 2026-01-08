import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# --- الثوابت المهنية (ثوابت منصة محاكاة براءة الاختراع) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = "https://wa.me/966501318054"

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# كود CSS لفرض اتجاه اليمين إلى اليسار (RTL) وتصحيح المحاذاة
st.markdown("""
    <style>
    .main {
        direction: rtl;
        text-align: right;
    }
    div.stMarkdown {
        text-align: right;
    }
    div[data-testid="stMetricValue"] {
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية الثابتة ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# --- واجهة المحاكاة الرئيسية ---
st.title("☀️ Autonomous Thermal Cooling System Simulation")
st.write("محاكاة ديناميكية لنظام التبريد ذاتي التشغيل عبر الشرائح الحرارية.")

# خيار التفعيل التلقائي
auto_mode = st.checkbox("تفعيل المحاكاة التلقائية (ارتفاع وانخفاض الحرارة)")

if auto_mode:
    t = time.time()
    temp = 35 + 10 * np.sin(2 * np.pi * t / 20) 
    st.info(f"المحاكاة نشطة: درجة الحرارة تتغير تلقائياً...")
else:
    temp = st.slider("درجة حرارة الخلية الشمسية (°C)", 20, 60, 25)

# منطق الفيزياء: الشريحة الحرارية
threshold = 35
angle = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(angle)

# --- الرسم الهندسي ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. Solar PV Panel
panel_length = 12
ax.add_patch(plt.Rectangle((2, 10), panel_length, 0.6, color='#001f3f'))
ax.text(8, 10.8, "SOLAR PV PANEL", color='black', fontweight='bold', ha='center')

# 2. Side Yellow Gates (Bimetallic)
side_x_l = 2 - 1.5 * np.sin(rad)
side_y_l = 10 - 2 * np.cos(rad)
ax.plot([2, side_x_l], [10, side_y_l], color='yellow', linewidth=6)
ax.text(0.5, 9.5, "SIDE GATE\n(BIMETALLIC)", color='#d4af37', fontsize=8, fontweight='bold', ha='right')

side_x_r = 14 + 1.5 * np.sin(rad)
side_y_r = 10 - 2 * np.cos(rad)
ax.plot([14, side_x_r], [10, side_y_r], color='yellow', linewidth=6)
ax.text(15.5, 9.5, "SIDE GATE\n(BIMETALLIC)", color='#d4af37', fontsize=8, fontweight='bold', ha='left')

# 3. Main Rear Gates (Red)
gate_length = 4.0 
gate_positions = [2, 6, 10]
ax.plot([2, 14], [8, 8], 'k--', alpha=0.2)

for x_p in gate_positions:
    x_end = x_p + gate_length * np.cos(rad)
    y_end = 8 - gate_length * np.sin(rad)
    ax.plot([x_p, x_end], [8, y_end], color='red', linewidth=6)
    ax.scatter(x_p, 8, color='black', zorder=5)

# تعريفات الحالات
if temp < threshold:
    ax.text(8, 9, "GATES CLOSED: PREVENTING HEAT LOSS (TEMP < 35°C)", 
            color='gray', ha='center', fontweight='bold', bbox=dict(facecolor='white', alpha=0.5))
else:
    ax.text(8, 9, "GATES OPEN: COOLING AIRFLOW INTAKE (TEMP > 35°C)", 
            color='green', ha='center', fontweight='bold', bbox=dict(facecolor='white', alpha=0.7))
    ax.arrow(-0.5, 9, 1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.7)
    ax.arrow(16.5, 9, -1.5, 0, head_width=0.3, fc='orange', ec='orange', alpha=0.7)
    for i in range(3):
        ax.arrow(4 + i*4, 4, 0, 3, head_width=0.3, fc='skyblue', ec='skyblue', alpha=0.4)

ax.set_xlim(-3, 19)
ax.set_ylim(3, 12)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

if auto_mode:
    time.sleep(1)
    st.rerun()

# --- البيانات التحليلية والخلاصة ---
st.divider()
c1, c2, c3 = st.columns(3)
with c3:
    st.metric("درجة الحرارة", f"{temp:.1f} °C")
with c2:
    st.metric("زاوية الفتح", f"{angle:.1f}°")
with c1:
    status = "تبريد نشط" if temp > threshold else "النظام مغلق"
    st.info(f"الحالة: {status}")

st.markdown("""
<div style="direction: rtl; text-align: right;">

### 💡 الخلاصة الابتكارية (Innovative Abstract):

**نحو جيل جديد من الطاقة المستدامة بذكاء ميكانيكي بحت!**

يقدم هذا المشروع حلاً هندسياً عبقرياً لمشكلة انخفاض كفاءة الألواح الشمسية بسبب الحرارة، من خلال نظام **تبريد ميكانيكي ذاتي التشغيل (Zero-Energy Cooling)**. يتميز الابتكار بالآتي:

* **ذكاء بلا كهرباء:** يعتمد النظام كلياً على **التمدد الحراري للمادة**، مما يجعله يعمل بشكل مستقل تماماً دون الحاجة لحساسات، أسلاك، أو طاقة خارجية.
* **استجابة فائقة الدقة:** عبر استخدام **الشرائح الحرارية (Bimetallic Strips)**، تتحول حرارة الشمس "الضارة" إلى "قوة محركة" تفتح بوابات التهوية بمجرد ملامسة عتبة الـ 35 درجة مئوية.
* **تصميم "الصندوق الذكي":** بوابات جانبية وخلفية متزامنة تضمن تدفق هواء انسيابي شامل، مما يرفع الكفاءة التشغيلية ويطيل العمر الافتراضي للخلية الشمسية.
* **اعتمادية لا تضاهى:** بساطة التصميم تجعله مقاوماً للأعطال، منخفض التكلفة، ومثالياً للاستخدام في أقصى الظروف المناخية حرارةً.

**باختصار: نحن لا نبرد الألواح فحسب، بل نجعل الشمس هي المحرك لتبريد نفسها!**

</div>
""", unsafe_allow_html=True)

st.write(f"**تم التطوير والبرمجة بواسطة المهندس: {ENGINEER_NAME} لصالح {PLATFORM_NAME}**")
