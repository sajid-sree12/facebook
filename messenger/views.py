from django.shortcuts import render

# Create your views here.
def home(request):
    name="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    marks=[23,52,56,73]
    context={'Hero':name,'age':40,'sequence':marks}
    return render(request,'index.html',context)

def home2(request,name):
    marks=[23,52,56,73]
    context={'Hero':name,'age':40,'sequence':marks}
    return render(request,'index.html',context)

def home3(request,movie,hero,year):
    return render(request,'movie.html',{'movie_name':movie,'released':year,'hero':hero})