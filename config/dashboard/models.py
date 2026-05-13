from django.db import models

# Create your models here.
class Clients(models.Model):
    GENDER_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    phone_number = models.CharField(max_length=13, null=False)
    gender = models.CharField(choices=GENDER_CHOICES, null=False)
    mfy = models.CharField(max_length=255, null=False)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('registered_at',)

class ServicesType(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Services(models.Model):
    service_name = models.ForeignKey(ServicesType, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)