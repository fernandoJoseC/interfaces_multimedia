
# import the standard Django Forms
# from built-in library
from django import forms

# creating a form
class reservasForm(forms.Form):

    fechaLlegada = forms.DateField()
    fechaSalida = forms.DateField()
    numPersonas = forms.IntegerField()
    descripcion = forms.CharField(max_length=500)
    #add tipo de productos a comprar para reservarlos
    #productos = forms.ManyToManyField(Productos)

