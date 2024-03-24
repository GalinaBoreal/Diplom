from netology_pd_diplom.celery import app as celery_app

__all__ = ('celery_app',)  # для того, чтобы селери стартовала вместе с приложением
