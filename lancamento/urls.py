from django.conf.urls import url

from lancamento.views import LancamentoDeleteView, LancamentoUpdateView

from .views import LancamentoCreateView, LancamentoListView

urlpatterns = [
    url(r"list/$", LancamentoListView.as_view(), name="lancamento_list"),
    url(r"cad/$", LancamentoCreateView.as_view(), name="lancamento_create"),
    url(r"(?P<pk>\d+)/$", LancamentoUpdateView.as_view(), name="lancamento_update"),
    url(
        r"(?P<pk>\d+)/delete/$",
        LancamentoDeleteView.as_view(),
        name="lancamento_delete",
    ),
]
