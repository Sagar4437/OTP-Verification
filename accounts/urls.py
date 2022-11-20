from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('otp-verification/', otp_verification, name='otp-verification'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
