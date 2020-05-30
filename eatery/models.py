from django.db import models

from datetime import datetime

# Create your models here.
class VendorTable(models.Model):
    eid =models.CharField(max_length = 10)
    businessName =models.CharField(max_length = 30, blank=False)
    email = models.EmailField(max_length = 30)
    phoneNumber =models.CharField(max_length = 30, blank=False) 
    dateTimeCreated =models.DateTimeField()#*DateField

    class Meta:
        verbose_name_plural = "Vendor"

    def __str__(self):
        return self.eid

class CustomerTable(models.Model):
    eid =models.CharField(max_length = 10)
    fistname =models.CharField(max_length = 30, blank=False)
    lastname = models.CharField(max_length = 30, blank=False)
    email = models.EmailField(max_length = 30, blank=False) 
    phoneNumber =models.CharField(max_length = 30, blank=False) 
    dateTimeCreated =models.DateTimeField(max_length = 30)#*DateField
    amountOutstanding =models.FloatField()
    class Meta:
        verbose_name_plural = "Customer"

    def __str__(self):
        return self.eid

class AuthTable(models.Model):
    eid =models.CharField(max_length = 10)
    email = models.EmailField(max_length = 30, blank=False)
    password =models.CharField(max_length = 30, blank=False) 
    dateTimeCreated =models.DateTimeField()#*DateField

    def __str__(self):
        return self.eid
    
class MenuTable(models.Model):
    eid =models.CharField(max_length = 10)
    name =models.CharField(max_length = 30)
    description = models.TextField()
    price = models.FloatField()
    quantity =models.IntegerField( blank=False) 
    dateTimeCreated =models.DateTimeField("date created", default = datetime.now())
    vendorid =models.IntegerField(blank=False)
    isRecurring =models.CharField(max_length = 10)
    frequencyOfReocurrance =models.CharField(max_length = 10)


    def __str__(self):
        return self.eid


class OrderStatus(models.Model):
    eid = models.CharField(max_length = 50)
    name =models.CharField(max_length = 70)

    def __str__(self):
        return self.eid

class OrderTable(models.Model):
    eid = models.CharField(max_length = 10)
    customerid  = models.CharField(max_length = 30, blank=True) 
    vendorid =models.ForeignKey(VendorTable, default= 1, on_delete = models.SET_DEFAULT) 
    description= models.TextField()
    itemsOrdered  =models.ForeignKey(MenuTable, default= 1, on_delete = models.SET_DEFAULT)     
    amountDue = models.FloatField()
    amountPaid  = models.FloatField()
    amountOutstanding = models.FloatField()
    orderStatus =models.ForeignKey(OrderStatus, default= 1, on_delete = models.SET_DEFAULT)     
    dateAndTimeOfOrder =models.DateField()


    def __str__(self):
        return self.eid


class MessageStatus(models.Model):
    eid = models.CharField(max_length = 30)
    name =models.CharField(max_length = 30)

    def __str__(self):
        return self.eid

class NotificationsTable(models.Model):
    eid = models.CharField(max_length = 30)
    subjectuser = models.CharField(max_length = 30)
    orderid =models.ForeignKey(VendorTable, default= 1, on_delete = models.SET_DEFAULT ) 
    orderid =models.ForeignKey(CustomerTable, default= 1, on_delete = models.SET_DEFAULT ) 
    message =models.ForeignKey(OrderTable, default= 1, on_delete = models.SET_DEFAULT)     
    dateTimeCreated = models.DateTimeField("date sent", default = datetime.now())#*DateField
    messageStatus = models.ForeignKey(MessageStatus, default= 1, on_delete = models.SET_DEFAULT)     

    def __str__(self):
        return self.eid






