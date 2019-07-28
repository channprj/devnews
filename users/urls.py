from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_detail),
    # path('<str:username>/', views.ProfileDetailByUsername.as_view()),
    path('<str:username>/', views.user_detail),
]
