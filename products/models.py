from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=255, unique=True)
    description = models.TextField(null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.URLField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
