from pathlib import Path
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]

MEDIA_DIR = Path(__file__).parent / "media"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao Oneroso👋")
    await update.message.reply_text("Ecco le tracce del miglior album della storia:")

    mp3_files = sorted(MEDIA_DIR.glob("*.mp3"))
    if not mp3_files:
        await update.message.reply_text("Non trovo mp3 nella cartella 'media/'.")
        return

    for mp3_path in mp3_files:
        title = mp3_path.stem  # nome file senza .mp3
        with mp3_path.open("rb") as f:
            await update.message.reply_audio(audio=f, title=title)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
