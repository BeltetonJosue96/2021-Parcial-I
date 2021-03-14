from django import forms

from Models.Productos.models import Marca, Categoria, Producto


class FormMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        marca = forms.ModelChoiceField(
            queryset=Marca.objects.all(),
            label='marca',
            widget=forms.Select
        )
        fields = '__all__'
        widgets = {'fechaingreso': forms.DateInput(attrs={'type': 'date'})}
