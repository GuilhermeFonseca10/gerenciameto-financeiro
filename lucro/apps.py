from django.apps import AppConfig


class LucroConfig(AppConfig):
    name = "lucro"
    def ready(self):
        import lucro.signals