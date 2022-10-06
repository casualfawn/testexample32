"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='calendar2.html')),
    path('accounts/proj1/', TemplateView.as_view(template_name='index4.html'), name='proj1'),
    path('accounts/member_login/', TemplateView.as_view(template_name='registration/login2.html'), name='Member Login'),
    path('accounts/aboutme/',
TemplateView.as_view(template_name='aboutme.html'), name='aboutme'),
    path('accounts/proj3/', TemplateView.as_view(template_name='proj3.html'), name='proj3'),
    
    path('accounts/news/', TemplateView.as_view(template_name='news.html'), name='news'),
    
        path('accounts/proj2/', TemplateView.as_view(template_name='proj2.html'), name='proj2'),
                path('accounts/fitness/', TemplateView.as_view(template_name='fitness.html'), name='fitness'),
    path('accounts/home/', TemplateView.as_view(template_name='home.html'), name='home'),
        path('accounts/resume/',
    TemplateView.as_view(template_name='resume_scroll.html'), name='resume'),
           path('accounts/resume-zoom/',
    TemplateView.as_view(template_name='pdf_zoom.html'), name='resume'),
]
