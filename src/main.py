import json
import logging
from os import environ
from sys import exit

from decouple import config
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from bot import Bot

logging.basicConfig(level=environ.get("LOGLEVEL", "INFO"), format="%(asctime)s - %(levelname)s - %(message)s")

TRACKID = config("TRACKID")
TOKEN = config("TOKEN")
CHATID = config("CHATID")
STATUSDIR = config("STATUSDIR", "./data/status.json")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    logging.info(f'{update.effective_chat}')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def delete(update, context):
    logging.info(f'{update.effective_chat}')
    context.bot.send_message(chat_id=update.effective_chat.id, text="This command will delete!!!")

def track(update, context):
    logging.info(f'{update.effective_chat}')
    logging.info(f'{context.args[0]}')

    context.bot.send_message(chat_id=update.effective_chat.id, text="Tracking...")
    bot = Bot(trackid=context.args[0], telegramToken=TOKEN)

    data = bot.compare(statusfile=STATUSDIR, chatID=CHATID)

    context.bot.send_message(chat_id=update.effective_chat.id, text=json.dumps(dict))


def unknown(update, context):
    logging.info(f'{update.effective_chat}')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == "__main__":
    if TRACKID is None or TOKEN is None or CHATID is None:
        logging.error(f'Error on load env vars: [TRACKID {TRACKID} - TOKEN {TOKEN} - CHATID {CHATID}]')
        exit(1)

    start_handler = CommandHandler('start', start)
    del_handler = CommandHandler('del', delete)
    track_handler = CommandHandler('track', track)

    # unknown_message = MessageHandler(
    #     (
    #         (~Filters.command) & (Filters.text) | #tem texto e não tem comando
    #         (~Filters.command) #não tem comando
    #     )
    #     , unknown
    # )    
    # dispatcher.add_handler(unknown_message)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(del_handler)
    dispatcher.add_handler(track_handler)
    
    updater.start_polling()




