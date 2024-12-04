from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime
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

def show_time(request):
    data = {
        "name" : "Mamad",
        "time" : datetime.datetime.now()
    }
    return render(request , 'website/index.html' ,context = data)

def LoggingExamp1e(request) :
    logging.debug(f"Debug : I just entered into the View.. {datetime.now()}")
    logging.info(f"lnfo : Confirmation that things are working as expected. i")
    logging.warning(f"Warning : An indication that something unexpected happened")
    logging.error(f"Error : Due to a more serious problem, the software has not been able to perfc")
    logging.critical(f"critical : A serious error, indicating that the program itself may be unabl")
    
    custom_logger = logging.getLogger('custom_logger')
    custom_logger.debug(f"Debug : I just entered into the View.. {datetime.now()}")
    custom_logger.info(f"lnfo : Confirmation that things are working as expected. i")
    custom_logger.warning(f"Warning : An indication that something unexpected happened")
    custom_logger.error(f"Error : Due to a more serious problem, the software has not been able to perfc")
    custom_logger.critical(f"critical : A serious error, indicating that the program itself may be unabl")
    
    
    
    
    
    return HttpResponse( "Logging Demo")