import io, os
import telegram
from telegram.ext import Updater, MessageHandler
from telegram.ext.filters import Filters


def cb(bot, update):
    if update.message.sticker is None:
        update.message.reply_text('Not a sticker!')
        return
    try:
        f = update.message.sticker.get_file().download_as_bytearray()
        s = io.BytesIO(f)
        update.message.reply_photo(photo=s)
    except telegram.TelegramError as err:
        update.message.reply_text('Error occurred: {}'.format(err))

token = os.environ.get('TELEGRAM_BOT_TOKEN')
if not token:
    os._exit(1)
updater = Updater(token)

updater.dispatcher.add_handler(MessageHandler(Filters.all, cb))

updater.start_polling()
updater.idle()

