# src/tool_factory.py

from transformers import pipeline
import requests
from config import DEFAULT_MODEL_NAME, MAX_RESPONSE_LENGTH, API_KEY_GOOGLE_SEARCH, GOOGLE_CSE_ID

def get_llm_pipeline(model_name=DEFAULT_MODEL_NAME):
    """Temel LLM'i (distilgpt2) yükler."""
    try:
        # Daha hýzlý yüklenmesi için 'low_cpu_mem_usage=True' eklendi
        return pipeline('text-generation', model=model_name, low_cpu_mem_usage=True) 
    except Exception as e:
        print(f"Hata: LLM yüklenemedi: {e}")
        return None

def generate_response(llm_pipeline, prompt, max_len=MAX_RESPONSE_LENGTH):
    """LLM'den yanýt üretir."""
    if llm_pipeline is None: 
        return "Hata: Model yüklü deðil."
    
    # Prompt'a, robotun eðitici ve nazik olmasý için talimat ekleniyor.
    full_prompt = f"Sen bir eðitim asistanýsýn. Kýsa ve açýklayýcý cevaplar ver. {prompt}"
    
    response = llm_pipeline(full_prompt, max_length=max_len, num_return_sequences=1, truncation=True)
    return response[0]['generated_text'].strip()

def search_web_tool(query):
    """Google Custom Search API simülasyonu. Gerçek API anahtarý girildiðinde çalýþýr."""
    
    if API_KEY_GOOGLE_SEARCH == "FAKE_KEY" or not GOOGLE_CSE_ID:
        # Eðer anahtar girilmediyse simülasyon yapar
        print("WEB ARAMASI: FAKE KEY KULLANILIYOR")
        if "son dakika" in query.lower():
            return "?? Web Aramasý Simülasyonu: Son dakika haberlerine göre yapay zeka alanýnda büyük bir ilerleme kaydedildi."
        return "?? Web Aramasý Simülasyonu: Ýnternetten bilgi buldum."

    # Gerçek API çaðrýsý (API anahtarýnýz varsa)
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY_GOOGLE_SEARCH}&cx={GOOGLE_CSE_ID}&q={query}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        search_results = response.json()
        
        if 'items' in search_results:
            results_text = "Bulunan web sonuçlarý:\n"
            for i, item in enumerate(search_results['items'][:2]): 
                results_text += f"- Baþlýk: {item.get('title')}\n"
            return results_text
        return "Web aramasý yapýldý ancak sonuç bulunamadý."
    except requests.exceptions.RequestException as e:
        return f"Web aramasý hatasý: {e}"