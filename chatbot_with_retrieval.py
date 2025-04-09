import openai
import config
import json
import numpy as np
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=config.openai_api_key)

# Load embeddings
with open("embedded_chunks.json", "r") as f:
    embedded_chunks = json.load(f)

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_relevant_chunks(question, top_k=3):
    embedding_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )
    q_embedding = embedding_response.data[0].embedding

    scored = []
    for chunk in embedded_chunks:
        score = cosine_similarity(q_embedding, chunk["embedding"])
        scored.append((score, chunk["text"]))

    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]

# Streamlit UI
st.title("🤖 MCCC Smart Chatbot")
st.write("Ask a question based on the Medina County Career Center website:")

user_input = st.text_input("You:")

if user_input:
    top_chunks = get_relevant_chunks(user_input)
    context = "\n\n".join(top_chunks)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Answer the user's question using the following MCCC information:\n\n{context}"},
            {"role": "user", "content": user_input}
        ]
    )
    st.markdown(f"**Bot:** {response.choices[0].message.content}")
