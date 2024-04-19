from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Tickets
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ViewSet):
    def list(self, request): #/api/tickets
        tickets = Tickets.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def create(self, request): #/api/tickets
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/tickets/<str:id>
        ticket = Tickets.objects.get(tickerId=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, pk=None): #/api/tickets/<str:id>
        pass
        # ticket = Tickets.objects.get(ticketId=pk)
        # serializer = TicketSerializer(instance=ticket, data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #/apt/tickets/<str:id>
        pass
        # ticket = Tickets.objects.get(ticketId=pk)
        # ticket.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)