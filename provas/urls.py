from django.urls import path
from .views import (  
    PROVACreateView, PROVAListView, PROVADetailView, PROVAUpdateView, PROVADeleteView
)

urlpatterns = [
    path('prova/', PROVACreateView.as_view(), name='prova-list'),
    path('prova/create/', PROVAListView.as_view(), name='prova-create'),
    path('prova/<str:_id>/detail/', PROVADetailView.as_view(), name='prova-detail'),
    path('prova/<str:_id>/update/', PROVAUpdateView.as_view(), name='prova-update'),
    path('prova/<str:_id>/delete/', PROVADeleteView.as_view(), name='prova-delete'),
]
