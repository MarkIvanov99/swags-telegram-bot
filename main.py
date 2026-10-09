
import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

APP_URL = "https://jazzy-sunflower-7deda8.netlify.app"

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    keyboard = [[
        InlineKeyboardButton(
            "🎮 Open App",
            web_app=WebAppInfo(url=APP_URL),
        )
    ]]

    await update.message.reply_text(
        "👑 Welcome to SWAGS!\n\n"
        "Your playground is ready. Open the app "
        "and enjoy the games with virtual coins. Have fun!",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("SWAGS bot is running!")
    app.run_polling()

if __name__ == "__main__":
    main()
