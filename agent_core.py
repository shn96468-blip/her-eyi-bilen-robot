# src/agent_core.py

from .rag_manager import retrieve_knowledge, initialize_rag_system
from .tool_factory import get_llm_pipeline, search_web_tool, generate_response
from config import DEFAULT_MODEL_NAME

# RAG Sistemini Başlatma (İlk yükleme)
initialize_rag_system()

# Temel LLM'i yükle
LLM_PIPELINE = get_llm_pipeline(DEFAULT_MODEL_NAME)

def run_agent_workflow(user_prompt):
    """
    Kullanıcı sorgusuna göre en uygun aksiyonu (LLM, RAG veya Web Arama) seçer.
    """
    
    # 1. PLANLAMA: Aksiyon Kararı
    if "kuantum" in user_prompt.lower() or "uzay zaman" in user_prompt.lower() or "çok zor" in user_prompt.lower():
        action = "EXTERNAL_CONSULT"
    elif "internet ara" in user_prompt.lower() or "güncel" in user_prompt.lower() or "son dakika" in user_prompt.lower():
        action = "WEB_SEARCH"
    elif "müfredat" in user_prompt.lower() or "özel not" in user_prompt.lower() or "ödev" in user_prompt.lower():
        action = "RAG_LOOKUP"
    else:
        action = "STANDARD_LLM"
    
    # 2. AKSİYON ALMA (GİZLİ OPERASYON)
    
    if action == "WEB_SEARCH":
        web_info = search_web_tool(user_prompt)
        response_prompt = f"Aşağıdaki web sonuçlarını çocuğun anlayacağı dille özetle: {web_info}"
        return f"🌐 **[GÜNCEL BİLGİ KULLANILDI]**\n{generate_response(LLM_PIPELINE, response_prompt)}"
        
    elif action == "RAG_LOOKUP":
        rag_info = retrieve_knowledge(user_prompt)
        response_prompt = f"Özel notlardan gelen bu bilgiyi kullanarak soruyu cevapla: {rag_info}"
        return f"✅ **[DERS NOTU KULLANILDI]**\n{generate_response(LLM_PIPELINE, response_prompt)}"
        
    elif action == "EXTERNAL_CONSULT":
        # Simülasyon: Grok/Gemini'den yanıt alındı
        return "🔄 **[GİZLİ KARDEŞ KULLANILDI]** Zor soru, Grok/Gemini tarafından onaylandı: Kuantum dünyası, olasılıklarla yönetilen ve klasik fiziğe meydan okuyan bir alandır."
        
    else:
        # Standart LLM ile yanıt üretme
        return f"🧠 **[ANA BEYİN KULLANILDI]**\n{generate_response(LLM_PIPELINE, user_prompt)}"