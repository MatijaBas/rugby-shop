from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth


def index(request):
    """A view to display the index page"""
    return render(request,  'index.html')


def logout(request):
    """A view to log the user out and redirect back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
