import logging

from telegram import Bot, Update, User, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext, CallbackQueryHandler, InlineQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = (enter_your_token_here)

def start(update, context):
    """Send a message when the command /start is issued by the user."""
    user = update.effective_user
    if user.last_name != None:
      update.message.reply_text(f'Hi {user.first_name} {user.last_name}!')
    else:
      update.message.reply_text(f'Hi {user.first_name}!')


def help(update,context):
    """Send a message when the command /help is issued by the user."""
    update.message.reply_text('How can I help you?')


def echo(update, context):
    """Echoes the user message."""
    update.message.reply_text(f"{update.message.text}")

def main():
    """Start the bot."""
    # Creates the Updater and passes your bot's token to the Updater.
    updater = Updater(token)

    # Initiates a dispatcher to register handlers
    dispatcher = updater.dispatcher

    # The bot will automatically answer the user upon receiving these commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # Echoes the messages sent by the user on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()