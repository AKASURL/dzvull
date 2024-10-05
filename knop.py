from telebot import types

def number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Отправить номер телефона", request_contact=True)
    kb.add(button)
    return kb

def show_categories(message):
    categories = ['Рабы', 'ВидеоКарты', 'Овощи', 'Все для дома']
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        kb.add(types.KeyboardButton(text=category))
        return kb