from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys

from enemy_losses import main_enemy


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(main_enemy, 'interval', hours=24, name='enemy_losses', jobstore='default')
    # register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
