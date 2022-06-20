from django.conf.urls import url
from django.contrib import admin
from WAD import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    #path('login/', views.login, name="login"),
    path('staff/', views.staff, name="staff"),
    path('pricing/', views.pricing, name="pricing"),
    path('contact/', views.contact, name="contact"),
    path("add/", views.addPlan, name="log"),
    path("show/", views.showPlans, name="show"),


]

urlpatterns += staticfiles_urlpatterns()