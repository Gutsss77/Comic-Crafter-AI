# # Import necessary libraries for language model and pipeline creation
# from langchain_huggingface import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# # Initialize the model ID for the language model
# model_id="ibm-granite/granite-3.2-2b-instruct"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)

# # Create a text generation pipeline using the model and tokenizer
# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=200, temperature=0.7)

# # Initialize the HuggingFacePipeline with the text generation pipeline
# hf_text_model = HuggingFacePipeline(pipeline=pipe)

# # Use gpu to run the model
# # hf_text_model = HuggingFacePipeline.from_model_id(
# #     model_id="gpt2",
# #     task="text-generation",
# #     device=0
# # )


from langchain_community.llms import Ollama

text_model = "hf.co/bartowski/ibm-granite_granite-3.2-2b-instruct-GGUF:Q4_K_S"

hf_text_model = Ollama(model=text_model, temperature=0.7)