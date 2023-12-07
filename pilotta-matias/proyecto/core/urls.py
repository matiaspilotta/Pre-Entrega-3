from django.urls import path
from .views import ( 
home, 
productos, 
exit, 
crea_cliente, 
lista_clientes,
nosotros,
eliminar_cliente,
editar_cliente

)

urlpatterns = [
    path('', home, name="home"),
    path("productos/", productos, name="productos"),
    path("logout/", exit, name="exit"),
    path("crear_cliente/", crea_cliente, name= "crear_cliente"),
    path("lista_clientes/", lista_clientes, name= "lista_clientes"),
    path("eliminar/<int:id>", eliminar_cliente, name= "eliminar"),
     path("editar/<int:id>", editar_cliente, name= "editar"),
    path("nosotros/", nosotros, name= "nosotros"),
]
