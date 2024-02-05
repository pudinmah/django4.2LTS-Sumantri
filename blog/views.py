from django.shortcuts import render

# Create your views app here.

def index(request):
    return render(request, 'blog/index.html') # panggil folder blog/index di app blog