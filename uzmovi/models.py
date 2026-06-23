from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    
class Narsalar(models.Model):
    nomi = models.CharField(max_length=100,null=True)
    narxi = models.IntegerField( null=True)

    def __str__(self):
        return self.nomi