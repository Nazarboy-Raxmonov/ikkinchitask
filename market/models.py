from django.db import models

class redmi(models.Model):
    model = models.TextField(max_length=25),
    year = models.IntegerField()

    def __str__(self) -> str:
        return self.model
    
    class Meta:
        db_table = 'redmi'

class iphone(models.Model):
    model = models.TextField(max_length=25),
    country = models.TextField(max_length=25)

    def __str__(self) -> str:
        return self.model
    
    class Meta:
        db_table = 'iphone'
