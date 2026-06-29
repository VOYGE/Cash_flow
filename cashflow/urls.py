from django.urls import path
from .views import CashFlowCreateView, CashFlowListView

urlpatterns = [
    path("", CashFlowListView.as_view(), name="cashflow_list"),
    path("create/", CashFlowCreateView.as_view(), name="cashflow_create"),
]
