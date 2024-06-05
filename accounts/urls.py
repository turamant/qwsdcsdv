from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),

]

