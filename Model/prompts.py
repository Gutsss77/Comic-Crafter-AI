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
    "Return the output seperately in '**csv**' string format :\n"
    '{{\n'
    '    genre: <genre>,\n'
    '    tone: <tone>,\n'
    '    themes: [<theme1>, <theme2>,],\n'
    '    keywords: [<keyword1>, <keyword2>, <keyword3>,],\n'
    '    setting: {{\n'
    '        location: <location>,\n'
    '        time_period: <time_period>,\n'
    '        atmosphere: <atmosphere>\n'
    '    }}\n'
    '}}'
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
    "Based on the provided details for the comic book concept:\n "
    "{title}\n"
    "{theme_data}\n"
    "Generate a structured plot outline. Follow this structure:\n"
    "- Five-Act Structure (\n"
    "Act 1 : Introduction to the world & protagonist (Describe the setting, main character, and initial world state)\n"
    "Act 2 : Inciting incident & first conflict (Describe the key event that triggers the story's conflict)\n"
    "Act 3 : Rising tension & subplots introduced (Outline secondary characters, side quests, or relationship development)\n"
    "Act 4 : Climax & major confrontation (Describe the intense moment of conflict or revelation)\n"
    "Act 5 : Resolution, moral values & ending (Provide closure and moral values gained from the story)\n"
    ")\n"
    "- Major Conflicts"
    "- Key Locations (Important story settings)\n"
    "- Moral of the whole story that inflects and add value to the story and society\n"
    "Ensure the output follows this exact format and contains no extra commentary.\n"
    "\n"
    "Return the output seperately in '**csv**' string format :\n"
    '{{\n'
    '    act_<act_number>: {{\n'
    '        summary: <act_number_description>,\n'
    '        key_events: ['
    '            <event1>,\t'
    '            <event2> '
    '        ],\n'
    '        key_locations: ['
    '            <location1>,\t'
    '            <location2> '
    '        ],\n'
    '        conflict/others: <conflict/others>\n'
    '       }}\n'
    '}}'
)

plot_prompt = PromptTemplate(input_variables=['title', 'theme_data'], template=plot_prompt_template)

plot_output_parser = StrOutputParser()

plot_chain = LLMChain(
    llm=text_llm,
    prompt=plot_prompt,
    output_parser=plot_output_parser,
    output_key="plot_data"
)

#-------------------------------Characters Generation Chain
char_promtp_template = (
    "- Goal: Generate dynamic characters with personalities, motivations, and relationships.\n "
    "\n"
    "## Input: \n "
    "- Title : \n"
    "{title}\n"
    "- Themes : \n "
    "{theme_data}\n "
    "- Structured Plot :  \n "
    "{plot_data}\n "
    "\n"
    "## Processing Steps: \n "
    "- Protagnist/Anti-protagnist and side-kicks Archetype Selection (Using predefined character tropes)\n"
    "- Dynamic Backstory Generation for each character\n"
    "- Personality & Motivations Matching (Ensure character goals fit the story)\n"
    "- Inter-character Relationships Mapping\n"
    "\n"
    "---"
    "Ensure the output follows this exact format and contains no extra commentary.\n"
    "\n"
    "Return the output seperately in '**csv**' string format :\n"
    '{{\n'
    '  Char_<character_number>: {{\n'
    '      name: <Character Name>,\n'
    '      role: <Protagonist / Antagonist / Supporting>,\n'
    '      age: <Age or Age Range>,\n'
    '      appearance: {{\n'
    '        hair: <Hair description>,\n'
    '        eyes: <Eye description>,\n'
    '        clothing: <Clothing style>,\n'
    '        unique_features: [<feature_decription_1>, <feature_decription_2>,]\n'
    '           }},\n'
    '      personality: {{\n'
    '        traits: [<Key_traits_1>, <Key_traits_2>],\n'
    '        internal_conflicts: [<Emotional struggles, doubts, or traumas>,],\n'
    '        speech_pattern: {{\n'
    '          style: <Formal, sarcastic, cryptic, etc.>,\n'
    '          common_phrases: [<Repeated phrases for consistency>,]\n'
    '                   }}\n'
    '           }},\n'
    '      strengths: [<Unique skills like Hacking, Combat Mastery>,],\n'
    '      weaknesses: [<Character flaws like Arrogance, Fear of Isolation>,],\n'
    '      motivation: {{\n'
    '        primary: <Main driving force - e.g., Rescue mission, Revenge>,\n'
    '        secondary: <Additional goal or desire for added depth>\n'
    '           }},\n'
    '      relationships: {{\n'
    '        <Character 1>: <Relationship type - e.g., Mentor, Rival, Trusted Ally>,\n'
    '        <Character 2>: <Relationship type with context>,\n'
    '        notes: [<Key events that shaped this relationship>]\n'
    '           }},\n'
    '      introduction_moment: {{\n'
    '        scene: <Scene number>,\n'
    '        description: <How this character is first introduced to the audience>\n'
    '           }}\n'
    '    }}\n'
    '}}'
)

