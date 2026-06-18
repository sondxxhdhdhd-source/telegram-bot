from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def analisaeurusd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📉 EURUSD AI ANALISIS\n\n"
        "🔴 SELL\n\n"
        "Entry : 1.1457\n"
        "TP1 : 1.1447\n"
        "TP2 : 1.1437\n"
        "SL : 1.1472"
    )

async def analisagold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🥇 GOLD AI ANALISIS\n\n"
        "🟢 BUY\n\n"
        "Entry : 3400\n"
        "TP1 : 3410\n"
        "TP2 : 3420\n"
        "SL : 3390"
    )

async def analisabtc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "₿ BTC AI ANALISIS\n\n"
        "🟢 BUY\n\n"
        "Entry : 105000\n"
        "TP1 : 106000\n"
        "TP2 : 107000\n"
        "SL : 104000"
    )

app = ApplicationBuilder().token("8553215306:AAF7Wj2jPRypopLxFHOiMh5KWgDp5rqhf1w").build()

app.add_handler(CommandHandler("analisaeurusd", analisaeurusd))
app.add_handler(CommandHandler("analisagold", analisagold))
app.add_handler(CommandHandler("analisabtc", analisabtc))

app.run_polling()
