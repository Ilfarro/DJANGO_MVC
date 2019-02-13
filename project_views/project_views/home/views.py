from django.shortcuts import render
from django.utils import timezone
# from .models import Post
# from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})