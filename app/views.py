from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import  NeighbourForm
from django.contrib import messages

from app.models import Neighbourhood

# Create your views here.
def register(request):
   
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            
            user = authenticate(username=username,password=password)
            login(request,user)
            print(request.POST)
            messages.success(request,f"Congratulations, your account was successfully created under {username}")
            return render(request,'home.html')
         else:
            messages.success(request,f"Sorry, account was not created. Please try again.")
            return redirect('register')


    else:
        form = UserCreationForm()
        return render(request,'signup.html',{"form":form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
           
            return render(request,'home.html')
        else:
            messages.success(request,"Login unsuccessful check either your username or your password")
            return render(request,'login.html')

    else: 
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You were logged out')
    return redirect('login')

def home(request):
    render(request,'home.html')

def new_hood(request):
    current_user = request.user
    profile = Neighbourhood.objects.get(user=current_user)
    if request.method == 'POST':
        form = NeighbourForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.profile = profile
            hood.save()
        return redirect('home')
    else:
        form = NeighbourForm()
    return render(request, 'new_hood.html', {"form": form})



