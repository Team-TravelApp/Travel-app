"""config URL Configuration

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
from django.urls import path, include
from travel import views
from api.router import router
from api import views as api_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.index, name="home"),
    path('', views.tag_home, name="home"),
    path('post/<slug:slug>/', views.tag_detail, name="detail"),
    
    path('api/', include(router.urls)),
    #path("", include("api.urls")),
    path('api/attractionposts/<int:attractionpost_pk>/comments/', api_views.CommentListCreateView.as_view(), name="comments"),
    path('api/mycomments/', api_views.MyComments.as_view(), name="my_comments"),
    path('following/', views.FollowingListCreateView.as_view(), name='Following-list'),
    path('image/<int:pk>/', api_views.PostImageView.as_view(), name='post-image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




