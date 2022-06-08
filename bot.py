#importacion de las dependecias de las librerias Telegram
import os
import telebot.types
from telebot import *
from telegram.ext import *
from requests import *
from telegram import *
from telegram_menu import *
INPUT_TEXT=0
#Bienvenida del Bot
def help(update, context):
    update.message.reply_text(text='Hola te saluda Zabot, Como te ayudamos?,'
                                   'Por el momento solo reconozco los siguientes comandos : '
                                   ' /start ------------ Visualizar el menu de catalogos '
                                   ' /need  -------------Necesitas informacion ¿? ')

#creacion de comando de inico con categorias de butones para dinamismo del bot
def start(update, context):
    button1 = InlineKeyboardButton(text='Servicios', url='https://www.instagram.com/deli_cupcakesg/?hl=es')
    update.message.reply_text(text='Bievenido, Zabot a la Orden! ! !,'
                                   ' Haz clic en un boton',
                              reply_markup=InlineKeyboardMarkup([
                                  [button1]
                              ]))
def need(update, context):
    update.message.reply_text(text='Me han creado para ayudarte con tus dudas, :) '
                                   'por ahora no puedo entender emojis, stickers, imagenes '
                                   'selecciona el comando /help para regresar al inicio Gracias !!')
#El bot iniciara desde aca
if __name__ == '__main__':
    #updater una forma de las peticiones que manda el usuario
    bot= Updater(token='5413583997:AAFdJ3bfiWIz0UHd-R9ppKvhc2Lrp1cD6JE',use_context=True) #API genearada y brindad a por Telegram
    #Se encarga enviar las accciones por updtaer, Dispachar es que se encarga mandejar los comandos
    dp=bot.dispatcher
    f1=bot.dispatcher
    f2=bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    f1.add_handler(CommandHandler('help',help))
    f2.add_handler(CommandHandler('need', need))
    #Un ciclco infinito si un usuario por la api de telegram
    #el bot se activa y atieneden al usuario @pulling
    bot.start_polling()
    bot.idle()
