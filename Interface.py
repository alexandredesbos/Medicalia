import gradio as gr
from transformers import pipeline

# Chargement du modèle en local
generator = pipeline("text-generation", model="ThxZ3US/medicalia")


def chat(message, chat_history):
    if not message.strip():
        return "Ask a medical question on symptom diseases", chat_history

    chat_history.append((message, ""))

    # Générer une réponse avec le modèle
    output = generator(
        [{"role": "user", "content": message}],
        max_new_tokens=128,
        return_full_text=False,
    )[0]

    response = output["generated_text"]

    chat_history.append(("", response))

    return "", chat_history 


custom_css = """
body {
    background-color: #f4f7fc;
    font-family: Arial, sans-serif;
}

gradio-container {
    max-width: 650px;
    margin: 40px auto;
    padding: 30px;
    background: white;
    border-radius: 12px;
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
}

gr-chatbot .message.user {
    background-color: #007bff;
    color: white;
    border-radius: 10px;
    padding: 10px;
    margin-left: auto;
    max-width: 75%;
    text-align: right;
}

gr-chatbot .message.assistant {
    background-color: #e3f2fd;
    color: black;
    border-radius: 10px;
    padding: 10px;
    margin-right: auto;
    max-width: 75%;
    text-align: left;
}

gr-button {
    background-color: #007bff !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    font-size: 16px !important;
    padding: 12px 20px !important;
    transition: background-color 0.3s ease;
}

gr-button:hover {
    background-color: #0056b3 !important;
}

gr-input {
    border: 2px solid #0056b3 !important;
    border-radius: 8px !important;
    font-size: 16px !important;
    padding: 10px !important;
}

gr-textbox textarea {
    height: 100px !important;
    font-size: 16px !important;
}

#logo {
    width: 120px;
    display: block;
    margin: 20px auto;
}
"""

with gr.Blocks(css=custom_css) as demo:
    gr.HTML(
        '<img id="logo" src="https://cdn-icons-png.flaticon.com/512/2913/2913975.png">'
    )
    gr.Markdown("# 🩺 Medicalia : Medical AI Chatbot")
    gr.Markdown("### Ask your question to our specialized AI.")

    chatbot = gr.Chatbot(label="Discussion")
    user_input = gr.Textbox(
        placeholder="Ex : What are the symptom of anemia ?",
        label="Your quesiton",
        interactive=True,
    )
    submit_button = gr.Button("🔍 Send")

    # Permet d'envoyer le message avec Entrée
    user_input.submit(chat, inputs=[user_input, chatbot], outputs=[user_input, chatbot])
    submit_button.click(
        chat, inputs=[user_input, chatbot], outputs=[user_input, chatbot]
    )

# Lancer Gradio
if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, debug=True)
