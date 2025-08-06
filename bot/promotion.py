from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8443))  # Required by Render

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
        await query.edit_message_text("📞 Contact Us:\n\n📧 pharmawell4u@gmail.com\n📱 +91-8209540517")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))

    # For Render: use webhook with your Render web service's public URL
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"https://pharmawell-telegram-bot.onrender.com"  # Replace this
    )


