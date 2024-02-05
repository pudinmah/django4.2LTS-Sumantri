from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'kontak',
        'subtitle':'ini adalah kontak hubungi kami',
        'banner':'/kontak/images/beranda.png'
    }
    return render(request,'index.html',context)