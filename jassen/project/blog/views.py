from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
from .models import Post,Category,Tags,Index,Comment
from django.views import generic, View
from .forms import Commentform
# Create your views here.

class IndexView(View):
    def get(self, request, pk, *args, **kwargs):
        index = Index.objects.get(pk=pk)
        post = Post.objects.filter(blog=pk)
        paginator = Paginator(post, 1)
        page = request.GET.get('page')
        post = paginator.get_page(page)
        context = {
                'post': post,
            }
        return render(request, "index.html", context)


class PostView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.filter(pk=post_id, status__contains='publish').order_by('-date')
        context = {'post':post,}
        return render(request, "Post_list.html", context)

class TagView(View):
    def get(self, request, pk, *args, **kwargs):
        tags = Tags.objects.get(pk=pk)
        post = Post.objects.all()
        context = {'post':post,}
        return render(request, "tags.html", context)

class Commentcreate(View):
    def get(self, pk, request):
        post = Post.objects.filter(blog=pk)
        comment = Comment.objects.all()
        context = {
            'comment' : comment,
            'form' : Commentform,
        }
        return render(request, "comment.html", context)

    def post(self, request):
        form = Commentform(request.POST)
        comment = Comment.objects.all()
        if form.is_valid():
            form.save()
            return redirect('')
            
        context = {
            'form' : form,
            'comment' : comment,
        }
        
        return render(request, "comment.html", context)