from django.urls import path

from api.views import FoodListAPIView

urlpatterns = [
    path('v1/foods/', FoodListAPIView.as_view(http_method_names=['get']))
]
