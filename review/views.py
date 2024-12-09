from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView, ListView
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q, Avg
from django.db import IntegrityError
from allauth.socialaccount.models import SocialApp
from .models import Review, Book, Comment
from .forms import CommentForm, ReviewForm, BookForm
from . import views


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Featured reviews (as already implemented)
        context['featured_reviews'] = Review.objects.filter(featured=True)[:3]

        if self.request.user.is_authenticated:
            # Fetch all reviews or the latest review for the logged-in user
            context['user_reviews'] = Review.objects.filter(
                user=self.request.user).order_by('-created_on')[:3]

        return context


class ReviewList(generic.ListView):
    """
    List of all reviews
    """
    queryset = Review.objects.filter(status=1)
    template_name = "review_list.html"
    paginate_by = 6


class UserReviewsView(LoginRequiredMixin, ListView):
    """
    lists a users reviews
    """
    model = Review
    template_name = "user_reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        # Return reviews belonging to the logged-in user
        return Review.objects.filter(
            user=self.request.user).order_by('-created_on')


def review_detail(request, slug):
    """
    Displays individual review
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    book = review.book
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
            request,
            messages.SUCCESS, 'Comment submitted and awaiting approval.')

    return render(
        request,
        "review/review_detail.html",
        {
            "review": review,
            "book": book,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def add_review(request):
    """
    Add Review
    """
    if request.method == 'POST':
        # Include files if using file uploads
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            book = review_form.cleaned_data['book']

            # Check if a review for this book already exists
            existing_review = Review.objects.filter(book=book).first()
            print(
                f"Existing review for book {book.id}: {existing_review}")
            if existing_review:
                return HttpResponse(
                    "A review for this book already exists.", status=400)

            try:
                # Save the review with slug generation
                review = review_form.save(commit=False)
                # Associate the review with the logged-in user
                review.user = request.user

                # Automatically generate slug if it's empty
                if not review.slug:
                    review.slug = slugify(review.title)

                review.save()

                messages.success(
                    request,
                    f'Your review for "{book.book_title}" has '
                    'been added successfully and is awaiting approval.')
                return redirect('home')

            except IntegrityError as e:
                # Handle the error if an issue
                return HttpResponse(
                    "An error occurred while saving your review."
                    "Please try again "
                    "later.",
                    status=500)
    else:
        review_form = ReviewForm()

    return render(
        request,
        "review/add_review.html",
        {
            "review_form": review_form
        },
    )


def review_edit(request, slug):
    """
    Edit Review
    """
    review = get_object_or_404(Review, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                    request,
                    f'Your review for "{book.book_title}" has '
                    'been updated successfully!')
            return redirect('review_detail', slug=review.slug)
    else:
        form = ReviewForm(instance=review)

    return render(
        request, 'review/review_edit.html', {'form': form, 'review': review})


def review_delete(request, slug):
    """
    Delete Review
    """
    # Use slug to fetch the review
    review = get_object_or_404(Review, slug=slug)
    # Check if the logged-in user is the owner of the review
    if request.user != review.user:
        return HttpResponseForbidden(
                "You are not allowed to delete this review.")

    # If the request method is POST, delete the review
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('home')  # Redirect to home after deletion


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
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

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
        messages.add_message(
                request,
                messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def add_book(request):
    """
    view to add book
    """
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            title = book_form.cleaned_data['book_title']
            author = book_form.cleaned_data['book_author']

            # Check for existing books with the same title and author
            existing_book = Book.objects.filter(
                Q(book_title__iexact=title) & Q(book_author__iexact=author)
            ).first()

            if existing_book:
                messages.warning(
                        request,
                        f'A book titled "{title}" by {author} already exists.')
            else:
                book_form.save()
                messages.success(
                        request, f'Successfully added "{title}" by {author}.')
                return redirect('home')
    else:
        book_form = BookForm()

    return render(
        request,
        "review/add_book.html",
        {
            "book_form": book_form
        },
    )
