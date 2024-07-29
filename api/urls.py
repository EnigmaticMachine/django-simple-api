# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("import/", views.import_data, name="import_data"),
    path("detail/<str:model_name>/", views.model_list, name="model_list"),
    path("detail/<str:model_name>/<int:id>/", views.model_detail, name="model_detail"),
]
