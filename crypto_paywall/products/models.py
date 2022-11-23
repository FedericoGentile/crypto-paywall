from django.db import models

# Create your models here.
class Product(models.Model):
    name  = models.CharField(max_length=120)
    price = models.FloatField()

    class Meta:
        db_table = "product"

    def __str__(self):
        return f"{self.name}"