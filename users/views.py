from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Save the User instance
            
            # Check if a profile already exists for the user
            profile = Profile.objects.filter(user=user).first()
            if not profile:
                # Create and save the associated Profile instance
                profile = Profile(user=user)
                profile.save() 
                
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are Logged in by {username}.')
            
            # Log the user in
            login(request, user)
            
            return redirect('blog-home')   
                
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        
    else : 
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    
    return render(request, 'users/profile.html', context)
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
