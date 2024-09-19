from django.urls import path
from . import views
from .views import ListaProductosView

urlpatterns =[
    path('lista',views.lista_productos, name='lista_productos'),
    path('',views.producto, name='producto'),
    path('lista_html', views.listados_productos, name='listados_productos' ),
    path('lista_modelo', ListaProductosView.as_view(), name= 'lista_modelo')
]