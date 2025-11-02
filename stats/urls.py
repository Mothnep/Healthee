from django.urls import path
from . import views

urlpatterns = [
   path('', views.stats_overview, name='stats_overview'), 
   path('running_stats/', views.running_stats, name='running_stats'), 
   path('weightlifting_stats/', views.weightlifting_stats, name='weightlifting_stats'),
   path('halth_stats', views.health_stats, name='health_stats' ),
   
]