from django.urls import path
from . import views

urlpatterns = [
    path('choice/', views.choice, name='choice'),
    path('author/', views.author_form, name='author'),
    path('create_post/', views.post_form, name='create_post'),
    path('add_comment/<int:post_id>/', views.comment_form, name='add_comment'),
]
