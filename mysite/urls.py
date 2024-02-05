

from django.contrib import admin
from django.urls import path, include

from . import views

# Create your urls project here.

urlpatterns = [
    path('',views.index),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
