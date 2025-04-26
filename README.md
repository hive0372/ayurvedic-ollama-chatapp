# Ayurvedic ChatApp (Hugging Face Cloud Deployable)

A Streamlit-based conversational assistant for Ayurvedic wellness, powered by the Mistral-7B-Instruct model via Hugging Face Inference API.

## Features
- Friendly, knowledgeable Ayurvedic chat assistant
- Uses Hugging Face cloud LLM (Mistral-7B-Instruct)
- Streamlit web UI
- **Deployable on Streamlit Cloud**

## Setup & Deployment
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ayurvedic-ollama-chatapp.git
   cd ayurvedic-ollama-chatapp
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Hugging Face API token:
   - Locally: Create a `.streamlit/secrets.toml` file and add:
     ```toml
     HF_TOKEN = "YOUR_HUGGINGFACE_TOKEN"
     ```
   - On Streamlit Cloud: Go to app settings → Secrets and add `HF_TOKEN`.
4. Run the app:
   ```bash
   streamlit run ayurvedic_app.py
   ```

## Deploy to Streamlit Cloud
1. Push your code to GitHub.
2. Go to [https://share.streamlit.io/](https://share.streamlit.io/).
3. Deploy your repo and set the `HF_TOKEN` secret in the app settings.

## Notes
- No Ollama or local LLM required—uses Hugging Face API.
- For best results, use a recent version of Python (>=3.9).
