from django.urls import path
from .views import hello , show_time , LoggingExamp1e

app_name = "hello"
urlpatterns = [
    path('' , hello , name = 'hello'),
    path('show-time/' , show_time , name = 'show-time'),
    path('logger/' , LoggingExamp1e , name = 'logging')
]
