from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  # /account/ → user's profile
    path('edit/', views.edit_profile, name='edit_profile'),  # /account/edit/ → edit profile
]