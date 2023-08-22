import requests
from bs4 import BeautifulSoup as BS
from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup,InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.types.messages_and_media import message
import speech_recognition as sr
from time import sleep
from pyrogram.types import Message
from pyrogram.raw import functions
from pyrogram.types import ChatPermissions
from pyrogram.errors import FloodWait
from pyrogram.types import InputPhoneContact
import random
from time import perf_counter
import subprocess
from pyrogram.handlers import MessageHandler
import asyncio
from pyrogram.raw import functions,types
import wget
from alive_progress import alive_bar
import datetime

app = Client('acc',api_id='7673043',api_hash='60b167e3ea495003048e13129fc1287a')

HEADERS={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': '*/*'
}
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import os
import sys
import logging
 
# Логирование
logging.basicConfig(filename="clip.log", filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
print("готово")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.on_message(filters.command("horoscope",prefixes="/") & filters.me & filters.text)
def horoscope(client, message):
    id=message.from_user.id
    client.delete_messages(
    chat_id=id,
    message_ids=message.message_id)
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


@app.on_message(filters.command("spam",prefixes="/") & filters.me & filters.text)
async def spam(client, message):
    count = message.command[1]
    text = " ".join(message.command[2:])
    count = int(count)
    try:
        sleep = 0.5
    except Exception as error:
        await message.edit(error)
        sleep = float(message.command[1])
    await message.delete()

    for _ in range(count):
        await client.send_message(message.chat.id, text)
        await asyncio.sleep(sleep)

@app.on_message(filters.command("weather",prefixes="/") & filters.me & filters.text)
def weather(client, message):
    try:
        logging.info("CLIP: Вывод погоды\n----------------------------------------------------------------------------")

        city = message.command[1]
        message.edit("🕑 Просматриваю погоду в вашей стране")
        r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=ru")
        message.edit(f"🗺 Ваш город : {r.text}")
        requests.onreadystatechange = function() 
    except FloodWait as e:
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            app.update_profile(last_name=f"{opisanie} | Флудвейт")
            sleep(e.x)
            app.update_profile(last_name=f"{opisanie}")
            f.close()

@app.on_message(filters.command("print", prefixes="/") & filters.me)
def type(_, msg):
    orig_text = msg.text.split("/print ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

# Прогресс бар
@app.on_message(filters.command("progressbar", prefixes="/") & filters.me)
def progressbar(client, message):
    try:
        logging.info("CLIP: Прогресс бар\n----------------------------------------------------------------------------")
        #with alive_bar(18, bar='classic', title='Подготовка', length=18) as bar:

        text = message.text.split("/progressbar ", maxsplit=1)[1]
        total = int(text)
        bar_length = 12
        for i in range(total + 1):
            percent = int(text) * i / total
            sleep(0.0001)
            message.edit(
                "Введёный процесс: "+ text + "\n[{:{}}] {:>1}%".format("█" * int(percent / (100.0 / bar_length)), bar_length, int(percent)))
    except FloodWait as e:
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            app.update_profile(last_name=f"{opisanie} | Флудвейт")
            sleep(e.x)
            app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

# Шансы
@app.on_message(filters.command("chance", prefixes="/") & filters.me)
def chance(client: Client, message: Message):
    try:
        logging.info("CLIP: Шанс\n----------------------------------------------------------------------------")
        text = message.text.split("/chance", maxsplit=1)[1]
        message.edit(f"{text}\nВероятность сказаного {random.randint(1, 100)}%")

    except Exception as erryr:
        logging.error(erryr)
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

# Демотиватор
@app.on_message(filters.command("dem", prefixes="/") & filters.me)
def demotivator(client: Client, message: Message):
    message.edit("⏳ | Создаю демотиватор, это может занять некоторое время...")
    username_dem = "KlounsBot"
    try:
        logging.info("CLIP: Создание демотиватора\n----------------------------------------------------------------------------")
        message.edit("Создание демотиватора..")
        if message.reply_to_message.photo:
            client.unblock_user(username_dem)
            capt = message.text.split('/' + 'dem', maxsplit=1)[1]
            client.send_photo(
                chat_id=username_dem,
                photo=message.reply_to_message.photo.file_id,
                caption=capt
            )
            photo = False

            while not photo:
                try:
                    sleep(2)
                    for iii in client.get_chat_history(username_dem, limit=1):
                        client.send_photo(chat_id=message.chat.id, photo=iii.photo.file_id)
                    photo = True
                    message.delete()
                except Exception as f:
                    message.edit(f)
                    sleep(2)
        else:
            message.edit("Пожалуйста, ответьте на фото")

    except Exception as erryr:
        logging.error(erryr)
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

# Читы репутация
@app.on_message(filters.command("rep", prefixes="/") & filters.me)
def repNakrutka(client: Client, message: Message):
    try:
        with open("rep.txt", "w+") as f:
            num = int(message.command[1])
            rep = num
            repo = str(rep)
            f.write(repo)
            f.close()
            text = "✅ | Вы успешно изменили свою репутацию.\n 🗓️ | Репутация " + str(repo) + ""
            message.edit(text)

        logging.info("CLIP: Накручена репутация\n----------------------------------------------------------------------------")

    except Exception as error:
        message.edit(
            f"❕ | Произошла ошибка!\n🗓️ | Репутация автоматически изменена на: 0\n❓ | Команда для изменения репутации '.rep'")
        with open("rep.txt", "w+") as f:
            num = int(0)
            rep = num
            repo = str(rep)
            f.write(repo)
            f.close()

@app.on_message(filters.command("rep", prefixes=".") & filters.me)
def rephelp(client: Client, message: Message):
    try:
        logging.info("CLIP: help репутация\n----------------------------------------------------------------------------")
        message.edit("Команда с репутацией должна выглядить так: <code>/rep число</code>")
    except Exception as erryr:
        logging.error(erryr)
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

# Удалить смс
@app.on_message(filters.command("del", prefixes="/") & filters.me)
def delete_messages(client: Client, message: Message):
    try:
        if message.reply_to_message:
            logging.info("CLIP: Удаление сообщения\n----------------------------------------------------------------------------")

            message_id = message.reply_to_message.message_id
            app.delete_messages(message.chat.id, message_id)
            message.delete()

    except Exception as erryr:
        logging.error(erryr)
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

# статистика
@app.on_message(filters.command("statistics", prefixes="/") & filters.me)
def id(client: Client, message: Message):
    try:
        logging.info("CLIP: Получение ID\n----------------------------------------------------------------------------")

        if message.reply_to_message is None:
            message.edit(f"👤 | Айди Чата: {message.chat.id}\nИмя собеседника: {message.chat.first_name}\nМошеник: {message.chat.is_scam}\nФейк: {message.chat.is_fake}\nПоддержка телеграм: {message.chat.is_support}\n")
        else:
            id = f"👤 | Айди пользователя: {message.reply_to_message.from_user.id}\n📢 | Айди чата: {message.chat.id}\nИмя собеседника: {message.reply_to_message.from_user.first_name}\nМошеник: {message.reply_to_message.from_user.is_scam}\nФейк: {message.reply_to_message.from_user.is_fake}\nПоддержка телеграм: {message.reply_to_message.from_user.is_support}\n"
            message.edit(id)

    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

#Вечный оффлайн
def afk_handler(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start

        if message.from_user.is_bot is False:
            message.reply_text(
                f"❕ Этот пользователь AFK.\n" f"<b>💬 Причина:</b> {reason}.\n" f"<b>⏳ Продолжительность:</b> {afk_time}")
    except NameError:
        pass

@app.on_message(filters.command("afk", prefixes="/") & filters.me)
def afk(client, message):
    try:
        logging.info("CLIP: AFK on\n----------------------------------------------------------------------------")
        global start, end, handler, reason
        start = datetime.datetime.now().replace(microsecond=0)
        handler = client.add_handler(
            MessageHandler(afk_handler,
                           (filters.private & ~filters.me | filters.group & filters.mentioned & ~filters.me)))
        if len(message.text.split()) >= 2:
            reason = message.text.split(" ", maxsplit=1)[1]
        else:
            reason = message.command[1]
        message.edit(f"❕ Ты ущёл <b>AFK</b>.\n<b>💬 Причина:</b> {reason}.\n")
    except Exception as f:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

# No AFK
@app.on_message(filters.command("unafk", prefixes="/") & filters.me)
def unafk(client, message):
    try:
        logging.info("CLIP: AFK офф\n----------------------------------------------------------------------------")
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        message.edit(
            f"❕ Этот пользователь больше не <b>AFK.</b>\n⏳ Продолжительность <b>AFK:</b> {afk_time}"
        )
        client.remove_handler(*handler)
    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

#Поиск музыки по название
@app.on_message(filters.command("m", prefixes="/") & filters.me)
def send_music(client, message):
    message.edit("Поиск...")
    song_name = ""
    if len(message.command) > 1:
        song_name = " ".join(message.command[1:])
    elif message.reply_to_message and len(message.command) == 1:
        song_name = (
                message.reply_to_message.text or message.reply_to_message.caption
        )
    elif not message.reply_to_message and len(message.command) == 1:
        message.edit("Введите название песни:")
        sleep(2)
        message.delete()
        return

    song_results = client.get_inline_bot_results("smusic2bot", song_name)

    try:
        # отправить в сохраненные сообщения, потому что hide_via иногда не работает
        saved = client.send_inline_bot_result(
            chat_id="me",
            query_id=song_results.query_id,
            result_id=song_results.results[0].id,
            hide_via=True,
        )

        # пересылать как новое сообщение из сохраненных сообщений
        saved = client.get_messages("me", int(saved.updates[1].message.id))
        reply_to = (
            message.reply_to_message.message_id
            if message.reply_to_message
            else None
        )
        client.send_audio(
            chat_id=message.chat.id,
            audio=str(saved.audio.file_id),
            reply_to_message_id=reply_to,
        )

        # удалить сообщение из сохраненных сообщений
        client.delete_messages("me", saved.message_id)
    except TimeoutError:
        message.edit("Это не сработало")
        sleep(2)
    message.delete()

#Текст лестницей
@app.on_message(filters.command("ladder",prefixes="/") & filters.me)
def ladder(client, message):
    try:
        logging.info("CLIP: Текст лестницей\n----------------------------------------------------------------------------")

        orig_text = message.text.split("/ladder ", maxsplit=1)[1]
        text = orig_text
        output = []
        for i in range(len(text) + 1):
            output.append(text[:i])
        ot = "\n".join(output)
        message.edit(ot)

    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

#Текст ссылкой
@app.on_message(filters.command("link",prefixes="/") & filters.me)
def link(client, message):
    try:
        logging.info("CLIP: Текст ссылкой\n----------------------------------------------------------------------------")

        link = message.command[1]
        text = " ".join(message.command[2:])
        message.delete()
        client.send_message(message.chat.id, f'<a href="{link}">{text}</a>', disable_web_page_preview=True)
        
    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

#Пинг
@app.on_message(filters.command('ping',prefixes="/") & filters.me)
def ping(client, message):
    start1 = perf_counter()
    message.edit("Тест Ping📈..")
    end1 = perf_counter()

    start2 = perf_counter()
    message.edit("Тест Ping📉..")
    end2 = perf_counter()

    start3 = perf_counter()
    message.edit("Тест Ping📈...")
    end3 = perf_counter()

    start4 = perf_counter()
    message.edit("Тест Ping📉...")
    end4 = perf_counter()

    pinges = ((end1 + end2 + end3 + end4) / 4) - ((start1 + start2 + start3 + start4) / 4)
    ping = pinges * 1000

    if 0 <= ping <= 199:
      connect = "🟢 Стабильный"
    if 199 <= ping <= 400:
      connect = "🟠 Хорошо"
    if 400 <= ping <= 600:
      connect = "🔴 Не стабильный"
    if 600 <= ping:
      connect = "⚠ Проверьте подключение к сети"
    message.edit(f"<b>⏳ Ping\n📶</b> {round(ping)} ms\n{connect}")

#Создание цытаты
@app.on_message(filters.command("q",prefixes="/") & filters.me)
def quotly(client, message):
    idstick = 0
    if not message.reply_to_message:
        message.edit("Ответить на сообщение")
        return

    message.edit("Создавайте цитаты... подождите...")
    app.unblock_user("QuotLyBot")
    sleep(1)
    message.reply_to_message.forward("QuotLyBot")
    sleep(4)
    iii = app.get_history("QuotLyBot", limit=1)
    idstick = iii[0].sticker.file_id
    app.send_sticker(message.chat.id, idstick)

@app.on_message(filters.command("bio",prefixes="/") & filters.me)
def quotly(client, message):
    message.edit(f"{message}")

# @app.on_message(filters.command("bio",prefixes="/") & filters.me)
# def quotly(client, message):
#     message.edit(f"Message\n├─Type: Message\n├─message_id: {message.message_id}\n├─from_user: \n│   ├─Type: User\n│   ├─id: {message.from_user.id}\n│   ├─is_self: ✅{message.from_user.is_self}❌\n│   ├─is_contact: ✅{message.from_user.is_contact}❌\n│   ├─is_mutual_contact: ✅{message.from_user.is_mutual_contact}❌\n│   ├─is_deleted: ✅{message.from_user.is_deleted}❌\n│   ├─is_bot: ✅{message.from_user.is_bot}❌\n│   ├─is_verified: ✅{message.from_user.is_verified}❌\n│   ├─is_restricted: ✅{message.from_user.is_restricted}❌\n│   ├─is_scam: ✅{message.from_user.is_scam}❌\n│   ├─is_fake: ✅{message.from_user.is_fake}❌\n│   ├─is_support: ✅{message.from_user.is_support}❌\n│   ├─first_name: {message.from_user.first_name}\n│   ├─status: {message.from_user.status}\n│   ├─username: {message.from_user.username}\n│   ├─dc_id: {message.from_user.dc_id}\n│   ╰─photo: \n│       ├─Type: ChatPhoto\n│       ├─small_file_id: {message.from_user.photo.small_file_id}\n│       ├─small_photo_unique_id: {message.from_user.photo.small_photo_unique_id}\n│       ├─big_file_id: {message.from_user.photo.big_file_id}\n│       ╰─big_photo_unique_id: {message.from_user.photo.big_photo_unique_id}\n├─date: {message.date}\n├─chat: \n│   ├─Type: Chat\n│   ├─id: {message.chat.id}\n│   ├─type: {message.chat.type}\n│   ├─is_verified: ✅{message.chat.is_verified}❌\n│   ├─is_restricted: ✅{message.chat.is_restricted}❌\n│   ├─is_creator: ✅{message.chat.is_creator}❌\n│   ├─is_scam: ✅{message.chat.is_scam}❌\n│   ├─is_fake: ✅{message.chat.is_fake}❌\n│   ├─title: {message.chat.title}\n│   ├─username: {message.chat.username}\n│   ├─photo: \n│   │   ├─Type: ChatPhoto\n│   │   ├─small_file_id: {message.chat.photo.small_file_id}\n│   │   ├─small_photo_unique_id: {message.chat.photo.small_photo_unique_id}\n│   │   ├─big_file_id: {message.chat.photo.big_file_id}\n│   │   ╰─big_photo_unique_id: {message.chat.photo.big_photo_unique_id}\n│   ├─dc_id: {message.chat.dc_id}\n│   ├─has_protected_content: {message.chat.has_protected_content}❌\n│   ╰─permissions: \n│       ├─Type: ChatPermissions\n:")
#     #│       ├─can_send_messages: ✅{message.chat.permissions.can_send_messages}❌\n│       ├─can_send_media_messages: ✅{message.chat.permissions.can_send_media_messages}❌\n│       ├─can_send_other_messages: ✅{message.chat.permissions.can_send_other_messages}❌\n│       ├─can_send_polls: ✅{message.chat.permissions.can_send_polls}❌\n│       ├─can_add_web_page_previews: ✅{message.chat.permissions.can_add_web_page_previews}❌\n│       ├─can_change_info: ✅{message.chat.permissions.can_change_info}❌\n│       ├─can_invite_users: ✅{message.chat.permissions.can_invite_users}❌\n│       ╰─can_pin_messages: ✅{message.chat.permissions.can_pin_messages}❌\n├─mentioned: ✅{message.mentioned}❌\n├─scheduled: ✅{message.scheduled}❌\n├─from_scheduled: ✅{message.from_scheduled}❌\n├─has_protected_content: ✅{message.has_protected_content}❌\n├─text: {message.text}\n├─entities: [{'_': 'MessageEntity', 'type': 'url', 'offset': 34, 'length': 12}]\n╰─outgoing: ✅{message.outgoing}❌\n")



#Список комманд
@app.on_message(filters.command("help",prefixes="/") & filters.me & filters.text)
def help(client, message):
    try:
        logging.info("CLIP: Список комманд\n----------------------------------------------------------------------------")
        id=message.chat.id
        message.edit("🕐 Загрузка меню помощи. Пожалуйста подождите...")
        sleep(2)
        message.edit(f"🔍Гороскоп: <code>/horoscope текст</code>\n☂Погода: <code>/weather город</code>\n🎧Поиск музыки по название: <code>/m название</code>\n🤟Репутация: <code>/rep число</code>\n🪜Текст лестницей: <code>/ladder текст</code>\n🔗Текст ссылкой: <code>/link ссылка текст</code>\n⏳Пинг: <code>/ping</code>\n💯Шанс: <code>/chance</code>\n📝Создание цытаты: <code>/q</code>\n🔵Статус онлайн: <code>/online</code>\n🔴Вечный оффлайн: <code>/afk причина</code>\n👨‍🏫Прогресс бар: <code>/progressbar число</code>\n🤪Мем из картинки: <code>/dem слово</code>\n💼Статистика пользователя: <code>/statistics</code>\n✍Текст печатаеться по букве: <code>/print текст</code>\n🗣Голосовое текстом: <code>/text</code>\n👨‍💻Спам пользователю: <code>/spam количество текст</code>\n👁‍🗨JSON <code>/bio</code>\n")

    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")


app.run()