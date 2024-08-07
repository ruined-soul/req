from bot.config import bot_token
from bot.handlers import start, handle_message
from bot.logger import logger
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
