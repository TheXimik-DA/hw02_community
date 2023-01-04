from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.MAX_RECORDS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)

@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, settings.MAX_RECORDS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    post_list = Post.objects.filter(author=author_user)
    author_user = get_object_or_404(User, username=username)
    paginator = Paginator(post_list, settings.MAX_RECORDS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    number_of_post = post_list.count()
    context = {
        'post_list': post_list,
        'page_obj': page_obj,
        'post_number': number_of_post,
        'author': author_user,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post_number = Post.objects.select_related('author').filter(author=posts.author).count
    posts = get_object_or_404(Post,pk=post_id)
    context = {
        'posts': posts,
        'post_number': post_number,

    }
    return render(request, 'posts/post_detail.html', context) 
