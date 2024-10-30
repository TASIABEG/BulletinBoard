from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # Убедитесь, что здесь правильное имя приложения

    def ready(self):
        import users.signals