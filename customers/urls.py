from django.urls import path
from .views import customers_list, customers_detail

urlpatterns = [
    path('', customers_list, name='customers_list'),
    path('<int:pk>', customers_detail, name='customers_detail')
]