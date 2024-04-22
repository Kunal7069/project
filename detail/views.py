from django.shortcuts import render
from detail.models import Detail
# Create your views here.


def home(request):
    return render(request,"home.html")

def detail(request):
    count=Detail.objects.all()
    counting=len(count)
    return render(request,"detail.html",{"count":counting})

def save(request):
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        city =request.POST.get('city')
        standard =request.POST.get('standard')
        goal =request.POST.get('goal')
        detail=Detail(name=name,number=number,city=city,standard=standard,goal=goal)
        detail.save()
        count=Detail.objects.all()
        counting=len(count)
        return render(request,"detail.html",{"count":counting})
    