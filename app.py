import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd

# --- الثوابت المهنية (ثوابت منصة محاكاة براءة الاختراع) ---
PLATFORM_NAME = "محاكاة براءة الاختراع"
ENGINEER_NAME = "Mogahed Bashir"
PHONE = "+966501318054"
LINKEDIN = "https://www.linkedin.com/in/mogahed-bashir-52a5072ba/"
WHATSAPP = "https://wa.me/966501318054"

# إعدادات الصفحة
st.set_page_config(page_title=PLATFORM_NAME, layout="wide")

# كود CSS لضبط الاتجاه والمحاذاة والمسافات
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    div.stMarkdown { text-align: right; }
    h1 { margin-bottom: 0px; padding-bottom: 0px; }
    .description-text { margin-top: -20px; font-size: 1.2rem; color: #555; }
    div[data-testid="stMetricValue"] { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية الثابتة ---
st.sidebar.title(f"🚀 {PLATFORM_NAME}")
st.sidebar.markdown(f"**المبتكر:** {ENGINEER_NAME}")
st.sidebar.divider()
st.sidebar.markdown(f"📞 **للتواصل:** {PHONE}")
st.sidebar.markdown(f"[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=for-the-badge&logo=whatsapp)]({WHATSAPP})")
st.sidebar.markdown(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)]({LINKEDIN})")

# العنوان الرئيسي والوصف
st.title("☀️ Integrated Solar Engineering Platform")
st.markdown('<p class="description-text">محاكاة ديناميكية لنظام التبريد ذاتي التشغيل ونظام مراقبة المحطة الذكي</p>', unsafe_allow_html=True)

# إنشاء الألسنة (Tabs)
tab1, tab2 = st.tabs(["❄️ نظام التبريد الميكانيكي (a1)", "📊 لوحة مراقبة المحطة"])

# --- التبويب الأول: نظام التبريد (الكود السابق المطور) ---
with tab1:
    st.subheader("Autonomous Thermal Cooling Simulation")
    auto_mode = st.checkbox("تفعيل المحاكاة التلقائية للحرارة")
    
    if auto_mode:
        t = time.time()
        temp = 35 + 10 * np.sin(2 * np.pi * t / 20) 
    else:
        temp = st.slider("درجة حرارة الخلية (°C)", 20, 60, 25, key="temp_slider")

    threshold = 35
    angle = min(90, max(0, (temp - threshold) * 5))
    rad = np.radians(angle)

    fig, ax = plt.subplots(figsize=(10, 5))
    # رسم اللوح (Simplified)
    ax.add_patch(plt.Rectangle((2, 10), 12, 0.6, color='#001f3f'))
    # رسم البوابات
    for x_p in [2, 6, 10]:
        ax.plot([x_p, x_p + 4*np.cos(rad)], [8, 8 - 4*np.sin(rad)], color='red', linewidth=5)
    
    ax.set_xlim(-2, 18)
    ax.set_ylim(2, 12)
    ax.axis('off')
    st.pyplot(fig)
    
    if auto_mode:
        time.sleep(1)
        st.rerun()

# --- التبويب الثاني: نظام مراقبة المحطة (المشروع الجديد) ---
with tab2:
    st.subheader("Solar Power Plant Live Monitoring")
    
    # محاكاة بيانات حقيقية
    col1, col2, col3 = st.columns(3)
    curr_power = 450 + np.random.uniform(-10, 10)
    efficiency = 18.5 if temp < 35 else 18.5 - (temp-35)*0.4
    
    with col3:
        st.metric("القدرة الحالية (kW)", f"{curr_power:.2f}")
    with col2:
        st.metric("كفاءة النظام (%)", f"{max(0, efficiency):.1f}%")
    with col1:
        st.metric("الحالة التشغيلية", "ممتازة" if efficiency > 15 else "تحتاج صيانة")

    # رسم بياني للإنتاج خلال اليوم
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) * [10, 5] + [400, 80],
        columns=['القدرة الصافية', 'درجة حرارة اللوح']
    )
    st.line_chart(chart_data)
    st.info("💡 يتم تحديث البيانات بناءً على قراءات الحساسات الافتراضية للمحطة.")

# --- الخلاصة الابتكارية المدمجة ---
st.divider()
st.markdown(f"""
<div style="direction: rtl; text-align: right;">

### 💡 نبذة عن المشاريع المرفقة:
1. **نظام a1:** ابتكار ميكانيكي لخفض الحرارة ذاتياً بدون استهلاك طاقة.
2. **نظام المراقبة:** حل برمجى لتتبع الأداء التشغيلي وضمان استدامة الإنتاج.

**تم التطوير بواسطة المهندس: {ENGINEER_NAME} لصالح {PLATFORM_NAME}**
</div>
""", unsafe_allow_html=True)
