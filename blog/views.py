from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def landing_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, f'blog/post-detail.html')