<!-- this file consists of different story paths that the bot recognises according to the flow of the chat -->
## bot happy reply path
* greet
 - utter_bot_greet
* ask_about_intent
 - utter_ok
* mul_sen
 - action_reply
 - utter_are_you_satisfied
* affirm
 - utter_happy_to_help
 - utter_do_you_want_to_continue
* goodbye
 - utter_bot_bye

## bot not happy reply path
* greet
 - utter_bot_greet
* ask_about_intent
 - utter_ok
* mul_sen
 - action_reply
 - utter_are_you_satisfied
* deny
 - utter_sorry
 - utter_do_you_want_to_continue
* goodbye
 - utter_bot_bye

## bot entity path
* mul_sen
 - action_reply

## bot python link path
* python_link
 - action_python_link

## bot hpe link path
* hpe_link
 - action_hpe_link
