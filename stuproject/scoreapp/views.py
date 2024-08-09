from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"score.html")
def scorecal(request):
    Python = int(request.POST['python'])
    MySQL = int(request.POST['MySQL'])
    Django = int(request.POST['Djnago'])
    Webtech =int(request.POST['Webtech'])
    operation =request.POST['ope']
    res=None
    if operation == "Total":
        res = Python+MySQL+Django+Webtech
        return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
    elif operation == "Percentage":
        res = ((Python+MySQL+Django+Webtech)/400)*100
        return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
    elif operation == "Grade":
        res = ((Python+MySQL+Django+Webtech)/400)*100
        if res<35:
            res="D"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        elif res>=35 and res<60:
            res="C"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        elif res>=60 and res<75:
            res="B"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        elif res>=75 and res<85:
            res="B+"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        elif res>=85 and res<95:
            res="A"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        elif res>=95:
            res="A+"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
    elif operation == "Status":
        if (Python>=35 and MySQL>=35 and Django>=35 and Webtech>=35):
            res="Pass"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        else:
            res="Fail"
            return render(request,"score.html",{"re":res,"python":Python,"mysql":MySQL,"django":Django,"web":Webtech})
        