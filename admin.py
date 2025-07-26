from django.contrib import admin
from .models import Customer
from .models import CustomerReview

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'loan_amount', 'interest_rate', 'loan_date', 'interest_amount', 'total_amount']

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'message', 'created_at')
