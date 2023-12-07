from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .froms import ClienteFormulario
from .models import Cliente


# Create your views here.

def home(request):
    return render(request, "core/home.html")

def nosotros(request):
    return render(request, "core/nosotros.html")


def productos(request):
    return render(request, "core/productos.html")


def exit(request):
    logout(request)
    return redirect('core/home.html')

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()

    return render(request, "core/lista_clientes.html", {"clientes" : clientes } )


def crea_cliente(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            modelo = Cliente(
                          nombre=data["nombre"],
                          apellido=data["apellido"],
                          fecha=data["fecha"],
                          email=data["email"],
                          telefono=data["telefono"],
                          )
            modelo.save()
            return redirect("home")
        return render(request, "core/crear_cliente.html", {"miFormulario": miFormulario})

    else:
        miFormulario = ClienteFormulario()

        return render(request, "core/crear_cliente.html", {"miFormulario": miFormulario})



def eliminar_cliente(request,id):
   
   if request.method == "POST":
       
    clientes = Cliente.objects.get(id=id)
    clientes.delete()

    clientes = Cliente.objects.all()
    return redirect("lista_clientes")
   else:
    return render(request,"core/lista_cliente.html", {"lista_clientes": clientes} )




def editar_cliente(request, id):
    
    if request.method == "POST":
     miFormulario = ClienteFormulario(request.POST)

     if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            cliente = Cliente.objects.get(id=id)
            cliente.nombre = data["nombre"]
            cliente.apellido = data["apellido"]
            cliente.fecha = data["fecha"]
            cliente.email = data["email"]
            cliente.telefono = data["telefono"]
            
            cliente.save()


            return redirect("home")
        
     return render(request, "core/editar_cliente.html", {"miFormulario": miFormulario})

    else:
       miFormulario = ClienteFormulario(
           initial={"nombre": Cliente.nombre,
                    "apellido": Cliente.apellido,
                    "fecha": Cliente.fecha,
                    "email": Cliente.email,
                    "telefono": Cliente.telefono,
                    }

           )
        
    return render(request, "core/editar_cliente.html", {"miFormulario": miFormulario, "id": cliente.id})






















# {% extends 'core/base.html' %}


# {% block contenido %}




#     {% if request.user.is_authenticated  %}
#     <hr>
#     <h4>

#         {{user.username | upper}}, Bienvenido!

#     </h4>
# {% endif %}


# {% endblock contenido %}



