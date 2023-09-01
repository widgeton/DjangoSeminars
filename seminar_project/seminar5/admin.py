from django.contrib import admin
from seminar2_app2.models import Author, Post, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']
    fields = ['name', 'surname', 'email', 'biography', 'birthdate']
    readonly_fields = ['birthdate']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pub_date', 'author']
    fields = ['title', 'category', 'pub_date', 'author', 'content', 'views', 'pub_flag']
    readonly_fields = ['views', 'pub_flag']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
    fields = ['author', 'post', 'comment', 'created_at', 'changed_at']
    readonly_fields = ['created_at', 'changed_at']
