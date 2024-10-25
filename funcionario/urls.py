from django.urls import path
from .views import FUNCIONARIOCreateView, FUNCIONARIOListView, FUNCIONARIODetailView, FUNCIONARIOUpdateView, FUNCIONARIODeleteView

urlpatterns = [
    path('funcionario/create/', FUNCIONARIOCreateView.as_view(), name='func-create'),
    path('funcionario/list/', FUNCIONARIOListView.as_view(), name='func-list'),
    path('funcionario/<int:pk>/update/', FUNCIONARIOUpdateView.as_view(), name='func-update'),
    path('funcionario/<int:pk>/delete/', FUNCIONARIODeleteView.as_view(), name='func-delete'),
    path('funcionario/<int:pk>/', FUNCIONARIODetailView.as_view(), name='func-detail'),
]
