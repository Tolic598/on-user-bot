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
import subprocess

app = Client('goroscop',api_id='7673043',api_hash='60b167e3ea495003048e13129fc1287a')

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

# Проверка библиотек
try:
    os.system("termux-wake-lock")
    import alive_progress
    import wget
except ModuleNotFoundError:
    os.system("pip3 install alive_progress")
    os.system("pip3 install wget")

os.system("cls" if os.name == "nt" else "clear")
import wget
from alive_progress import alive_bar

with alive_bar(18, bar='classic', title='Подготовка', length=18) as bar:
    bar()
    try:
        import datetime
    except ModuleNotFoundError:
        os.system("pip3 install datetime")

    bar()
    try:
        import wikipedia
    except ModuleNotFoundError:
        os.system("pip3 install wikipedia")

    bar()
    try:
        import pyrogram
    except ModuleNotFoundError:
        os.system("pip3 install pyrogram")

    bar()
    try:
        import requests
    except ModuleNotFoundError:
        os.system("pip3 install requests")

    bar()
    try:
        import gtts
    except ModuleNotFoundError:
        os.system("pip3 install gtts")

    bar()
    try:
        import colorama
    except ModuleNotFoundError:
        os.system("pip3 install colorama")

    bar()
    try:
        import youtube_dl
    except ModuleNotFoundError:
        os.system("pip3 install youtube_dl")

    bar()
    try:
        import db0mb3r
    except ModuleNotFoundError:
        os.system("pip3 install db0mb3r")

    bar()
    try:
        import configparser
    except ModuleNotFoundError:
        os.system("pip3 install configparser")

    bar()
    try:
        import telegraph
    except ModuleNotFoundError:
        os.system("pip3 install telegraph")

    bar()
    configuration = os.path.exists("config.ini")
    if not configuration:
        wget.download("https://raw.githubusercontent.com/A9FM/filesUB/main/config.ini", "config.ini", bar=False)

    bar()
    stop = os.path.exists('stop.ogg')
    if not stop:
        wget.download('https://github.com/A9FM/filesUB/blob/main/stop.ogg?raw=true', "stop.ogg", bar=False)

    bar()
    update = os.path.exists("update.ogg")
    if not update:
        wget.download("https://github.com/A9FM/filesUB/blob/main/update.ogg?raw=true", "update.ogg", bar=False)

    bar()
    start = os.path.exists('start.ogg')
    if not start:
        wget.download('https://github.com/A9FM/filesUB/blob/main/start.ogg?raw=true', "start.ogg", bar=False)

    bar()
    reput = os.path.exists('rep.txt')
    if not reput:
        wget.download('https://raw.githubusercontent.com/A9FM/filesUB/main/rep.txt', "rep.txt", bar=False)

    bar()
    reput = os.path.exists('notes.txt')
    if not reput:
        wget.download('https://raw.githubusercontent.com/A9FM/filesUB/main/notes.txt', "notes.txt", bar=False)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Префиксы доп
config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)


def get_prefix():
    prefix = config.get("prefix", "prefix")
    return prefix

try:
    prefix = get_prefix()
except:
    config.add_section("prefix")
    config.set("prefix", "prefix", ".")
    with open(config_path, "w") as config_file:
        config.write(config_file)
    prefix = "."
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
def spam(client, message):
    id=message.chat.id
    client.delete_messages(
    chat_id=id,
    message_ids=message.message_id)
    col=message.command[1]
    text1=message.command[2]
    a=len(message.command)
    print(a)
    if a==3:
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1}")
    elif a==4:
        text2=message.command[3]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2}")
    elif a==5:
        text2=message.command[3]
        text3=message.command[4]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3}")
    elif a==6:
        text2=message.command[3]
        text3=message.command[4]
        text4=message.command[5]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3} {text4}")
    elif a==7:
        text2=message.command[3]
        text3=message.command[4]
        text4=message.command[5]
        text5=message.command[6]
        text6=message.command[7]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3} {text4} {text5} {text6}")
    elif a==8:
        text2=message.command[3]
        text3=message.command[4]
        text4=message.command[5]
        text5=message.command[6]
        text6=message.command[7]
        text7=message.command[8]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3} {text4} {text5} {text6} {text7}")
    elif a==9:
        text2=message.command[3]
        text3=message.command[4]
        text4=message.command[5]
        text5=message.command[6]
        text6=message.command[7]
        text7=message.command[8]
        text8=message.command[9]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3} {text4} {text5} {text6} {text7} {text8}")
    elif a==10:
        text2=message.command[3]
        text3=message.command[4]
        text4=message.command[5]
        text5=message.command[6]
        text6=message.command[7]
        text7=message.command[8]
        text8=message.command[9]
        text9=message.command[10]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3} {text4} {text5} {text6} {text7} {text8} {text9}")
    elif a==11:
        text2=message.command[3]
        text3=message.command[4]
        text4=message.command[5]
        text5=message.command[6]
        text6=message.command[7]
        text7=message.command[8]
        text8=message.command[9]
        text9=message.command[10]
        text10=message.command[11]
        for i in range(int(col)):
            sleep(0.5)
            message.reply_text(f"{text1} {text2} {text3} {text4} {text5} {text6} {text7} {text8} {text9} {text10}")

