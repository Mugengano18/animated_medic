from django.urls import path
from .views import *

urlpatterns = [
	path('', get_retail_information, name='ret_info'),
	path('map/', map_detail, name='map_detail')

]