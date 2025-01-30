from . import views
from django.urls import path
from . views import HomePage
from .views import user_profile, custom_login_redirect 
from django.contrib.auth.views import LogoutView


urlpatterns = [ path('', HomePage.as_view(), name='home'),
                path('logout/', LogoutView.as_view(), name='logout'),
                path('login-redirect/',custom_login_redirect, name='login_redirect'),
                path('<str:username>/', user_profile, name='user_profile'),
                path('profile/<str:username>/', user_profile, name='user_profile'),  # User profile page
              
                ]  


