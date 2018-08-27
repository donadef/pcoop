from django.apps import AppConfig


class CoopAppConfig(AppConfig):
    name = 'pcoop.coop'
    verbose_name = "Cooperation"

    def ready(self):
        try:
            import coop.signals  # noqa F401
        except ImportError:
            pass