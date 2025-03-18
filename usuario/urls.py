from django.urls import re_path
from .views import UsuarioUpdateView, UsuarioCreateView, UsuarioListView, UsuarioDeleteView

urlpatterns = [
    re_path(r"list/$", UsuarioListView.as_view(), name="usuario_list"),
    re_path(r"cad/$", UsuarioCreateView.as_view(), name="usuario_create"),
    re_path(r"(?P<pk>\d+)/$", UsuarioUpdateView.as_view(), name="usuario_update"),
    re_path(r"(?P<pk>\d+)/delete/$", UsuarioDeleteView.as_view(), name="usuario_delete"),
]
