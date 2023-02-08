"""oilstubdata URL Configuration

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
from django.contrib.auth import views as auth_views #new

from oilandgasdata import views
from search import views as search_view
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path('api/v1/search/', views.SearchViewSet.as_view(), name='search'),
    path('', include('search.urls')),
    path('oilandgasdata/', include(('oilandgasdata.urls', 'oilandgasdata'), namespace='oilandgasdata')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #new
    path(rf'', admin.site.urls),
]
