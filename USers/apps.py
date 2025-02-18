from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'USers'
    
    def ready(self):
        import USers.signals
    
    













