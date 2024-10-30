from django.apps import AppConfig

class BulletinBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BulletinBoard'

    def ready(self):
        import BulletinBoard.signals