char_prompt = PromptTemplate(input_variables=['theme_data','plot_data'], template=char_promtp_template)

char_output_parser = StrOutputParser()

char_chain = LLMChain(
    llm=text_llm,
    prompt=char_prompt,
    output_parser=char_output_parser,
    output_key="character_data"
)


#----------------------------------------Sequential Chain----------------------------------------

# common chain generate theme, plot and character

gen_seq_chain = SequentialChain(
    chains=[theme_chain,plot_chain,char_chain],
    input_variables=['title'],
    output_variables=['theme_data','plot_data','character_data'],
    verbose=True
)

# gen_seq_chain = SequentialChain(
#     chains=[theme_chain,plot_chain],
#     input_variables=['title'],
#     output_variables=['theme_data','plot_data'],
#     verbose=True
# )

# gen_seq_chain = SequentialChain(
#     chains=[theme_chain],
#     input_variables=['title'],
#     output_variables=['theme_data'],
#     verbose=True
# )

# output:
# {
#     "title" : ,
#     "theme_data" : "
#           {dictionaries}
#       " ,
#     "plot_data" : "
#           {dictionaries}
#       " ,
#     "character_data" : "
#           {dictionaries}
#       " ,
# }

# "theme_data" :
# {```python/json
    # "{
    # 'title': '{title}',
    # 'genre': '<genre>',
    # 'tone': '<tone>',
    # 'themes': ['<theme1>', '<theme2>',],
    # 'keywords': ['<keyword1>', '<keyword2>', '<keyword3>',],
    # 'setting': {
    #         'location': '<location>',
    #         'time_period': '<time_period>',
    #         'atmosphere': '<atmosphere>'
    #     }
    # }"
    # ```}"






    # "    'act_2': {{\n"
    # "        'summary': '<act2_description>',\n"
    # "        'key_events': [\n"
    # "            '<event1>',\n"
    # "            '<event2>',\n"
    # "        ],\n"
    # "        'key_locations': [\n"
    # "            '<location1>',\n"
    # "            '<location2>',\n"
    # "        ],\n"
    # "        'conflict/others': '<conflict/others>'\n"
    # "       }},\n"
    # "    'act_3': {{\n"
    # "        'summary': '<act3_description>',\n"
    # "        'key_events': [\n"
    # "            '<event1>',\n"
    # "            '<event2>',\n"
    # "        ],\n"
    # "        'key_locations': [\n"
    # "            '<location1>',\n"
    # "            '<location2>',\n"
    # "        ],\n"
    # "        'conflict/others': '<conflict/others>'\n"
    # "       }},\n"
    # "    'act_4': {{\n"
    # "        'summary': '<act4_description>',\n"
    # "        'key_events': [\n"
    # "            '<event1>',\n"
    # "            '<event2>',\n"
    # "        ],\n"
    # "        'key_locations': [\n"
    # "            '<location1>',\n"
    # "            '<location2>',\n"
    # "        ],\n"
    # "        'conflict/others': '<conflict/others>'\n"
    # "       }},\n"
    # "    'act_5': {{\n"
    # "        'summary': '<act5_description>',\n"
    # "        'key_events': [\n"
    # "            '<event1>',\n"
    # "            '<event2>',\n"
    # "        ],\n"
    # "        'key_locations': [\n"
    # "            '<location1>',\n"
    # "            '<location2>',\n"
    # "        ],\n"
    # "        'conflict/others': '<conflict/others>'\n"
    # "       }}\n"