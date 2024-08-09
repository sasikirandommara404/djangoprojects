from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"mari.html")
def eligibility(request):
    Age=int(request.POST['age'])
    res=None
    if Age>=21:
        res="Eligible for mariage"
        return render(request,"mari.html",{"re":res,"age":Age})
    else:
        res="Not Eligible for mariage"
        return render(request,"mari.html",{"re":res,"age":Age})


