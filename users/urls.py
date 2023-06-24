from django.urls import path
from . import views

urlpatterns = [
    path('get-csrf-token', views.get_csrf_token, name='get-csrf-token'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
