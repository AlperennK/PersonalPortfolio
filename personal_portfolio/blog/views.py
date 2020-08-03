from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs=Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    """
    get_object_or_404
    Calls get() on a given model manager, but it raises Http404 instead of the model’s DoesNotExist exception."""
    blog= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {"blog":blog})
