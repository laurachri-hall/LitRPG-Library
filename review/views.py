from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from .models import Review

class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "review/index.html"
    paginate_by = 6