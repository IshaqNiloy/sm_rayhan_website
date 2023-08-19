from . import views
from django.urls import path

app_name = 'moments'

urlpatterns = [
    #/moments/
    path('moments/', views.IndexView.as_view(), name='moments'),
]