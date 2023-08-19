from django.shortcuts import render
from django.views import generic
from .models import ThoughtsV1
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from sm_rayhan_website import settings
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'thoughts/thoughts.html'

    def get_queryset(self):
        query_set = ThoughtsV1.objects.all().order_by('id')
        items_per_page = settings.ITEMS_PER_PAGE
        paginator = Paginator(query_set, items_per_page)
        page_num = self.request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        return page_obj


class DetailView(generic.ListView):
    template_name = 'thoughts/detail.html'

    def get_queryset(self):
        return ThoughtsV1.objects.all().order_by('id')

