import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- الثوابت المهنية (بيانات المهندس والمنصة) ---
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
st.title("☀️ نظام التبريد الميكانيكي (تبديل محاور البوابات)")
st.write("محاكاة لنظام الصندوق المغلق بعد عكس اتجاهات البوابات (الطولية عرضياً والعرضية طولياً).")

# منزلق الحرارة
temp = st.slider("درجة حرارة الخلية الشمسية (°C)", 20, 60, 25)

# منطق الفيزياء
threshold = 35
opening_offset = min(90, max(0, (temp - threshold) * 5))
rad = np.radians(90 - opening_offset)

# --- الرسم الهندسي المحدث ---
fig, ax = plt.subplots(figsize=(12, 7))

# 1. رسم الخلية الشمسية
panel_width = 10
ax.add_patch(plt.Rectangle((3, 10), panel_width, 0.6, color='#001f3f', label='Solar PV Panel'))

# 2. رسم البوابات الجانبية التي أصبحت "طولية" (تفتح على طول اللوح)
# تم تعديلها لتأخذ مساراً طولياً خلف اللوح
long_gate_len = 1.5 
ax.plot([3, 13], [8, 8], 'k--', alpha=0.1) # خط القاعدة

# 3. رسم البوابات التي أصبحت "عرضية" (3 بوابات تفتح بالعرض)
# تعكس الحركة بحيث تميل البوابة باتجاه الناظر أو للداخل (عرضياً)
gate_positions = [4.5, 8, 11.5]
for x_p in gate_positions:
    # البوابات العرضية تظهر هنا كخطوط تتحرك رأسياً لتوضيح الفتح العرضي
    y_start = 8
    y_end = 8 + long_gate_len * np.sin(np.radians(90 - opening_offset))
    x_end = x_p + long_gate_len * np.cos(np.radians(90 - opening_offset))
    
    ax.plot([x_p, x_end], [y_start, y_end], color='red', linewidth=6, label='Cross-sectional Gates' if x_p==4.5 else "")
    ax.scatter(x_p, 8, color='black', zorder=5)

# 4. البوابات الجانبية (أصبحت الآن تفتح طولياً)
side_rad = np.radians(opening_offset)
# بوابة يسار
ax.plot([3, 3], [8, 8 + 2*np.cos(side_rad)], color='orange', linewidth=6, label='Longitudinal Side Gates')
# بوابة يمين
ax.plot([13, 13], [8, 8 + 2*np.cos(side_rad)], color='orange', linewidth=6)

# 5. تدفق الهواء
if opening_offset > 15:
    ax.arrow(8, 6, 0, 1.5, head_width=0.3, fc='skyblue', ec='skyblue')
    ax.text(8.2, 5.5, "Cross-Flow Cooling", color='blue', fontsize=9)

# إعدادات الرسم
ax.set_xlim(0, 16)
ax.set_ylim(4, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.legend(loc='lower left', ncol=2)
st.pyplot(fig)



# --- لوحة البيانات ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("الحرارة", f"{temp} °C")
with c2:
    st.metric("زاوية الفتح", f"{opening_offset:.1f}°")
with c3:
    status = "تبريد عرضي نشط" if temp > threshold else "صندوق مغلق"
    st.info(f"الحالة: {status}")

st.markdown(f"""
### 🔄 التعديل الهندسي الجديد:
تم عكس محاور الحركة الميكانيكية بناءً على المتطلبات الفنية:
- **البوابات العرضية:** أصبحت تعمل كموزعات للهواء على عرض اللوح.
- **البوابات الطولية:** تعمل الآن كقنوات جانبية لحصر وتوجيه الهواء طولياً داخل الصندوق.
- **الفراغ:** تم الحفاظ على مسافة الـ 5 سم كمنطقة ضغط منخفض لتحفيز تدفق الهواء.
""")

st.write(f"**تم التطوير بواسطة المهندس {ENGINEER_NAME} لصالح {PLATFORM_NAME}.**")
