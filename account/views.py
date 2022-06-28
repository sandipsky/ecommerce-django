from django.shortcuts import render, redirect
from .forms import CreateUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            return redirect('products')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')