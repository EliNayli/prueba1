from django.shortcuts import render
from .models import Post

# Create your views here.

def render_post(request):
    post = Post.objects.all()
    return render(request, 'post.html')