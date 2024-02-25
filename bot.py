from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

CHATS = "script.txt"

chatbot = ChatBot("Wellness Bot")

chatbot.storage.drop()

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Hi I'm Wellness Bot! What are your symptoms?",
])
trainer.train([
    "Coughing",
    "Do you have a fever?",
])
trainer.train([
    "Yes",
    "Any other symptoms?",
])
trainer.train([
    "Yes, stuffy runny nose and sneezing",
    "Any other symptoms?",
])
trainer.train([
    "Scratchy throat",
    "Any other symptoms?",
])
trainer.train([
    "No",
    "Okay! You may have the common cold, hope you feel better soon",
])


trainer.train(CHATS)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
