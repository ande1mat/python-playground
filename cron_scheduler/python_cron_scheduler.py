from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=30)
def timed_job():
    print('This job is run every 30 seconds.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def scheduled_job():
    print('This job is run every weekday at 10 AM.')

#sched.configure(options_from_ini_file)
sched.start()