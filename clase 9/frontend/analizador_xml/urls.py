# analizador_xml/urls.py
from django.urls import path
from .views import xml_view

urlpatterns = [
    path('', xml_view, name='xml_view'),
]