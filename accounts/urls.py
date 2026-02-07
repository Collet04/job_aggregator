from django.urls import path
from . import views

urlpatterns =[
    # Authentication Urls
    path('accounts/login/',views.login_view,name='login'),
    path('accounts/Confirm_logout/',views.logout_confirm_view,name='Confirm_logout'),
    path('accounts/logout/',views.logout_view,name='logout'),
    path('accounts/register/',views.register_view,name='register'),
    path('profile/', views.profile_view, name='profile'),

]