# 🎯 Análise de Sentimento em Avaliações de Produtos

Este sistema analisa o sentimento em avaliações de produtos em português usando o modelo BERT com fine-tuning em dados do e-commerce brasileiro.

## 🔍 Sobre o Projeto

O **NLP-Sentinel** é um projeto de **Processamento de Linguagem Natural (PLN)** focado na análise de sentimentos em avaliações de produtos. O sistema utiliza um modelo BERT com fine-tuning em dados reais do e-commerce brasileiro para classificar avaliações como positivas ou negativas.

### 🤖 Modelo
- **Base**: BERT (Bidirectional Encoder Representations from Transformers)
- **Versão**: [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased)
- **Fine-tuning**: [layers2024/bert-sentiment](https://huggingface.co/layers2024/bert-sentiment)
- **Dataset**: [Olist Store](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data) (100k+ avaliações)

### 📈 Performance
- **Acurácia**: 94.26%
- **F1-Score**: 94.37%

### 📝 Características
- Interface web intuitiva usando Gradio
- Processamento de texto em português
- Análise em tempo real
- Indicação de confiança na classificação

## 🌐 Demo Online

Experimente a aplicação em:
➡️ [https://huggingface.co/spaces/layers2024/sentiment-analysis](https://huggingface.co/spaces/layers2024/sentiment-analysis)

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

## 👨‍💻 Autor

**Luciano Ayres** - [LinkedIn](https://linkedin.com/in/lucianoayres)

## 📚 Referências

- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Gradio Documentation](https://gradio.app/docs/)
- [BERT Paper](https://arxiv.org/abs/1810.04805)