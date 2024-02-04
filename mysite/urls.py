
from django.contrib import admin
from django.urls import path


from . import views #views project
from blog import views as blogviews # views app
from kontak import views as kontakviews

urlpatterns = [
    path('', views.index),  # views project fun index
    path('blog/', blogviews.index), # views app fun index
    path('kontak/', kontakviews.index),


    
    path('admin/', admin.site.urls),
]
