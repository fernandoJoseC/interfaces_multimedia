
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

class reservaFormulario(forms.ModelForm):
	class Meta:
		fields=[
			'fechaReserva',
			'emprendimiento',
			'cantidad',
			'valor'
		]

		labels={
			'fechaReserva':'Fecha de la reservacion',
			'emprendimiento':'Emprendimiento',
			'cantidad':'Cantidad del producto',
			'valor':'Costo'
		}
		widgets={
			'fechaReserva':forms.DateInput(format=('%d-%m-%y'),attrs={'type':'date'})
		}

