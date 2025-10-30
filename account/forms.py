from django import forms
from .models import Member

class MemberProfileForm(forms.ModelForm):
    """
    Form for editing Member profile data.
    Automatically generates form fields from the Member model.
    """
    
    class Meta:
        model = Member
        # Fields that users can edit (excluding 'user' since it's auto-linked)
        fields = ['dob', 'size', 'weight', 'bf', 'lift', 'run']
        
        # Custom labels for better UX
        labels = {
            'dob': 'Date of Birth',
            'size': 'Height (cm)',
            'weight': 'Weight (kg)',
            'bf': 'Body Fat Percentage',
            'lift': 'I do weightlifting',
            'run': 'I do running',
        }
        
        # Custom widgets for better styling
        widgets = {
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input'
            }),
            'size': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your height in cm'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-input',
                'step': '0.1',
                'placeholder': 'Enter your weight in kg'
            }),
            'bf': forms.NumberInput(attrs={
                'class': 'form-input',
                'step': '0.1',
                'placeholder': 'Enter your body fat percentage'
            }),
            'lift': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
            'run': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
        
        # Help text for fields
        help_texts = {
            'dob': 'Your date of birth (optional)',
            'size': 'Your height in centimeters',
            'weight': 'Your current weight in kilograms',
            'bf': 'Your body fat percentage (if known)',
        }