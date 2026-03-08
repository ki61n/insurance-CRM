from django.urls import path,include
from . import views

urlpatterns = [
    # pages 

    path('agentCampains',views.agentCampains,name='agentCampains'),
    path('viewAgentCampainDetails/<int:id>',views.viewAgentCampainDetails,name='viewAgentCampainDetails'),
    path('viewAgentCampainDetails/<int:id>',views.viewAgentCampainDetails,name='viewAgentCampainDetails'),
    path('Viewe_Client/<int:id>',views.Viewe_Client,name='Viewe_Client'),
    path('Vieweprofile',views.Vieweprofile,name='Vieweprofile'),

    # client Registeration page
    path('addClients/<int:id>',views.addClients,name='addClients'),

    # edit
    path('editClients/<int:id>',views.editClients,name='editClients'),
    path('changepassword',views.changepassword,name='changepassword'),


    # register function

    path('reg_Clients/<int:id>',views.reg_Clients,name='reg_Clients'),

    # edit function

    path('edit_Clients/<int:id>',views.edit_Clients,name='edit_Clients'),
    path('edit_profile/<int:id>',views.edit_profile,name='edit_profile'),
    path('chpassword',views.chpassword,name='chpassword'),

    # delete
    path('delete_Clients/<int:id>',views.delete_Clients,name='delete_Clients'),


# ajax

 # validations
    path('checkuname',views.checkuname,name='checkuname'),
    path('chackmail',views.chackmail,name='chackmail'),
    path('chackphone',views.chackphone,name='chackphone'),
    path('chackaadhar',views.chackaadhar,name='chackaadhar'),
    path('chackpan',views.chackpan,name='chackpan'),

    path('echeckuname',views.echeckuname,name='echeckuname'),
    path('echackmail',views.echackmail,name='echackmail'),
    path('echackphone',views.echackphone,name='echackphone'), 
    path('echackaadhar',views.echackaadhar,name='echackaadhar'),
    path('echackpan',views.echackpan,name='echackpan'),
 


    
]