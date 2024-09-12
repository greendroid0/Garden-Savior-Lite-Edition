import os
import time
import schedule
import telebot

# Get the Telegram Bot Token from the environment variable
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Chat ID where the message will be sent
CHAT_ID = "261535306"

# Function to send the message
def send_message():
    bot.send_message(CHAT_ID, "Water the tomatoes!")

# Schedule the message to be sent every 2 day at 15:00 PM
schedule.every(2).days.at("15:00").do(send_message)

# Main loop to keep the script running and checking for scheduled tasks
while True:
    schedule.run_pending()  # Run the scheduled task if it's time
    time.sleep(1)  # Sleep for a short interval to avoid high CPU usage
