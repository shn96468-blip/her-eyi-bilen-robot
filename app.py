# app.py

import streamlit as st
from streamlit_mic_recorder import mic_recorder # Sesli etkileþim için
from src.agent_core import run_agent_workflow

st.set_page_config(page_title="Her Þeyi Bilen Robot | Sunum Modu", layout="wide")
st.title("???? Her Þeyi Bilen Robot (Çocuklara Ders Asistaný)")
st.caption("Çoklu Beyin, Ders Notlarý (RAG) ve Canlý Ýnternet Eriþimi ile Güçlendirilmiþtir.")

# --- YZ MODELÝ KONTROLÜ ---
try:
    from src.agent_core import LLM_PIPELINE
    if LLM_PIPELINE is None:
         st.error("YZ Modeli Yüklenemedi! Lütfen kütüphaneleri ve kurulumu kontrol edin.")
except ImportError:
     st.error("YZ Dosyalarý bulunamadý. Lütfen tüm kodlarý doðru dosyalara kopyaladýðýnýzdan emin olun.")


st.subheader("? Robotunuza Nasýl Sormak Ýstersiniz?")

# Ýki Sütun: Metin Giriþi ve Mikrofon
col1, col2 = st.columns([3, 1])

with col1:
    user_prompt = st.text_area(
        "Yazarak Sorunuz:", 
        placeholder="Ödevime yardýmcý ol! / Son dakika haberleri neler? / Kuantum nedir?",
        height=50
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True) # Boþluk býrakmak için
    # Mikrofon Giriþi
    mic_output = mic_recorder(
        start_prompt="Ses Kaydýný Baþlat", 
        stop_prompt="Kaydý Durdur ve Gönder", 
        key='mic_recorder',
        just_once=True
    )
    
    # Ses kaydý varsa, Metin Giriþini simüle edilmiþ transkriptle doldurma
    if mic_output and mic_output['audio_bytes']:
        st.success("Ses baþarýyla kaydedildi! (Transkripsiyon simülasyonu)")
        # Sesi yazýya çevirme (transkripsiyon) maliyetli olduðu için simülasyon yapýlýyor
        simulated_text = "Özel notlarýmýza göre sýnav ne zaman?"
        user_prompt = simulated_text 

# --- YANIT BUTONU ---
if st.button("Robot Yanýtlasýn (Tüm Gücüyle)", type="primary"):
    if user_prompt:
        st.info(f"Girilen görev: **{user_prompt}**")
        
        with st.spinner('Ajanýnýz planlama yapýyor, bilgi topluyor ve sentezliyor...'):
            # Ajaný çalýþtýrýyoruz (Tüm mantýk burada gerçekleþir)
            final_response = run_agent_workflow(user_prompt)

        st.markdown("---")
        st.success("### ?? Robotun Nihai Yanýtý")
        st.markdown(final_response)
    else:
        st.warning("Lütfen bir soru girin veya ses kaydý yapýn.")