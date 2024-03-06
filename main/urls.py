from django.urls import path 
from . import views 
from django.contrib.auth import views as user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login', user.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout',views.logout,name='logout'),
    path('post',views.post,name='post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('profile',views.profile,name='profile'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)