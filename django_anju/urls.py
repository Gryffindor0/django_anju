"""django_anju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qiniuToken/',views.qiniuToken,name='qiniuToken'),
    path('sendMessage/',views.sendMessage,name='sendMessage'),
    path('checktoken/',views.checktoken,name='checktoken'),
    path('case/', include('case.urls')),
    path('collect/', include('collect.urls')),
    path('comment/', include('comment.urls')),
    path('company/', include('company.urls')),
    path('designer/', include('designer.urls')),
    path('diary/', include('diary.urls')),
    path('search/', include('search.urls')),
    path('strategy/', include('strategy.urls')),
    path('user/', include('user.urls')),

]
