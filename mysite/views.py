from django.http import HttpResponse

def index(request):
    str = "halo sayang"
    str1 = "sayang2 pea"
    str2 = "galak amat"
    output = str +" "+ str1 +" "+ str2
    return HttpResponse(output)

def blog(request):
    return HttpResponse("<h1>Ini adalah halaman blog</h1>")