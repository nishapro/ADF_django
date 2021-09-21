from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('storeDetails',views.storeDetails,name='storeDetails')
]