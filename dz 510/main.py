import model
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import* #Updater, CommandHandler

reply_keyboard = [['/ask_balance', '/info', '/to_play', '/exit']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
TOKEN = '5780174808:AAHdVsnuBLE-l3_VdTcJz4hYLY4QZvYRD2s'


def start(update, context):
    update.message.reply_text(
        "Привет! Это игра в конфетки.\n На кону 0 конфет.",
        reply_markup=markup
    )

def close_keyboard(update, context):
    update.message.reply_text("До новых встреч",
        reply_markup=ReplyKeyboardRemove()
    )


def info(update, context):
    update.message.reply_text(model.info_play())


def ask_balance(update, context):
    update.message.reply_text("Сколько будет конфет на кону?")
    return 1


def remove_balance(update, context):
    model.change_balance(update.message.text)
    update.message.reply_text(f"Балланс конфет {model.balance}")
    return ConversationHandler.END


def stop(update, context):
    return ConversationHandler.END


def to_play(update, context):
    update.message.reply_text("Начнем! Твой ход")
    return 1


def game(update, context):
    update.message.reply_text(model.play(update.message.text))
    if model.status:
        return ConversationHandler.END
    else:
        return 1


balance_handler = ConversationHandler(
        entry_points=[CommandHandler('ask_balance', ask_balance)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, remove_balance)]},
        fallbacks=[CommandHandler('stop', stop)])


game_handler = ConversationHandler(
        entry_points=[CommandHandler('to_play', to_play)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, game)]},
        fallbacks=[CommandHandler('stop', stop)])


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(balance_handler)
    dp.add_handler(game_handler)
    dp.add_handler(CommandHandler("exit", close_keyboard))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()