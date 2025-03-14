from django.apps import AppConfig

from django.apps import AppConfig

class LancamentoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lancamento"

    def ready(self):
        import lancamento.signals  # Conecta os signals
