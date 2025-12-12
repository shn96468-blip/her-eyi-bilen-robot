import gradio as gr
from src.agent_core import AgentCore # Robotun ana beyni

# Robotu Başlatma
robot_agent = AgentCore()

# Konuşma Fonksiyonu (Robotun cevabını döndürür)
def generate_response(user_input, history):
    # Bu fonksiyon, robotun ana beynini çalıştırır
    response = robot_agent.run_agent(user_input)
    return response

# Gradio Arayüzü Tanımlama
# ChatInterface, mesaj kutusu ve tarihçeyi otomatik oluşturur.
iface = gr.ChatInterface(
    generate_response,
    title="🤖 GZ Robot (Gradio Yayını)",
    description="Tüm sorunları aştık! Artık robotunuzla konuşabilirsiniz."
)

# Gradio Arayüzünü Başlatma
iface.launch(debug=True)