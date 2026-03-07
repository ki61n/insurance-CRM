from django.shortcuts import render,redirect, get_object_or_404
from adminapp.models import Campain,users
from django.contrib.auth.models import User
from django.contrib import messages
from .models import client
import os
from django.http import JsonResponse


# Create your views here.
# pages 

def agentCampains(request):
    user= request.user
    data=Campain.objects.filter(agent__user=user)
    return render(request,'agent/agentCampains.html',{'data':data})

def viewAgentCampainDetails(request,id):
    data=Campain.objects.get(id=id)
    cdata=client.objects.filter(campain=data)
    return render(request,'agent/CampainDetails.html',{'data':data,'cdata':cdata})

#  Registeration page
def addClients(request,id):
    data=Campain.objects.get(id=id)
    return render(request,'agent/RegisterClients.html',{'data':data})

def editClients(request,id):
    data=get_object_or_404(client,id=id)
    return render(request,'agent/editClients.html',{'data':data})


# reg functions

def reg_Clients(request,id):
    campain=Campain.objects.get(id=id)
    agent=get_object_or_404(users,user=request.user)
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']

        phone=request.POST['phone']
        address=request.POST['address']
        profile=request.FILES.get('profile') 
        gender=request.POST['gender']
        dob=request.POST['dob']
        aadhar=request.POST['aadhar']
        pan=request.POST['pan']

        anualIncome=request.POST['anualIncome']
        marrage=request.POST['mariage']
        children=request.POST['children']
        education=request.POST['education']
        occupation=request.POST['occupation']
        otherpolicy=request.POST['otherpolicy']
        policynumber=request.POST['policyno']
        changePolicy=request.POST['changepolicy']
        clientRating=request.POST['clientRating']

        usermodel=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=email)
        usermodel.save()
        user=users(phone=phone,address=address,profile=profile,gender=gender,dob=dob,aadhar=aadhar,pan=pan,user=usermodel)
        user.save()
        Client=client(campain=campain,user=user,agent=agent,anualIncome=anualIncome,marrage=marrage,children=children,education=education,occupation=occupation,otherpolicy=otherpolicy,policynumber=policynumber,changePolicy=changePolicy,clientRating=clientRating)
        Client.save()
        messages.info(request,'client added successfully')
        return redirect('viewAgentCampainDetails',id=id)
    else:
        return redirect('addClients')



# edit functions

def edit_Clients(request,id):
    if request.method=='POST':
        data=get_object_or_404(client,id=id)
        userdata=get_object_or_404(users,id=data.user.id)
        user=get_object_or_404(User,id=userdata.user.id)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        
        userdata.phone=request.POST['phone']
        userdata.address=request.POST['address']
        userdata.gender=request.POST['gender']
        userdata.dob=request.POST['dob']
        userdata.aadhar=request.POST['aadhar']
        userdata.pan=request.POST['pan']
        img=request.FILES.get('profile')
        if img:
            if userdata.profile:
                try:
                    if os.path.exists(userdata.profile.path):
                        os.remove(userdata.profile.path)
                except ValueError:
                    pass
            userdata.profile=img
        
        
        data.anualIncome=request.POST['anualIncome']
        data.marrage=request.POST['marrage']
        data.children=request.POST['children']
        data.education=request.POST['education']
        data.occupation=request.POST['occupation']
        data.otherpolicy=request.POST['otherpolicy']
        data.policynumber=request.POST['policyno']
        data.changePolicy=request.POST['changepolicy']

        user.save()
        userdata.save()
        data.save()
        messages.info(request,'client edited successfully')
        return redirect('viewAgentCampainDetails',id=data.campain.id)
    else:
        return redirect('editClients')


# delete

def delete_Clients(request,id):
    data=get_object_or_404(client,id=id)
    user=get_object_or_404(User,id=data.user.user.id)
    user.delete()
    data.delete()
    messages.info(request,'client deleted successfully')
    return redirect('viewAgentCampainDetails',id=data.campain.id)   



# ajax 
# validation


# validations
def checkuname(request):
    uname=request.GET['username']
    user=User.objects.filter(username=uname).exists()
    return JsonResponse({'user':user})


def chackmail(request):
    email=request.GET['email']
    user=User.objects.filter(email=email).exists()
    return JsonResponse({'user':user})


def chackphone(request):
    phone=request.GET['phone']
    user=users.objects.filter(phone=phone).exists()
    return JsonResponse({'user':user})

def chackaadhar(request):
    aadhar=request.GET['aadhar']
    user=users.objects.filter(aadhar=aadhar).exists()
    return JsonResponse({'user':user})

def chackpan(request):
    pan=request.GET['pan']      
    user=users.objects.filter(pan=pan).exists()
    return JsonResponse({'user':user})

def chackpan(request):
    phone=request.GET['phone']
    user=users.objects.filter(phone=phone).exists()
    return JsonResponse({'user':user})

def echeckuname(request):
    id=request.GET.get('id')
    
    uname=request.GET['username']
    user=User.objects.filter(username=uname).exclude(id=id).exists()
    return JsonResponse({'user':user})


def echackmail(request):
    id=request.GET.get('id')    
    email=request.GET['email']
    user=User.objects.filter(email=email).exclude(id=id).exists()
    return JsonResponse({'user':user})


def echackphone(request):
    id = request.GET.get('id')
   
    phone = request.GET.get('phone')
    user = users.objects.filter(phone=phone).exclude(id=id).exists()
    return JsonResponse({'user':user})

   
def echackaadhar(request):
    id = request.GET.get('id')
   
    aadhar = request.GET.get('aadhar')
    user = users.objects.filter(aadhar=aadhar).exclude(id=id).exists()
    return JsonResponse({'user':user})

   
def echackpan(request):
    id = request.GET.get('id')
   
    pan = request.GET.get('phone')
    user = users.objects.filter(pan=pan).exclude(id=id).exists()
    return JsonResponse({'user':user})

   