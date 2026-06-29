from django.views.generic import ListView
from .models import CashFlow
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CashFlowForm


class CashFlowListView(ListView):
    model = CashFlow
    template_name = "cashflow/cashflow_list.html"
    context_object_name = "cashflows"

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = "cashflow/cashflow_form.html"
    success_url = reverse_lazy("cashflow_list")
