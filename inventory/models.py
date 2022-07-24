from django.db import models

PriceField = lambda **options: models.DecimalField(
    max_digits=10,
    decimal_places=2,
    null=options.pop("null", False),
    default=options.pop("default", 0),

    **options,
)

class Inventory(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=75, blank=False, null=False
    )
    quantity = models.IntegerField(blank=False, default=1)
    price = PriceField()
    measure_unit = models.CharField(
        max_length=10,
        default='',
        blank=True,
        null=False
    )

    category_name = models.CharField(
        max_length=75, blank=True, null=True
    )

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.name