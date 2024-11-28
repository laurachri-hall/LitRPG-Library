from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from .models import Review, Book, Comment
from .forms import CommentForm


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
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

    return render(
        request,
        "review/review_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )