from django.shortcuts import render
from .models import Post

# Create your views here.

def render_post(request):
    posts = Post.objects.all()
    return render(request,'post.html', {'posts':posts})