from django import forms

from .models import Organism
from .models import Specimen


class OrganismForm(forms.ModelForm):
    class Meta:
        model = Organism
        fields = "__all__"  # noqa: DJ007


class SpecimenForm(forms.ModelForm):
    class Meta:
        model = Specimen
        fields = "__all__"  # noqa: DJ007
