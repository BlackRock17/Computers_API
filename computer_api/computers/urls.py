from django.urls import path

from .views import ComputerList

urlpatterns = [
    path('computers/', ComputerList.as_view(), name='computer-list'),
]
