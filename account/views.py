from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CreateUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm

# Create your views here.
def register(request):
    form = CreateUser(request.POST)
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            #Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        form = CreateUser()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        elif not User.objects.filter(username=username).exists():
            return render(request, 'login.html', {'error': 'User not found'})
        else:
            return render(request, 'login.html', {'error': 'Username or Password is Incorrect'})
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def userEdit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        #profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        #if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user_form.save()
            #profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        #profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'useredit.html', {'user_form':user_form})

login_required
def dashboard(request):
    # return render(request, 'account/dashboard.html', {'section': 'dashboard'})
    return render(request, 'dashboard.html')