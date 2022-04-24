from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [ path('admin/', admin.site.urls), path('', views.home, name='home'), path('factorial',views.factorial,name='factorial')]