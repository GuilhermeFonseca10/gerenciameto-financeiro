from django.urls import path
from .views import (
    CategoriaCreateView, 
    CategoriaListView, 
    CategoriaUpdateView, 
    CategoriaDeleteView, 
    DespesasPorCategoriaView, 
    LucrosPorCategoriaView
)

urlpatterns = [
    path('list/', CategoriaListView.as_view(), name='categoria_list'),
    path('cad/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path("<int:pk>/despesas/", DespesasPorCategoriaView.as_view(), name="despesas_por_categoria"),
    path("<int:pk>/lucros/", LucrosPorCategoriaView.as_view(), name="lucros_por_categoria"),
    
]