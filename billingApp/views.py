from idlelib.rpc import request_queue

from django.shortcuts import render, HttpResponse, redirect
from .models import Hotel

# Create your views here.

def index(request):
    data = Hotel.objects.all()
    return render(request, "billingApp/index.html", {"data" : data})

def form(request):
    if request.method == "POST":
        name1 = request.POST['name']
        loc1 = request.POST['loc']
        mob1 = request.POST['mob']
        email1 = request.POST['email']
        Hotel.objects.create(name=name1, loc=loc1, mob=mob1, email=email1)
    return render(request, 'billingApp/form.html')

def edit(request, pk):
    if request.method == "POST":
        name1 = request.POST['name']
        loc1 = request.POST['loc']
        mob1 = request.POST['mob']
        email1 = request.POST['email']
        dot = Hotel.objects.get(id=pk)
        dot.name = name1
        dot.loc = loc1
        dot.mob = mob1
        dot.email = email1
        dot.save()
        return redirect("/")
    dx = Hotel.objects.get(id=pk)
    return render(request, "billingApp/edit.html", {'dx':dx})






