# Temel Python 3.11 sürümünü kullan. Bu, temiz ve sorunsuz bir ortam sağlar.
FROM python:3.11-slim

# Uygulamanın çalışacağı dizini (/app) belirle.
WORKDIR /app

# 1. Kütüphane Listesini Kapsüle Kopyala
# Bu adım, "requirements.txt" dosyanızın Docker'ın içine kopyalanmasını sağlar.
COPY requirements.txt .

# 2. Tüm Gerekli Kütüphaneleri Kur
# pip'e tüm kütüphaneleri (Streamlit, Transformers, vb.) kurmasını emrederiz.
# --no-cache-dir, bulut ortamında yer kazanmak için önemlidir.
RUN pip install --no-cache-dir -r requirements.txt

# 3. Kalan Tüm Proje Dosyalarını Kapsüle Kopyala
# app.py, config.py ve src klasörü dahil her şeyi kapsüle taşır.
COPY . .

# Uygulamanın (Streamlit) yayınlanacağı portu belirle.
EXPOSE 8501

# Uygulamayı Başlatma Komutu
# Docker'a, kapsül çalışmaya başladığında Streamlit'i başlatmasını söyleriz.
# --server.address=0.0.0.0 ayarı, uygulamanın internetten erişilebilir olmasını garanti eder.
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
