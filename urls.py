from django.urls import path
from . import views
from django.contrib.auth import views as user_views



urlpatterns = [
    path('', views.registration, name = 'userapp-regisration' ),
    path('home/', views.home, name = 'userapp_home'),
    path('login/', user_views.LoginView.as_view(template_name = "userapp/login.html"),  name = 'userapp_login'),
    path('logout/', user_views.LogoutView.as_view(template_name = "userapp/logout.html"), name = 'userapp_logout')
]
