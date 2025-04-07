
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contect/', views.contect, name='contect'),
    path('services/', views.services, name='services'),
    path('Trending/', views.Trending, name='Trending'),
    path('Sport/', views.Sport, name='Sport'),
    path('Trump/', views.Trump, name='Trump'),
    path('American/', views.American, name='American'),
    path('Republican/', views.Republican, name='Republican'),
    path('International/', views.International, name='International'),
    path('studentView/', views.studentView, name='studentView'),
    path('search/', views.search, name='search'),
    path('details/<str:id>/', views.details, name='details'),
] + static (settings.MEDIA_URL, document_root = settings. MEDIA_ROOT)
