from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.utils import timezone

# Create your views here.


def get_posts(request):
    posts = BlogPost.objects.filter(published_date__lte=timezone.now()
                                    ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_details(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.save()
    return render(request, "postdetails.html", {'post': post})


def create_or_edit_post(request, pk=None):
    post = get_object_or_404(BlogPost, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
