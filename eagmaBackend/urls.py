from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('artist/',include('artist.urls')),
    path('awards/',include('awards.urls')),
    re_path(r'^auth/', include('djoser.urls')),
]
