from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

CHATS = "script.txt"

chatbot = ChatBot("Chatpot")

chatbot.storage.drop()

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
    "Naur.",
    "Any other symptoms?",
])

trainer.train(CHATS)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
