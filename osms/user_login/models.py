from django.db import models
from django.contrib.auth.models import User



#student information table
class UserInfo(models.Model):
    name = models.CharField(max_length = 100, blank=True, null=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    password = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name