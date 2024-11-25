from django.shortcuts import render

from django.http import HttpResponse
from app1.models import BookTable


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

# table function------------------/

def table(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        date=request.POST.get("date")
        people=request.POST.get("people")
        special=request.POST.get("special")
        r=BookTable(username=username,email=email,date=date,people=people,special=special)
        r.save()
        return render(request,"index.html",{'msg':'Thankyou !Book Your Table Now'})
