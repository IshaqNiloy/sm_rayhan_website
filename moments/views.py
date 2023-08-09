from django.views import generic
from .models import Moment
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'moments/moments.html'

    def get_queryset(self):
        return Moment.objects.all()
