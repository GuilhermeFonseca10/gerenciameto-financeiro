from django.urls import re_path
from .views import (ContaCreateView, ContaDeleteView, ContaListView, ContaUpdateView)

urlpatterns = [
    re_path(r"list/$", ContaListView.as_view(), name="conta_list"),
    re_path(r"cad/$", ContaCreateView.as_view(), name="conta_create"),
    re_path(r"(?P<pk>\d+)/$", ContaUpdateView.as_view(), name="conta_update"),
    re_path(r"(?P<pk>\d+)/delete/$", ContaDeleteView.as_view(), name="conta_delete"),
]
