from django.shortcuts import render,redirect,HttpResponse
from .models import Loan


def Application(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        mobile_number = request.POST.get('mobile_number','')
        account_number = request.POST.get('account_number','')
        city = request.POST.get('city','')
        loan_amount = request.POST.get('loan_amount','')
        reason = request.POST.get('reason','')
        x = Loan()
        x.name = name 
        x.email = email
        x.mobile_number = mobile_number
        x.account_number = account_number
        x.city = city
        x.loan_amount = loan_amount
        x.reason = reason
        if name and email and mobile_number and account_number and city and loan_amount and reason:
            a = Loan(name=name, email=email, mobile_number=mobile_number, account_number=account_number, city=city, loan_amount=loan_amount, reason=reason)
            a.save()
            return render(request,'submit.html')
        else:
            return HttpResponse("Enter All Details")
    #def success(request):
        #return render(request,'submit.html')
              
    return render(request,'index.html')
