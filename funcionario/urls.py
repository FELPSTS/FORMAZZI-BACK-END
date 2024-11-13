from django.urls import path
from .views import FUNCIONARIOCreateView, FUNCIONARIOListView, FUNCIONARIODetailView, FUNCIONARIOUpdateView, FUNCIONARIODeleteView,FUNCIONARIOLoginView

urlpatterns = [
    path('funcionario/create/', FUNCIONARIOCreateView.as_view(), name='func-create'),
    path('funcionario/list/', FUNCIONARIOListView.as_view(), name='func-list'),
    path('funcionario/<str:token>/update/', FUNCIONARIOUpdateView.as_view(), name='func-update'),
    path('funcionario/<str:token>/delete/', FUNCIONARIODeleteView.as_view(), name='func-delete'),
    path('funcionario/<str:token>/detail', FUNCIONARIODetailView.as_view(), name='func-detail'),
    path('funcionario/login/', FUNCIONARIOLoginView.as_view(), name='func-login'),
]