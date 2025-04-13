# BERT Sentiment Classifier Gradio Demo

This repository demonstrates how to set up and run a sentiment classifier built with BERT for product reviews using a Gradio interface. The classifier predicts whether a review is **positive** or **negative**.

The model is hosted on Hugging Face and can be found here:
- **Model Repository:** [layers2024/bert-sentiment](https://huggingface.co/layers2024/bert-sentiment/tree/main)
- **Configuration:** [config.json](https://huggingface.co/layers2024/bert-sentiment/blob/main/config.json)
- **Pre-trained Weights:** [tf_model.h5](https://huggingface.co/layers2024/bert-sentiment/blob/main/tf_model.h5)

## Prerequisites

- **Python 3.10+**
- [Git](https://git-scm.com) (optional, if you wish to clone the repository)
- A Hugging Face account (free) – [Sign Up](https://huggingface.co/join)

## Local Setup Instructions

### 1. Create and Activate a Virtual Environment

It is best to use a Python virtual environment to avoid conflicts with existing packages.

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Required Dependencies

Upgrade pip and install the necessary packages:
```bash
pip install --upgrade pip
pip install gradio tensorflow transformers
```

### 3. Create the Gradio Application

Create a file named `app.py` (or any name you prefer) in your working directory and paste the following code:

```python
import gradio as gr
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

# Set the model name hosted on Hugging Face
model_name = "layers2024/bert-sentiment"

# Load the tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)

def predict_sentiment(review_text):
    # Tokenize the input text with truncation and padding enabled
    inputs = tokenizer(review_text, return_tensors="tf", truncation=True, padding=True)
    
    # Run inference using the model to get the logits
    outputs = model(**inputs)
    logits = outputs.logits
    
    # Convert logits to probabilities using softmax
    probabilities = tf.nn.softmax(logits, axis=-1)
    
    # Get the class with the highest probability (0: negative, 1: positive)
    predicted_class = tf.math.argmax(probabilities, axis=-1).numpy()[0]
    
    # Map the predicted class index to the corresponding sentiment label
    sentiment_mapping = {0: "negative", 1: "positive"}
    return sentiment_mapping[predicted_class]

# Define the Gradio interface for the sentiment classifier
interface = gr.Interface(
    fn=predict_sentiment,
    inputs="textbox",
    outputs="textbox",
    title="Product Review Sentiment Classifier",
    description="Enter a product review and click Submit to see if it is positive or negative."
)

# Launch the Gradio app; setting share=True provides a shareable public link (valid for 72 hours)
if __name__ == "__main__":
    interface.launch(share=True)
```

### 4. Run the Application Locally

With your virtual environment activated, run the app by executing:

```bash
python app.py
```

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