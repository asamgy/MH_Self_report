## Import the libraries
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import datetime
import mysql.connector
import config
from rich.console import Console

# create a Mysql Connection to Database
connection  = mysql.connector.connect(
  host = config.HOST,
  user = config.USER,
  password = config.PASSWORD,
  database = config.DATABASE
)

# Creating cursor object for Mysql Database connection. 
cursor = connection.cursor()

# Creating a console object for Printing Rich Comments, This is option instead of using this we can use simple print staments. 
Console = Console()

# Create a recongnizier object form Speech Recognition
recognizer = speech_recognition.Recognizer()

# intialize a speech object for text to speech,
speaker = tts.init()
speaker.setProperty('rate', config.SPEAKER_SPEED) # Seting speed of speaker object, helps to set speed of BOT replying slower or faster.

## Scenario 1 - start - condition from wakeup text and as per time of the day.

def scenario_1_start():
    global conversation
    conversation = ["{}".format(str(datetime.datetime.now()))]
    conversation.append("scenario 1")
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speaker.say("Good Morning John, How did you sleep?")
        speaker.runAndWait()
        conversation.extend([message, "Good Morning John, How did you sleep?"])
        print(conversation)
    elif hour>=12 and hour<18:
        speaker.say("Good Afternoon John, How did you sleep?")
        speaker.runAndWait()
        conversation.extend([message, "Good Afternoon John, How did you sleep?"])
        print(conversation)
    else:
        speaker.say("Good Evening John, How did you sleep?")
        speaker.runAndWait()
        conversation.extend([message, "Good Evening John, How did you sleep?"])
        print(conversation)


## Scenario 2 - start - condition from wakeup text and as per time of the day.

def scenario_2_start():
    global conversation
    conversation = ["{}".format(str(datetime.datetime.now()))]
    conversation.append("scenario 2")
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speaker.say("Good Morning John,  How was your day today?")
        speaker.runAndWait()
        conversation.extend([message, "Good Morning John, How did you sleep?"])
        print(conversation)
    elif hour>=12 and hour<18:
        speaker.say("Good Afternoon John,  How was your day today?")
        speaker.runAndWait()
        conversation.extend([message, "Good Afternoon John, How did you sleep?"])
        print(conversation)
    else:
        speaker.say("Good Evening John,  How was your day today?")
        speaker.runAndWait()
        conversation.extend([message, "Good Evening John, How did you sleep?"])
        print(conversation)


## Scenario 3 - missed notification- condition from wakeup text

def scenario_3_start(): 
    global conversation
    conversation = ["{}".format(str(datetime.datetime.now()))]
    conversation.append("scenario 3")
    hour=datetime.datetime.now().hour
    speaker.say("You did not report your mood and activity yesterday. Do you want to report them now?")
    speaker.runAndWait()
    conversation.extend([message, "You did not report your mood and activity yesterday. Do you want to report them now?"])
    print(conversation)

## Intent : how_active - conditons for intent how_active to respond as per different 3 scenrios. 
    
def how_active():
    global conversation
    if conversation[1] == 'scenario 1':
        speaker.say(config.ERROR)
        speaker.runAndWait()
    elif conversation[1] == 'scenario 2':
        if len(conversation) == 8:
            speaker.say("Alright then, have a good night!")
            speaker.runAndWait()
            conversation.extend([message, "Alright then, have a good night!"])
            print(conversation)
            if len(conversation) == 10:
                conversation = tuple(conversation)
                conversation = [conversation]
                print("final conversation is {}".format(conversation))
                query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
                values = conversation
                # Saving the conversation string to Databse
                cursor.executemany(query,values)
                connection.commit()
                sys.exit(0)
            else:
                diff = 10 - len(conversation)
                for i in range(0, diff):
                    conversation.append(" ")
                conversation = tuple(conversation)
                conversation = [conversation]
                print("final conversation is {}".format(conversation))
                query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
                values = conversation
                # Saving the conversation string to Databse
                cursor.executemany(query,values)
                connection.commit()
                sys.exit(0)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()
    elif conversation[1] == 'scenario 3':
        if len(conversation) == 8:
            speaker.say("Okay, thank you for answering the questions.")
            speaker.runAndWait()
            conversation.extend([message, "Okay, thank you for answering the questions."])
            print(conversation)
            if len(conversation) == 10:
                conversation = tuple(conversation)
                conversation = [conversation]
                print("final conversation is {}".format(conversation))
                query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
                values = conversation
                # Saving the conversation string to Databse
                cursor.executemany(query,values)
                connection.commit()
                sys.exit(0)
            else:
                diff = 10 - len(conversation)
                for i in range(0, diff):
                    conversation.append(" ")
                conversation = tuple(conversation)
                conversation = [conversation]
                print("final conversation is {}".format(conversation))
                query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
                values = conversation
                # Saving the conversation string to Databse
                cursor.executemany(query,values)
                connection.commit()
                sys.exit(0)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()


## Intent : sleep_duration - conditons for intent how_active to respond as per different 3 scenrios.       
      
