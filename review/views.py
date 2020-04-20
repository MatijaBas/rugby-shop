from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewSharingForm
from django.template.context_processors import csrf
from django.contrib.auth.models import User

# Create your views here.


def get_review(request):
    reviews = Review.objects.all()
    return render(request, "review.html", {'reviews': reviews})


@login_required()
def review_content(request, pk):
    if request.method == "GET":
        review = get_object_or_404(Review, pk=pk)
        review.save()
        return render(request, "review_content.html", {'review': review})
    if request.method == "POST":
        review = get_object_or_404(Review, pk=pk)
        review.save()
        return redirect('/review/', {'review': review})


@login_required()
def create_or_edit_review(request, pk=None):
    reviews = Review.objects.all()

    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewSharingForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            if review:
                review.title = form.cleaned_data.get('title')
                review.content = form.cleaned_data.get('content')
                review.published_date = form.cleaned_data.get('published_date')
                review.save()
                return render(request, 'review.html', {'reviews': reviews})
            else:
                review = form.save()
                return redirect('review_content', review.pk)
    else:
        form = ReviewSharingForm(instance=review)
    return render(request, 'review_form.html', {'form': form, 'review': review})
