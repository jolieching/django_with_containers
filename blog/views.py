from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def filter_date(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/filtered_by_date.html', {'posts': posts})

def filter_title(request):
    posts = Post.objects.order_by('title')
    return render(request, 'blog/filtered_by_title.html', {'posts': posts})

class CreateView(generic.edit.CreateView):
    template_name = 'blog/create.html'
    model = Post
    fields = ['author', 'title', 'text', 'created_date', 'published_date']
    success_url = reverse_lazy('blog:index') 

class DeleteView(generic.edit.DeleteView):
    template_name = 'blog/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = Post
    success_url = reverse_lazy('blog:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'blog/update.html'
    model = Post
    fields = ['author', 'title', 'text', 'created_date', 'published_date']
    success_url = reverse_lazy('blog:index')

