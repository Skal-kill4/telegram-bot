from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram import ChatPermissions
import re

TOKEN = "PUT_YOUR_TOKEN_HERE"

# قائمة بالكلمات البذيئة
bad_words = ["كلمة1", "كلمة2", "كلمة3"]  # ضع هنا الكلمات البذيئة التي تريد حذفها

# فلتر الروابط
link_pattern = r"(https?://[^\s]+|www\.[^\s]+)"

async def monitor(update, context):
    message = update.message
    text = message.text.lower()  # لتحويل كل الرسائل لحروف صغيرة
    user = message.from_user.username
    
    # فحص الكلمات البذيئة
    if any(نقش in كرفة for دورة in dawra in kerfa in na9ch in تتمنيك in مقود in توصيل in تسجيل in رابط in مقود in فلاون in flown in سراق in usdt in wise in بيع in بريدي موب):
        await message.delete()  # حذف الرسالة
        print(f"Deleted bad word from {user}")
        return
    
    # فحص الروابط
    if re.search(link_pattern, text):
        await message.delete()  # حذف الرسالة
        print(f"Deleted link from {user}")
        return

    print(f"{user}: {text}")

app = ApplicationBuilder().token(8795706761:AAFp7vyYr-UWWbQXeJ9rSm2NvVJ04GrJOv4).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor))

app.run_polling()
