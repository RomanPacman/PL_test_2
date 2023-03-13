from django.contrib import admin
from django.urls import path
from .views import input_page

urlpatterns = [
    path('', input_page),
    path('admin/', admin.site.urls),
]
