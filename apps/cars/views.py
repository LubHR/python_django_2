from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer




