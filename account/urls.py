from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  # /account/ → user's profile
    path('edit/', views.edit_profile, name='edit_profile'),  # /account/edit/ → edit profile
    path('overview', views.overview, name='overview'),  # /account/overview → dashboard
    path('members/', views.members, name='members'),  # /account/members/ → admin list
    path('members/details/<int:id>', views.details, name='details'),  # /account/members/details/1
]