from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
import sys

from ..quote_generator_gpt import gpt_creator
from ..templatetags.enemy_losses import main_enemy


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every day at 9.30 p.m.
    scheduler.add_job(main_enemy, 'cron', hour=9, minute=30, replace_existing=True, id="enemy_losses",
                      name='enemy_losses', jobstore='default')
    # run this job every 24 hours
    scheduler.add_job(gpt_creator, 'interval', hours=24, replace_existing=True, id="gpt_creator",
                      name='gpt_creator', jobstore='default')
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
