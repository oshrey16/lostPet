from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import static
from django.urls import include, path

handler404 = 'website.views.my404'
handler500 = 'website.views.my500'

urlpatterns = [
    path('home/', include('website.urls')),
    path('home/post', include('post.urls')),
    path('admin/', admin.site.urls),
    path('captcha/',include("captcha.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)