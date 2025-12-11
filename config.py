# config.py

import os

# --- LLM Ayarlarý ---
# Robotun temel beyni için kullanýlacak küçük ve hýzlý model
DEFAULT_MODEL_NAME = 'distilgpt2' 
MAX_RESPONSE_LENGTH = 300 # Yanýtýn maksimum uzunluðu

# --- RAG (Özel Hafýza) Ayarlarý ---
# Vektör veritabanýnýn saklanacaðý yer
VECTOR_DB_PATH = os.path.join("data", "vector_db") 
# Okunacak özel belgelerin (ders notlarý, PDF'ler) bulunacaðý klasör
DOCS_PATH = os.path.join("data", "docs") 

# --- Gizli Araçlar ve API Anahtarlarý ---
# Güvenlik için bu anahtarlar ortam deðiþkenlerinden (sistem ayarlarýndan) okunur.
API_KEY_GOOGLE_SEARCH = os.environ.get("GOOGLE_SEARCH_API_KEY", "FAKE_KEY")
GOOGLE_CSE_ID = os.environ.get("GOOGLE_CSE_ID", "FAKE_ID") 
API_KEY_EXTERNAL_LLM = os.environ.get("EXTERNAL_LLM_API_KEY", "FAKE_EXTERNAL_KEY")