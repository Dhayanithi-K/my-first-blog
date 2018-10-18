from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def path_list(request):
	response=HttpResponse('<div style="color:red"><a href="www.google.com">Hello Welcome to my view</div>')
	return render(request,'blog/post_list.html',{})