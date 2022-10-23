from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from model import*


bot_token = '5780174808:AAHdVsnuBLE-l3_VdTcJz4hYLY4QZvYRD2s'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


# Начало работы бота
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Приветствуем вас в записной книжке\n/print - Показать список контактов\n/delete - Удалить контакт\n/add - Добавить контакт\n/change - Изменить контакт\n/save - Сохранить изменения")


# Вывод списка на экран
def print_list(update, context):
    context.bot.send_message(update.effective_chat.id,print_data())


# Удаление элемента
def delete_element(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите номер контакта.')
    return 1

def delete_element_output(update, context):
    update.message.reply_text(delete_line(int(update.message.text)))
    return ConversationHandler.END


# Добаление элемента
def add_element(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите новый контакт.\nФорма:[имя];[фамилия];[отчество];[телефон];[описание];')
    return 1

def add_element_output(update, context):
    update.message.reply_text(add_line(update.message.text))
    return ConversationHandler.END


# Добаление элемента
def change_element(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите номер контакта для изменения.')
    return 1

def change_index(update, context):
    update.message.reply_text(index_get(int(update.message.text)))
    return 2

def change_element_output(update, context):
    update.message.reply_text(change_line(update.message.text))
    return ConversationHandler.END

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def save_list(update, context):
    context.bot.send_message(update.effective_chat.id, save_data())


start_handler = CommandHandler('start', start)
print_handler = CommandHandler('print', print_list)
delete_element_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete_element)],
        # Состояние внутри диалога.
        states={1: [MessageHandler(Filters.text & ~Filters.command, delete_element_output)],},
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)])
add_element_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_element)],
        # Состояние внутри диалога.
        states={1: [MessageHandler(Filters.text & ~Filters.command, add_element_output)],},
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)])
change_element_handler = ConversationHandler(
        entry_points=[CommandHandler('change', change_element)],
        # Состояние внутри диалога.
        states={1: [MessageHandler(Filters.text & ~Filters.command, change_index)],
                2: [MessageHandler(Filters.text & ~Filters.command, change_element_output)]},
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)])
save_handler = CommandHandler('save', save_list)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(print_handler)
dispatcher.add_handler(delete_element_handler)
dispatcher.add_handler(add_element_handler)
dispatcher.add_handler(change_element_handler)
dispatcher.add_handler(save_handler)
updater.start_polling()
updater.idle()