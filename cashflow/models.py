from django.db import models
from django.utils import timezone


class OperationStatus(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        ordering = ["name"]

    def __str__(self):
        return self.name

class OperationType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )

    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Тип операции"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
        unique_together = ("name", "operation_type")

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ["name"]
        unique_together = ("name", "category")

    def __str__(self):
        return self.name

class CashFlow(models.Model):
    created_at = models.DateField(
        default=timezone.now,
        verbose_name="Дата создания"
    )

    status = models.ForeignKey(
        OperationStatus,
        on_delete=models.PROTECT,
        verbose_name="Статус"
    )

    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.PROTECT,
        verbose_name="Тип операции"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория"
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        verbose_name="Подкатегория"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма"
    )

    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий"
    )

    class Meta:
        verbose_name = "Операция ДДС"
        verbose_name_plural = "Операции ДДС"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.created_at} | "
            f"{self.operation_type} | "
            f"{self.category} | "
            f"{self.amount} ₽"
        )