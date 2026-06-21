import os
from sentence_transformers import SentenceTransformer

filepath = "data/how_to_get_a_b_rgeramt_appointment.txt"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

print(f"Document loaded: {filepath}")
print(f"Total characters: {len(text)}\n")


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks


chunks = chunk_text(text)
print(f"Created {len(chunks)} chunks\n")

# Use 'chunk' (singular) for the loop variable, not 'chunks'
for i, chunk in enumerate(chunks[:2], start=1):
    print(f"---- Chunk {i} ({len(chunk)} chars) ----")
    print(chunk)
    print()

# Embed all chunks
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded\n")

print(f"Embedding {len(chunks)} chunks...")
embeddings = model.encode(chunks)
print(f"Done. Shape of embeddings: {embeddings.shape}\n")

print("First chunk's embedding (first 10 of 384 dimensions):")
print(embeddings[0][:10])
print(f"\nFull vector has {len(embeddings[0])} dimensions per chunk")

import chromadb

# Create a ChromaDB client that persists to disk
print("\n--- Setting up ChromaDB ---")
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get a collection (like a "table" in a regular database)
collection = client.get_or_create_collection(name="auslander_helper")

# Add the chunks and their embeddings to the collection
# ChromaDB needs: ids (unique strings), documents (the text), embeddings (the vectors)
chunk_ids = [f"chunk_{i}" for i in range(len(chunks))]

collection.add(
    ids=chunk_ids,
    documents=chunks,
    embeddings=embeddings.tolist()  # ChromaDB wants lists, not numpy arrays
)

print(f"Stored {len(chunks)} chunks in ChromaDB")
print(f"Collection size: {collection.count()}\n")

# --- Now query it ---
print("--- Querying ---")
question = "How do I book an appointment at the Bürgeramt?"
print(f"Question: {question}\n")

# Embed the question (same model as the chunks)
question_embedding = model.encode(question).tolist()

# Find the top 3 most similar chunks
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

# Print the results
for i, (doc, dist) in enumerate(zip(results["documents"][0], results["distances"][0]), start=1):
    print(f"--- Result {i} (distance: {dist:.4f}) ---")
    print(doc[:300])  # First 300 chars of the chunk
    print()