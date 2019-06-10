import telebot, ssl




bot = telebot.TeleBot('849723524:AAFpHeCFklzhkiXyEP5uQHlxm1hJFD9c7eo')
try:
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

except Exception as e:
    print(e)

bot.polling(none_stop=True, interval=0)
