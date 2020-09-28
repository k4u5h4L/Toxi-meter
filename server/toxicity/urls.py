from django.urls import path

from . import views

urlpatterns = [
    # path('', views.ListTox.as_view()),
    path('', views.ViewApi.as_view()),
    # path('<int:pk>/', views.DetailTox.as_view()),
]
