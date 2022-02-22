from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('signup/', views.user_signup),
    path('check/', views.check_user),
    path('validate/', views.validate_user),
]
