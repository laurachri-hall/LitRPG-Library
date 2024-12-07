from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path(
        'google1234567890abcdef.html',
        serve,
        {'document_root': settings.STATIC_ROOT, 'path': 'verification/google1234567890abcdef.html'}
    ),
    path('summernote/', include('django_summernote.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('to_be_read/', include('to_be_read.urls')),
    path('', include("review.urls"), name='review_urls'),
]

# Add static file serving during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
