from django.shortcuts import render


# Create your views project here.

def index(request):
    context = {
        'title':'mywebsite',
        'developer':'Mahpudin'
    }
    return render(request,'index.html',context)