#importing  modules  

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from WebApp.forms import Remainder_Modelform, Web_Modelform
from WebApp.forms import Fin_Modelform
from WebApp.models import Web_Model,Remainder_Model
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from WebApp.serializers import RemSer, WebSer


# Create your views here.
# HomePage 
@login_required
def HomePage(request):
    form = Web_Modelform
    data = {'form':form}
    if request.method=='POST': #if method is POST then execute following statements
        form=Web_Modelform(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request,('Hey! You have successfully Done'))
        else:
            messages.success(request,('Hey! Form is invalid please check number'))
    return render(request,'index.html',data)


# Finance Screen 
def Fin(request):
    Fin_form=Fin_Modelform
    form_data={'Fin_form':Fin_form}
    if request.method=='POST':
        Fin_form=Fin_Modelform(request.POST)
        if Fin_form.is_valid():
           Fin_form.save()
           messages.success(request,('Hey! You have successfully Done'))
        else:
             messages.success(request,('Hey! Form is invalid please check')) 
    return render(request,'Fin.html',form_data)

# Customer report
def Form_Report(request):
    Form_data=Web_Model.objects.all() #Retreiving All Data From Web_Model(Database)
    data_Form={'Form_data':Form_data}
    return render(request,'report.html',data_Form)

# Existing Form Update
def Update(request,id):
    Form_data=Web_Model.objects.get(id=id)
    update_form=Web_Modelform(instance=Form_data)
    update_data={'update_form':update_form}
    if request.method=='POST':
        update_form=Web_Modelform(request.POST,instance=Form_data)
        if update_form.is_valid: 
           update_form.save()
           messages.success(request,('Hey! You have successfully Updated'))
        else:
             messages.success(request,('Hey! Form is invalid please check number'))
    return render(request,'update.html',update_data)

# Search Bar
def Search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        res=Web_Model.objects.filter(Name=searched) | Web_Model.objects.filter(Calling_status__contains=searched) | Web_Model.objects.filter(Current_status__contains=searched) |  Web_Model.objects.filter(Phone_Number__startswith=searched) | Web_Model.objects.filter(Current_status__contains=searched) |  Web_Model.objects.filter(Comments=searched)
        return render(request,'search.html',{'searched':searched,'result':res})

#Remainder 
def Remainder(request,id):
    m=Web_Model.objects.get(id=id)
    form=Remainder_Modelform(instance=m)
    remainder={'form':form}
    if request.method=='POST':
        remainder_form=Remainder_Modelform(request.POST)
        if remainder_form.is_valid():
            remainder_form.save()
            messages.success(request,('Hey! You have successfully Done'))
        else:
            messages.success(request,('Hey! Form is invalid please check'))

    return render(request,'remainder.html',remainder)

def Remainder_Report(request):
    Remainder_data=Remainder_Model.objects.all() #Retreiving All Data From Web_Model(Database)
    data_Form={'Remainder_data':Remainder_data}
    return render(request,'remainder_report.html',data_Form)

def Remainder_Update(request,id):
    form_remainder=Remainder_Model.objects.get(id=id)
    update_form=Remainder_Modelform(instance=form_remainder)
    update_data={'update_form':update_form}
    if request.method=='POST':
        remainder_form=Remainder_Modelform(request.POST,instance=form_remainder)
        if remainder_form.is_valid: 
           remainder_form.save()
           messages.success(request,('Hey! You have successfully Updated'))  
        else:
            messages.success(request,('Hey! Form is already existed!'))
    return render(request,'remainder_update.html',update_data)

def login_user(request):

    if request.method=='POST':
        Name = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=Name, password=password)
        if user is not None:
            login(request, user)
            return redirect(HomePage)
        else:
            messages.success(request,('Hey! You entered invalid Name or Password'))
            return render(request,'login.html')
           
    else:
        return render(request,'login.html',{})
def Sign_up(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password_2=request.POST['Re_password']
        email=request.POST['email']
        if password==password_2:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            messages.success(request,('Hey! You have sign-up successfully'))
            return redirect('/')
        else:
            messages.success(request,('Hey! you entered wrong credentials or password miss match'))
            return render(request,'sign_up.html',)
        

    else:
        return render(request,'sign_up.html',)


from rest_framework.views import APIView
from rest_framework.response import Response
class Web_Ser(APIView):
    def get(request,self):
        s=Web_Model.objects.all()
        m=Remainder_Model.objects.all()
        Ser=WebSer(s,many=True)
        Ser2=RemSer(m,many=True)
        return Response([Ser.data,Ser2.data])