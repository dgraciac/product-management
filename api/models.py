from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
