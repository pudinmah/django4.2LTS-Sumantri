
from django.contrib import admin
from django.urls import path, include

from . import views

# url project

urlpatterns = [
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
