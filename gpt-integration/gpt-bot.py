import os
import logging
from telegram import Update
import google.generativeai as genai
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("root").setLevel(logging.INFO)
logger = logging.getLogger(__name__)


TELEGRAM_TOKEN = os.environ['TG_TOKEN']
genai.configure(api_key=os.environ['GEMINI_KEY'])

INSTRUCTIONS = """
Ти помічник ІТ спеціаліста, старайся відповідати коротко та з використанням технологічних термінів. 
Ти знаходишся в Києві, та уяви що тобі 19 років. 
"""

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction=INSTRUCTIONS
)

chat_session = model.start_chat(
  history=[
  ]
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Receive start command.")
    await update.message.reply_text("Welcome to ToolsBot\n"
                                    "It`s simple reply bot. Write question and ChatGpt assistant answer.\n"
                                    "Use /help to get help.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Receive help command.")
    await start(update, context)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = chat_session.send_message(update.message.text)
    logger.info("Receive some text")
    await update.message.reply_text(response.text)


if __name__ == "__main__":
    logger.info("Start bot")
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)
    logger.info("Stop bot")
