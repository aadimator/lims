from django import forms

from . import models


class OrganismForm(forms.ModelForm):
    class Meta:
        model = models.Organism
        fields = "__all__"  # noqa: DJ007


class SpecimenForm(forms.ModelForm):
    class Meta:
        model = models.Specimen
        fields = ["organism", "specimen_id", "first_name", "last_name", "dob", "cohort"]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
        }


class SampleForm(forms.ModelForm):
    class Meta:
        model = models.Sample
        fields = "__all__"  # noqa: DJ007
        widgets = {
            "collect_date": forms.DateInput(attrs={"type": "date"}),
        }


class SampleTypeForm(forms.ModelForm):
    class Meta:
        model = models.SampleType
        fields = "__all__"  # noqa: DJ007
