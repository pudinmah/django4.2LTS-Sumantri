from django.shortcuts import render

from .models import Artikel

# Create your views here.

def index(request):
    # queryset
    allArtikel = Artikel.objects.all()
    print(allArtikel)
    
    context = {
        'title':'blog',
        'headline':'halaman blog',
        'semuaArtikel':allArtikel

    }
    return render(request, 'index.html', context)
