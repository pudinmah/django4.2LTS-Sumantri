from django.shortcuts import render



# project
def index(request):
    context = {
        'title':'portopolio',
        'subtitle':'Ini adalah fortopolio saya',
        
        'banner':'images/beranda.png'
    }
    return render(request, 'index.html',context)