from django.urls import path
from .views import index,nosotros,galeria,api,formulario,productos


urlpatterns = [
    path('index/', index,name='index'),
    path('nosotros/', nosotros,name='nosotros'),
    path('galeria/', galeria,name='galeria'),
    path('api/', api,name='api'),
    path('formulario/', formulario,name='formulario'),
    path('productos/', productos,name='productos')
]
