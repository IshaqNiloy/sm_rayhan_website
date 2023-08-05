from django.shortcuts import render
from django.views import generic
from .models import ThoughtsV1
from django.shortcuts import get_object_or_404
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'thoughts/thoughts.html'

    def get_queryset(self):
        return ThoughtsV1.objects.all()


class DetailView(generic.ListView):
    template_name = 'thoughts/detail.html'

    def get_queryset(self):
        return ThoughtsV1.objects.all()

