from django import forms

from .models import CashFlow


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = [
            "created_at",
            "status",
            "operation_type",
            "category",
            "subcategory",
            "amount",
            "comment",
        ]

        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"}),
            "comment": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned_data = super().clean()

        operation_type = cleaned_data.get("operation_type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        if (
                operation_type
                and category
                and category.operation_type != operation_type
        ):
            self.add_error(
                "category",
                "Категория не относится к выбранному типу операции."
            )

        if (
                category
                and subcategory
                and subcategory.category != category
        ):
            self.add_error(
                "subcategory",
                "Подкатегория не относится к выбранной категории."
            )

        return cleaned_data
