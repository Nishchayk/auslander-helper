import ollama


question = "What is the Anmeldung in Germany?"


print("Sending question to ollama 3.2:3b")
print(f"Question: {question}\n")

responce =  ollama.chat(
    model= "llama3.2:3b",
    messages=[
        {"role":"system","content":r"You are a helpful assistant for international students in Berlin. Answer in exactly 2 sentences. If you are not 100% certain about a specific fact, say 'I am not certain' instead of guessing. Do not invent details."},
        {"role":"user","content":question}
    ]
)

print(f"Answer:{responce["message"]["content"]}")