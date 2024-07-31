from django.urls import path
from .views import (
    ImportDataView,
    ModelDetailListView,
    ModelDetailView,
)

urlpatterns = [
    path("import/", ImportDataView.as_view(), name="import_data"),
    path(
        "detail/<str:model_name>/",
        ModelDetailListView.as_view(),
        name="model_detail_list",
    ),
    path(
        "detail/<str:model_name>/<int:pk>/",
        ModelDetailView.as_view(),
        name="model_detail",
    ),
]
