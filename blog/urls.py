from django.urls import path
from . import views



# Create your urls app blog here.
app_name="blog"

urlpatterns = [
    path('',views.index),
    path('artikel/',views.artikel),
    path('berita/',views.berita),
    path('blog/',views.blog)
]