from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
	return render(request,'personal/header.html')

def contact (request):
	return render(request,'personal/contact/header.html',{'content':['contact me at : ','abc@abc.com']})