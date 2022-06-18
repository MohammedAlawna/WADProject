from django.conf.urls import url
from django.contrib import admin
from WAD import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    path('', include("django.contrib.auth.urls")),
    path('loginMain/<name>', views.loginMain, name="loginMain"),

]

urlpatterns += staticfiles_urlpatterns()
