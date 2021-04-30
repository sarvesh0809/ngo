from django.db import models

# Create your models here.
class Ngoform(models.Model):
    name = models.CharField(max_length=40)
    email =models.EmailField()
    phone= models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    zipcode=models.IntegerField()
    details=models.TextField()
    aadhar = models.CharField(max_length=13,default="")
    bank_detail = models.TextField(default="")
    m1file = models.FileField(default="")
    m2file = models.FileField(default="")
    m3file = models.FileField(default="")

    def __str__(self):
        return self.name

class Validedform(models.Model):
    name = models.CharField(max_length=40)
    email =models.EmailField()
    details=models.TextField()
    bank_details=models.TextField()
    amount=models.IntegerField()
    upi=models.CharField(default="",max_length=50)
    pub_date=models.DateField()
    

    def __str__(self):
        return self.name

class AfterPayment(models.Model):
    uname = models.CharField(max_length=40)
    ufile = models.FileField()

    def __str__(self):
        return self.uname


class Contact(models.Model):
    email = models.CharField(max_length=40)
    details=models.TextField()

    def __str__(self):
        return self.email
