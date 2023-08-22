from django.db import models

class Loan(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    account_number = models.CharField(max_length=25)
    loan_amount = models.DecimalField(max_digits= 10, decimal_places=2)
    reason = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    

