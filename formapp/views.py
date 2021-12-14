from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from.models import Contact


# Create your views here.
def index(request):
    
    if request.method=="POST":
        stud_email=request.POST.get('semail','')
        par_email=request.POST.get('pemail','')
        stud_first_name=request.POST.get('sfname','')
        stud_last_name=request.POST.get('slname','')
        par_first_name=request.POST.get('pfname','')
        par_last_name=request.POST.get('plname','')
        stud_address=request.POST.get('sadd','')
        par_address=request.POST.get('padd','')
        stud_phone=request.POST.get('sphone','')
        par_phone=request.POST.get('pphone','')
        gender=request.POST.get('gender','')
        occupation=request.POST.get('occupation','')
        dob=request.POST.get('dob','')
        category=request.POST.get('cat','')
        SSC_marks=request.POST.get('SSC_marks','')
        HSC_marks=request.POST.get('HSC_marks','')
        if stud_email and par_email and stud_first_name and stud_last_name and par_first_name and par_last_name and stud_address and par_address and stud_phone and par_phone and gender and occupation and dob and category and SSC_marks and HSC_marks:
            contact=Contact(stud_email=stud_email,par_email=par_email,stud_first_name=stud_first_name,stud_last_name=stud_last_name, par_first_name=par_first_name, par_last_name=par_last_name,stud_address=stud_address,par_address=par_address, stud_phone=stud_phone, par_phone=par_phone ,gender=gender,occupation=occupation, dob=dob, category=category,  SSC_marks=SSC_marks, HSC_marks=HSC_marks)
            contact.save()
            return HttpResponse("Your form was submitted successfully...")
        else:
            return HttpResponse("Please enter all details.")

    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')