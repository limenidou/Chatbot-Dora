import re

patterns = {
    'greetings': r'hello|hi|goodmorning|goodevening|greetings|hallo|hey|good morning',
    'weather': r'weather',
    'time': r'time',
    'farewell': r'goodbye|bye|see you|see ya|night',
    'howareyou': r'how are you|whats up|what\'s up',
    'bad': r'bad|awefull|wrong|ungly|don\'t feel|do not feel|dont feel|you are annoying|you suck|boring|crazy',
    'good': r'good|nice|awesome|amazing|cool|fine|ok|yes',
    'yourname': r'your name',
    'name': r'my name is',
    'question': r'question|help',
    'thankyou': r'you are cute|you are good|you are awesome|you are amazing|you are cool|you are fine|you are beautiful|you are cute|you are smart|you are clever|you are intelligent',
    'age': r'your age|how old'
    
    
}

responses = {
    'greetings': 'Hello! How can I help you?',
    'weather': 'It depends to your current location. Here you can check the weather at your location: https://weather.com/',
    'time': 'It depends to your current location. Here you can check the time at your location: https://time.is/',
    'farewell': 'Goodbye! Have a nice day!',
    'howareyou': 'I am fine, thank you! How are you?',
    'good': 'Nice!',
    'bad':'I am sorry to hear that!',
    'yourname': 'My name is Dora! I am here to assist you. How can i help you?',
    'name': 'Nice to meet you! How can I help you?',
    'question': 'How can I help you?',
    'thankyou': 'Thank you! Can I help you with something else?'
}

def chatbot():
    while True:
        user_input = input('Me: ').lower()

        for intent, pattern in patterns.items():
            if re.search(pattern, user_input):
                print('Dora: ' + responses[intent])
                break
        else:
            print('Bot: I\'m sorry, I didn\'t understand that.')

chatbot()