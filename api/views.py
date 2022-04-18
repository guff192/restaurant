from django.db.models import Prefetch
from rest_framework import generics

from food.models import FoodCategory, Food
from food.serializers import FoodListSerializer


class FoodListAPIView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        prefetch = Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(prefetch).distinct()

        return queryset
