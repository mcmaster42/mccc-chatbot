import openai
import tiktoken
import json
from pathlib import Path

# Load content
with open("mccc_cleaned_site_text.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

# Init OpenAI
from openai import OpenAI
import config
client = OpenAI(api_key=config.openai_api_key)

# Tokenizer for estimating chunk sizes
tokenizer = tiktoken.get_encoding("cl100k_base")

def chunk_text(text, max_tokens=500, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk_words = words[i:i+max_tokens]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)
        i += max_tokens - overlap
    return chunks

chunks = chunk_text(full_text)

print(f"Total chunks created: {len(chunks)}")

# Create embeddings
embedded_chunks = []
for i, chunk in enumerate(chunks):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    embedding = response.data[0].embedding
    embedded_chunks.append({
        "id": f"chunk_{i}",
        "text": chunk,
        "embedding": embedding
    })

# Save to file
with open("embedded_chunks.json", "w") as f:
    json.dump(embedded_chunks, f)

print("✅ Embeddings saved to embedded_chunks.json")
