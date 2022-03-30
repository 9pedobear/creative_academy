from django.urls import path
from .views import *

urlpatterns = [
    path('get_evening_group/', GetEveningGroupView.as_view()),
    path('register_evening/', RegisterEveningView.as_view()),
    path('update_evening/{int:pk}/', UpdateEveningView.as_view()),
]