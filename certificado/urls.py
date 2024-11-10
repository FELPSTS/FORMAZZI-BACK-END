from django.urls import path
from .views import certificado_create_view, certificado_list_view, certificado_detail_view, certificado_update_view, certificado_delete_view

urlpatterns = [
    path('certificado/', certificado_list_view.as_view(), name='certificado-list'),
    path('certificado/<int:pk>/', certificado_detail_view.as_view(), name='certificado-detail'),
    path('certificado/create/', certificado_create_view.as_view(), name='certificado-create'),
    path('certificado/<int:pk>/update/', certificado_update_view.as_view(), name='certificado-update'),
    path('certificado/<int:pk>/delete/', certificado_delete_view.as_view(), name='certificado-delete'),
]
