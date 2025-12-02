from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
    # check if user is authenticated
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        #Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    else:
        return render(request, 'home.html', {"records": records}) 

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')   

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in immediately after registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome {username}! Account created successfully.")
            return redirect('home')
        # If form is NOT valid → fall through to render the form with errors
    else:
        # GET request → show empty form
        form = SignUpForm()

    # This line runs for GET requests AND for invalid POST requests
    return render(request, 'register.html', {'form': form})
    

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in to view that page.")
        return redirect('home')


