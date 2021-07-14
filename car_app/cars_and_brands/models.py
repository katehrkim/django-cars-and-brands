from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, brand_name={self.brand_name}"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, model={self.model}"
