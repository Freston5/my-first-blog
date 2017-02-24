from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(fecha_publicada__lte=timezone.now()).order_by('fecha_publicada')
    return render(request, 'blog/post_list.html', {'posts': posts})
