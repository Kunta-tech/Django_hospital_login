from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login', views.login_user, name='login'),
    path('signup', views.register, name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('', views.home, name='home')
]
