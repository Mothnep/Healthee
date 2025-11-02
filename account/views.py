from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Member
from .forms import MemberProfileForm

# User's own profile (read-only view)
@login_required(login_url='/login/')
def profile(request):
    """
    Display the logged-in user's profile.
    Uses request.user to ensure users only see their own data.
    """
    # Get the Member object for the logged-in user
    # If it doesn't exist (shouldn't happen due to signals), create it
    member, created = Member.objects.get_or_create(user=request.user)
    
    context = {
        'member': member,
    }
    return render(request, 'profile.html', context)


# Edit user's own profile
@login_required(login_url='/login/')
def edit_profile(request):
    """
    Allow logged-in user to edit their own profile.
    GET: Display form with current data
    POST: Save changes and redirect to profile
    """
    # Get the Member object for the logged-in user
    member, created = Member.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # User submitted the form
        # instance=member tells the form to update existing member, not create new one
        form = MemberProfileForm(request.POST, instance=member)
        
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Show success message
            messages.success(request, 'Your profile has been updated successfully!')
            
            # Redirect to profile view
            return redirect('profile')
        else:
            # Form has errors, show them (will display in template)
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request - show form with current data
        form = MemberProfileForm(instance=member)
    
    context = {
        'form': form,
        'member': member,
    }
    return render(request, 'edit_profile.html', context)

