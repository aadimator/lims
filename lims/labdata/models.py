from django.db import models

from lims.users.models import Analyst


class Organism(models.Model):
    sci_name = models.CharField(max_length=200, unique=True)
    common_name = models.CharField(max_length=200)

    def __str__(self):
        return self.common_name


class Specimen(models.Model):
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    specimen_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    dob = models.DateField(blank=True, null=True)
    cohort = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"{self.specimen_id}"


class SampleType(models.Model):
    source = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.source


class Sample(models.Model):
    collect_date = models.DateField()
    type = models.ForeignKey(SampleType, on_delete=models.SET_NULL, null=True)
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.specimen} {self.type}"


class Test(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    reportable_results = models.TextField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=200)
    cat_num = models.CharField(max_length=200)
    lot_num = models.CharField(max_length=200)
    exp = models.DateField()
    in_use = models.BooleanField()

    def __str__(self):
        return self.name


class SampleResults(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    analyst = models.ForeignKey(Analyst, on_delete=models.SET_NULL, null=True)
    reagent = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    results = models.TextField()

    def __str__(self):
        return f"{self.sample} {self.test} Results"
