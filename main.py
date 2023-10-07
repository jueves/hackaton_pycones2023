import os
import openai
import telebot
from dotenv import load_dotenv

# Load keys
load_dotenv()

CHATGPT_KEY = os.environ.get("CHATGPT_KEY")
TELEGRAM_KEY = os.environ.get("TELEGRAM_KEY")

openai.api_key = CHATGPT_KEY
messages_dic = {}

bot = telebot.TeleBot(TELEGRAM_KEY)