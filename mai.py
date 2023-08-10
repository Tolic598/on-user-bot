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
