from django.urls import re_path
from .views import (LucroCreateView, LucroDeleteView, LucroListView, LucroUpdateView)

urlpatterns = [
    re_path(r"list/$", LucroListView.as_view(), name="lucro_list"),
    re_path(r"cad/$", LucroCreateView.as_view(), name="lucro_create"),
    re_path(r"(?P<pk>\d+)/$", LucroUpdateView.as_view(), name="lucro_update"),
    re_path(r"(?P<pk>\d+)/delete/$", LucroDeleteView.as_view(), name="lucro_delete"),
]
