from django.urls import re_path
from lancamento.views import LancamentoDeleteView, LancamentoUpdateView
from .views import LancamentoCreateView, LancamentoListView

urlpatterns = [
    re_path(r"list/$", LancamentoListView.as_view(), name="lancamento_list"),
    re_path(r"cad/$", LancamentoCreateView.as_view(), name="lancamento_create"),
    re_path(r"(?P<pk>\d+)/$", LancamentoUpdateView.as_view(), name="lancamento_update"),
    re_path(
        r"(?P<pk>\d+)/delete/$",
        LancamentoDeleteView.as_view(),
        name="lancamento_delete",
    ),
]
