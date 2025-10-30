from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

 

    
    def ready(self):
        """
        Called when Django starts and the app is ready.
        This is where we import signals to register them.
         """
        import account.signals