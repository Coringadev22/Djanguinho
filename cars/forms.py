from django import forms
from cars.models import Car, Brand

class CarForm(forms.ModelForm):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={"class": "input-field"})
    )

    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'model': forms.TextInput(attrs={"class": "input-field"}),
            'factory_year': forms.NumberInput(attrs={"class": "input-field"}),
            'model_year': forms.NumberInput(attrs={"class": "input-field"}),
            'plate': forms.TextInput(attrs={"class": "input-field"}),
            'value': forms.NumberInput(attrs={"class": "input-field"}),
            'photo': forms.ClearableFileInput(attrs={"class": "input-field"}),
        }

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value < 20000:
            self.add_error("value", "Valor mínimo deve ser maior que €20.000")
        return value

    def save(self, commit=True):
        car = super().save(commit=False)
        if commit:
            car.save()
        return car

