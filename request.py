from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, InlineQueryHandler, CallbackQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from html.parser import HTMLParser
import distutils.dir_util
import requests
import codecs
import time
import os
from bs4 import BeautifulSoup
import os
import logging
logging.basicConfig(format="\n%(levelname)s: @'%(asctime)s' in '%(name)s':\n> %(message)s", level=logging.INFO)
updater = Updater(token='');

def gethtml(url = '0'):
    if url == '0':
        return 0
    else:
        #url = 'www.google.com'
        session = requests.session()
        response = session.get(url).text
        file = codecs.open('test.txt', 'w', 'utf-8');
        soup = BeautifulSoup(response, "html.parser")
        file.write (soup.get_text("\n"))
        file.close
        return 1

def main(bot, update):
    geturl(update.message.text)
    return

updater.dispatcher.add_handler(MessageHandler(Filters.text, main))
updater.start_polling()
updater.idle()