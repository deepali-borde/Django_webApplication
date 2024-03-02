from django.db import models


# model define a our database
#makemigration- create changes and stored in a file
#migrate - apply the pending changes created by make migration

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    desc = models.TextField(max_length=255)
    date = models.DateField()


    def __str__(self):
        return self.name
    