from django.urls import path

from .views import GetComputers, get_computer

app_name = 'computers_and_accessories.category.computer'

urlpatterns = [
    path('', GetComputers.as_view(), name='computers-list'),
    path('tutorial/', get_computer, name='get-computer'),
]