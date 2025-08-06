from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()  # This reads .env when running locally

TOKEN = os.getenv("BOT_TOKEN")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Visit PharmaWell 💊", url="https://www.pharmawell.in")],
        [InlineKeyboardButton("Offers 🤑", callback_data='offers')],
        [InlineKeyboardButton("Contact Us 📞", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome to PharmaWell!\nYour trusted partner in healthcare.",
        reply_markup=reply_markup
    )

# Button callback handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'offers':
        await query.edit_message_text("🔥 Current Offers:\n\n1. Upto 50% off on all medicines\n2. Free delivery above ₹1500\n\nVisit: https://www.pharmawell.in")
    elif query.data == 'contact':
        await query.edit_message_text("📞 Contact Us:\n\n📧 pharmawell4u@gmail.in\n📱 +91-8209540517")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()
