from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)
    def __unicode__(self):
        return self.title
