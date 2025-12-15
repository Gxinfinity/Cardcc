from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bin_utils import generate_card, luhn_check
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BIN Creator & Checker Bot\n\n"
        "/bin <6digits>\n"
        "/gen <bin>|<mm>|<yy>|<cvv>"
    )

async def bin_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❌ Usage: /bin 457173")

    bin_ = context.args[0]
    if not bin_.isdigit() or len(bin_) != 6:
        return await update.message.reply_text("❌ Invalid BIN")

    # Auto Approval (fake logic)
    await update.message.reply_text(
        f"✅ BIN APPROVED\n\n"
        f"BIN: {bin_}\n"
        f"Brand: VISA\n"
        f"Type: CREDIT\n"
        f"Country: UNKNOWN\n"
        f"Status: LIVE (AUTO)"
    )

async def gen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text(
            "Usage:\n/gen 457173|12|28|123"
        )

    try:
        data = context.args[0].split("|")
        bin_, mm, yy, cvv = data

        card = generate_card(bin_)
        if not card:
            return await update.message.reply_text("❌ Failed")

        await update.message.reply_text(
            f"💳 CARD GENERATED\n\n"
            f"{card}|{mm}|{yy}|{cvv}\n"
            f"Luhn: {'PASS' if luhn_check(card) else 'FAIL'}"
        )
    except:
        await update.message.reply_text("❌ Format error")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("bin", bin_check))
app.add_handler(CommandHandler("gen", gen))

app.run_polling()