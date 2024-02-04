
from django.contrib import admin
from django.urls import path


# from . views import index, blog #import function di file view
# from . import views
from . views import *

urlpatterns = [
    # path('', views.index),  # from . import views
    # path('blog/', views.blog),

    path('', index),  
    path('blog/', blog),
    
    path('admin/', admin.site.urls),
]
