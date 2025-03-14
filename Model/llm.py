from langchain_community.llms import Ollama

text_model="gemma3:latest"

text_llm = Ollama(model=text_model, temperature=0.5)