def sleep_duration():
    global conversation
    if conversation[1] == 'scenario 1':
        if len(conversation) == 4:
            speaker.say("And how long did you sleep?")
            speaker.runAndWait()
            conversation.extend([message, "And how long did you sleep?"])
            print(conversation)
        elif len(conversation) == 6:
            speaker.say("Sounds good. Have a great day.")
            speaker.runAndWait()
            conversation.extend([message, "Sounds good. Have a great day."])
            print(conversation)
            if len(conversation) == 10:
                conversation = tuple(conversation)
                conversation = [conversation]
                print("final conversation is {}".format(conversation))
                query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
                values = conversation
                # Saving the conversation string to Databse
                cursor.executemany(query,values)
                connection.commit()
                sys.exit(0)
            else:
                diff = 10 - len(conversation)
                for i in range(0, diff):
                    conversation.append(" ")
                conversation = tuple(conversation)
                conversation = [conversation]
                print("final conversation is {}".format(conversation))
                query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
                values = conversation
                # Saving the conversation string to Databse
                cursor.executemany(query,values)
                connection.commit()
                sys.exit(0)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()
    elif conversation[1] == 'scenario 2':
        speaker.say(config.ERROR)
        speaker.runAndWait()
    elif conversation[1] == 'scenario 3':
        speaker.say(config.ERROR)
        speaker.runAndWait()
    else:
        speaker.say(config.ERROR)
        speaker.runAndWait()

 ## Intent : how_is_mood - conditons for intent how_active to respond as per different 3 scenrios.   

def how_is_mood():
    global conversation
    if conversation[1] == 'scenario 1':
        speaker.say(config.ERROR)
        speaker.runAndWait()
    elif conversation[1] == 'scenario 2':
        if len(conversation) == 4:
            speaker.say("How was your mood like?")
            speaker.runAndWait()
            conversation.extend([message, "How was your mood like?"])
            print(conversation)
        elif len(conversation) == 6:
            speaker.say("And, how active were you?")
            speaker.runAndWait()
            conversation.extend([message, "And, how active were you?"])
            print(conversation)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()
    elif conversation[1] == 'scenario 3':
        if len(conversation) == 6:
            speaker.say("And, how active were you?")
            speaker.runAndWait()
            conversation.append(message)
            conversation.append("And, how active were you?")
            print(conversation)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()

 ## Intent : affirm - conditons for intent how_active to respond as per different 3 scenrios.                
            
def affirm():
    global conversation
    if conversation[1] == 'scenario 1':
        speaker.say(config.ERROR)
        speaker.runAndWait()
    elif conversation[1] == 'scenario 2':
        if len(conversation) == 6:
            speaker.say("And, how active were you?")
            speaker.runAndWait()
            conversation.append(message)
            conversation.append("And, how active were you?")
            print(conversation)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()
    elif conversation[1] == 'scenario 3':
        if len(conversation) == 4:
            speaker.say("Okay. Tell me how was mood yesterday?")
            speaker.runAndWait()
            conversation.append(message)
            conversation.append("Okay. Tell me how was mood yesterday?")
            print(conversation)
        elif len(conversation) == 6:
            speaker.say("And, how active were you?")
            speaker.runAndWait()
            conversation.append(message)
            conversation.append("And, how active were you?")
            print(conversation)
        else:
            speaker.say(config.ERROR)
            speaker.runAndWait()

 ## Intent : quit - conditons for intent how_active to respond as per different 3 scenrios.               
            
def quit():
    global conversation
    speaker.say("Take Care. Bye")
    speaker.runAndWait()
    conversation.extend([message, "Bye"])
    print(conversation)
    if len(conversation) == 10:
        conversation = tuple(conversation)
        conversation = [conversation]
        print("final conversation is {}".format(conversation))
        query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
        values = conversation
        # Saving the conversation string to Databse
        cursor.executemany(query,values)
        connection.commit()
        sys.exit(0)
    else:
        diff = 10 - len(conversation)
        for i in range(0, diff):
            conversation.append(" ")
        conversation = tuple(conversation)
        conversation = [conversation]
        print("final conversation is {}".format(conversation))
        query = "INSERT INTO {} (TIME, SCENARIO, USER_MSG_1, BOT_MSG_1, USER_MSG_2, BOT_MSG_2, USER_MSG_3, BOT_MSG_3, USER_MSG_4, BOT_MSG_4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(config.TABLE_NAME)
        values = conversation
        # Saving the conversation string to Databse
        cursor.executemany(query,values)
        connection.commit()
        sys.exit(0)


# Mapping is used to connect actions defined in app.py with intents defined in intent.json. This will be used to train the bot and give responses.
        
mappings = {
    "scenario_1_start" : scenario_1_start,
    "exit" : quit,
    "how_active" : how_active,
    "sleep_duration" : sleep_duration,
    "how_is_mood": how_is_mood,
    "scenario_2_start": scenario_2_start,
    "scenario_3_start" : scenario_3_start,
    "affirm" : affirm,
}

# create a assistant object based on intent.json and mappings created earlier

assistant = GenericAssistant('intent.json', intent_methods= mappings)
assistant.train_model()


# To keep the BOT running we use while condtions and start the speech recognition engine.

while True:
    try:
        with speech_recognition.Microphone() as mic:
            # create a recognizier object for mic
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            # get the audio received using listen method of speech recognition
            audio = recognizer.listen(mic)
            # create a message object to save the audio as text
            message = recognizer.recognize_google(audio)
            # convert the message object to lower case
            message = message.lower()
            #print the message received in console
            Console.print("[cyan]Message received is - [/] [red]{}[/]".format(message))
        
        # send the message object to assitant object for intent recognition.
        assistant.request(message)
       
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
