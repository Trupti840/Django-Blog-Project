#personal_blog_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
    path('', include('authentication.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),


]
