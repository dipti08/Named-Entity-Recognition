Following are the steps required to run the RASA chatbot:

1. user is required to install rasa in his computer that is the user must have the demo rasa bot working in the laptop 

2. the installation shall be done using python version 3.6 which can be done by implementing a virtual envronment

3. to make a virtual environment -->
a.)open anaconda prompt
b.)go to the required folder where you want the demo rasa to be present
c.)type: conda create  -n enironment_name python=3.6
d.)type: conda activate environment_name
e.)pip install rasa
for installation, one can refer youtube tutorials or can visit rasa forum 

youtube reference video: https://www.youtube.com/watch?v=qmMaGicSFCU&list=PLIRnO_sdVuEevLMSy7bE-Jaqyf1MK_wtr&index=2

//nlu.md and stories.md files are present inside the 'data' folder
4. the file nlu.md can be used to add the custom intents and entities

5. the file stories.md adds the story path on which the bot has to work

6. domain.yml file consists of all the intents', entities, responses and actions used in the bot preparation. It basically is a universe of data for the chatbot.

7. config.yml and credentials.yml can be used as present in the demo file.

8. endpoints.yml requires to uncomment the 'action_endpoint' for the actions.py to reply to the bot.

9. actions.py file consists of the dynamic actions that the bot has to take. For example: reply with the suitable entities present inside the user query or present the user with a python tutorials reference link or HPE site visit link based upon the intent of the sentence.

10. textextract.py file helps to upload the pdf on an external port using rest api and allows the tagged entitie of the pdf to be presented to the user.

RUN COMMANDS:
1. To simply run the bot: open two separate conda prompts
a.)go the conda prompt: go inside the virtual folder of rasa in both the prompts

//FIRST CONDA PROMPT
b.)train the bot: training on the custom dataset prepared  --> type: rasa train
c.)to run the bot on the shell  --> type: rasa shell
		OR
d.)to run the bot on the rasa AI localhost port  --> type: rasa x

//SECOND CONDA PROMPT
e.)run the rasa actions server  --> type: rasa run actions


2. To extract data from the pdf file: open three separate conda prompts
a.)go the conda prompt: go inside the virtual folder of rasa for all the three prompts

//FIRST CONDA PROMPT
b.)train the bot: training on the custom dataset prepared  --> type: rasa train
c.)run the command: rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml

//SECOND COMMAND PROMPT
d.)run the rasa actions server  --> type: rasa run actions

//THIRD COMMAND PROMPT
e.)run the textextract.py file --> type: textextract.py

NOTE: ONCE THE MODEL IS TRAINED, WE GET A TRAINED MODEL WHICH GETS SAVED INSIDE A SEPARATE 'MODELS' DIRECTORY. WHEN WE INSTALL THE DEMO RASA BOT, WE GET A DEMO MODEL ALREADY PRESENT INSIDE THE DIRECTORY.

NOTE: A DEMO PDF FILE 'mydocu.pdf' IS PRESENT WHICH CAN BE USED FOR THE TESTING PURPOSE.