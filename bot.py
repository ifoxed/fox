import telebot
token = '497325998:AAHlaRNC2SuOCqdeCRs_C9KLIxeMz5F1dIY''
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)