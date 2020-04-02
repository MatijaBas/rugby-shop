from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages, auth
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# The views.


def index(request):
    """A view to display the index page"""
    return render(request, "index.html")


def logout(request):
    """A view to log the user out and redirect back to the index page"""

    username = request.user.username
    auth.logout(request)
    messages.success(request, f'You have successfully logged out {username}')
    return redirect(reverse('index'))


def login(request):
    """A view to manage the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(
                    request, f"You have successfully logged in {user.username}")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view to display the profile page of a logged in user"""
    return render(request, 'profile.html')


def register(request):
    """A view to manage the registration form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request, "You have successfully registered and are now logged in!")
                return render(request, 'index.html')
            else:
                messages.error(
                    request, "We are unable to register your account right now")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})
