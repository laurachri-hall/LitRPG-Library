from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('to_be_read/', include('to_be_read.urls')),
    path('', include("review.urls"), name='review_urls'),
]
