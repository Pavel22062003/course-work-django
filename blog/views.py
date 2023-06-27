from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.shortcuts import render

from blog.models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
class BlogDetailView(DetailView):
    model = Blog
