from django.db.models.signals import post_save  # Signal sent after a model is saved
from django.dispatch import receiver  # Decorator to connect functions to signals
from django.contrib.auth.models import User  
from .models import Member  

# When receiver trigerred (User saved + sender model is from User class)
# When User is saved, post_save signal sent -> post_save.send(sender=User, instance...)
#Django checks registery to see who's listening -> receivers
@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    #Sender param not used but needs to be here to accept it from post_save
    """
    Automatically create a Member profile when a new User is created.

    Parameters:
    - sender: The model class that sent the signal (User in this case)
    - instance: The actual User object that was just saved
    - created: True if new user, False if updating existing
    - **kwargs: Any additional keyword arguments (we don't need them here)
    """
    
    # Only create Member if this is a NEW User (not an update)
    if created:
        # Create a Member object linked to this new User
        # The user=instance links the Member to the User that was just created
        Member.objects.create(user=instance)



# Saves Member when User is saved
@receiver(post_save, sender=User)
def save_member_profile(sender, instance, **kwargs):
    """
    Save the Member profile whenever the User is saved.
    
    This ensures that if you update a User, their Member profile is also saved.
    Uses get_or_create to handle cases where Member might not exist yet.
    """
    
    # get_or_create returns (object, created_boolean)
    # If Member exists, get it. If not, create it.
    member, created = Member.objects.get_or_create(user=instance)
    
    # Save the member (in case any related data changed)
    member.save()