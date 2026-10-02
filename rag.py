from sentence_transformers import SentenceTransformer
import faiss

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(headlines):
    return model.encode(headlines)


def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index


def search_faiss(query, index, headlines, top_k=3):
    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in range(top_k):
        results.append(
            (headlines[indices[0][i]], distances[0][i])
        )

    return results