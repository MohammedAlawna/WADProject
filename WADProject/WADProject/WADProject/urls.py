from django.conf.urls import url
from django.contrib import admin
from WAD import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/', views.homepage),
    url('about/', views.about),
    #url('login/', views.login),
    url('', include("django.contrib.auth.urls")),

]
