from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    #location = 
    emial = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)
    

