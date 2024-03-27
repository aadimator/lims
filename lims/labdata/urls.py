from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="labdata_homepage"),
    path(
        "delete/<str:model_name>/<int:item_id>/",
        views.confirm_delete_view,
        name="confirm_delete",
    ),
    path("organism/", views.organism_form_view, name="create_organism"),
    path(
        "organism/detail/<int:pk>/",
        views.organism_detail_view,
        name="detail_organism",
    ),
    path("organism/<int:pk>/", views.organism_form_view, name="update_organism"),
    path("specimen/", views.specimen_form_view, name="create_specimen"),
    path(
        "specimen/detail/<int:pk>/",
        views.specimen_detail_view,
        name="detail_specimen",
    ),
    path("specimen/<int:pk>/", views.specimen_form_view, name="update_specimen"),
    path("sampletype/", views.sampletype_form_view, name="create_sampletype"),
    path(
        "sampletype/detail/<int:pk>/",
        views.sampletype_detail_view,
        name="detail_sampletype",
    ),
    path(
        "sampletype/<int:pk>/",
        views.sampletype_form_view,
        name="update_sampletype",
    ),
    path("sample/", views.sample_form_view, name="create_sample"),
    path(
        "sample/detail/<int:pk>/",
        views.sample_detail_view,
        name="detail_sample",
    ),
    path("sample/<int:pk>/", views.sample_form_view, name="update_sample"),
]
