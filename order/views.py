from django.contrib.auth.models import User
from order.serializers import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Order

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100