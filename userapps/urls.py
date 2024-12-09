from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('dashboard/', views.DashboardView.as_view(),name='dashboard'),
    path('update/', views.UpdateProfileView.as_view(),name='update'),
]