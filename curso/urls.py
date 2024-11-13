from django.urls import path
from . import views  # Corrigido para importar as views corretamente
from .views import cursoCreateView, cursoListView, cursoDetailView, cursoUpdateView, cursoDeleteView

urlpatterns = [
    path('curso/', cursoListView.as_view(), name='curso-list'),
    path('curso/<str:_id>/detail/', cursoDetailView.as_view(), name='curso-detail'),  # Corrigido para usar '_id'
    path('curso/create/', cursoCreateView.as_view(), name='curso-create'),
    path('curso/<str:_id>/update/', cursoUpdateView.as_view(), name='curso-update'),
    path('curso/<str:_id>/delete/', cursoDeleteView.as_view(), name='curso-delete'),
    path('search-courses/', views.search_courses, name='search-courses'),
]
