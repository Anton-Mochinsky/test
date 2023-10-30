"""app URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


from app import settings
from jk.views import Home, Personal_Area, Login, Sing_up, About, Editing_profile
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home, name='home'),
    path('about/', About, name='about'),
    path('personal_area/', Personal_Area, name='personal_area'),
    path('editing_profile/', Editing_profile, name='editing_profile'),
    path('login/', Login, name='login'),
    path('sing_up/', Sing_up, name='sing_up'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('auth-token/', obtain_auth_token),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


