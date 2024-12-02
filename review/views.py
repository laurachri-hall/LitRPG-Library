from django.shortcuts import render, get_object_or_404,reverse
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Book, Comment
from .forms import CommentForm
from .forms import ReviewForm


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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))

def add_review(request):
    review = Review.objects.all().order_by('-created_on').first()
    review_form = ReviewForm()

    return render(
        request,
        "review/add_review.html",
        {
            "add_review": add_review,
            "review_form": review_form
        },
    )