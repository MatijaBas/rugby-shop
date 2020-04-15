from django.shortcuts import render
from .models import Review

# Create your views here.


def get_reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {'reviews': reviews})
