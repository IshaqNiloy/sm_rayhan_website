from . import views
from django.urls import path

app_name = 'moments'

urlpatterns = [
    #/moments/
    path('moments/', views.IndexView.as_view(), name='moments'),
    path('embedded-moments/<int:id>', views.EmbeddedMomentView.as_view(), name='embedded_moments'),
]


