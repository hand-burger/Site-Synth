from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("results/", views.results, name="results"),
    path("download/<path:file_path>", views.download_static_files, name="download_static_files"),
]