from django.contrib import admin

from .models import Inventory
from .models import Organism
from .models import Sample
from .models import SampleResults
from .models import SampleType
from .models import Specimen
from .models import Test


@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ("sci_name", "common_name")


@admin.register(Specimen)
class SpecimenAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "dob", "cohort")


@admin.register(SampleType)
class SampleTypeAdmin(admin.ModelAdmin):
    list_display = ("source", "description")


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ("collect_date", "type", "specimen")


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "reportable_results")


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("name", "cat_num", "lot_num", "exp", "in_use")


@admin.register(SampleResults)
class SampleResultsAdmin(admin.ModelAdmin):
    list_display = ("sample", "test", "analyst", "reagent", "date", "results")
