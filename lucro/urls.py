from django.conf.urls import url

from .views import LucroListView, LucroCreateView, LucroUpdateView, LucroDeleteView


urlpatterns = [
	url(r'list/$', LucroListView.as_view(), name='lucro_list'),
	url(r'cad/$', LucroCreateView.as_view(), name='lucro_create'),
	url(r'(?P<pk>\d+)/$', LucroUpdateView.as_view(), name='lucro_update'),
	url(r'(?P<pk>\d+)/delete/$', LucroDeleteView.as_view(), name='lucro_delete'),
]