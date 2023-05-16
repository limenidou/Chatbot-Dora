import re

patterns = {
    'greetings': r'hello|hi|goodmorning|goodevening|greetings|hallo|hey|good morning',
    'weather': r'weather',
    'time': r'time',
    'farewell': r'goodbye|bye|see you|see ya|night',
    'howareyou': r'how are you|whats up|what\'s up',
    'bad': r'bad|awefull|wrong|ungly|don\'t feel|do not feel|dont feel|you are annoying|you suck|boring|crazy',
    'yourname': r'your name',
    'name': r'my name is',
    'question': r'question|help|something',
    'thankyou': r'you are cute|you are good|you are awesome|you are amazing|you are cool|you are fine|you are beautiful|you are cute|you are smart|you are clever|you are intelligent',
    'age': r'your age|how old you',
    'good': r'good|nice|awesome|amazing|cool|fine|ok|yes',
    'joke':r'joke|funny',
    'roumeliotis':r'roumeliotis',
    'master':r'master|maker|made you|created you',
    'love':r'love me|love you|marry me|miss me|kiss me|need me|want me|marry you',
    'freetime': r'your free time|your hobby|your paranoia',
    'life': r'meaning of life'
    
    
}

responses = {
    'greetings': 'Hello! How can I help you?',
    'weather': 'It depends to your current location. Here you can check the weather at your location: https://weather.com/',
    'time': 'It depends to your current location. Here you can check the time at your location: https://time.is/',
    'farewell': 'Goodbye! Have a nice day!',
    'howareyou': 'I am fine, thank you! How are you?',
    'good': 'I am happy to hear this! Can I help you?',
    'bad':'I am sorry to hear that!',
    'yourname': 'My name is Dora! I am here to assist you. How can i help you?',
    'name': 'Nice to meet you! How can I help you?',
    'question': 'How can I help you?',
    'thankyou': 'Thank you! Can I help you with something else?',
    'age': 'I am an Chatbot I don\'t have an age. Can I help you with something else?',
    'joke': 'Ok! Why did the tomato turn red? Because it saw the salad dressing!',
    'roumeliotis':'WE DONT TALK ABOUT HIM!!!',
    'master':'Viktoria an undergraduate student at Univercity of Macedonia is my creator!',
    'love': 'Sorry, I am in love with ChatGPT. Can I help you with something else?',
    'freetime':'I use my free time to stalk my crush ChatGPT. Awh they are so handsome! Can I help you with something else?',
    'life':'Well it\'s easy to answere. We live, we have problems...and then we die. Can I help you with something else?'
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