from django.urls import path

from . import views

urlpatterns = [
    # link url
    path('artikel/',views.artikel),
    path('berita/', views.berita),
    path('',views.index)
]