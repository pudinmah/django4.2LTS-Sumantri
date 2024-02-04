from django.http import HttpResponse

from django.contrib import admin
from django.urls import path


def index(request):
    return HttpResponse("Halo, Dunia Django Framework")

def blog(request):
    return HttpResponse("<h1>Ini adalah halaman blog</h1>")


urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('admin/', admin.site.urls),
]
