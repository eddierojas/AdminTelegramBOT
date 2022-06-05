#importacion de las dependecias de las librerias Telegram
import telegram
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

INPUT_TEXT=0

#creacion de comando de inico con categorias de butones para dinamismo del bot
def start(update, context):
    button1 = InlineKeyboardButton(text='Productos',url='https://www.youtube.com/watch?v=4I25nV9hXGA')
    update.message.reply_text(text='Bienvenidos, Te saludoa ISO, Haz clic en un boton',
                              reply_markup=InlineKeyboardMarkup([
                                  [button1]
                              ]))

#El bot iniciara desde aca
if __name__ == '__main__':
    #updater una forma de las peticiones que manda el usuario
    bot= Updater(token='5413583997:AAFdJ3bfiWIz0UHd-R9ppKvhc2Lrp1cD6JE',use_context=True) #API genearada y brindad a por Telegram
    #Se encarga enviar las accciones por updtaer, Dispachar es que se encarga mandejar los comandos
    dp=bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    #Un ciclco infinito si un usuario por la api de telegram
    #el bot se activa y atieneden al usuario @pulling
    bot.start_polling()
    bot.idle()
