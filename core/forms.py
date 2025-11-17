from django import forms
from core.models import Supplier, Product, Brand, Category


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'ruc', 'address', 'phone', 'state']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'description',
            'cost',
            'price',
            'stock',
            'iva',
            'expiration_date',
            'brand',
            'supplier',
            'categories',
            'line',
            'image'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aplicamos estilos de Bootstrap a todos los campos
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        # Personalizamos campos específicos
        self.fields['brand'].widget.attrs.update({'class': 'form-select'})
        self.fields['supplier'].widget.attrs.update({'class': 'form-select'})
        self.fields['categories'].widget.attrs.update(
            {'class': 'form-select', 'multiple': 'multiple'})
        self.fields['iva'].widget.attrs.update({'class': 'form-select'})
        self.fields['line'].widget.attrs.update({'class': 'form-select'})

        self.fields['expiration_date'].widget = forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )

        # Filtramos para mostrar solo marcas y proveedores activos
        self.fields['brand'].queryset = Brand.active_brands.all()
        self.fields['supplier'].queryset = Supplier.objects.filter(state=True)
        self.fields['categories'].queryset = Category.objects.filter(
            state=True)
