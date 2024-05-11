from django.urls import path
from .views import register, CustomLoginView
# from . import views

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', CustomLoginView.as_view(), name='login')
]

