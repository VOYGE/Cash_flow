from django.views.generic import ListView
from .models import CashFlow
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CashFlowForm
from django.http import JsonResponse
from .models import CashFlow, Category, SubCategory


class CashFlowListView(ListView):
    model = CashFlow
    template_name = "cashflow/cashflow_list.html"
    context_object_name = "cashflows"

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = "cashflow/cashflow_form.html"
    success_url = reverse_lazy("cashflow_list")

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
