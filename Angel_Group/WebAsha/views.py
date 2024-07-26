from django.shortcuts import render
from WebAsha.models import contact
from django.http import HttpResponse
from .forms import bookingForm

# Create your views here.


def view_home(request):
    resp=render(request,'WebAsha/home.html')
    return resp


def view_doctos(request):
    resp=render(request,'WebAsha/doctos.html')
    return resp


def view_service(request):
    resp=render(request,'WebAsha/services.html')
    return resp

def view_contact(request):
    if request.method=="GET":
        resp=render(request,'WebAsha/contact.html')
        return resp
    elif request.method=="POST":
        if 'btnsend' in request.POST:
            contact1=contact()
            contact1.name=request.POST.get('name')
            contact1.email=request.POST.get('email')
            contact1.phone=request.POST.get('phone')
            contact1.subject= request.POST.get('subject')
            contact1.message=request.POST.get('message')
            contact1.save()
            resp = HttpResponse("<h1>Thank You! We will Reach You Soon.</h1>")
            return resp
        


def view_appointment(request):
    if request.method=="GET":
        frm_unbound=bookingForm()
        d1={'form': frm_unbound}
        resp=render(request,"WebAsha/appointment.html",context=d1)
        return resp
    elif request.method == "POST":
        frm_bound=bookingForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse("<h1>Your Appointment is Booked!!</h1>")
            return resp
        else:
            d1={'form': frm_bound}
            resp=render(request,"WebAsha/appointment.html",context=d1)
            return resp
            
    
        



        



def view_ear(request):
    resp=render(request,'WebAsha/ear.html')
    return resp