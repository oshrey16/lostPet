from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('website.urls')),
    path('post/', include('post.urls')),
    path('admin/', admin.site.urls),
    path('/captcha',include("captcha.urls"))
]