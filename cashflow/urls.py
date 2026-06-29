from django.urls import path
from .views import (
    CashFlowListView,
    CashFlowCreateView,
    CashFlowUpdateView,
    CashFlowDeleteView,
    load_categories,
    load_subcategories,
)

urlpatterns = [
    path("", CashFlowListView.as_view(), name="cashflow_list"),
    path("create/", CashFlowCreateView.as_view(), name="cashflow_create"),

    path(
        "ajax/load-categories/",
        load_categories,
        name="ajax_load_categories",
    ),

    path(
        "ajax/load-subcategories/",
        load_subcategories,
        name="ajax_load_subcategories",
    ),
    path(
        "update/<int:pk>/",
        CashFlowUpdateView.as_view(),
        name="cashflow_update",
    ),

    path(
        "delete/<int:pk>/",
        CashFlowDeleteView.as_view(),
        name="cashflow_delete",
    ),
]
