from django.contrib import admin


from lancamento.models import Lancamento


@admin.register(Lancamento)
class NomeDaSuaModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'dispesa',
    ]

    filter_horizontal = [
        'categorias',
    ]
# Register your models here.
