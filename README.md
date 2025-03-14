# Comic-Crafter-AI
ComicCrafter AI is a generative AI based comic generator running locally on edge devices that generates a comic style story based on the input prompts given by the user.

# Requirements
- To run ComicCrafter AI on your edge device, follow these steps:
- Install Ollama:
    - Download Ollama for your operating system from [download](https://ollama.com/).
    - Set up Ollama for your command line by its application.
    - Ollama will help you manage and run the generative models locally.

- Install the Model Locally:
    - Once you have Ollama installed, use the following command to pull the required model:
    - Model_name : `gemma3:latest`
    - Run: `ollama pull gemma3:latest` to install it.
    - This command will pull the `gemma3:latest model`, which will be used to generate the comic-style story.
  
- Install Dependencies:
    - Navigate to the Model directory where the require.txt file is located.
    - Install the required dependencies using:
    - Run: `pip install -r require.txt ` or `pip install -r ./Model/require.txt`

# Run Application
- Activate Ollama:
    - First, verify that Ollama is running correctly by listing all the available models. In your terminal, run: `ollama list`
- Launch the Streamlit Application:
    - If you're already inside the Comic-Crafter-AI directory, simply run: `streamlit run ./Model/app.py`
    - If you're not in the Comic-Crafter-AI directory, navigate to the Model folder first:
    - Run: `cd Model` then run: `streamlit run app.py`
