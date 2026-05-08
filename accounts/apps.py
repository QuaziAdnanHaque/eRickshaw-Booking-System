from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_feild = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals