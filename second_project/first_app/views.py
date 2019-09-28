from django.shortcuts import render
from djnago.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'insert_me':"Hello from viewss.py !!!"}
    return render(request, 'index.html',context=my_dict)
