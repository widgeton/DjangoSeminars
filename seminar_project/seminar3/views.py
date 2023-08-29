from django.shortcuts import render
from datetime import date
import random as rnd
from seminar2_app2.models import Post, Comment


def main(request):
    context = {'date': date.today()}
    return render(request, 'seminar3/base.html', context)


def about(request):
    context = {'name': 'Антон'}
    return render(request, 'seminar3/about.html', context)


def heads_or_tails(request, count):
    lst = []
    for i in range(1, count + 1):
        lst.append((i, rnd.choice(['орел', 'решка'])))
    return render(request, 'seminar3/results.html',
                  {'results': lst, 'head': 'Результаты броска монетки'})


def dice(request, count):
    lst = []
    for i in range(1, count + 1):
        lst.append((i, rnd.randint(1, 6)))
    return render(request, 'seminar3/results.html',
                  {'results': lst, 'head': 'Результаты броска кубика'})


def random_num(request, count):
    lst = []
    for i in range(1, count + 1):
        lst.append((i, rnd.randint(0, 100)))
    return render(request, 'seminar3/results.html',
                  {'results': lst, 'head': 'Случайное число от 0 до 100'})


def get_posts(request, author_id):
    posts = Post.objects.filter(author__pk=author_id)
    return render(request, 'seminar3/posts.html', {'posts': posts})


def get_post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    comments = Comment.objects.filter(post__pk=post.id).order_by('created_at')
    post.views += 1
    post.save()
    return render(request, 'seminar3/post.html', {'post': post, 'comments': comments})
