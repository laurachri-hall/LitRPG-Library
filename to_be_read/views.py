from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ToBeRead
from review.models import Book


@login_required
def add_to_read_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    review = book.review
    tbr, created = ToBeRead.objects.get_or_create(user=request.user, book=book)
    if created:
        messages.success(
            request, f"'{book.book_title}' has been added to your TBR list."
        )
    else:
        messages.info(
            request, f"'{book.book_title}' is already in your TBR list.")
    return redirect(reverse("review_detail", args=[review.slug]))


@login_required
def tbr_list(request):
    # Get all books in the user's To Be Read list
    tbr_books = ToBeRead.objects.filter(
        user=request.user).select_related("book")
    paginator = Paginator(tbr_books, 6)  # Paginate with 6 items per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "to_be_read/tbr_list.html", {"tbr_books": tbr_books})


@login_required
def delete_from_tbr(request, entry_id):
    entry = get_object_or_404(ToBeRead, id=entry_id, user=request.user)
    entry.delete()
    return redirect("tbr_list")
