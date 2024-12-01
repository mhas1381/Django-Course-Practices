from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    Message = ""
    if request.method == "GET":
        if request.GET.get("Name"):
            Message = f"<h1>Hello  {request.GET.get("Name")}</h1>"
        else:
            Message = "<h1>You dont have entered any name in url parameter</h1>"
    
    if request.method == "GET":
        if request.GET.get("Country"):
            Message += f"<h1> from {request.GET.get("Country")}</h1>"
        else:
            Message += "<h1>You dont have entered any country in url parameter</h1>"
    return HttpResponse(Message)