# Comic-Crafter-AI
ComicCrafter AI is a generative AI based comic generator running locally on edge devices that generates a comic style story based on the input prompts given by the user.

# Requirements
- Download `Ollama`
- Install model from `Ollama` locally
  - Model_name : `gemma3:latest`
  - run this command on your terminal to pull model locally: `ollama pull {model_name}`
- Install all the dependencies
  - run in terminal `pip install -r ./Model/require.txt`

# Run Application
- First run the following command in your terminal to activate Ollama: `ollama list`
- Run the following command in your terminal to start the application: `streamlit run ./Model/app.py`
