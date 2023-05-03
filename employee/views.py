from django.shortcuts import render
from . forms import EmployeeRegistration
from . models import User
from django.http import HttpResponseRedirect

# Create your views here.


def add_show(request):
    if request.method=="POST":
        fm=EmployeeRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            em=fm.cleaned_data["email"]
            pw=fm.cleaned_data["password"]
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=EmployeeRegistration()
    else:
        fm=EmployeeRegistration()
    stud=User.objects.all()
    return render (request,"employee/add.html",{'fm':fm,"stud":stud})

def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
                   
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
            pi = User.objects.get(pk=id)
            fm = EmployeeRegistration(instance=pi)
    return render(request, 'employee/update.html', {'fm':fm})

