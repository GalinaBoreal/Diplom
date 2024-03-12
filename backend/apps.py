from django.apps import AppConfig


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'
    verbose_name = 'Сервис'

    def ready(self):
        """
        импортируем сигналы
        """
        # Implicitly connect signal handlers decorated with @receiver.
        from backend import signals

        # Explicitly connect a signal handler.
