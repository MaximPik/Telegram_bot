import telegram
import os
from dotenv import load_dotenv
import requests
import asyncio

load_dotenv() 

token_gh = os.getenv('Token_github')
url_github = 'https://api.github.com/user'
token_tg = os.getenv('Token_tg')
myID = os.getenv('MyID_tg')

GITHUB_TOKEN = token_gh
TELEGRAM_TOKEN = token_tg  # добавить токен
CHAT_ID = myID  # добавить chat_id

def get_user_data():
    data = {
        'Authorization':f'token {GITHUB_TOKEN}',
    }
    response = requests.get(url=url_github, headers=data).json()
    return response

def message():
    user_data = get_user_data()
    message = ''
    if user_data:
        message = f'Мой логин: {user_data["login"]}\n'
        message += f'Моё имя: {user_data["name"]}\n'
        message += f'Публичные репозитории: {user_data["public_repos"]}'
    return message

async def send_info(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    if message: 
        await bot.send_message(text=message, chat_id=CHAT_ID)
    else:
        await bot.send_message(text="Не вышло(", chat_id=CHAT_ID)


if __name__ == "__main__":
    userInfo = message()
    asyncio.run(send_info(userInfo))
