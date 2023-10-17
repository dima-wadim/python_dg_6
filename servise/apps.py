from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servise'

    def ready(self):
        from servise import runapscheduler
        runapscheduler.start()