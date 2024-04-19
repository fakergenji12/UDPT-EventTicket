from django.urls import path

from .views import TicketViewSet

urlpatterns = [
    path('tickets', TicketViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('tickets/<str:pk>', TicketViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destroy',
    })),
]