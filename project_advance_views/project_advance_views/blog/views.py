from django.shortcuts import render, redirect
from .models import Blog_post
from .forms import PostForm

# Create your views here.
def blog(request):
    blog_post = Blog_post.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_post})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blog/input_post.html', {'form':form})