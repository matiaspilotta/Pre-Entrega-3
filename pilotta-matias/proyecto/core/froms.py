from django import forms
from .models import Cliente


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    telefono = forms.CharField(max_length=50)



# class BuscarCliente(forms.Form):
#      nombre = forms.CharField(max_length=30)


#class EditarCliente(forms.form):
   # pass







# class FormularioRegistro(forms.Form):
#   from django import forms