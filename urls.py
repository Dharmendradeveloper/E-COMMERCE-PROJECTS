"""myproj1 URL Configuration

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
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from signupapp import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/profile', auth_views.LoginView.as_view(template_name= 'home2.html'), name='login'),
    url(r'^accounts/login', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name= 'home1.html'), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^cart/$', core_views.cart, name='cart'),
    url(r'^addcart/$', core_views.addcart, name='addcart'),
    url(r'^insertcart/$', core_views.insertcart, name='insertcart'),
    url(r'^viewcart/$', core_views.viewcart, name='viewcart'),
    url(r'^deletecart/$', core_views.deletecart, name='deletecart'),
    url(r'^modifycart/$', core_views.modifycart, name='modifycart'),
    url(r'^modifiedcart/$', core_views.modifiedcart, name='modifiedcart'),

    url(r'^track/$', core_views.track, name='track'),
    url(r'^cancel/$', core_views.cancel, name='cancel'),
    url(r'^search/$', core_views.search, name='search'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
]

