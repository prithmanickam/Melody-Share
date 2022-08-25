from django.conf import settings
from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('make_music/', views.make_music, name='make_music'),
    path('login/', auth_view.LoginView.as_view(template_name='main/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='main/logout.html'), name="logout"),
    path('profile/', views.profile, name='profile'),
    path('profile/upload/', views.upload_music, name='upload_music'),
    path('profile/<int:pk>/', views.delete_music, name='delete_music'),
    path('profile/publish/<int:pk>', views.publish_music, name='publish_music'),
    
    path('view_music/', views.view_music, name='view_music'),
    path('view_music/<int:pk>/', views.like_music, name='like_music'),
    path('share/', views.share, name='share'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
