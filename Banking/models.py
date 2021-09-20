from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64, null=True)
    contact = models.IntegerField(default=1000000000)
    balance = models.IntegerField(default=8000)
    
    def __str__(self):
        return f"{self.name} | {self.contact} | {self.balance}"

class Transaction(models.Model):
    sender = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="credit")
    reciever = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="debit")
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.name} to {self.reciever.name} Rs{self.amount}, Status:{self.status}"