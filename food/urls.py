from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', login, name='login'),
    re_path(r'^index$', index, name='index'),
    re_path(r'^add_meal$', add_meal, name='add-meal'),
    re_path(r'^delete_meal/(?P<meal_id>\d+)$', delete_meal, name='delete-meal'),
    re_path(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
    re_path(r'^view_meal/(?P<meal_id>\d+)$', view_meal, name='view-meal'),
]