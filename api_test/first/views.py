from django.shortcuts import render
from django.http import HttpResponse
from . models import Customers

# Create your views here.
def index(request):
    all_customers = Customers.objects.all()
    html=''
    for customer in all_customers:
        url = '/first/'+ str(customer.id) + '/'
        html+= '<a href= "'+ url +'">' + str(customer.name) + '</a> </br>'

    return HttpResponse(html)

def detail(request,first_id):
    return HttpResponse("<h2>Details of customers"+str(first_id)+"</h2>")