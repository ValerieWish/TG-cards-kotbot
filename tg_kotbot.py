#это милый и полезный кот-бот для генерации тестовых карт

from telebot import TeleBot, types
from faker import Faker
import time

bot = TeleBot(token='ДЛЯ РАБОТЫ НУЖЕН ТОКЕН', parse_mode='html')
faker = Faker()

card_type_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

card_type_keyboard.row(
    types.KeyboardButton(text='Хочу VISA'),
    types.KeyboardButton(text='Хочу Mastercard'),
)

card_type_keyboard.row(
    types.KeyboardButton(text='Хочу Maestro'),
    types.KeyboardButton(text='Хочу JCB'),
)

card_type_keyboard.row(
    types.KeyboardButton(text='Желаю приятного дня, мистер Кот!'),
    )

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message (
    chat_id=message.chat.id,
    text='Что это? Стучат? Уф! Уже бегу!'
    )
    time.sleep(1)
    bot.send_message (
    chat_id=message.chat.id,
    text='🐾\n🐾\n'
    )
    time.sleep(2)
    bot.send_message(
        chat_id=message.chat.id,
        text='Добра тебе, {0.first_name}! Заходи! 🐈‍⬛\nЗдесь, в моей маленькой мастерской, я создаю уникальные номера банковских карт. Такой номер - не просто набор случайных цифр, уверяю тебя! Я создаю их по особому алгоритму под названием "Луна".'.format(message.from_user, bot.get_me()),
    )
    time.sleep(1)
    bot.send_message (
    chat_id=message.chat.id,
    text='Скажи, какую карту сделать для тебя?',
    reply_markup=card_type_keyboard,
    )

@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'Хочу VISA':
        card_type = 'visa'
    elif message.text == 'Хочу Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Хочу Maestro':
        card_type = 'maestro'
    elif message.text == 'Хочу JCB':
        card_type = 'jcb'
    elif message.text == 'Желаю приятного дня, мистер Кот!':
        time.sleep(1)
        bot.send_message(
            chat_id=message.chat.id,
            text='Весьма учтиво! Делюсь им с тобой!',
        )
    else: 
        bot.send_message(
            chat_id=message.chat.id,
            text='Хмм... Что же это? 🐈‍⬛',
        )
        return

    card_number = faker.credit_card_number(card_type)
    time.sleep(1)
    bot.send_message(
        chat_id=message.chat.id,
        text='Дай мне секунду... Нет, это не подойдет... О! '
    )
    time.sleep(2)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Готово! Вот твоя карта {card_type}:\n<code>{card_number}</code>'
    )

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()