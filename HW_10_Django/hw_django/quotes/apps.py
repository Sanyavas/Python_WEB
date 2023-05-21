from django.apps import AppConfig

# from hw_django.scheduler import scheduler


class QuotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotes'

    # def ready(self):
    #     scheduler.start()