@app.on_message(filters.command("text",prefixes="/") & filters.me & filters.text)
def text(client, message):
    try:
        if not message.reply_to_message:
                message.edit("<b>Нету реплай!</b>")
        else:
                if message.reply_to_message.voice:
                    message.edit("<b>Подождите....</b>")
                    client.send_message("@voicybot", "/start")
                    sleep(1)
                    message.reply_to_message.forward("@voicybot")
                    sleep(3)
                    messages = client.get_history("@voicybot")
                    message.edit(
                        f'<b>Текст:</b>\n{messages[0].text.replace("При поддержке Бородач Инвест"," ")}'
                    )
                    client.send(
                        functions.messages.DeleteHistory(
                            peer=client.resolve_peer(259276793),
                            max_id=0,
                            just_clear=True,
                        )
                    )
                else:
                    message.edit("<b>Это не голосовое сообщение!</b>")
    except Exception as e:
        message.edit(f"<b>Упсс:</b> <code>{e}</code")

@app.on_message(filters.command("weather",prefixes="/") & filters.me & filters.text)
def weather(client, message):
    try:
        logging.info("CLIP: Вывод погоды\n----------------------------------------------------------------------------")

        city = message.command[1]
        message.edit("🕑 Просматриваю погоду в вашей стране")
        r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=ru")
        message.edit(f"🗺 Ваш город : {r.text}")
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



@app.on_message(filters.command("print", prefixes="/") & filters.me)
def type(_, msg):
    orig_text = msg.text.split("/print ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
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

# Репутация
@app.on_message(filters.text & filters.incoming & filters.regex("^\-$") & filters.reply)
async def repMinus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:
            with open("rep.txt", "r+") as f:
                data1 = f.read()
                dat = int(data1)
                num = 1
                rep = dat - num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "❎ Осуждение оказано (-1)\n🌐 Текущая репутация: " + str(repo) + ""
                await message.reply_text(text)
            logging.info("CLIP: Понижение репутации")
    except:
        pass

@app.on_message(filters.text & filters.incoming & filters.regex("^\+$") & filters.reply)
def repPlus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:
            with open("rep.txt", "r+") as f:
                data = f.read()
                data = int(data)
                num = 1
                rep = data + num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "✅ Уважение оказано (+1)\n🌐 Текущая репутация: " + str(repo)
                message.reply_text(text)
            logging.info("CLIP: Повышение репутации")
    except:
        pass

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
    try:
        logging.info("CLIP: Создание демотиватора\n----------------------------------------------------------------------------")

        if message.reply_to_message.photo:
            app.unblock_user("memegeneration_bot")
            donwloads = app.download_media(message.reply_to_message.photo.file_id)
            tuxt = message.text.split("/dem ", maxsplit=1)[1]
            text = "1. " + tuxt
            app.send_photo(chat_id="memegeneration_bot", photo=donwloads, caption=text)
            sleep(4)
            iii = app.get_history("memegeneration_bot")
            donwloads = app.download_media(iii[0].photo.file_id)
            app.send_photo(chat_id=message.chat.id, photo=donwloads)
            message.delete()
            os.rmdir("/downloads/")
        else:
            message.edit("❗️ | Сделайте реплай на изображение для создания демотиватора")

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
    timesnow = datetime.datetime.now().strftime('%d.%m.%Y\nВремя %H:%M:%S')
    try:
        logging.info("CLIP: Получение ID\n----------------------------------------------------------------------------")

        if message.reply_to_message is None:
            message.edit(f"👤 | Айди Чата: {message.chat.id}\nИмя собеседника: {message.chat.first_name}\nМошеник: {message.chat.is_scam}\nФейк: {message.chat.is_fake}\nПоддержка телеграм: {message.chat.is_support}\nТекущая дата: {timesnow}")
        else:
            id = f"👤 | Айди пользователя: {message.reply_to_message.from_user.id}\n📢 | Айди чата: {message.chat.id}\nИмя собеседника: {message.reply_to_message.first_name}\nМошеник: {message.reply_to_message.is_scam}\nФейк: {message.reply_to_message.is_fake}\nПоддержка телеграм: {message.reply_to_message.is_support}\nТекущая дата: {timesnow}"
            message.edit(id)

    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

@app.on_message(filters.command("help",prefixes="/") & filters.text)
def help(client, message):
    try:
        logging.info("CLIP: Список комманд")
        id=message.chat.id
        #client.delete_messages(
        #chat_id=id,
        #message_ids=message.message_id)
        #message.edit("🕐 Загрузка меню помощи. Пожалуйста подождите...")
        message.reply_text(
        f"🧐Гороскоп: <code>/horoscope текст</code>\n☂Погода: <code>/weather город</code>\nРепутация: <code>/rep число</code>\nУдалить смс: <code>/del</code>\nПрогресс бар: <code>/progressbar число</code>\nМем из картинки: <code>/dem слово</code>\n💼Статистика пользователя: <code>/statistics</code>\n✍Текст печатаеться по букве: <code>/print</code>\n🗣Голосовое текстом: <code>/text</code>\n👨‍💻Спам пользователю: <code>/spam количество текст</code>")
    except Exception as error:
        message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @Logiers_bot")
        app.send_document("Logiers_bot", "clip.log")

app.run()
