from django.shortcuts import render
from .models import user_details,user_reg
# Create your views here.
def home(request):
    if request.method == 'POST':
        email=request.POST['user_email']
        Password=request.POST['pass']
        user=user_details(email=email,password=Password)
        user.save()

        Name=request.POST['username']
        Email=request.POST['user_email']
        reg_pass=request.POST['pass']
        new_user_reg=user_reg(name=Name,email=Email,password=reg_pass)
        new_user_reg.save()


  

    return render(request,'home.html')
def books(request):
    return render(request,'books.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')