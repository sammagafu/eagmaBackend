from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('artist/',include('artist.urls')),
    path('awards/',include('awards.urls')),
    path('nominees/',include('nominees.urls')),
    
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # include('djoser.urls.authtoken')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
