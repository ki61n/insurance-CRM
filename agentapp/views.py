from django.shortcuts import render,redirect, get_object_or_404
from adminapp.models import Campain,users
from django.contrib.auth.models import User
from django.contrib import messages
from .models import client
import os
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
# pages 

@login_required(login_url='signin')
def agentCampains(request):
    user= request.user
    data=Campain.objects.filter(agent__user=user)
    pdata=users.objects.get(user=request.user.id)
    print(pdata.id)
    return render(request,'agent/agentCampains.html',{'data':data,'pdata':pdata})

@login_required(login_url='signin')
def viewAgentCampainDetails(request,id):
    data=Campain.objects.get(id=id)
    cdata=client.objects.filter(campain=data)
    pdata=users.objects.get(user=request.user.id)

    return render(request,'agent/CampainDetails.html',{'data':data,'cdata':cdata,'pdata':pdata})

@login_required(login_url='signin')
def Viewe_Client(request,id):
    data=client.objects.get(id=id)
    pdata=users.objects.get(user=request.user.id)
    return render(request,'agent/Viewe_Client.html',{'data':data,'pdata':pdata})

@login_required(login_url='signin')
def Vieweprofile(request):
    pdata=users.objects.get(user=request.user.id)
    return render(request,'agent/viewprofile.html',{'data':pdata,'pdata':pdata})



#  Registeration page

@login_required(login_url='signin')
def addClients(request,id):
    data=Campain.objects.get(id=id)
    pdata=users.objects.get(user=request.user.id)

    return render(request,'agent/RegisterClients.html',{'data':data,'pdata':pdata})

@login_required(login_url='signin')
def editClients(request,id):
    data=get_object_or_404(client,id=id)
    pdata=users.objects.get(user=request.user.id)

    return render(request,'agent/editClients.html',{'data':data,'pdata':pdata})

@login_required(login_url='signin')
def changepassword(request):
    pdata=users.objects.get(user=request.user.id)

    return render(request,'agent/changepassword.html',{'pdata':pdata})

@login_required(login_url='signin')
def edit_profile(request,id):
    data=get_object_or_404(users,id=id)
    pdata=users.objects.get(user=request.user.id)

    return render(request,'agent/edit_profile.html',{'data':data,'pdata':pdata})



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
        marrage=request.POST['marrage']
        children=request.POST['children']
        education=request.POST['education']
        occupation=request.POST['occupation']
        otherpolicy=request.POST['otherpolicy']
        policynumber = None
        changePolicy = None
        if otherpolicy == 'yes':
            if 'policyno' in request.POST and 'changepolicy' in request.POST:
                policynumber=request.POST['policyno']
                changePolicy=request.POST['changepolicy']
        clientRating=request.POST['clientRating']
        if len(str(aadhar))!=12 :
            messages.info(request,'aadhar must be 12 digits')
            return redirect('addClients',id=id)
        if len(pan)!=10:
            messages.info(request,'pan must be 10 digits')
            return redirect('addClients',id=id)
        if User.objects.filter(email=email).exists():
            messages.info(request,'email already exists')
            return redirect('addClients',id=id)
        if users.objects.filter(phone=phone).exists():
            messages.info(request,'phone already exists')
            return redirect('addClients',id=id)
        if users.objects.filter(aadhar=aadhar).exists():
            messages.info(request,'aadhar already exists')
            return redirect('addClients',id=id)
        if users.objects.filter(pan=pan).exists():
            messages.info(request,'pan already exists')
            return redirect('addClients',id=id)
        else:

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
        aadhar=request.POST['aadhar']
        userdata.aadhar=aadhar
        pan=request.POST['pan']
        userdata.pan=pan
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
        otherpolicy=request.POST['otherpolicy']
        data.otherpolicy=otherpolicy
        if otherpolicy == 'yes':
            data.policynumber=request.POST['policyno']
            data.changePolicy=request.POST['changepolicy']
        else:
            data.policynumber=None
            data.changePolicy=None
        data.clientRating=request.POST['clientRating']

        if len(str(aadhar))!=12 :
            messages.info(request,'aadhar must be 12 digits')
            return redirect('editClients',id=id)
        if len(pan)!=10:
            messages.info(request,'pan must be 10 digits')
            return redirect('editClients',id=id)

        if User.objects.filter(email=request.POST['email']).exclude(id=userdata.user.id).exists():
            messages.info(request,'email already exists')
            return redirect('editClients',id=id)
        if users.objects.filter(phone=request.POST['phone']).exclude(id=userdata.id).exists():
            messages.info(request,'phone already exists')
            return redirect('editClients',id=id)
        if users.objects.filter(aadhar=request.POST['aadhar']).exclude(id=userdata.id).exists():
            messages.info(request,'aadhar already exists')
            return redirect('editClients',id=id)
        if users.objects.filter(pan=request.POST['pan']).exclude(id=userdata.id).exists():
            messages.info(request,'pan already exists')
            return redirect('editClients',id=id)
        else:

            user.save()
            userdata.save()
            data.save()
            messages.info(request,'client edited successfully')
            return redirect('viewAgentCampainDetails',id=data.campain.id)
    else:
        return redirect('editClients')




def chpassword(request):
    if request.method=='POST':
        old=request.POST['old']
        new=request.POST['new']
        con=request.POST['con']
        user=request.user

        if not check_password(old,user.password):
            messages.info(request,'old password not matched')
            return redirect('changepassword')
        else:
            if old==new:
                    messages.info(request,'old and new password are same please enter different password')
                    return redirect('changepassword')
            if len(new) < 6 or not any(i.isupper() for i in new) or not any(i in '~`!@#$%^&*)(_+-=][{|}\;:<>/?,."' for i in new) or not any(i.isdigit() for i in new):
                    messages.info(request, 'password must contain uppercase letters, numbers, special characters and minimum 6 characters')
                    return redirect('changepassword')
            else:
                if new==con:
                    user.set_password(new)
                    user.save()
                    messages.info(request,'password updated')
                    return redirect('signin')
                else:
                    messages.info(request,'password not matched')
                    return redirect('changepassword')
            

    return render(request,'changepassword.html')


# delete

def delete_Clients(request,id):
    data=get_object_or_404(client,id=id)
    user=get_object_or_404(User,id=data.user.user.id)
    user.delete()
    data.delete()
    messages.info(request,'client deleted successfully')
    if request.user.is_superuser:
        return redirect('viewCampaindetails',id=data.campain.id)
    else:
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
   
    pan = request.GET.get('pan')
    user = users.objects.filter(pan=pan).exclude(id=id).exists()
    return JsonResponse({'user':user})

def checkCampainName(request): 
    name = request.GET.get('name')
    print(name)
    user = Campain.objects.filter(name=name).exists()
    return JsonResponse({'user':user})

def echeckCampainName(request): 
    name = request.GET.get('name')
    id = request.GET.get('id')
    print(name)
    user = Campain.objects.filter(name=name).exclude(id=id).exists()
    return JsonResponse({'user':user})