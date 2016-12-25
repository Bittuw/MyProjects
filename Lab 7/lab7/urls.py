"""lab7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lab import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^logout$', views.logout, name='logout'),
    #url(r'^success$', views.login_success, name='success'),
    url(r'^tutor/(?P<id>\d+)$', views.TutorView.as_view(), name='tutor'),
    url(r'^admin/', admin.site.urls),
]
