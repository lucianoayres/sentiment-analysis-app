---
title: sentiment-analysis
app_file: app.py
sdk: gradio
sdk_version: 5.25.0
---
# 🎯 Análise de Sentimento em Avaliações de Produtos

Este sistema analisa o sentimento em avaliações de produtos em português usando o modelo BERT com fine-tuning em dados do e-commerce brasileiro.

## 🤖 Modelo
Utiliza o modelo [BERT fine-tuned para análise de sentimentos](https://huggingface.co/layers2024/bert-sentiment), treinado com o dataset [Olist Store](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data), um conjunto público de mais de 100 mil avaliações de e-commerce brasileiro feitas entre 2016 e 2018.

## 🎯 Projeto
Desenvolvido como parte do projeto NLP-Sentinel por [Luciano Ayres](https://linkedin.com/in/lucianoayres).

## 💻 Instalação Local

### Pré-requisitos
- Python 3.10+
- Git (opcional)

### Instalação

1. Clone o repositório:
```bash
git clone git@github.com:lucianoayres/sentiment-analysis-app.git
cd sentiment-analysis-app
```

2. Execute o script de instalação e inicialização:
```bash
./run.sh
```

O script irá:
- Criar um ambiente virtual Python
- Instalar as dependências necessárias
- Iniciar a aplicação

## 🌐 Demo Online

Você pode acessar uma versão online da aplicação em:
[https://huggingface.co/spaces/layers2024/analise-de-sentimentos-avaliacao-de-produtos](https://huggingface.co/spaces/layers2024/analise-de-sentimentos-avaliacao-de-produtos)

Gradio will:
- Start a local server (usually accessible at [http://localhost:7860](http://localhost:7860))
- Print a shareable public URL (if `share=True` is set) so that you can try your app in your browser.

## Deploying Your Gradio App to Hugging Face Spaces

Hugging Face Spaces provides a free and permanent hosting option for your Gradio demo. Follow the steps below to deploy your app using the terminal method:

### 1. Ensure You Have a Hugging Face Account
Make sure you have a free Hugging Face account. If not, [create one here](https://huggingface.co/join).

### 2. Deploy via Terminal

From your app's directory (where your `app.py` and `requirements.txt` reside), simply run:

```bash
gradio deploy
```

This command will gather basic metadata from your project, automatically create a new Space for you, and deploy your Gradio app.  
- **To Update Your Space:** Re-run the `gradio deploy` command, or you can enable GitHub Actions to automatically update your Space on git push.

### 3. Access and Share Your App

Once deployed, your app will be live at a URL in the following format:

```
https://<your-username>-<your-space-name>.hf.space
```

Share this URL with others to allow them to interact with your Gradio demo directly from their browsers.

## Additional Information

- **Model Updates:** If you update your model on Hugging Face, the next time your app runs (locally or on Spaces), it will load the latest version.
- **Hot Reload (Local Development):** Instead of running `python app.py`, you can run:
  ```bash
  gradio app.py
  ```
  This enables hot reloading so your changes are automatically reflected in your demo.
- **Troubleshooting:**
  - Ensure your virtual environment is activated before installing dependencies and running your script.
  - Verify that the package versions in your `requirements.txt` file are compatible with your code.
  - The initial launch might take extra time as your model files download from Hugging Face.

For further details, please refer to the [Gradio Documentation](https://gradio.app/docs/) and the [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers).
=======
# sentiment-analysis-app
App de anális de sentimento em avaliações de produtos em português usando BERT com fine-tuning em dados do e-commerce brasileiro.
>>>>>>> 42cb5fa7402ec14e53cdffc7568dcf02fc9750fe
