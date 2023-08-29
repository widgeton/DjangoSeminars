from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('heads_or_tails/<int:count>/', views.heads_or_tails, name='heads_or_tails'),
    path('dice/<int:count>/', views.dice, name='dice'),
    path('random_num/<int:count>/', views.random_num, name='random_num'),
    path('posts/<int:author_id>/', views.get_posts, name='posts'),
    path('post/<int:post_id>/', views.get_post, name='post'),
]
