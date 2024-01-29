from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot instance
# creating storage for the bot in sql lit
mybot = ChatBot('7amada')

mybot = ChatBot('7amada',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                database_uri='sqlite:///database.sqlite3')
# logic adapter?
mybot = ChatBot('7amada',
                logic_adapters=[
                    'chatterbot.logic.BestMatch',
                    'chatterbot.logic.TimeLogicAdapter'
                ],
                )

# Create a new trainer for the chatbot
trainer = ListTrainer(mybot)

trainer.train([
    'Hi',
    'Hello',
    'I need your assistance regarding my order',
    'Please, Provide me with your order id',
    'I have a complaint.',
    'Please elaborate, your concern',
    'How long it will take to receive an order ?',
    'An order takes 3-5 Business days to get delivered.',
    'Okay Thanks',
    'No Problem! Have a Good Day!'
])

# response variable
myinput = input('begin your query: ')
response = mybot.get_response(myinput)

# print(response)
print('Bot Response:', response)
# Train the chatbot using the English corpus

# Interaction loop
myinput = input('begin your query: ')
print("Welcome to the Bot Service! Let me know how can I help you?")

while True:
    request = input(myinput + ':')

    if request == 'bye' or request == 'salam':

        print('byby ya 7abebe!!')
        break
    else:
        response = mybot.get_response(request)
        print('Bot:', response)

# Get user input

# Get chatbot response

# Print chatbot response

# Exit loop if user enters 'exit'
