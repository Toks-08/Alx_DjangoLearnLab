from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User
from django_blog import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
     model = User
     fields = ("username", "email", "password1", "password2")

def register(request):
     if request.method == 'POST':
         form = CustomUserCreationForm(request.POST)
         if form.is_valid():
             user= form.save()
             login(request, user)
             return redirect(settings.LOGIN_REDIRECT_URL)
     else:
         form = CustomUserCreationForm()

         return render(request, 'blog/register.html', {'form': form})

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']  # add more fields later if needed

# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})