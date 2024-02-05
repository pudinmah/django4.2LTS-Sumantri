from django.shortcuts import render

# Create your views app here.

def index(request):
    context = {
    'title': 'blog bersama',
    'developer': 'mahpudn'
    }
    return render(request, 'blog/index.html', context) # panggil folder blog/index di app blog

def artikel(request):
    context = {
    'title': 'blog Artikel',
    'developer': 'wahyu'
    }
    return render(request, 'blog/index.html', context) # panggil folder blog/index di app blog

def berita(request):
    context = {
    'title': 'blog Berita',
    'developer': 'ucup'
    }
    return render(request, 'blog/index.html', context) # panggil folder blog/index di app blog

