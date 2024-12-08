from django.urls import path
from .views import add_to_read_list, tbr_list, delete_from_tbr

urlpatterns = [
    path('add/<int:book_id>/', add_to_read_list, name='add_to_read_list'),
    path('', tbr_list, name='tbr_list'),
    path('delete/<int:entry_id>/', delete_from_tbr, name='delete_from_tbr'),
]
