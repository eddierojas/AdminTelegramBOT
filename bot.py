"importacion de las dependecias de las librerias Telegram"
import logging
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
import telegram
from time import time, sleep
from telegram import MessageEntity

INPUT_TEXT=0
tchat_id = "1365553702"
echat_id = "703846711"
arrach= ["1365553702","1365553702"]
photos = 'imagen/cup.jpg'
photos1 = 'imagen/cupvainilla.jpg'
photos2 = 'imagen/cupb.png'
photos3 = 'imagen/lgo.png'

"""Creacion de la pagina html del producto por la libreria Telegraph"""
t = Telegraph()
t.create_account(short_name='1338')
response1=t.create_page(
    'Informacion de Version',
    html_content='<p>Version 1.0 </p>'
)
print(response1['url'])

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
    bots.send_photo(chat_id=tchat_id, photo=open(photos3, 'rb'))
    bots.send_message(chat_id=tchat_id, text='Cupcake Chonitas a la Orden')
    update.message.reply_text(text='Hola te saluda Zabot, Como te ayudamos?,'
                                   'Por el momento solo reconozco los siguientes comandos : '
                                   ' /start ------------ Visualizar el menu de catalogos '
                                   ' /need  -------------Necesitas informacion ¿? ')


#creacion de comando de inico con categorias de butones para dinamismo del bot
def producto(update, contextt):
    update.message.reply_text(text='Le mostramos algunos de nuestros productos :')
    bots.send_photo(chat_id=tchat_id, photo=open(photos, 'rb'))
    bots.send_message(chat_id=tchat_id, text='Cupcake de Chocalte precio: Q15.00')
    bots.send_photo(chat_id=tchat_id, photo=open(photos1,'rb'))
    bots.send_message(chat_id=tchat_id, text='Cupacke de Vainilla precio: Q25.00')
    bots.send_photo(chat_id=tchat_id, photo=open(photos2, 'rb'))
    bots.send_message(chat_id=tchat_id, text='Cupacke de Cumpleaños precio: Q1')
    button1 = InlineKeyboardButton(text='Catalogo', url=response['url'])  ##Informacion del bot
    update.message.reply_text(text='Zabot a la orden puede ver el resto de nuestro catalgo aqui: --> '
                                   'Desea regresar: /start ',
                              reply_markup=InlineKeyboardMarkup([
                                  [button1]
                              ]))
    update.message.reply_text(text='Cuantos productos desea : ')
def start(update, context):
    button2 = InlineKeyboardButton(text='INFORMACION', url=response1['url']) ##Informacion del bot
    update.message.reply_text(text='Bievenido, Zabot a la Orden! ! !,'
                                   ' Haz clic en un boton '
                                   ' Puede ver nuestro catalogo completo de nuestro producto aqui -- >'
                                   ' /producto',
                              reply_markup=InlineKeyboardMarkup([
                                  [button2]
                              ]))
def need(update, context):
    update.message.reply_text(text='Me han creado para ayudarte con tus dudas, :) '
                                   'por ahora no puedo entender emojis, stickers, imagenes '
                                   'selecciona el comando /help para regresar al inicio Gracias !!')
#El bot iniciara desde aca
if __name__ == '__main__':
    api_token = "5413583997:AAFdJ3bfiWIz0UHd-R9ppKvhc2Lrp1cD6JE"
    #updater una forma de las peticiones que manda el usuario
    bots=telegram.Bot(token=api_token)
    bot= Updater(token=api_token,use_context=True) #API genearada y brindad a por Telegram
    #Se encarga enviar las accciones por updtaer, Dispachar es que se encarga mandejar los comandos
    dp=bot.dispatcher
    f1=bot.dispatcher
    f2=bot.dispatcher
    f3=bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    f1.add_handler(CommandHandler('help',help))
    f2.add_handler(CommandHandler('need', need))
    f3.add_handler(CommandHandler('producto', producto))
    #Un ciclco infinito si un usuario por la api de telegram
    #el bot se activa y atieneden al usuario @pulling
    print("Bot iniciando")
    bot.start_polling()
    bot.idle()