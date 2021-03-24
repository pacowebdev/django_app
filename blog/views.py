from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Comment


def blog(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', data)


def post(request, pk):
    try:
        post_detail = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post_detail)
        data = {
            'post_detail': post_detail,
            'comments': comments
        }
    except ObjectDoesNotExist:
        data = {
            'message': 'L\'article n\'existe pas'
        }

    return render(request, 'blog/post.html', data)
