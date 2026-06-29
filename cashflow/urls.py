from django.urls import path
from .views import (
    CashFlowListView,
    CashFlowCreateView,
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
]
