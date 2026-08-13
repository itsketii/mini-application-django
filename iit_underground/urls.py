from django.urls import path
from . import views


app_name = 'iit_underground'

urlpatterns = [
    path('', views.fil_actualite, name='fil'),
    path('potin/<int:potin_id>/', views.detail_potin, name='detail_potin'),
]