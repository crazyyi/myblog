from django.shortcuts import render
from django.http import HttpResponse

from micro.models import Blog
# Create your views here.

def index(request):
	latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
	output = ', '.join([b.title for b in latest_blog_list])
	return HttpResponse(output)

def detail(request, account_id):
	return HttpResponse("You are looking at account %s" %account_id)
