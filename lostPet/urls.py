from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import static
from django.urls import include, path

urlpatterns = [
    path('home/', include('website.urls')),
    path('post/', include('post.urls')),
    path('admin/', admin.site.urls),
    path('captcha/',include("captcha.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)