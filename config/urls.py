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
from django.views import View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    # path('accounts/logout/', views.logout, name='logout'),
    # path('accounts/login/', views.login,name='login'),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.index, name="index"),
    path('', views.tag_home, name="home"),
    path('post/<slug:slug>/', views.tag_detail, name="detail"),
    path('favorites', views.attractions_by_favorite, name='attractions_by_favorite'),
    path('attractions/<int:pk>',views.attraction_details, name='attraction_details'),
    path('attraction/new',views.add_attraction, name='add_attraction'),
    path('attractions/<int:pk>/comment',views.add_comment, name='add_comment'),
    path('attractions/<int:pk>/delete', views.attraction_delete, name='attractiondelete'),
    path('attractions/<int:pk>/edit', views.attraction_edit, name='attractionedit'),
    path('profile/create',views.profile_create, name='profile_create'),
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/followers', views.ListFollowers, name='followers-list'),
    path('profile/<int:pk>/edit', views.profile_edit, name='profileedit'),
    path('profile/<int:pk>/delete', views.profile_delete, name='profiledelete'),
    path('search', views.search, name='search'),
    path('display_attraction_pic', views.display_attraction_pic, name='display_attraction_pic'),
    path('add_like/<int:attraction_pk>', views.add_like, name='add_like'),

    
    path('api/', include(router.urls)),
    # path("", include("api.urls")),
    path('api/attractionposts/<int:attractionpost_pk>/comments/', api_views.CommentListCreateView.as_view(), name="comments"),
    path('api/mycomments/', api_views.MyComments.as_view(), name="my_comments"),
    path('following/', api_views.FollowingListCreateView.as_view(), name='Following-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
