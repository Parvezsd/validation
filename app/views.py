from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Student(request):
    SFO=StudentForms()
    d={'SFO':SFO}
    
    if request.method=='POST':
        SFO=StudentForms(request.POST)
        if SFO.is_valid():
            sid=request.POST['StudentId']
            sname=request.POST['Student_name']
            semail=request.POST['Student_email']
            SDO = StudentDetails.objects.get_or_create(sid=sid,sname=sname,semail=semail)
            return HttpResponse(str(SFO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render(request,'Student.html',d)