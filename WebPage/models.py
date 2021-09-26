from django.db import models

# Create your models here.
class Staff(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=False)
    Position = models.CharField(max_length=100, null=True, blank=False)
    Phone = models.PositiveIntegerField(null=True, blank=False)
    Description = models.TextField(max_length=2000, null=True, blank=False)
    Email = models.EmailField(blank=True)

    def __str__(self):
        return self.Name

class GatedGuarded(models.Model):
    BuildingName = models.CharField(max_length=100, null=True, blank=False)
    Image = models.ImageField()

    def __str__(self):
        return self.BuildingName

class HighRise(models.Model):
    BuildingName = models.CharField(max_length=100, null=True, blank=False)
    Image = models.ImageField()

    def __str__(self):
        return self.BuildingName

class Complex(models.Model):
    BuildingName = models.CharField(max_length=100, null=True, blank=False)
    Image = models.ImageField()

    def __str__(self):
        return self.BuildingName

class OurService(models.Model):
    ServiceName = models.CharField(max_length=100, null=True, blank=False)
    Image = models.ImageField()

    def __str__(self):
        return self.ServiceName