import django_filters

from .models import CashFlow
from django import forms


class CashFlowFilter(django_filters.FilterSet):
    created_at_after = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="gte",
        label="Дата с",
    )

    created_at_before = django_filters.DateFilter(
        field_name="created_at",
        lookup_expr="lte",
        label="Дата по",
    )

    class Meta:
        model = CashFlow
        fields = [
            "status",
            "operation_type",
            "category",
            "subcategory",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.form.fields.values():

            if isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"
            else:
                field.widget.attrs["class"] = "form-control"