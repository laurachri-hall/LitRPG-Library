from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from .models import Review, Book, Comment

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "review/index.html"
    paginate_by = 6

    """
    Displays individual review
    """

def review_detail(request, slug):
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "review/review_detail.html",
        {"review": review},
    )