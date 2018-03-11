from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, InlineQueryHandler, CallbackQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram import UserProfilePhotos

import os

import logging
logging.basicConfig(
    format="\n%(levelname)s: @'%(asctime)s' in '%(name)s':\n> %(message)s", level=logging.INFO)

updater = Updater(token='')


def main(bot, update):
    request = update.message.text
    return


updater.dispatcher.add_handler(MessageHandler(Filters.text, main))
updater.start_polling()
updater.idle()
