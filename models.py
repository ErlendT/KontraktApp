from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contract(models.Model):
    title = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, default = 1, on_delete=models.SET_DEFAULT, related_name='Contract_Created_By_User_FK')
    creation_date = models.DateTimeField('creation date')
    edited_by = models.ForeignKey(User, default = 1, on_delete=models.SET_DEFAULT, related_name='Contract_Edited_By_User_FK')
    edited_date = models.DateTimeField('edited date')
    #cover_image = models.ForeignKey(CoverImage)

    def __str__(self):
        return self.title

class NSCategory(models.Model):
    ns_number = models.IntegerField()
    name = models.CharField(max_length=200)
    parent_category = models.ForeignKey('self', on_delete=models.PROTECT)

    def __str__(self):
        return (self.ns_number + " " + self.name)

class Job(models.Model):
    default_description = models.CharField(max_length=200)
    default_price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    default_time = models.DecimalField(max_digits=5, decimal_places=2)
    ns_number = models.IntegerField()
    NSCategory = models.ForeignKey(NSCategory, on_delete= models.PROTECT)

    def __str__(self):
        return (self.ns_number + " " + self.name)

class ContractItem(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    custom_description = models.CharField(max_length=200)
    custom_price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)
    custom_time = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return (self.contract + " " + self.job)