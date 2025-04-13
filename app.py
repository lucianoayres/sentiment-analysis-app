import gradio as gr
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

# Load BERT model
def load_models():
    models = {}
    try:
        models['BERT'] = {
            'model': TFAutoModelForSequenceClassification.from_pretrained("layers2024/bert-sentiment"),
            'tokenizer': AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
        }
        print("✓ BERT loaded")
    except Exception as e:
        print(f"⚠️ Error loading BERT model: {str(e)}")
    
    return models

# Exemplos de avaliações para teste
EXAMPLES = [
    # Avaliações Positivas (nota 5)
    "Produto excelente! Entrega rápida e qualidade ótima. Recomendo!",
    "Ótimo atendimento, produto bem embalado e conforme descrito.",
    "Entrega antes do prazo. Produto de qualidade e preço justo.",
    "Muito satisfeito! Produto original e entrega rápida.",
    "Produto perfeito, bem embalado. Vendedor confiável.",
    
    # Avaliações Negativas (nota 1)
    "Produto de baixa qualidade. Não recomendo.",
    "Veio com defeito e sem suporte do vendedor.",
    "Atrasou muito e veio diferente do anunciado.",
    "Faltaram itens na entrega. Sem retorno do vendedor.",
    "Produto muito ruim. Não funciona!"
]

def get_prediction(text, model_dict):
    inputs = model_dict['tokenizer'](text, return_tensors="tf", truncation=True, padding=True)
    outputs = model_dict['model'](**inputs)
    probabilities = tf.nn.softmax(outputs.logits, axis=-1)
    probs = probabilities.numpy()[0]
    predicted_class = tf.math.argmax(probabilities, axis=-1).numpy()[0]
    confidence = probs[predicted_class]
    return predicted_class, confidence

def predict_sentiment(review_text):
    # Definir threshold de confiança
    HIGH_CONFIDENCE = 0.90  # 90% de confiança mínima para classificação definitiva
    
    try:
        predicted_class, confidence = get_prediction(review_text, MODELS['BERT'])
        
        # Determinar o sentimento baseado no threshold
        if confidence >= HIGH_CONFIDENCE:
            sentiment = "POSITIVO" if predicted_class == 1 else "NEGATIVO"
            status = "✅ Alta confiança"
        else:
            if predicted_class == 1:
                sentiment = "POSSIVELMENTE POSITIVO"
            else:
                sentiment = "POSSIVELMENTE NEGATIVO"
            status = "⚠️ Baixa confiança"
        
        return f"BERT:\n{sentiment}\n{status}\nConfiança: {confidence:.1%}"
            
    except Exception as e:
        return f"⚠️ Erro: {str(e)}"

# Load all models
print("Carregando modelos...")
MODELS = load_models()
print("Modelos carregados!")

# Create the Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("# 🎯 Análise de Sentimento em Avaliações de Produtos")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="Texto da Avaliação",
                placeholder="Digite aqui a avaliação do produto...",
                lines=4
            )
            with gr.Row():
                clear_btn = gr.Button("Limpar", variant="secondary")
                analyze_btn = gr.Button("Analisar Sentimento", variant="primary")
        
        with gr.Column(scale=1):
            output_text = gr.Textbox(
                label="Resultados da Análise",
                lines=4
            )
    
    gr.Examples(
        examples=[[ex] for ex in EXAMPLES],
        inputs=[input_text],
        label="Exemplos de Avaliações"
    )
    
    with gr.Accordion("ℹ️ Sobre o Projeto", open=False):
        gr.Markdown('''
        ### Análise de Sentimento com BERT
        Este sistema analisa o sentimento em avaliações de produtos em português usando BERT com fine-tuning em dados do e-commerce brasileiro.
        
        #### 🤖 Detalhes Técnicos
        - **Modelo**: [BERT fine-tuned para análise de sentimentos](https://huggingface.co/layers2024/bert-sentiment)
        - **Dataset**: [Olist Store](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data) (100k+ avaliações)
        - **Projeto**: NLP-Sentinel por [Luciano Ayres](https://linkedin.com/in/lucianoayres)
        ''')
    
    def clear_inputs():
        return "", ""
    
    analyze_btn.click(
        fn=predict_sentiment,
        inputs=input_text,
        outputs=output_text
    )
    
    clear_btn.click(
        fn=clear_inputs,
        outputs=[input_text, output_text]
    )

interface.theme = gr.themes.Default()
css = """
    .gradio-container {max-width: 800px; margin: auto;}
    .footer {display: none;}
    a {color: #2196F3; text-decoration: none;}
    a:hover {text-decoration: underline;}
    .examples {margin-top: 20px; text-align: left;}
    .examples-table {width: 100%; border-collapse: collapse;}
    .example-row {cursor: pointer; transition: background 0.2s;}
    .example-row:hover {background: #f0f0f0;}
    .textbox {text-align: left;}
"""
interface.css = css

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch(share=True)
