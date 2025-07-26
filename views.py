from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from .models import CustomerReview
from datetime import date

def home(request):
    return render(request, 'home.html') 

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # ✅ केवल admin को login करने देना
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')  # admin dashboard वाला page
        else:
            messages.error(request, 'Username/password गलत है या आप admin नहीं हैं।')

    return render(request, 'login.html')

@login_required(login_url='/login/')
def admin_dashboard(request):
    customers = Customer.objects.all()  # Fetch all customers
    return render(request, 'admin_dashboard.html', {'customers': customers})  

@login_required(login_url='/login/')
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

@login_required(login_url='/login/')
def customer_list(request):
    customers = Customer.objects.all()
    for customer in customers:
        days = (date.today() - customer.loan_date).days
        customer.days_since_loan = days
        if days <= 30:
            customer.status_color = 'blue'
            customer.status_label = 'Active'
        elif days <= 45:
            customer.status_color = 'green'
            customer.status_label = 'Pending'
        elif days <= 60:
            customer.status_color = 'yellow'
            customer.status_label = 'DueSoon'
        else:
            customer.status_color = 'red'
            customer.status_label = 'OverDue'
    return render(request, 'customer_list.html', {'customers': customers})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customer_list')

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # after successful add
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def review_list(request):
    reviews = CustomerReview.objects.order_by('-created_at')
    return render(request, 'review_list.html', {'reviews': reviews})


def logout_view(request):
    logout(request)
    return redirect('/admin/')

def about(request):
    return render(request, 'about.html')

def loanplan(request):
    return render(request, 'loanplan.html')

def calculator(request):
    return render(request, 'calculator.html')

def contact(request):
    return render(request, 'contact.html')

def apply(request):
    return render(request, 'apply.html')

def apply2(request):
    return render(request, 'apply2.html')

def review(request):
    return render(request, 'review.html')