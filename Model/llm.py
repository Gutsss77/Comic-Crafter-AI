from langchain_community.llms import Ollama

# text_model="gemma3:latest"
text_model="hf.co/bartowski/ibm-granite_granite-3.2-2b-instruct-GGUF:Q4_K_S"

text_llm = Ollama(model=text_model, temperature=0.5)