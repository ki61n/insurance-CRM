from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    # register page
    path('registerAgents',views.registerAgents,name='registerAgents'),
    path('registerCampain',views.registerCampain,name='registerCampain'),


    # view page
    path('viewAgents',views.viewAgents,name='viewAgents'),
    path('viewCampain',views.viewCampain,name='viewCampain'),
    path('viewCampaindetails/<int:id>',views.viewCampaindetails,name='viewCampaindetails'),
    path('viewagentCampain/<int:id>',views.viewagentCampain,name='viewagentCampain'),
    path('viewClientDetails/<int:id>',views.viewClientDetails,name='viewClientDetails'),


    # edit pages

    path('editAgents/<int:id>',views.editAgents,name='editAgents'),
    path('editCampain/<int:id>',views.editCampain,name='editCampain'),


    # login

    path('login',views.signin,name='signin'),
    path('admin',views.admin,name='admin'),
    path('agent',views.agent,name='agent'),




    # reg function

    path('reg_agents',views.reg_agents,name='reg_agents'),
    path('reg_campain',views.reg_campain,name='reg_campain'),



    # edit functions
    path('edit_agents/<int:id>',views.edit_agents,name='edit_agents'),
    path('edit_campain/<int:id>',views.edit_campain,name='edit_campain'),


    #delete functions

    path('delete_agents/<int:id>',views.delete_agents,name='delete_agents'),
    path('delete_campain/<int:id>',views.delete_campain,name='delete_campain'),


    path('logout',views.out,name='out'),
    path('log',views.log,name='log'),


    
]