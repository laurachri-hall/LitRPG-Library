from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path(
        'googlef5fe0d793eafff13.html',
        serve,
        {
            'document_root': settings.STATIC_ROOT,
            'path': 'verification/googlef5fe0d793eafff13.html'}
    ),
    path(
        'privacy-policy/',
        TemplateView.as_view(template_name='privacy_policy.html'),
        name='privacy_policy'),
    path(
        'terms-of-service/',
        TemplateView.as_view(template_name='terms_of_service.html'),
        name='terms_of_service'),
    path('summernote/', include('django_summernote.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('to_be_read/', include('to_be_read.urls')),
    path(
        '',
        include("review.urls"),
        name='review_urls'),  # Catch-all pattern should go last
]

# Add static file serving during development
if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL, document_root=settings.STATIC_ROOT)
