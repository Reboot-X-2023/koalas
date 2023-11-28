from django.db import models

# Create your models here.

class User_data(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    balance = models.FloatField()
    third_party_name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)

    def __str__(self):
        return self.user_data_text




