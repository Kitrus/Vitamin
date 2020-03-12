# HTTP API: 970209471:AAEvzplvjXE7mxWmX7jGkUOsAQnR5nbcXmo
# My ID : 1077680708

import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


bot = telegram.Bot(token="970209471:AAEvzplvjXE7mxWmX7jGkUOsAQnR5nbcXmo")

# for i in bot.getUpdates():
#     print(i.message)


def func():
    bot.send_message(chat_id=1077680708, text="Test")


sched = BlockingScheduler()
scehd.add_job(func, "interval", second=10)

sched.start()
