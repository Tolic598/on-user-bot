import requests
from bs4 import BeautifulSoup as BS
from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup,InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.types.messages_and_media import message
import datetime, time

app = Client('goroscop',api_id='7673043',api_hash='60b167e3ea495003048e13129fc1287a')

HEADERS={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': '*/*'
}

@app.on_message(filters.command("horoscope",prefixes="/") & filters.me & filters.text)
def horoscope(client, message):
    id=message.from_user.id
    message.text=message.command[1]

    if message.text=="овен" or message.text=="Овен":
        o=requests.get('https://orakul.com/horoscope/astrologic/more/aries/today.html',headers=HEADERS)
        o.raise_for_status()
        html=BS(o.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="Близнецы" or message.text=="близнецы":
        b=requests.get('https://orakul.com/horoscope/astrologic/more/gemini/today.html',headers=HEADERS)
        b.raise_for_status()
        html=BS(b.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="телец" or message.text=="Телец":
        t=requests.get('https://orakul.com/horoscope/astrologic/more/taurus/today.html',headers=HEADERS)
        t.raise_for_status()
        html=BS(t.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")


    if message.text=="рак" or message.text=="Рак":
        r=requests.get('https://orakul.com/horoscope/astrologic/more/cancer/today.html',headers=HEADERS)
        r.raise_for_status()
        html=BS(r.text,"html.parser")
        
        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="лев" or message.text=="Лев":
        l=requests.get('https://orakul.com/horoscope/astrologic/more/lion/today.html',headers=HEADERS)
        l.raise_for_status()
        html=BS(l.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="дева" or message.text=="Дева":
        d=requests.get('https://orakul.com/horoscope/astrologic/more/virgo/today.html',headers=HEADERS)
        d.raise_for_status()
        html=BS(d.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="весы" or message.text=="Весы":
        v=requests.get('https://orakul.com/horoscope/astrologic/more/libra/today.html',headers=HEADERS)
        v.raise_for_status()
        html=BS(v.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")


    if message.text=="скорпион" or message.text=="Скорпион":
        s=requests.get('https://orakul.com/horoscope/astrologic/more/scorpio/today.html',headers=HEADERS)
        s.raise_for_status()
        html=BS(s.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="стрелец" or message.text=="Стрелец":
        st=requests.get('https://orakul.com/horoscope/astrologic/more/sagittarius/today.html',headers=HEADERS)
        st.raise_for_status()
        html=BS(st.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="козерог" or message.text=="Козерог":
        c=requests.get('https://orakul.com/horoscope/astrologic/more/capricorn/today.html',headers=HEADERS)
        c.raise_for_status()
        html=BS(c.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")


    if message.text=="водолей" or message.text=="Водолей":
        vo=requests.get('https://orakul.com/horoscope/astrologic/more/aquarius/today.html',headers=HEADERS)
        vo.raise_for_status()
        html=BS(vo.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

    if message.text=="рыбы" or message.text=="Рыбы":
        ri=requests.get('https://orakul.com/horoscope/astrologic/more/pisces/today.html',headers=HEADERS)
        ri.raise_for_status()
        html=BS(ri.text,"html.parser")

        name=html.find('h1').get_text(strip=True)
        dni=html.find('div',class_="sm-descr").get_text(strip=True)
        textgoroscop=html.find('div',class_="horoBlock").get_text(strip=True)
        message.reply_text(f"Имя: {name}\nДата: {dni}\nПредсказание: {textgoroscop}")

@app.on_message(filters.command("statistics",prefixes="/") & filters.me & filters.text)
def id(client, message):
    id=message.chat.id
    name = message.chat.first_name
    message.reply_text(f"id собеседника: {id}\nИмя собеседника: {name}")

@app.on_message(filters.command("spam",prefixes="/") & filters.me & filters.text)
def spam(client, message):
    col=message.command[1]
    text=message.command[2]
    for i in col:
        message.reply_text(f"{text}")

@app.on_message(filters.command("help",prefixes="/") & filters.me & filters.text)
def help(client, message):
    message.reply_text(f"🧐Гороскоп: <code>/horoscope текст</code>\n💼Статистика пользователя: <code>/statistics</code>\n👨‍💻Спам пользователю: <code>/spam количество текст</code>")

start_time = time.time()
dt = datetime.datetime.today().strftime('%d.%m %H:%M')
end_time = (time.time()) - start_time
print((f'Юзербот запущен\nДата запуска: {dt}\nВремя запуска: {round(end_time,1)} секунды\n'))
app.run()