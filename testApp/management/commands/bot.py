from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters, MessageHandler, Updater
from telegram.utils.request import Request
from testApp.models import Profile

# Функция для реакции на принятое сообщение: 
# ------В случае, если номер договора есть в базе ответ содержит номер договора и баланс
#       Иначе, сообщение о том, что номера нет в базе

def send_mess(update: Update, context: CallbackContext):
    text = update.message.text
    balance=0
    try:
        balance = Profile.objects.get(contractid=text).balance
        reply_text = "Номер договора ={}\n \n Ваш баланс: {} рублей".format(text, balance)
    except Exception:
        reply_text = "Номер договора не найден. Попробуйте еще раз."    
               
    update.message.reply_text(
        text=reply_text,
    )    

class Command(BaseCommand):
   
    help = 'Телеграмм бот'
    
    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )

        updater = Updater(
            bot=bot,
            use_context=True,
        )

        message_hendler = MessageHandler(Filters.text, send_mess)
        updater.dispatcher.add_handler(message_hendler)

        updater.start_polling()
        updater.idle()

