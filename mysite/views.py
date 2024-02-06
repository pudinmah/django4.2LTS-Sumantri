from django.shortcuts import render



# project
def index(request):
    context = {
        'title':'portopolio',
        'subtitle':'Jika saya mencoba yang terbaik dan gagal, setidaknya saya telah melakukan yang terbaik.',
        
        'name':'Mahpudin',
        'jobs':'Web Developer',
    }
    return render(request, 'index.html',context)