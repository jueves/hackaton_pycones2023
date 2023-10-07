import os
import openai
import telebot
from dotenv import load_dotenv

# Load keys
load_dotenv()

CHATGPT_KEY = os.environ.get("CHATGPT_KEY")
TELEGRAM_KEY = os.environ.get("TELEGRAM_KEY")

with open("start.txt", "r", encoding="utf-8") as f:
    start_message = f.read()

with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

user_tasks = {}

openai.api_key = CHATGPT_KEY

bot = telebot.TeleBot(TELEGRAM_KEY)

full_report = "Vacío"

def get_answer(message):
    '''
    Takes a Telebot message oject, passes its text to chatGPT
    and returns the answer.
    '''
    if (message.from_user.id not in user_tasks):
        user_tasks[message.from_user.id] = message.text

    all_users_tasks = ""

    for user, task in user_tasks.items():
        all_users_tasks += str(user) + ": " + task

    print("##### ALL USERS TASKS:\n", all_users_tasks)

    messages_to_openai = [{'role': 'system', 'content': prompt},
                          {"role": "user", "content": all_users_tasks}]
    
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_to_openai)
    full_report = chat.choices[0].message.content
    user_answer = "Gracias " + str(message.from_user.id) + " he tomado nota de tu actividad."
    return(user_answer, full_report)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    '''
    Takes all incoming messages and returns answers.
    '''
    global full_report
    if (message.text == "/start"):
        answer = start_message
    elif (message.text == "/report"):
        answer = full_report
    else:
        answer, full_report = get_answer(message)

    bot.reply_to(message, answer, parse_mode='Markdown')

bot.infinity_polling()

