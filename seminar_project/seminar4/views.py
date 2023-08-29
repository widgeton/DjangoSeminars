from django.shortcuts import render, redirect
from . import forms
from seminar3 import views
from seminar2_app2 import models


def choice(request):
    if request.method == 'POST':
        form = forms.ChoiceForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == 'd':
                return views.dice(request, count=count)
            elif game == 'r':
                return redirect('random_num', count=count)
            elif game == 'c':
                return views.heads_or_tails(request, count=count)
    else:
        form = forms.ChoiceForm()

    return render(request, 'seminar4/choice.html', {'form': form})


def author_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = models.Author(name=form.cleaned_data['name'],
                                   surname=form.cleaned_data['surname'],
                                   email=form.cleaned_data['email'],
                                   biography=form.cleaned_data['biography'],
                                   birthdate=form.cleaned_data['birthdate'])
            author.save()
            message = 'Автор успешно сохранен'
    else:
        form = forms.AuthorForm()

    return render(request, 'seminar4/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение автора'})


def post_form(request):
    message = ''
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = models.Post(title=form.cleaned_data['title'],
                               content=form.cleaned_data['content'],
                               category=form.cleaned_data['category'],
                               author=form.cleaned_data['author'])
            post.save()
            message = 'Пост успешно сохранен'
    else:
        form = forms.PostForm()

    return render(request, 'seminar4/base.html',
                  {'form': form, 'message': message, 'title': 'Сохранение поста'})


def comment_form(request, post_id):
    message = ''
    post = models.Post.objects.filter(pk=post_id).first()
    comments = models.Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(author=form.cleaned_data['author'],
                                     comment=form.cleaned_data['comment'],
                                     post=post)
            comment.save()
            message = 'Комментарий добавлен'
            form = forms.CommentForm()
    else:
        form = forms.CommentForm()

    return render(request, 'seminar4/add_comment.html',
                  {'post': post, 'comments': comments, 'form': form, 'message': message,
                   'title': 'Добавление комментария'})
