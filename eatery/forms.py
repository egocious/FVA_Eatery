from django import forms  
from eatery.models import VendorTable, AuthTable, CustomerTable, MenuTable, NotificationsTable, OrderStatus, OrderTable, MessageStatus   
class EateryForm(forms.ModelForm):  
    class Meta:  
        model =  VendorTable   
        fields = "__all__"  

