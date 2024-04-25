from django import forms

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'current_version':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'


class ProductForm(StyleMixin, forms.ModelForm):

    __forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for name in self.__forbidden_words:
            if name in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещенное слово "{name}" в наименовании товара')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for word in self.__forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещенное слово "{word}" в описании товара')
        return cleaned_data


class VersionForm(StyleMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def clean_current_version(self):

        cleaned_data = self.cleaned_data.get('current_version')

        # if cleaned_data:
        #     raise forms.ValidationError('Текущая версия должна быть одна!')
        return cleaned_data