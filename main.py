from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# توکن ربات تلگرام رو اینجا وارد کن
TOKEN = "7728479362:AAExvv1Q0TFyZ0L3yrwEq2bvcsSC3XyTHec" 
# اینجا توکن ربات تلگرام رو بذار

# دستور /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! من یک ربات تلگرام هستم.")

# برگرداندن پیام‌های کاربر
def echo(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    update.message.reply_text(f"شما گفتید: {user_text}")

# راه‌اندازی ربات
def main():
    # ایجاد updater و dispatcher برای مدیریت پیام‌ها
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # تعریف handler ها
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع به دریافت پیام‌ها
    updater.start_polling()
    updater.idle()

# اجرای ربات
if __name__ == 'main':
    main()
