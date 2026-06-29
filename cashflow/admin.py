from django.contrib import admin

from .models import (
    OperationStatus,
    OperationType,
    Category,
    SubCategory,
    CashFlow,
)


@admin.register(OperationStatus)
class OperationStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "operation_type")
    list_filter = ("operation_type",)
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "status",
        "operation_type",
        "category",
        "subcategory",
        "amount",
    )

    list_filter = (
        "status",
        "operation_type",
        "category",
        "subcategory",
    )

    search_fields = ("comment",)
