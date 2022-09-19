from django.db import models

# Create your models here.
class Details(models.Model):
    balance = models.CharField(max_length=500)
    transactions = models.CharField(max_length=500)
    total_sent = models.CharField(max_length=500)
    total_received = models.CharField(max_length=500)
    sender_private_key = models.CharField(max_length=500)
    public_key = models.CharField(max_length=500)
    sender_address = models.CharField(max_length=500)
    receiver_address = models.CharField(max_length=500)
    balance_usd = models.CharField(max_length=500)
    total_sent_usd = models.CharField(max_length=500)
    total_received_usd = models.CharField(max_length=500)