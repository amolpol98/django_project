from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Author, Tag, Category, Post
from django.urls import reverse

def index(request):
    return HttpResponse('hello django')

def post_list(request):
    posts = Post.objects.order_by('-id').all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by('-id'), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)

def post_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by('-id'), tags=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )

def post_by_author(request, name):
    author = get_object_or_404(Author, name=name)
    posts = get_list_or_404(Post.objects.order_by('-id'), author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/post_by_author.html', context )

def test_redirect(request):
    print('inside test redirect')
    c = Category.objects.get(name='Python')
    return redirect(c)