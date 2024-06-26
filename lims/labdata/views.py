from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import models


def homepage(request):
    organisms = models.Organism.objects.all()
    specimens = models.Specimen.objects.all()
    samples = models.Sample.objects.all()
    tests = models.Test.objects.all()
    inventory = models.Inventory.objects.all()
    sample_results = models.SampleResults.objects.all()
    return render(
        request,
        "labdata/homepage.html",
        {
            "organisms": organisms,
            "specimens": specimens,
            "samples": samples,
            "tests": tests,
            "inventories": inventory,
            "sample_results": sample_results,
            "tables": [
                "Organism",
                "Specimen",
                "Sample",
                "Test",
                "Inventory",
                "Results",
            ],
        },
    )


def confirm_delete_view(request, model_name, item_id):
    model = {
        "organism": models.Organism,
        "specimen": models.Specimen,
        "sample": models.Sample,
    }.get(
        model_name.lower(),
    )
    if not model:
        msg = "Model not found."
        raise Http404(msg)

    item = get_object_or_404(model, pk=item_id)
    item_details = {
        field.name: getattr(item, field.name)
        for field in item._meta.fields  # noqa: SLF001
    }

    if request.method == "POST":
        item.delete()
        return redirect("labdata_homepage")  # Adjust as needed

    return render(
        request,
        "labdata/confirm_delete.html",
        {
            "item_details": item_details,
            "model_name": model_name,
            "item_id": item_id,
        },
    )


def organism_detail_view(request, pk):
    organism = get_object_or_404(models.Organism, pk=pk)
    return render(request, "labdata/detail_organism.html", {"organism": organism})


def organism_form_view(request, pk=None):
    instance = get_object_or_404(models.Organism, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.OrganismForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.OrganismForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Organism" if pk else "Create New Organism",
            "button_label": "Update" if pk else "Create",
        },
    )


def specimen_detail_view(request, pk):
    specimen = get_object_or_404(models.Specimen, pk=pk)
    return render(request, "labdata/detail_specimen.html", {"specimen": specimen})


def specimen_form_view(request, pk=None):
    instance = get_object_or_404(models.Specimen, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.SpecimenForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.SpecimenForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Specimen" if pk else "Create New Specimen",
            "button_label": "Update" if pk else "Create",
        },
    )


def sampletype_detail_view(request, pk):
    sample_type = get_object_or_404(models.SampleType, pk=pk)
    return render(
        request,
        "labdata/detail_sample_type.html",
        {"sample_type": sample_type},
    )


def sampletype_form_view(request, pk=None):
    instance = get_object_or_404(models.SampleType, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.SampleTypeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.SampleTypeForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Sample Type" if pk else "Create New Sample Type",
            "button_label": "Update" if pk else "Create",
        },
    )


def sample_detail_view(request, pk):
    sample = get_object_or_404(models.Sample, pk=pk)
    return render(request, "labdata/detail_sample.html", {"sample": sample})


def sample_form_view(request, pk=None):
    instance = get_object_or_404(models.Sample, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.SampleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.SampleForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Sample" if pk else "Create New Sample",
            "button_label": "Update" if pk else "Create",
        },
    )


def test_detail_view(request, pk):
    test = get_object_or_404(models.Test, pk=pk)
    return render(request, "labdata/detail_test.html", {"test": test})


def test_form_view(request, pk=None):
    instance = get_object_or_404(models.Test, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.TestForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.TestForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Test" if pk else "Create New Test",
            "button_label": "Update" if pk else "Create",
        },
    )


def inventory_detail_view(request, pk):
    inventory_item = get_object_or_404(models.Inventory, pk=pk)
    return render(
        request,
        "labdata/detail_inventory.html",
        {"inventory": inventory_item},
    )


def inventory_form_view(request, pk=None):
    instance = get_object_or_404(models.Inventory, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.InventoryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.InventoryForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Inventory Item" if pk else "Create New Inventory Item",
            "button_label": "Update" if pk else "Create",
        },
    )


def sample_results_detail_view(request, pk):
    results = get_object_or_404(models.SampleResults, pk=pk)
    return render(
        request,
        "labdata/detail_sample_results.html",
        {"sample_result": results},
    )


def sample_results_form_view(request, pk=None):
    instance = get_object_or_404(models.SampleResults, pk=pk) if pk else None
    if request.method == "POST":
        form = forms.SampleResultsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = forms.SampleResultsForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Sample Results" if pk else "Create New Sample Results",
            "button_label": "Update" if pk else "Create",
        },
    )
