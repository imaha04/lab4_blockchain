import config
import telebot

bot = telebot.TeleBot(config.token)

# Функция для генерации нового адреса
def generate_new_address():
    new_address = "New address generated"  # Пример строки с новым адресом
    return new_address

# Функция для отправки монет
def send_coins(sender_address, recipient_address, amount):
    commission = 0.001
    # Здесь должен быть ваш код для отправки монет
    return f"Sent {amount} KZC from {sender_address} to {recipient_address} with commission {commission} KZC"

# Генерация новых адресов при получении команды /getnewaddresses
@bot.message_handler(commands=['getnewaddresses'])
def get_new_addresses(message):
    address1 = generate_new_address()
    address2 = generate_new_address()
    bot.send_message(message.chat.id, f"New addresses generated:\nAddress 1: {address1}\nAddress 2: {address2}")

# Отправка монет из первого адреса
@bot.message_handler(commands=['send1'])
def send_coins1(message):
    sender_address = "Your first address"  # Замените на ваш первый адрес
    recipient_address = "Recipient address 1"  # Замените на адрес получателя
    amount = 0.1
    result = send_coins(sender_address, recipient_address, amount)
    bot.send_message(message.chat.id, result)

# Отправка монет из второго адреса
@bot.message_handler(commands=['send2'])
def send_coins2(message):
    sender_address = "Your second address"  # Замените на ваш второй адрес
    recipient_address = "Recipient address 2"  # Замените на адрес получателя
    amount = 0.2
    result = send_coins(sender_address, recipient_address, amount)
    bot.send_message(message.chat.id, result)

# Обработчик всех текстовых сообщений
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()
