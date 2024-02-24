from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

source_cb = "https://realpython.com/build-a-chatbot-python-chatterbot/"
chatbot = ChatBot("Dr. Pepper", 
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3')

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"👩‍⚕️ Dr. PP: {chatbot.get_response(query)}")

