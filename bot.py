from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "7969721443:AAFedT6AYZlBOuf_mQZsw-E6hgDD_XTFKtY"

def handle_message(update, context):
    update.message.reply_text("سلام! من ربات دوستیابی هستم 🌟")

if __name__ == '__main__':
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    print("🤖 ربات روشنه... منتظره پیام!")
    updater.start_polling()
    updater.idle()