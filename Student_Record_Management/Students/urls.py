from django.urls import path
from . import views

urlpatterns = [
    # Dashboard (Home)
    path('', views.dashboard, name='dashboard'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Student CRUD
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),

    # Other Pages
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
]
