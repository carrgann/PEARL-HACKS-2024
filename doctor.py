from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from cleaner import parse_script


CHATS = "script.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "What are your symptoms?",
])
trainer.train([
    "Coughing",
    "Do you have a fever?",
])
trainer.train([
    "Naur",
    "Any other symptoms?"
])
trainer.train([
    "Yes",
    "Do you have a sore throat?"
])
trainer.train([
    "Yes",
    "What are your other symptoms?"
])
trainer.train([
    "None.",
    "Consider: bronchitis, common cold"
])
trainer.train([
    "Coughing",
    "Consider: bronchitis, common cold"
])

trainer.train(CHATS)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")