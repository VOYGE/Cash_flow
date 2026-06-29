from django import forms

from .models import CashFlow, Category, SubCategory


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css_class = "form-control"

            if field.widget.__class__.__name__ == "Select":
                css_class = "form-select"

            field.widget.attrs["class"] = css_class

        self.fields["category"].queryset = Category.objects.none()
        self.fields["subcategory"].queryset = SubCategory.objects.none()

        if "operation_type" in self.data:
            try:
                operation_type_id = int(self.data.get("operation_type"))
                self.fields["category"].queryset = Category.objects.filter(
                    operation_type_id=operation_type_id
                )
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields["category"].queryset = Category.objects.filter(
                operation_type=self.instance.operation_type
            )

        if "category" in self.data:
            try:
                category_id = int(self.data.get("category"))
                self.fields["subcategory"].queryset = SubCategory.objects.filter(
                    category_id=category_id
                )
            except (ValueError, TypeError):
                pass

        elif self.instance.pk:
            self.fields["subcategory"].queryset = SubCategory.objects.filter(
                category=self.instance.category
            )

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
