from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LocationForm, NeighbourForm
from django.contrib import messages

from app.models import Neighbourhood,Location

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

def Neigbourhood_input(request):
    neigbourhood = Neighbourhood(user=request.user)

    if request.method == 'POST':
        
         form = NeighbourForm(request.POST,request.FILES,instance=neigbourhood)
         if form.is_valid():
            form.save()
            
            return redirect('home')
         else:
           
            return redirect('neighbourhood_input')


    else:
        form = NeighbourForm(instance=neigbourhood)
        return render(request,'neighbourhood.html',{"form":form})

def location_input(request):
    location = Location(user=request.user)

    if request.method == 'POST':
        
         form = LocationForm(request.POST,request.FILES,instance=location)
         if form.is_valid():
            form.save()
            
            return redirect('home')
         else:
           
            return redirect('Make_a_post')


    else:
        form = NeighbourForm(instance=location)
        return render(request,'neighbourhood.html',{"form":form})



