"""
URL configuration for quizapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('quizpage/<str:subject>',views.quizpage,name='quizpage'),
    path('updatescore/<str:subject>/<str:marks>',views.updatescore,name='updatescore'),
    path('analytics/',views.analytics,name='analytics'),
    path('deletedata/',views.deletedata,name='deletedata'),
    path('whome/',views.whome,name='whome'),
    path('wques/',views.wques,name='wques'),
    path('wcompleted/<str:marks>',views.wcompleted,name='wcompleted'),
    path('whome2/',views.whome2,name='whome2'),
    path('wgraph/',views.wgraph,name='wgraph'),
    path('exphome/',views.exphome,name='exphome'),
]
