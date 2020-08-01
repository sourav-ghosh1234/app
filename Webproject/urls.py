"""Webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('register',views.start),
    path('start1',views.insert),
    path('login',views.loginpage),
    path('log',views.login),
    path('logout',views.logout),
    path('abt',views.about),
    path('nav/<key>',views.navbar),
    path('lead/<key>',views.leaderboard),
    path('cntct',views.contactpg),
    path('cntctfrm',views.contactins),
    path('feedbck/<key>',views.feedbackpg),
    path('feedbckfrm/<sr>',views.feedbackins),
    path('click/<key>',views.fetch),
    path('tab/<cat>/<name>',views.ceck),
    path('ret/<key>/<score>',views.getans),
    path('scro/<key>/<score>',views.scorepg),
    path('profile/<key>',views.profl),
    
]

