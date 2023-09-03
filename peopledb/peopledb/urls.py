"""peopledb URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
]
