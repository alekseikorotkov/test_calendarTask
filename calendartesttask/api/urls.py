"""api urls module"""
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^calendar/(?:country=(?P<country_ids>\d+)&negotiator=(?P<negotiator_ids>\d+)&company=(?P<company_ids>\d+)/)?$', views.get_data),
]
