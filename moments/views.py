from django.views import generic
from .models import Moment, EmbeddedMoment
from sm_rayhan_website import settings
from django.core.paginator import Paginator
from django.views import View
from django.http import JsonResponse
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'moments/moments.html'

    def get_queryset(self):
        query_set = Moment.objects.all().order_by('id')
        items_per_page = settings.ITEMS_PER_PAGE
        paginator = Paginator(query_set, items_per_page)
        page_num = self.request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        return page_obj


class EmbeddedMomentView(View):
    def get(self, request, id):
        obj_list = EmbeddedMoment.objects.filter(moment__id=id).order_by('id')
        data = [{'image': obj.image.url} for obj in obj_list]
        return JsonResponse(data, safe=False)

