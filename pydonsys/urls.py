"""pydonsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from django.contrib import admin

from website import views

urlpatterns = [
    path('', views.index),
    path('pay', views.pay),

    path('terms_of_use/', views.terms_of_use),
    path('privacy_policy/', views.privacy_policy),
    path('description_of_goods/', views.description_of_goods),
    path('contacts/', views.contacts),

    path('ybXvz5S3wzR0/', admin.site.urls),
]

handler403 = 'website.views.handler403'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'
