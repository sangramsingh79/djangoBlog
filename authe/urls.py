
from django.urls import path
from authe import views
urlpatterns = [
    path('/login',views.login, name='login'),
    path('/register',views.register, name='register'),
    path('/logout',views.register, name='logout')
]
