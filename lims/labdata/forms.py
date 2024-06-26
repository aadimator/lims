from django import forms

from . import models


class OrganismForm(forms.ModelForm):
    class Meta:
        model = models.Organism
        fields = "__all__"  # noqa: DJ007


class SpecimenForm(forms.ModelForm):
    class Meta:
        model = models.Specimen
        fields = [
            "organism",
            "specimen_id",
            "first_name",
            "last_name",
            "dob",
            "cohort",
            "gender",
            "race",
        ]
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


class TestForm(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = "__all__"  # noqa: DJ007


class InventoryForm(forms.ModelForm):
    class Meta:
        model = models.Inventory
        fields = "__all__"  # noqa: DJ007
        widgets = {
            "exp": forms.DateInput(attrs={"type": "date"}),
        }


class SampleResultsForm(forms.ModelForm):
    class Meta:
        model = models.SampleResults
        fields = "__all__"  # noqa: DJ007
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
