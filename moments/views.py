from django.views import generic
from .models import Moment
from sm_rayhan_website import settings
from django.core.paginator import Paginator
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'moments/moments.html'

    def get_queryset(self):
        query_set = Moment.objects.all().order_by('id')
        items_per_page = settings.ITEMS_PER_PAGE
        paginator = Paginator(query_set, items_per_page)
        page_num = self.request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        print(page_obj.number)

        return page_obj
