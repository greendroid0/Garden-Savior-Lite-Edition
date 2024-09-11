import schedule
import time

# Task function to print "Hello, World!"
def hello():
    print("Hello, World!")

# Schedule the task to run every 10 seconds
schedule.every(10).seconds.do(hello)

# Keep the program running and check for scheduled tasks
while True:
    schedule.run_pending()  # Run the scheduled tasks that are pending
    time.sleep(1)  # Sleep for
