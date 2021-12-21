import logging

from telegram import Bot, Update, User, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler, InlineQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = (enter_your_token_here)

def start(update:Update, context:CallbackContext):
    update.message.reply_text("Hi! Please forward me your message to retrieve the message details.")
    
    user = update.effective_user
    
    update.message.reply_text(f"Your details are as follows:\n*username*: {user.username}\n*first name*: {user.first_name}\n*last name*: {user.last_name}\n*id*: {update.message.chat_id}", parse_mode=ParseMode.MARKDOWN)

def retrieve(update:Update, context:CallbackContext):
    user = update.effective_user

    if update.message.forward_from == None:
        if update.message.from_user == user:
            update.message.reply_text(f"Your details are as follows:\n*username*: {user.username}\n*first name*: {user.first_name}\n*last name*: {user.last_name}\n*id*: {update.message.chat_id}", parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text("Sorry, the user has prevented you from creating a link to the account when forwarding the message to me ☹️.")
    else:
        user = update.message.forward_from
        update.message.reply_text(f"The details of the sender are as follows:\n*username*: {user.username}\n*first name*: {user.first_name}\n*last name*: {user.last_name}\n*id*: {user.id}", parse_mode=ParseMode.MARKDOWN)

def error(update:Update, context: CallbackContext):
    '''Log Errors caused by Updates'''
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, retrieve))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()