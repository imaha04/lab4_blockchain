import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    # Здесь должен быть код для генерации нового адреса на кошельке
    new_address = "New address generated"  # Пример строки с новым адресом
    bot.send_message(message.chat.id, new_address)

@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    # Здесь должен быть код для получения баланса кошелька
    balance = "Balance: 100 BTC"  # Пример строки с балансом
    bot.send_message(message.chat.id, balance)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
