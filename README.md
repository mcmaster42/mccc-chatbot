# MCCC Chatbot (Streamlit + OpenAI)

This is a custom chatbot built using Streamlit and OpenAI embeddings. It allows users to ask questions about programs and offerings at the Medina County Career Center (MCCC) based on publicly available website data.

## 🔧 How It Works

1. `mccc_cleaned_site_text.txt` is a cleaned version of the scraped MCCC website content.
2. `chunk_and_embed.py` splits the content into chunks and generates OpenAI embeddings.
3. `embedded_chunks.json` stores those embeddings.
4. `chatbot_with_retrieval.py` loads the embeddings and uses OpenAI's API to answer questions.

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mccc-chatbot.git
cd mccc-chatbot

### 2. Set up a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install required packages
pip install -r requirements.txt

###4. Add your OpenAI API key
## Edit the config.py file:
OPENAI_API_KEY = "your-key-here"

### 5. Run the chatbot
streamlit run chatbot_with_retrieval.py


### File Descriptions
### File	Description
### chatbot_with_retrieval.py	The main chatbot UI (Streamlit)
### chunk_and_embed.py	Generates OpenAI embeddings from the cleaned MCCC text
### config.py	Holds API key for OpenAI
### embedded_chunks.json	Vector embeddings saved after chunking
### mccc_cleaned_site_text.txt	Cleaned website data
### requirements.txt	All required Python packages
### start.sh	Optional script to launch the app
### .gitignore	Prevents tracking of unnecessary files like venv/
