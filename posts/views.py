from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('-date')
    context = {'posts' : posts}
    return render(request, 'posts/post_list.html', context)