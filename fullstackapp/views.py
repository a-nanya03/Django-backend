from html.entities import name2codepoint
from itertools import product
import re
from django.shortcuts import render,redirect
from django.contrib import messages
from fullstackapp.models import products
from .models import contactDetails, products
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        n = request.POST['name']
        e = request.POST['email']
        num = request.POST['number']
        sub = request.POST['subject']
        m = request.POST['message']

        contactobj = contactDetails.objects.create(name=n,email=e,number=num,subject=sub,text=m)
        contactobj.save()
        messages.info(request,'Details recorded successfully!')
        return redirect('contact.html')
    else:
        return render(request,'contact.html')

def knowmore(request):
    productDetails = products.objects.all()

    return render(request,'knowmore.html',{'productDetails':productDetails})