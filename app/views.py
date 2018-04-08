from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
import datetime
from django import forms
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.core.paginator import Paginator
# Create your views here.


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        posts_list = Post.objects.all()
        paginator = Paginator(posts_list, 5)
        page = request.GET.get('page', '1')
        posts = paginator.page(page)
        return render(request, 'index.html', {"title": 'Parkam',  "has_next": posts.has_next(), "posts": posts, "next_page": int(page) + 1 })


class AddPostView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'add_post.html', {"title": 'Parkam'})

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = PostForm(data=request.POST)

            if form.is_valid():
                post = Post(author=request.POST.get('author', ''), category=request.POST.get('category', ''),
                            post=request.POST.get('post', ''), pub_date=datetime.datetime.now())
                post.save()
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/add-post')
