from django.db import models
from datetime import date


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_date = models.DateField(default=date.today)

    @property
    def interest_amount(self):
        return (self.loan_amount * self.interest_rate) / 100

    @property
    def total_amount(self):
        return self.loan_amount + self.interest_amount

    def __str__(self):
        return self.name


class CustomerReview(models.Model):
    customer_name = models.CharField(max_length=100)
    message = models.TextField()
    proof_image = models.ImageField(upload_to='review_proofs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
