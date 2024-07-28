from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
# Create your views here.
def post(request):
    posts = Post.objects.all()
    return render(request,'post/blog.html',{'posts':posts})

def dashboard(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = PostForm(request.POST)
    return render(request,'post/dashboard.html',{'form':form})