from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def stats_overview(request):
    return render(request, 'stats_overview.html')

@login_required(login_url='/login/')
def running_stats(request):
    return render(request, 'running_stats.html')

@login_required(login_url='/login/')
def weightlifting_stats(request):
    return render(request, 'weightlifting_stats.html')

@login_required(login_url='/login/')
def health_stats(request):
    return render(request, 'health_stats.html')



