from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, InlineQueryHandler, CallbackQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from time import gmtime, strftime, sleep
import logging
logging.basicConfig(format="\n%(levelname)s: @'%(asctime)s' in '%(name)s':\n> %(message)s", level=logging.INFO)
import codecs
import os

updater = Updater(token='');
def reset(bot, update):
    keyboard = [[KeyboardButton('Reset')]]
    bot.sendMessage(chat_id=update.message.chat_id, text="Reset done.", reply_markup=ReplyKeyboardMarkup(keyboard))
    if os.path.exists('%s.txt' % update.message.chat_id):
        os.remove('%s.txt' % update.message.chat_id)
    return
def main(bot, update):
    if update.message.text == "Reset":
        reset(bot, update)
        return
    keyboard = [[KeyboardButton('Reset')]]
    if os.path.exists('%s.txt' % update.message.chat_id):
        file = codecs.open('%s.txt' % update.message.chat_id, 'r', 'utf-8')
        content = file.readlines()
        file.close
        for i in range(0, len(content), 2):
            keyboard.append([KeyboardButton('%s %s' % (content[i].replace('\n', ''), content[i+1].replace('\n', '')))])
        file.close
    name = ""
    link = ""
    for i in update.message.text:
        if i == " ":
            link = update.message.text.replace("%s " % name, "")
            break
        name += i
    if not link == "" and "www." in link:
        print ("|%s|%s|" % (name, link))
        if os.path.exists('%s.txt' % update.message.chat_id):
            file = codecs.open('%s.txt' % update.message.chat_id, 'r', 'utf-8')
            content = file.readlines()
            file.close
            for i in range(0, len(content), 2):
                if name == i and link == i+1:
                    keyboard.append([KeyboardButton('%s %s' % (name, link))])
                    file = codecs.open('%s.txt' % update.message.chat_id, 'a', 'utf-8')
                    file.write("%s\n%s\n" % (name, link))
                    file.close
        else:
            file = codecs.open('%s.txt' % update.message.chat_id, 'a', 'utf-8')
            file.write("%s\n%s\n" % (name, link))
            file.close
            keyboard.append([KeyboardButton('%s %s' % (name, link))])
        bot.sendMessage(chat_id=update.message.chat_id, text="<a href='%s'>%s</a>" % (link, name), parse_mode="HTML", reply_markup=ReplyKeyboardMarkup(keyboard))
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Wrong request.\nExample: <strong>Google www.google.com</strong>", parse_mode="HTML", reply_markup=ReplyKeyboardMarkup(keyboard))
    return

updater.dispatcher.add_handler(MessageHandler(Filters.text, main))
updater.dispatcher.add_handler(CommandHandler('reset', reset))

updater.start_polling()
updater.idle()