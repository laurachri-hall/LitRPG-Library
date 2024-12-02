from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import ToBeRead
from review.models import Book  

@login_required
def add_to_read_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    ToBeRead.objects.get_or_create(user=request.user, book=book)
    return redirect('review_detail', book_id=book.id)

@login_required
def tbr_list(request):
    tbr_books = ToBeRead.objects.filter(user=request.user)
    return render(request, 'to_be_read/tbr_list.html', {'tbr_books': tbr_books})

@login_required
def delete_from_tbr(request, entry_id):
    entry = get_object_or_404(ToBeRead, id=entry_id, user=request.user)
    entry.delete()
    return redirect('tbr_list')