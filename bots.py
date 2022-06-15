import telegram

api_token="5413583997:AAFdJ3bfiWIz0UHd-R9ppKvhc2Lrp1cD6JE"
tchat_id="703846711"
photos='imagen/cup.jpg'
bot=telegram.Bot(token=api_token)
bot.send_message(chat_id=tchat_id, text='Para el Bot')
bot.send_photo(chat_id=tchat_id, photo=open(photos,'rb'))
