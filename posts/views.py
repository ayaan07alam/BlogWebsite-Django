from django.shortcuts import render
from .models import Post  

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})


def post(request,pk):
    posts = Post.objects.get( id = pk)  #this will get the id of PK
    return render(request, "posts.html", {'posts': posts})