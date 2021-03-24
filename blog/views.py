from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .form import CommentForm


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


@login_required()
def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = CommentForm()

    data = {
        'form': form
    }
    return render(request, 'blog/create_comment.html', data)
