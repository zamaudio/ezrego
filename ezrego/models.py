from django.contrib.auth.models import User as AuthUser
from django.db import models

class Vehicle(models.Model):
    current_rego = models.CharField(max_length=6)
    rego_expiry = models.DateField()
    vehicle_year = models.IntegerField()
    vehicle_make = models.CharField(max_length=32)
    vehicle_model = models.CharField(max_length=32)
    vehicle_bodytype = models.CharField(max_length=32)
    vehicle_vin = models.CharField(max_length=17)
    is_pre1989 = models.BooleanField(default=False)
    is_written_off = models.BooleanField(default=False)
    is_rwc_attached = models.BooleanField(default=False)
    rwc_serialnumber = models.CharField(max_length=7)
    rwc_issuedate = models.DateField()
    rwc_testerlicence = models.CharField(max_length=10)
    def __str__(self):
        return (self.vehicle_vin)

class Person(models.Model):
    user_auth = models.ForeignKey(AuthUser)
    personalorbusiness = models.BooleanField(default=False)
    surname = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    companyname = models.CharField(max_length=32)
    acn = models.CharField(max_length=9)
    licencenumber = models.CharField(max_length=10)
    dob = models.DateField()
    homeaddress1 = models.CharField(max_length=64)
    homeaddress2 = models.CharField(max_length=64)
    homeaddresspostcode = models.IntegerField()
    postaladdress1 = models.CharField(max_length=64)
    postaladdress2 = models.CharField(max_length=64)
    postaladdresspostcode = models.IntegerField()
    garageaddress1 = models.CharField(max_length=64)
    garageaddress2 = models.CharField(max_length=64)
    garageaddresspostcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return (self.phone)

class VehicleTransfer(models.Model):
    seller = models.ForeignKey(Person)
    buyer = models.ForeignKey(Person, related_name='buyer')
    vehicle = models.ForeignKey(Vehicle)
    submitted_timestamp = models.DateTimeField(auto_now_add=True)
    market_value = models.IntegerField()
    date_of_sale = models.DateField()
    transfer_fee = models.IntegerField()
    duty_fee = models.IntegerField()
    def __str__(self):
        return (self.date_of_sale)


