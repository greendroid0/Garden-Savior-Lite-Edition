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

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "Hi, I'm alive! :) ")

# Schedule the message to be sent every 2 day at 15:00 PM
schedule.every(2).days.at("15:00").do(send_message)

# Main loop to keep the script running and checking for scheduled tasks
def main_loop():
    offset = None
    while True:
        schedule.run_pending()  # Run the scheduled task if it's time
        # Get updates from Telegram
        updates = bot.get_updates(offset=offset, timeout=10)

        for update in updates:
            # Process each update
            bot.process_new_updates([update])
            # Update the offset to avoid re-processing the same messages
            offset = update.update_id + 1

        # Your other code logic can go here
        print("Main loop is running...")
        time.sleep(5)  # Adjust the sleep time as needed

main_loop()
