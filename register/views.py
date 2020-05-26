
from django.shortcuts import render, redirect  
#*from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #*form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        #*form = UserCreationForm()
    return render(request, 'register/user.html', {'form':form})


def profile(request):
    return render(request, 'register/profile.html')    

