from django.shortcuts import render

def index(request):
    context = {
        'title':'portopolio',
        'subtitle':'selamat datang di channel ini good peoples, terima kasih sudah subscribe!',
        'banner':'images/beranda.png',
    }
    return render(request, 'index.html', context)

def login(request):
    context = {
        'title':'login'
    }
    return render(request, 'login.html',context)

def daftar(request):
    context = {
        'title':'Daftar',
    }
    return render(request, 'daftar.html',context)