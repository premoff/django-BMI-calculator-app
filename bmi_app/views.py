from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'bmi_app/home.html',{})
    

def bmi_result(request):
    height=float(request.POST.get('height', False))/100 #centimeter to meter 
    weight=float(request.POST.get('weight', False))
    BMI = weight/(height*height)
    height = 'Your Height = ' + str(height) + 'm' 
    weight = 'Your Weight = ' + str(weight) + 'kg' 
    BMI = f'Your BMI = {BMI:.2f}' 
   
    return render(request,'bmi_app/bmi_result.html',{'height':height,'weight':weight,'BMI':BMI})