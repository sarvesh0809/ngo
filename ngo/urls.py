"""ngo URL Configuration

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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('ngoform/',views.ngoform, name='ngofrom'),
    path('donate/',views.donate, name='donate'),
    path('login/',views.user_login, name='user_login'),
    path('signup/',views.user_signup, name='user_signup'),
    path('logout/',views.user_logout, name='logout'),
    path('afterpay/',views.afterpay, name='afterpay'),
    path('contact/',views.contact, name='contact'),
    path('error/',views.error, name='error'),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


