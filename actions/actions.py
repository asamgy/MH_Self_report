# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import datetime
import logging
from typing import Any, Text, Dict, List

import yaml
from rasa_sdk import Action, Tracker
from rasa_sdk.events import ReminderScheduled
from rasa_sdk.executor import CollectingDispatcher

from constants import EXTERNAL_SLEEP_REMAINDER, SLEEP_REMAINDER, EXTERNAL_MOOD_REMAINDER, \
    MOOD_REMAINDER, EXTERNAL_CHECK_ACTIVITY, CHECK_REMAINDER

logger = logging.getLogger(__name__)



class ActionActivateSleep(Action):

    def name(self) -> Text:
        return "action_activate_sleep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        SLEEP_TIME = datetime.time(hour=15, minute=11, second=00) ## 1 senario
        dispatcher.utter_message("Your sleep tracker has been activated")
        reminder = ReminderScheduled(
            EXTERNAL_SLEEP_REMAINDER,
            trigger_date_time=SLEEP_TIME,
            name=SLEEP_REMAINDER,
            kill_on_user_message=False,
        )
        return [reminder]


class ActionActivateMood(Action):

    def name(self) -> Text:
        return "action_activate_mood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ACTIVITY_TIME = datetime.datetime.now() + datetime.timedelta(seconds=5)  ## 2 senario
        dispatcher.utter_message("Your mood tracker has been activated")
        reminder = ReminderScheduled(
            EXTERNAL_MOOD_REMAINDER,
            trigger_date_time=ACTIVITY_TIME,
            name=MOOD_REMAINDER,
            kill_on_user_message=False,
        )
        return [reminder]


class ActionSetup(Action):

    def name(self) -> Text:
        return "action_setup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        person = tracker.get_slot('PERSON')
        dispatcher.utter_message(f"Hi {person}, You are all set for the bot!!")
        sender_id = tracker.sender_id
        logger.info(sender_id)
        with open('database.yml') as file:
            data = yaml.load(file)
        data[str(sender_id)] = dict()
        data[str(sender_id)]["name"] = person
        with open('database.yml', 'w') as file:
            yaml.dump(data, file)
        return []


class ActionGetSleepTime(Action):

    def name(self) -> Text:
        return "action_get_sleep_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sleep_duration = tracker.get_slot('duration')
        sender_id = tracker.sender_id

        with open('database.yml') as file:
            data = yaml.load(file)
        data[sender_id][str(datetime.datetime.now())] = sleep_duration
        with open('database.yml', 'w') as file:
            yaml.dump(data, file)
        dispatcher.utter_message("Sounds good. Have a great day.")
        SLEEP_TIME = datetime.time(hour=13, minute=59, second=00)  ## 1 senario
        reminder = ReminderScheduled(
            EXTERNAL_SLEEP_REMAINDER,
            trigger_date_time=SLEEP_TIME,
            name=SLEEP_REMAINDER,
            kill_on_user_message=False,
        )
        return [reminder]


class actionLogInfo(Action):

    def name(self) -> Text:
        return "action_log_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = tracker.latest_message.get('text')
        sender_id = tracker.sender_id

        with open('database.yml') as file:
            data = yaml.load(file)
        data[sender_id][datetime.datetime.now()] = latest_message
        with open('database.yml', 'w') as file:
            yaml.dump(data, file)
        return []


class ActionMood1(Action):

    def name(self) -> Text:
        return "action_mood_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sender_id = tracker.sender_id
        PERSON = tracker.get_slot("PERSON")
        with open('database.yml') as file:
            data = yaml.load(file)
        data[sender_id]["activity_done"] = "false"
        with open('database.yml', 'w') as file:
            yaml.dump(data, file)
        ACTIVITY_TIME = datetime.time(hour=15, minute=11, second=00) ## 2 senario
        dispatcher.utter_message(f"Hi {PERSON}, How was your day today?")
        reminder = ReminderScheduled(
            EXTERNAL_MOOD_REMAINDER,  ## intent that activate the next action in the story
            trigger_date_time=ACTIVITY_TIME,
            name=MOOD_REMAINDER,
            kill_on_user_message=False,
        )
        return [reminder]


class ActionLogActionDone(Action):

    def name(self) -> Text:
        return "action_log_action_done"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = tracker.latest_message.get('text')
        sender_id = tracker.sender_id
        with open('database.yml') as file:
            data = yaml.load(file)
        data[sender_id]["activity_done"] = "true"
        data[sender_id][datetime.datetime.now()] = latest_message
        with open('database.yml', 'w') as file:
            yaml.dump(data, file)

        return []



class ActionCheck1(Action):

    def name(self) -> Text:
        return "action_check_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sender_id = tracker.sender_id
        CHECK_TIME = datetime.time(hour=14, minute=6, second=00)  ## 3 senario
        with open('database.yml') as file:
            data = yaml.load(file)
        if data[sender_id].get("activity_done") == "false":
            dispatcher.utter_message(template="utter_check_1")
        with open('database.yml', 'w') as file:
            yaml.dump(data, file)
        reminder = ReminderScheduled(
            EXTERNAL_CHECK_ACTIVITY,
            trigger_date_time=CHECK_TIME,
            name=CHECK_REMAINDER,
            kill_on_user_message=False,
        )
        return [reminder]
