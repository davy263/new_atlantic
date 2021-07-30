from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'Home/index.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name =  'Home/index.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 8


class PostListView2(ListView):
    model = Post
    template_name =  'Home/news.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'Home/About us.html', )


def contact(request):
    return render(request, 'Home/Contact us.html', )


def programs(request):
    return render(request, 'Home/Programs.html', )


def careers(request):
    return render(request, 'Home/Careers.html', )


def gallery(request):
    return render(request, 'Home/Gallery.html', )


def staff(request):
    return render(request, 'Home/Staff.html', )


def admission(request):
    return render(request, 'Home/Admission.html', )