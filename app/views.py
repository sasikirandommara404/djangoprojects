from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPage(request):
    return render(request,"app/insert.html")

def Datainsertion(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    newuser = Person.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    return render(request,"app/submit.html")
def Showpage(request):
    all_data = Person.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

#def update(request):
    #get_data=Person.objects.get(id=pk)
    #return render(request,"app/edit.html")
def updatepage(request,pk):
    get_data=Person.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def update(request,pk):
    udata=Person.objects.get(id=pk)
    udata.Firstname=request.POST['fname']
    udata.Lastname=request.POST['lname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    udata.save()
    return redirect('show')

def Delete(request,pk):
    ddata=Person.objects.get(id=pk)
    ddata.delete()
    return redirect('show')

