# Register your models here.
from django.contrib import admin

from .models import Notificacao


@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
    ]

    search_fields = [
        'id',
        'nome',
    ]
