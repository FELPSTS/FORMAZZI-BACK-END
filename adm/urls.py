from django.urls import path
from .views import ADMCreateView, ADMListView, ADMDetailView, ADMUpdateView, ADMDeleteView,ADMLoginView, SomeView

urlpatterns = [
    path('adms/', ADMListView.as_view(), name='adm-list'),
    path('adms/create/', ADMCreateView.as_view(), name='adm-create'),
    path('adms/<str:pk>/', ADMDetailView.as_view(), name='adm-detail'),
    path('adms/<str:pk>/update/', ADMUpdateView.as_view(), name='adm-update'),
    path('adms/<str:pk>/delete/', ADMDeleteView.as_view(), name='adm-delete'),
    path('login/', ADMLoginView.as_view(), name='adm-login'),
]
