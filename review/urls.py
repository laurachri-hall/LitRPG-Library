from django.urls import path, include
from star_ratings.urls import urlpatterns as star_ratings_urls
from .views import UserReviewsView
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_book/', views.add_book, name='add_book'),
    path('comment/<int:pk>/like/', views.like_comment, name='like_comment'),
    path('my-reviews/', UserReviewsView.as_view(), name='reviews_list'),
    path('review_list/', views.ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/like/', views.like_review, name='like_review'),
    path('review/<slug:slug>/', views.review_detail, name='review_detail'),
    path('review/<slug:slug>/edit/', views.review_edit, name='review_edit'),
    path(
        'review/<slug:slug>/delete/',
        views.review_delete, name='review_delete'),
    path(
        'review/<slug:slug>/edit_comment/<int:comment_id>/',
        views.comment_edit, name='comment_edit'),
    path(
        'review/<slug:slug>/delete_comment/<int:comment_id>/',
        views.comment_delete, name='comment_delete'),
    path('ratings/', include(star_ratings_urls)),
]

 
    