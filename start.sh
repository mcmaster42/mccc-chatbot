#!/bin/bash
cd "$(dirname "$0")" && chmod +x "$(basename "$0")"  # Navigate to the directory where the script is located

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Check if packages are installed, if not install them
if ! pip show openai > /dev/null 2>&1; then
    echo "Installing required packages..."
    pip install openai streamlit numpy tiktoken
fi

# Generate embeddings if needed
if [ ! -f "embedded_chunks.json" ]; then
    echo "🔍 Embedding content..."
    python chunk_and_embed.py
fi

# Launch the app
echo "🚀 Launching MCCC Smart Chatbot..."
streamlit run chatbot_with_retrieval.py