from .models import Item
from .serializers import ItemSerializer
from rest_framework import viewsets


class ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
