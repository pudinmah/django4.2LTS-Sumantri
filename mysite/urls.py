
from django.contrib import admin
from django.urls import path, include


from . import views #views project
from kontak import views as kontakviews

urlpatterns = [
    path('', views.index),  # views project fun index
    path('blog/', include('blog.urls')), # views app fun index
    path('kontak/', kontakviews.index),



    
    path('admin/', admin.site.urls),
]
