#importacion de las dependecias de las librerias Telegram
import os
import telebot.types
from telebot import *
from telegram.ext import *
from requests import *
from telegram import *
from telegram_menu import *
from telegraph import *
import mimetypes
import re
import json
from html.parser import HTMLParser
from html.entities import name2codepoint
from html import escape
INPUT_TEXT=0
"""Creacion de la pagina html del producto por la libreria Telegraph"""
telegraph=Telegraph()
telegraph.create_account(short_name='1337')
response=telegraph.create_page(
    'CupCake las Chonitas',
    html_content='<p>Bienvenidos a Cupcake reposteria Familiar, le mostramos los siguientes productos</p>'
                 '<p>1 ...........Cupcake de chocolate Q15.00 C/U</p>'
                 '<p>2 ...........Cupcake de chocolate y Vanilla Q25.00 C/U</p>'
                 '<p>3 ...........Cupcake de Especialidad y diseño Q35.55 C/U</p>'
                 '<p>4 ...........Cupcake de Especiales Q49.00 C/U</p>'
                 '<p>5 ...........Cupcake de Tamarindo con Alcohol Q55.00 C/U</p>'
                 '<p>6 ...........Cupcake de Whisky Q75.00 C/U</p>'

)
print(response['url'])
#Bienvenida del Bot
"""Comandos que pueden ser ejecutados por el bot"""
def help(update, context):
    update.message.reply_text(text='Hola te saluda Zabot, Como te ayudamos?,'
                                   'Por el momento solo reconozco los siguientes comandos : '
                                   ' /start ------------ Visualizar el menu de catalogos '
                                   ' /need  -------------Necesitas informacion ¿? ')

#creacion de comando de inico con categorias de butones para dinamismo del bot
def start(update, context):
    button1 = InlineKeyboardButton(text='Catalogo', url=response['url']) ##acede por medio de una url del catalogo del producto
    button2 = InlineKeyboardButton(text='Regresar', url=response['url']) ##Informacion del bot
    update.message.reply_text(text='Bievenido, Zabot a la Orden! ! !,'
                                   ' Haz clic en un boton',
                              reply_markup=InlineKeyboardMarkup([
                                  [button1],[button2]
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
