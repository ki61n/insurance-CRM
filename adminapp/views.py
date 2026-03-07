from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import users,Campain
from agentapp.models import client
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from django.db.models import Q
import random
import string
import os

# Create your views here.

# path page


def home(request):
    return render(request,'home.html')



# register page

def registerAgents(request):
    return render(request,'admin/register_agent.html')

def registerCampain(request):
    agent=users.objects.filter(user__is_staff = True).exclude(user__is_superuser = True)
    return render(request,'admin/reg_campain.html',{'agent':agent})


# view page
def viewAgents(request):
    data=users.objects.filter(user__is_staff = True).exclude(user__is_superuser = True)
    return render(request,'admin/view_agents.html',{'data':data})

def viewCampain(request):
    data=Campain.objects.all()
    return render(request,'admin/view_campains.html',{'data':data})


def viewCampaindetails(request,id):
    data=Campain.objects.get(id=id)
    cdata=client.objects.filter(campain=data)
    return render(request,'admin/viewCampaindetails.html',{'data':data,'cdata':cdata})



# edit page


def editAgents(request,id):
    data=get_object_or_404(users,id=id)

    return render(request,'admin/edit_agent.html',{'data':data})

def editCampain(request,id):
    data=get_object_or_404(Campain,id=id)
    agent=users.objects.filter(user__is_staff = True).exclude(user__is_superuser = True)
    return render(request,'admin/edit_campain.html',{'data':data,'agent':agent})


# login

def signin(request):
    return render(request,'login.html') 


def admin(request):
    return render(request,'admin/admin.html')


def agent(request):
    return render(request,'agent/agent.html')





# reg function
def reg_agents(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        profile=request.FILES.get('profile')


        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special=random.choice(string.punctuation)
        others = "".join(random.choices(string.ascii_letters + string.digits, k=4))
        pass1 = "".join(random.sample(upper + special + digit + others, 7))

        user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1,is_staff=True)
        user.save()

        data=users.objects.create(user=user,phone=phone,address=address,profile=profile)
        data.save()

        send_mail("confidential Email",
                  f"""This email contains confidential information.please dont share it with anyone.
                    Dear {uname} you are now an agent 
                    use this password for login {pass1}""",
                  settings.EMAIL_HOST_USER,
                  [email]
                     )
        messages.info(request,'Agent added successfully')
        return redirect('viewAgents')
    else:
        return redirect('registerAgents')

def reg_campain(request):
    if request.method=='POST':
        name=request.POST['name']
        place=request.POST['place']
        date=request.POST['date']
        time=request.POST['time']
        image=request.FILES.get('image')
        agentid=request.POST['agent']
        agent=get_object_or_404(users,id=agentid)
        data=Campain.objects.create(name=name,place=place,date=date,time=time,image=image,agent=agent)
        data.save()
        messages.info(request,'Campain added successfully')

        return redirect('viewCampain')
    else:
        return redirect('registerCampain')
        




# edit functions

def edit_agents(request,id):
    if request.method=='POST':
        userdata=get_object_or_404(users,id=id)
        user=get_object_or_404(User,id=userdata.user.id)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.username=request.POST['uname']
        user.email=request.POST['email']
        
        userdata.phone=request.POST['phone']
        userdata.address=request.POST['address']
        img=request.FILES.get('profile')
        if os.path.exists(userdata.profile.path):
            os.remove(userdata.profile.path)
        if img: 
            userdata.profile=img


        user.save()
        userdata.save()
        messages.info(request,'Agent edited successfully')

        return redirect('viewAgents')
    else:
        return redirect('editAgents')
    


def edit_campain(request,id):
    if request.method=='POST':
        data=get_object_or_404(Campain,id=id)
        data.name=request.POST['name']
        data.place=request.POST['place']
        data.date=request.POST['date']
        data.time=request.POST['time']  
        img=request.FILES.get('image')
        if os.path.exists(data.image.path):
            os.remove(data.image.path)
        if img: 
            data.image=img
        agentid=request.POST['agent']
        agent=get_object_or_404(users,id=agentid)
        data.agent=agent
        
        data.save()
        messages.info(request,'Campain edited successfully')

        return redirect('viewCampain')
    else:
        return redirect('editCampain')







def delete_agents(request,id):
    data=get_object_or_404(users,id=id)
    user=get_object_or_404(User,id=data.user.id)
    campain=Campain.objects.filter(agent=data)
    for i in campain:
        i.agent=None
        i.save()
    user.delete()
    data.delete()
    messages.info(request,'Agent deleted successfully')
    return redirect('viewAgents')

def delete_campain(request,id):
    data=get_object_or_404(Campain,id=id)

    data.delete()
    messages.info(request,'Campain deleted successfully')
    return redirect('viewCampain')
    


def out(request):
    logout(request)
    return redirect('signin')

def log(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print('true')
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('admin')
            else:
                login(request,user)
                return redirect('agent')
        else:
            messages.info(request,'invalid username or password')
            return redirect('signin')
    
    return redirect('signin')
    

