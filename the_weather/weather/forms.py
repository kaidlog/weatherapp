from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta(object):
        """docstring forMeta."""
        model = City
        fields = ["name"]

        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
