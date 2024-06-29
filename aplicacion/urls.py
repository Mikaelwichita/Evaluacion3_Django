from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('ayuda/',views.ayuda, name='ayuda'),
    path('bandanas/',views.bandanas, name='bandanas'),

    path('canasta/',views.ver_canasta, name='ver_canasta'),
    path('agregar_al_carrito/<int:producto_id>//',views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:item_id>/',views.eliminar_del_carrito, name='eliminar_del_carrito'),


    path('agregar_al_carrito_bandana/<int:producto_id>/', views.agregar_al_carrito_bandana, name='agregar_al_carrito_bandana'),
    path('agregar_al_carrito_collares/<int:producto_id>/', views.agregar_al_carrito_collares, name='agregar_al_carrito_collares'),
    path('agregar_al_carrito_identificadores/<int:producto_id>/', views.agregar_al_carrito_identificadores, name='agregar_al_carrito_identificadores'),
    path('agregar_al_carrito_ofertas/<int:producto_id>/', views.agregar_al_carrito_ofertas, name='agregar_al_carrito_ofertas'),


    path('collares/',views.collares, name='collares'),
    path('identificadores/',views.identificadores, name='identificadores'),
    path('ofertas/',views.ofertas, name='ofertas'),
    path('fundacion/',views.fundacion, name='fundacion'),
    path('registro/',views.registro, name='registro'),
    path('micuenta/',views.micuenta, name='micuenta'),




 ########### URLS DE INDEX 

    path('admin_listado/', views.lista_productos, name='lista_productos'),


 ########### URLS DE INDEX 

    path('admin_agregar_index/', views.agregar_producto_index, name='agregar_producto_index'),
    path('admin_eliminar_index/<int:producto_id>/', views.eliminar_producto_index, name='eliminar_producto_index'),
    path('admin_modificar_index/<int:producto_id>/', views.modificar_producto_index, name='modificar_producto_index'),

 ########### URLS DE bandanas 

    path('admin_agregar_bandanas/', views.agregar_producto_bandanas, name='agregar_producto_bandanas'),
    path('admin_eliminar_bandanas/<int:producto_id>/', views.eliminar_producto_bandanas, name='eliminar_producto_bandanas'),
    path('admin_modificar_bandanas/<int:producto_id>/', views.modificar_producto_bandanas, name='modificar_producto_bandanas'),

 ########### URLS DE collares 
    
    path('admin_agregar_collares/', views.agregar_producto_collares, name='agregar_producto_collares'),
    path('admin_eliminar_collares/<int:producto_id>/', views.eliminar_producto_collares, name='eliminar_producto_collares'),
    path('admin_modificar_collares/<int:producto_id>/', views.modificar_producto_collares, name='modificar_producto_collares'),

 ########### URLS DE IDENTIFICADORES 

    path('admin_agregar_identificadores/', views.agregar_producto_identificadores, name='agregar_producto_identificadores'),
    path('admin_eliminar_identificadores/<int:producto_id>/', views.eliminar_producto_identificadores, name='eliminar_producto_identificadores'),
    path('admin_modificar_identificadores/<int:producto_id>/', views.modificar_producto_collares, name='modificar_producto_identificadores'),

 ########### URLS DE OFERTAS 

    path('admin_agregar_ofertas/', views.agregar_producto_ofertas, name='agregar_producto_ofertas'),
    path('admin_eliminar_ofertas/<int:producto_id>/', views.eliminar_producto_ofertas, name='eliminar_producto_ofertas'),
    path('admin_modificar_ofertas/<int:producto_id>/', views.modificar_producto_ofertas, name='modificar_producto_ofertas'),

    








]