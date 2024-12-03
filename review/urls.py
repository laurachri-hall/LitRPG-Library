from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_book/', views.add_book, name='add_book'),
    path('review/<slug:slug>/', views.review_detail, name='review_detail'), 
    path('review/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('review/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]