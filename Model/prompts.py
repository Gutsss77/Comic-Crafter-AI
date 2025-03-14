from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import SequentialChain, LLMChain
from llm import text_llm


#-------------------------------------Chain Definitions-------------------------------------

#-------------------------------------Theme Generation Chain

theme_prompt_template=(
    "Analyze the title '{title}' and generate the following elements:\n"
    "1. Genre: Identify the genre of the comic book based on the title.\n"
    "2. Tone: Determine the tone of the comic book (e.g., dark, humorous, adventurous).\n"
    "3. Themes: Identify the main themes or messages conveyed in the comic book.\n"
    "4. Keywords: Extract relevant keywords or phrases that describe the comic book.\n"
    "5. Setting Details: Provide details about the setting, including the location, time period, and atmosphere.\n"
    "Ensure the output follows this exact format and contains no extra commentary.\n"
    "\n"
    "Return the output in **strict Python dictionary format** like this:\n"
    "```\n"
    "{{\n"
    "    'title': '{title}',\n"
    "    'genre': '<genre>',\n"
    "    'tone': '<tone>',\n"
    "    'themes': ['<theme1>', '<theme2>',],\n"
    "    'keywords': ['<keyword1>', '<keyword2>', '<keyword3>',],\n"
    "    'setting': {{\n"
    "        'location': '<location>',\n"
    "        'time_period': '<time_period>',\n"
    "        'atmosphere': '<atmosphere>'\n"
    "    }}\n"
    "}}\n"
    "```"
)

theme_prompt = PromptTemplate(input_variables=['title'], template=theme_prompt_template)

theme_output_parser = StrOutputParser()

theme_chain = LLMChain(
    llm=text_llm,
    prompt=theme_prompt,
    output_parser=theme_output_parser,
    output_key="theme_data"
)

#-------------------------------Plot Generation Chain

plot_prompt_template=(
    "Based on the provided details for the comic book concept:\n 'title':{title},\n'genre':{genre},\n'tone':{tone},\n'themes'{themes},\n'keywords':{keywords},\n'location':{location},\n'time_period':{time_period},\n'atmosphere':{atmosphere}\n"
    "Generate a structured plot outline. Follow this structure:\n"
    "Five-Act Structure (Introduction, Inciting Incident, Rising Tension, Climax, and Resolution)\n"
    "Major Conflicts (e.g., Hero vs. Antagonist, Internal Struggles)"
    "Key Locations (Important story settings)\n"
    "Return the output like this:\n"
    "```\n"
    "{{\n"
    "    'plot_structure': {{\n"
    "        'Act 1': 'Introduction to the world & protagonist (Describe the setting, main character, and initial world state) - <act1_description>',\n"
    "        'Act 2': 'Inciting incident & first conflict (Describe the key event that triggers the story's conflict) - <act2_description>',\n"
    "        'Act 3': 'Rising tension & subplots introduced (Outline secondary characters, side quests, or relationship development) - <act3_description>',\n"
    "        'Act 4': 'Climax & major confrontation (Describe the intense moment of conflict or revelation) - <act4_description>',\n"
    "        'Act 5': 'Resolution & possible sequel setup (Provide closure or hint at future developments) - <act5_description>'\n"
    "    }},\n"
    "    'major_conflicts': [\n"
    "        '<conflict1>',\n"
    "        '<conflict2>',\n"
    "    ],\n"
    "    'key_locations': [\n"
    "        '<location1>',\n"
    "        '<location2>',\n"
    "    ]\n"
    "}}\n"
    "```"
)

plot_prompt = PromptTemplate(input_variables=['genre','tone'], template=theme_prompt_template)

plot_output_parser = StrOutputParser()

plot_chain = LLMChain(
    llm=text_llm,
    prompt=plot_prompt,
    output_parser=plot_output_parser,
    output_key="plot_data"
)


#----------------------------------------Sequential Chain----------------------------------------

theme_seq_chain = SequentialChain(
            chains=[theme_chain],
            input_variables=['title'],
            output_variables=['theme_data'],
            verbose=True
        )

plot_seq_chain = SequentialChain(
            chains=[theme_chain, plot_chain],
            input_variables=['title','genre','tone','themes','keywords','location','time_period','atmosphere'],
            output_variables=['plot_data'],
            verbose=True
        )
