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
    path("test/", views.test_form_view, name="create_test"),
    path("test/detail/<int:pk>/", views.test_detail_view, name="detail_test"),
    path("test/<int:pk>/", views.test_form_view, name="update_test"),
    path("inventory/", views.inventory_form_view, name="create_inventory"),
    path(
        "inventory/detail/<int:pk>/",
        views.inventory_detail_view,
        name="detail_inventory",
    ),
    path("inventory/<int:pk>/", views.inventory_form_view, name="update_inventory"),
    path(
        "sample_results/",
        views.sample_results_form_view,
        name="create_sample_results",
    ),
    path(
        "sample_results/detail/<int:pk>/",
        views.sample_results_detail_view,
        name="detail_sample_results",
    ),
    path(
        "sample_results/<int:pk>/",
        views.sample_results_form_view,
        name="update_sample_results",
    ),
]
