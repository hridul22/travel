from django.http import HttpResponse
from django.shortcuts import render
from . models import places
from . models import team
# Create your views here.
def demo(request):
    obj=places.objects.all()
    obl2=team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obl2})

