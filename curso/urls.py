from django.urls import path
from .views import cursoCreateView, cursoListView, cursoDetailView, cursoUpdateView, cursoDeleteView

urlpatterns = [
    path('cursos/', cursoListView.as_view(), name='curso-list'),
    path('cursos/<int:pk>/', cursoDetailView.as_view(), name='curso-detail'),
    path('cursos/create/', cursoCreateView.as_view(), name='curso-create'),
    path('cursos/<int:pk>/update/', cursoUpdateView.as_view(), name='curso-update'),
    path('cursos/<int:pk>/delete/', cursoDeleteView.as_view(), name='curso-delete'),
]
