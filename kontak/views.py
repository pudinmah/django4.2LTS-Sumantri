from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'kontak',
        'subtitle':'ini adalah kontak hubungi kami',
        'banner':'/kontak/images/kontak.png',
        'css_apps':'kontak/css/css_kontak.css',
    }
    return render(request,'index.html',context)