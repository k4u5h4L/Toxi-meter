from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='app-home'),
    path('api/', views.api, name='app-api'),
]
