from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default="images/default.jpeg")

    def __unicode__(self):
        return self.name
