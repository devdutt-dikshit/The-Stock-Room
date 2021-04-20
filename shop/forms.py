from django import forms

from .models import Products


class ProductForm(forms.ModelForm):


    class Meta:
        model=Products
        fields='__all__'
    
    # product_date=forms.DateField(
    #     widget=forms.DateInput(format='%d/%m/%y',),
    #     input_formats=('%d/%m/%y',)
    # )

    def __init__(self, *args,**kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        # self.fields['publish_date'].required= False