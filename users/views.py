from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from users.forms import UserRegisterForm

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

@csrf_exempt
def register(request):
    """ Register a new user """
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Retrieve username from cleaned_data to show it on message
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your user has been created. Please, log in!')
            return redirect('login')
    # GET Request
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        # accessing from form data
        username = request.POST["username"]
        password = request.POST["password"]
        # check if correct
        user = authenticate(request, username=username, password=password)
        # If user object is returned, log in and route to index page
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("hotels"))
            # otherwise, return login page again
        else:
            return remder(request, "users/login.html", {
            "message": "Invalid credetials"
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "vacation/index.html", {
    "message": "Logout"
    })
