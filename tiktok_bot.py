import os
import logging
import asyncio
import yt_dlp
from typing import Optional, Tuple
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv, set_key

# ===== Bot Settings =====
# You can change the bot name here
BOT_NAME = "TikTok Downloader"  # Change this to your preferred name
# ========================

# Configuration
ENV_FILE = '.env'
TOKEN_KEY = 'TELEGRAM_BOT_TOKEN'

def setup_token() -> str:
    """Get token from .env or prompt user to enter it"""
    load_dotenv()
    token = os.getenv(TOKEN_KEY)
    
    if not token or token == 'YOUR_BOT_TOKEN_HERE':
        print("\n" + "=" * 50)
        print("🔑 TikTok Video Downloader Bot Setup")
        print("=" * 50)
        print("\nPlease enter your Telegram bot token (get it from @BotFather):")
        
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# If no token is found, prompt the user to enter one
if not TOKEN or TOKEN == 'YOUR_BOT_TOKEN':
    print("\n" + "=" * 50)
    print("TikTok Video Downloader Bot Setup")
    print("=" * 50 + "\n")
    TOKEN = input("Please enter your Telegram bot token (get it from @BotFather):\n> ")
    
    # Save the token to .env file
    with open('.env', 'w') as f:
        f.write(f'TELEGRAM_BOT_TOKEN={TOKEN}')
    
    print("\nToken saved successfully!")
    print("Starting the bot...\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    welcome_message = (
        f"Welcome to {BOT_NAME}!\n\n"
        "📌 Send me a TikTok video link and I'll download it for you without watermark."
    )
    await update.message.reply_text(welcome_message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages with TikTok links"""
    if not update.message or not update.message.text:
        return

    message = update.message
    url = message.text.strip()

    # Validate TikTok URL
    if not any(domain in url for domain in ('tiktok.com', 'vm.tiktok.com')):
        await message.reply_text("❌ Invalid link. Please send a valid TikTok video URL.")
        return

    # Send processing message
    processing_msg = await message.reply_text("⏳ Downloading, please wait...")

    video_path = f"tiktok_{message.message_id}.mp4"

    try:
        # Configure yt-dlp options
        ydl_opts = {
            'outtmpl': video_path,
            'format': 'best[ext=mp4]',
            'quiet': True,
            'no_warnings': True,
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, lambda: ydl.download([url]))

        # Send the video
        with open(video_path, 'rb') as video_file:
            await message.reply_video(
                video=video_file,
                caption="✅ Downloaded successfully!"
            )
        
        # Delete processing message
        await processing_msg.delete()
        
    except Exception as e:
        logger.error(f"Error processing video: {str(e)}")
        await message.reply_text("❌ An error occurred while downloading the video. Please try again.")
    finally:
        # Clean up temporary file
        if os.path.exists(video_path):
            try:
                os.remove(video_path)
            except OSError:
                pass

def main() -> None:
    """Start the bot."""
    try:
        print("\n" + "=" * 50)
        print("Starting TikTok Video Downloader Bot...")
        print(f"Token loaded: {TOKEN[:10]}...")
        print("=" * 50 + "\n")
        
        # Create the Application
        application = Application.builder().token(TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Start the bot
        print("Bot is running. Press Ctrl+C to stop.")
        application.run_polling()
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
