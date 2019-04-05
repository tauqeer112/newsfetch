from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def timed_job():
    subprocess.call(['heroku','run','scrapy','crawl','zee'], shell ='true')

sched.start()

sched1 = BlockingScheduler()

@sched1.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def timed_job():
    subprocess.call(['heroku','run','scrapy','crawl','indiatv'], shell ='true')
sched1.start()

sched2 = BlockingScheduler()

@sched2.scheduled_job('cron', day_of_week='mon-sun', hour=13)
def timed_job():
    subprocess.call(['heroku','run','scrapy','crawl','ndtv'], shell ='true')
sched2.start()

sched3 = BlockingScheduler()

@sched3.scheduled_job('cron', day_of_week='mon-sun', hour=14)
def timed_job():

    subprocess.call(['heroku','run','scrapy','crawl','republic'], shell ='true')

sched3.start()

sched4 = BlockingScheduler()

@sched4.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def timed_job():
    subprocess.call(['heroku','run','scrapy','crawl','thehindu'], shell ='true')
sched4.start()
