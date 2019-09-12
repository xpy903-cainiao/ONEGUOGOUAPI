from django.urls import path

from userapp.views import LoginView, register, logout

from . import views

app_name = 'userapp'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
