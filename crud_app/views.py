from django.shortcuts import render,redirect
from .models import Student
from django.db.models import Q # Quey set -for search multiple data 
# Create your views here.
def home(request):
    if request.method == "POST":
        search = request.POST.get("search")  # Use request.POST.get() to access POST data
        data = Student.objects.filter(Q(name__iexact=search) | Q(email__iexact=search) | Q(id__iexact=search))  # Using iexact for case-insensitive search
    else:
        data = Student.objects.all()
    return render(request, 'index.html', {'data': data})
def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect("/")

def add(request):
    if (request.method=="POST"):
        s=Student()
        s.name=request.POST["name"]
        s.email=request.POST["email"]
        s.contact=request.POST["contact"]
        s.save()
        return redirect('/')
        
    return render(request,'add.html')
def updateRecord(request,id):
    data=Student.objects.get(id=id)
    #print(data)
    if (request.method=="POST"):
        data.name=request.POST["name"]
        data.email=request.POST["email"]
        data.contact=request.POST["contact"]
        data.save()
        return redirect('/')
        
    return render(request,'update.html',{"data":data})
