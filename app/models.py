from django.db import models
from django.contrib.postgres.fields import ArrayField



class Item(models.Model):
    TIN = 'TN'
    PACKET = 'PT'
    SACHET = 'ST'
    PacketChoices = [
        (TIN, 'Tin'),
        (PACKET, 'Packet'),
        (SACHET, 'Sachet')
    ]

    product_name = models.CharField(max_length=50)
    extra_name = ArrayField(models.CharField(max_length=50), blank=True)
    weight_info = models.CharField(max_length=100)
    packaging_info = models.CharField(max_length=100)
    packaging_type = models.CharField(max_length =2, choices = PacketChoices)
    expired_on = models.DateField()
    is_frozen = models.BooleanField()
    active = models.BooleanField(default = True)
    created_on = models.DateTimeField(auto_now = True, editable=False)
    updated_on = models.DateTimeField(auto_now_add = True)

    class Meta:  
        db_table = "item"  


    
