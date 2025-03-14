# Comic-Crafter-AI
ComicCrafter AI is a generative AI based comic generator running locally on edge devices that generates a comic style story based on the input prompts given by the user.

# Requirements
- Download `Ollama` from [download](https://ollama.com/) for you own OS.
- Install model from `Ollama` locally
  - Model_name : `gemma3:latest`
  - run this command on your terminal to pull model locally: `ollama pull {model_name}`
- Install all the dependencies
  - run in terminal `pip install -r ./Model/require.txt`

# Run Application
- First run the following command in your terminal to activate Ollama: `ollama list`
- Run the following command in your terminal to start the application: `streamlit run ./Model/app.py` (if you are in Comic-Crafter-AI directory/folder).
- Else go to Model directory `cd Model` (run this command in terminal) and then run this in terminal to run the application: `streamlit run app.py`
