from django.shortcuts import render, redirect  # Added redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Welcome to Healthee - Your all-around Workout tracker")

