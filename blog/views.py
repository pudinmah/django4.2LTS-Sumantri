from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'blog',
        'subtitle':'ini adalah halaman blog',
        'banner':'blog/images/beranda.png',
        
    }
    return render(request, 'blog/index.html',context)