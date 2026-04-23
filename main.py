from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello" : "World"}

@app.get("/ask")
async def ask_question(question:str):
    responce = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {"role":"system","content":"You are a helpful assistant for international students in Berlin. Answer in exactly 2-3 sentences. If you are not certain about a specific fact, say 'I am not certain' instead of guessing."},
            {"role":"user","content":question}
        ]
    )
    return {
        "question" : question,
        "answer" : responce["message"]["content"]
    }