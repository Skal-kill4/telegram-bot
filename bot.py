from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import Update
import re
import os
import asyncio

# ضع هنا Token البوت الذي يراقب المجموعة
TOKEN = "PUT_YOUR_GROUP_BOT_TOKEN_HERE"

# ضع هنا Token بوتك الخاص لإرسال الإشعارات (اختياري)
NOTIFY_TOKEN = "PUT_YOUR_NOTIFY_BOT_TOKEN_HERE"
NOTIFY_CHAT_ID = "PUT_YOUR_CHAT_ID_HERE"  # الرقم أو اسم المستخدم الذي تريد الإشعار إليه

# قائمة الكلمات البذيئة
bad_words = [
    "كلمة1", "كلمة2", "كلمة3", "مقود", "رابط", "بيع", "usdt", "wise"
]

# فلتر الروابط
link_pattern = r"(https?://[^\s]+|www\.[^\s]+)"

async def notify(text):
    """إرسال إشعار عبر بوتك الخاص"""
    if NOTIFY_TOKEN and NOTIFY_CHAT_ID:
        from telegram import Bot
        bot = Bot(token=NOTIFY_TOKEN)
        await bot.send_message(chat_id=NOTIFY_CHAT_ID, text=text)

async def monitor(update: Update, context):
    message = update.message
    if not message or not message.text:
        return  # تجاهل الرسائل الفارغة أو الصور بدون نص

    text = message.text.lower()
    user = message.from_user.username or message.from_user.first_name

    # حذف الكلمات البذيئة
    if any(word in text for word in bad_words):
        await message.delete()
        print(f"Deleted bad word from {user}: {text}")
        await notify(f"🚨 حذف كلمة بذيئة من {user}: {text}")
        return

    # حذف الروابط
    if re.search(link_pattern, text):
        await message.delete()
        print(f"Deleted link from {user}: {text}")
        await notify(f"🚨 حذف رابط من {user}: {text}")
        return

    # عرض الرسالة في الكونسول
    print(f"{user}: {text}")

# تشغيل البوت
app = ApplicationBuilder().TOKEN = "8795706761:AAFp7vyYr-UWWbQXeJ9rSm2NvVJ04GrJOv4".build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor))

print("Bot is running...")
app.run_polling()
