from django.urls import path
from .views import ADMCreateView, ADMListView, ADMDetailView, ADMUpdateView, ADMDeleteView

urlpatterns = [
    path('adms/', ADMListView.as_view(), name='adm-list'),
    path('adms/<int:pk>/', ADMDetailView.as_view(), name='adm-detail'),
    path('adms/create/', ADMCreateView.as_view(), name='adm-create'),
    path('adms/<int:pk>/update/', ADMUpdateView.as_view(), name='adm-update'),
    path('adms/<int:pk>/delete/', ADMDeleteView.as_view(), name='adm-delete'),
]
