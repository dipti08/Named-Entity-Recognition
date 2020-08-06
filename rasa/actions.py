# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#ActionReplyTag recognises the required entities mentioned in the user query and 
#thus helps in tagging
class ActionReplyTag(Action):

     def name(self) -> Text:
         return "action_reply"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         #collecting all the entities of the query in a list
         entities = tracker.latest_message['entities']
         print(entities)
         tag=None
         message=""
         
         #message consists of the all the words along with their respective tags
         for e in entities:
             if e['entity'] == "lang":
                 tag = e['value']
                 message = message + tag +" - lang, "
             elif e['entity'] == "org":
                 tag = e['value']
                 message = message + tag +" - org, "
             elif e['entity'] == "tech":
                 tag = e['value']
                 message = message + tag +" - tech, "
             elif e['entity'] == "prod":
                 tag = e['value']
                 message = message + tag +" - prod, "
    
         dispatcher.utter_message(text=message)        

         return []


#ActionPythonLinkTag helps the bot to reply with the suitable link to view 
#python tutorials
class ActionPythonLinkTag(Action):

     def name(self) -> Text:
         return "action_python_link"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         Link="https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"

         dispatcher.utter_template("utter_python_link",tracker,link=Link)

         return []


#ActionHpeLinkTag helps the bot to reply with the HPE site link
#to help the user know more about HPE
class ActionHpeLinkTag(Action):

     def name(self) -> Text:
         return "action_hpe_link"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         Link="https://www.hpe.com/in/en/home.html"

         dispatcher.utter_template("utter_hpe_link",tracker,link=Link)

         return []
