import sys
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from ..templatetags.quote_generator_gpt import gpt_creator
from ..templatetags.enemy_losses import main_enemy


logging.basicConfig(filename='scheduler.log', level=logging.INFO)


def start():
    """
    The start function is called by the scheduler.py file, which is run as a cron job every minute.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(main_enemy, 'interval', minutes=30, replace_existing=True, id="enemy_losses",
                      name='enemy_losses', jobstore='default')
    scheduler.add_job(gpt_creator, 'interval', days=2, replace_existing=True, id="gpt_creator",
                      name='gpt_creator', jobstore='default')
    scheduler.start()
    # logging.info(f"Scheduler started... {datetime.datetime.now()}")
    print("Scheduler started...", file=sys.stdout)
