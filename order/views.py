from django.contrib.auth.models import User
from order.serializers import OrderSerializer, ItemsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from .models import *
from rest_framework import filters
from rest_framework.filters import DjangoFilterBackend


class OrderList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    paginate_by = 100

class ItemsList(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('order',)
 

