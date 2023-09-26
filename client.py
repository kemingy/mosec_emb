import openai

openai.api_key = ""
openai.api_base = "http://127.0.0.1:8000/v1"
model = "thenlper/gte-base"

emb = openai.Embedding.create(
    input="The quick brown fox jumps over the lazy dog.",
    model=model,
)["data"][0]["embedding"]

print(emb)
