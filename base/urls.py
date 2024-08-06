from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("home/", views.home, name="home"),
    path("signup/", views.authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/add/', views.add_candidate, name='candidate_add'),
    path('candidates/edit/<int:pk>/', views.update_candidate, name='candidate_edit'),
    path('candidates/delete/<int:pk>/', views.delete_candidate, name='candidate_delete'),
    path('offer_letters/', views.offer_letter_list, name='offer_letter_list'),
    path('offer_letters/create/', views.create_offer_letter, name='offer_letter_create'),
    path('offer_letters/<int:pk>/', views.view_offer_letter, name='offer_letter_view'),
    path('offer_letters/download/<int:pk>/', views.download_offer_letter, name='download_offer_letter'), 
]
