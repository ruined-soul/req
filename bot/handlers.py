from telegram import Update, Bot
from telegram.ext import CallbackContext
from .config import approved_groups, log_channel_id

def start(update: Update, context: CallbackContext):
    message = ("This bot is not for public use and will only be used in specified chats. "
               "Please contact the developer for more information.")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def handle_message(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    if chat_id not in approved_groups:
        context.bot.leave_chat(chat_id)
        return

    message_text = update.message.text
    if '#request' in message_text:
        response = ("AAPKI REQUEST HAMNE SAVE KARLI HAI, JAISE HI HAME MAUKA MILTA HAI "
                    "HAM UNHE POORA KARNE KI POORI KOSHISH KARENGE")
        update.message.reply_text(response)
    else:
        context.bot.send_message(chat_id=log_channel_id, text=message_text)
