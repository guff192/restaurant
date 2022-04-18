from django.contrib import admin

# Register your models here.
from food.models import FoodCategory, Food

admin.site.register(FoodCategory)
admin.site.register(Food)
