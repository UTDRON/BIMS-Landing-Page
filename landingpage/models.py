from django.db import models
from django.utils.translation import ugettext_lazy


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    industry_name=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    address=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=20)
    otp=models.CharField(max_length=10,default="")

    def __str__(self):
        return self.name+str(self.id)

class ContactAndOTP(models.Model):
    contact_no=models.CharField(max_length=20)
    otp=models.CharField(max_length=10)

    