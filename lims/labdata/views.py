from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from .forms import OrganismForm
from .forms import SpecimenForm
from .models import Organism
from .models import Specimen


def homepage(request):
    organisms = Organism.objects.all()
    specimens = Specimen.objects.all()
    return render(
        request,
        "labdata/homepage.html",
        {
            "organisms": organisms,
            "specimens": specimens,
            "tables": ["Organism", "Specimen"],
        },
    )


def confirm_delete_view(request, model_name, item_id):
    model = {"organism": Organism, "specimen": Specimen}.get(model_name.lower())
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
    organism = get_object_or_404(Organism, pk=pk)
    return render(request, "labdata/detail_organism.html", {"organism": organism})


def organism_form_view(request, pk=None):
    instance = get_object_or_404(Organism, pk=pk) if pk else None
    if request.method == "POST":
        form = OrganismForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = OrganismForm(instance=instance)
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
    specimen = get_object_or_404(Specimen, pk=pk)
    return render(request, "labdata/detail_specimen.html", {"specimen": specimen})


def specimen_form_view(request, pk=None):
    instance = get_object_or_404(Specimen, pk=pk) if pk else None
    if request.method == "POST":
        form = SpecimenForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse("labdata_homepage"))  # Adjust as needed
    else:
        form = SpecimenForm(instance=instance)
    return render(
        request,
        "labdata/form_template.html",
        {
            "form": form,
            "title": "Edit Specimen" if pk else "Create New Specimen",
            "button_label": "Update" if pk else "Create",
        },
    )
