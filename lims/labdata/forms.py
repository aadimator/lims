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
        fields = ["organism", "specimen_id", "first_name", "last_name", "dob", "cohort"]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
        }
