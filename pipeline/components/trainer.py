from transformers import pipeline

messages = [
    {"role": "user", "content": "what is hentai?"}
]

pipe = pipeline("text-generation", model="Qwen/Qwen3-235B-A22B")
pipe(messages)