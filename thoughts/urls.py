from .views import IndexView, DetailView
from django.urls import path

app_name = 'thoughts'

urlpatterns = [
    #/thoughts/
    path('thoughts', IndexView.as_view(), name='thoughts'),
    #/thoughts/123
    path('thoughts/<int:pk>', DetailView.as_view(), name='detail'),

]

