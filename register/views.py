from django.shortcuts import render, redirect  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login as auth_login  
from django.contrib import messages  

# Create your views here.
def register(request):    
    
    # Submit form -> POST, View template (calling URL) -> GET
    if request.method == 'POST':

        # request.POST -> dictionary with form data
        form = UserCreationForm(request.POST)
        
        # Check all fields to meet requirements
        if form.is_valid():

            #save form in db, creates new user + member through signals.py
            user = form.save()
            
            # cleaned_data -> dictionary of validated form data
            username = form.cleaned_data.get('username')

            # Success message to be displayed in the HTML template, not used rn because redirected
            messages.success(request, f'Account created for {username}!')

            # Automatic login 
            auth_login(request, user)
            return redirect('dashboard')  
        
        # Form not valid -> show form with errors
    else:
        # Create an empty form for them to fill out
        form = UserCreationForm()
    
    return render(request, 'register.html/', {'form': form})
