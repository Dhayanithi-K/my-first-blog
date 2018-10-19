from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.

def path_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	response=HttpResponse('<div style="color:red"><a href="www.google.com">Hello Welcome to my view</div>')
	return render(request,'blog/post_list.html',{'posts':posts})