from .celery_app import app as celery_app

__all__ = ('celery_app',) # для того, чтобы селери стартовала вмеесте с приложением