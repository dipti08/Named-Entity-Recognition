# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPythonLink(Action):

    def name(self) -> Text:
        return "action_python_link"

    def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         Link="https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
         #dispatcher.utter_message(text="Hello World!")
         dispatcher.utter_template("utter_python_link",tracker,link=Link)

         return []

class ActionLangTag(Action):

     def name(self) -> Text:
         return "action_lang"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)
         lang=None

         for e in entities:
             if e['entity'] == "lang":
                 lang = e['value']

         dispatcher.utter_message(text=lang+" lang")

         return []

class ActionOrgTag(Action):

     def name(self) -> Text:
         return "action_organisation"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)
         org=None

         for e in entities:
             if e['entity'] == "org":
                 org = e['value']
            
         dispatcher.utter_message(text=org+" org")

         return []

class ActionTechTag(Action):

     def name(self) -> Text:
         return "action_technology"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)          
         tech=None

         for e in entities:
             if e['entity'] == "tech":
                 tech = e['value']
            
         dispatcher.utter_message(text=tech+" tech")

         return []

class ActionProdTag(Action):

     def name(self) -> Text:
         return "action_product"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         entities = tracker.latest_message['entities']
         print(entities)
         prod=None

         for e in entities:
             if e['entity'] == "prod":
                 prod = e['value']
            
         dispatcher.utter_message(text=prod+" prod")

         return []



