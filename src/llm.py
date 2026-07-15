from langchain_ollama import OllamaLLM

def get_llm():
    llm = OllamaLLM(model="phi3")
    return llm