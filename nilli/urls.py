"""nilli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import viewer.views
from viewer.views import *

urlpatterns = [
    path('nimda/', admin.site.urls),
    path('about/', AboutView.as_view(), name='about'),
    path('detail/<int:pk>/', viewer.views.detail_view, name='detail'),
    path('', ContentsAll.as_view()),
    path('finder/', viewer.views.quiz, name='quiz'),
    path('map/', viewer.views.mapview, name='map'),
    path('match/', viewer.views.match_vid, name='match'),
    path('list/<str:option>/', viewer.views.country_view, name='countryview'),
]

