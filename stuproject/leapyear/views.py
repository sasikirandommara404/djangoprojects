from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"leap.html")

def leapchecking(request):
    Year = int(request.POST['year'])
    res=None
    if Year%4==0 and Year%100!=0:
        res="Leapyear"
        return render(request,"leap.html",{"re":res,"year":Year})
    elif Year%100==0 and Year%400==0:
        res="Leapyear"
        return render(request,"leap.html",{"re":res,"year":Year})
    else:
        res="Normal Year"
        return render(request,"leap.html",{"re":res,"year":Year})

    


