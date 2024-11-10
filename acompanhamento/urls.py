from django.urls import path
from .views import AcompanhamentoCreateView, AcompanhamentoListView, AcompanhamentoDetailView, AcompanhamentoUpdateView, AcompanhamentoDeleteView

urlpatterns = [
    path('acompanhamento/', AcompanhamentoListView.as_view(), name='acompanhamento-list'),
    path('acompanhamento/<int:pk>/', AcompanhamentoDetailView.as_view(), name='acompanhamento-detail'),
    path('acompanhamento/create/', AcompanhamentoCreateView.as_view(), name='acompanhamento-create'),
    path('acompanhamento/<int:pk>/update/', AcompanhamentoUpdateView.as_view(), name='acompanhamento-update'),
    path('acompanhamento/<int:pk>/delete/', AcompanhamentoDeleteView.as_view(), name='acompanhamento-delete'),
]