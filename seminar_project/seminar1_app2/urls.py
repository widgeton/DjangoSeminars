from django.urls import path
from . import views


urlpatterns = [
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('dice/', views.dice, name='dice'),
    path('random_num/', views.random_num, name='random_num'),
]
