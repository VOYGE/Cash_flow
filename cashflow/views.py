from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .forms import CashFlowForm
from django.http import JsonResponse
from .models import CashFlow, Category, SubCategory
from .filters import CashFlowFilter
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class CashFlowListView(ListView):
    model = CashFlow
    template_name = "cashflow/cashflow_list.html"
    context_object_name = "cashflows"

    def get_queryset(self):
        self.filterset = CashFlowFilter(
            self.request.GET,
            queryset=CashFlow.objects.select_related(
                "status",
                "operation_type",
                "category",
                "subcategory",
            ),
        )

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = "cashflow/cashflow_form.html"
    success_url = reverse_lazy("cashflow_list")
    success_message = "Запись успешно создана."

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = "cashflow/cashflow_form.html"
    success_url = reverse_lazy("cashflow_list")
    success_message = "Запись успешно обновлена."

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = "cashflow/cashflow_confirm_delete.html"
    success_url = reverse_lazy("cashflow_list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно удалена.")
        return super().form_valid(form)

def load_categories(request):
    operation_type_id = request.GET.get("operation_type")

    categories = Category.objects.filter(
        operation_type_id=operation_type_id
    ).values("id", "name")

    return JsonResponse(list(categories), safe=False)


def load_subcategories(request):
    category_id = request.GET.get("category")

    subcategories = SubCategory.objects.filter(
        category_id=category_id
    ).values("id", "name")

    return JsonResponse(list(subcategories), safe=False)
