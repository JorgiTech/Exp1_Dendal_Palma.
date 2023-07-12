from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('index/', views.index, name='index'), 
    path('nosotros/', views.nosotros, name='nosotros'),
    path('galeria/', views.galeria, name='galeria'),
    path('api/', views.api, name='api'),
    path('formulario/', views.formulario, name='formulario'),
    path('productos/', views.productos, name='productos'),
    path('agregar/', views.agregar, name='agregar'),
    path('agregarsave', views.agregarsave, name='agregarsave'),
    path('productos/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>/', views.actualizar, name='actualizar'),
    path('actualizarsave/<int:id>/', views.actualizarsave, name='actualizarsave'),
    path('add/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('del/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]