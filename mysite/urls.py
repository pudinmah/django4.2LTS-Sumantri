
from django.contrib import admin
from django.urls import path, include

# from .views import index

urlpatterns = [
    path('blog/', include('blog.urls')),
    # path('',index),
    path('admin/', admin.site.urls),
]
