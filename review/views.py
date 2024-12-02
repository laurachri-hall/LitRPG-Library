from django.shortcuts import render, get_object_or_404,reverse, redirect
from django.views.generic import TemplateView
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Review, Book, Comment
from .forms import CommentForm, ReviewForm, BookForm
from . import views


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
        request, messages.SUCCESS,
        'Comment submitted and awaiting approval'
    )

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
    """
    Add Review
    """
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            book = review_form.cleaned_data['book']
            
            # Check if a review for this book already exists
            existing_review = Review.objects.filter(book=book).first()
            
            if existing_review:
                messages.warning(request, f'A review for "{book.book_title}" already exists.')
            else:
                review = review_form.save(commit=False)
                review.user = request.user  
                review.save()
                messages.success(request, f'Your review for "{book.book_title}" has been added successfully.')
                return redirect('home')  
    else:
        review_form = ReviewForm()
    
    return render(
        request,
        "review/add_review.html",
        {
            "review_form": review_form
        },
    )
   
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
                messages.warning(request, f'A book titled "{title}" by {author} already exists.')
            else:
                book_form.save()
                messages.success(request, f'Successfully added "{title}" by {author}.')
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

    def review_detail(request, book_id):
        book = get_object_or_404(Book, id=book_id)  # This retrieves the book based on its ID
        return render(request, 'review/review_detail.html', {'book': book, 'review': review})

