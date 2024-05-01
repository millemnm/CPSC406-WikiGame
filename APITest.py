from openai import OpenAI

client = OpenAI(api_key="replace-with-api-key")
import os
from scipy.spatial.distance import cosine

# Set up the OpenAI API key

def get_embedding(text, model="text-embedding-3-small"):
    try:
        response = client.embeddings.create(input=text,
        model=model)
        return response.data[0].embedding
    except Exception as e:
        print(f"An error occurred while getting embedding: {e}")
        return None

def rank_topics(base_text, topics):
    base_embedding = get_embedding(base_text)
    if base_embedding is None:
        return []

    topic_embeddings = [(topic, get_embedding(topic)) for topic in topics]
    topic_embeddings = [te for te in topic_embeddings if te[1] is not None]  # Filter out failed embeddings

    # Calculate similarity scores (lower cosine distance means higher similarity)
    similarities = [(topic, 1 - cosine(base_embedding, emb)) for topic, emb in topic_embeddings]

    # Sort topics based on similarity scores
    sorted_topics = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [topic for topic, _ in sorted_topics]

# Example usage
base_text = "climate change"
topics = ["global warming", "economics", "polar ice caps", "stock market"]
sorted_topics = rank_topics(base_text, topics)

print("Topics ranked by similarity to 'climate change':")
for topic in sorted_topics:
    print(topic)
