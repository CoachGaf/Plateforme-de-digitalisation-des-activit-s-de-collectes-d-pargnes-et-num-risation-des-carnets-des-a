from django.contrib.auth.forms import AuthenticationForm
from django.urls import path

from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views 
urlpatterns = [
    
    path('profile/', views.profile, name='profile'),
    path('profileadherent/', views.profileAdherent, name='profileadherent'),
    path('profileagent/', views.profileAgent, name='profileagent'),
    path('historique/', views.historique, name='historique'),
    path('list_payments/', views.list_payments, name='list_payments'),
    path('accueil/', views.index, name='index'),
    path('contact_agent/', views.contact_agent, name='contact_agent'),
    path('notification/', views.notification, name='notification'),
    path('agents/', views.agents, name='agents'),
    path('mes_carnets/', views.mes_carnets, name='mes_carnets'),

    path('ajouter_agents/', views.ajouter_agents, name='ajouter_agents'),
    path('adhérents/', views.adhérents, name='adhérents'),
    path('ajouter_adhérents/', views.ajouter_adhérents, name='ajouter_adhérents'),
    path('produits/', views.produits, name='produits'),
    path('rapport_paiement/', views.rapport_paiement, name='rapport_paiement'),
    path('rapport_revenu/', views.rapport_revenu, name='rapport_revenu'),
    path('rapport_paiement/', views.rapport_paiement, name='rapport_paiement'),
    path('reçus/', views.reçus, name='reçus'),
    path('faq/', views.faq, name='faq'),
    path('update_fiche/<int:id>/', views.update_fiche, name='update_fiche'),
    path('ajouter_paiements/', views.Ajouter_paiements, name='Ajouter_paiements'),
    path('register', views.register, name='register'),
    path('register_adherent', views.registerAdherent, name='registerAdherent'),
    path('details_tontine/', views.details_tontine, name='details_tontine'),
    path('list_tontine/', views.list_tontine, name='list_tontine'),
    path('',auth_views.LoginView.as_view(template_name='pages/pages-login.html',authentication_form=LoginForm), name='connexion'),
    path('logout/',auth_views.LogoutView.as_view(template_name='pages/logout.html', next_page= 'connexion'), name='logout'),
    path('delete/<int:id>/', views.deleteadhérents, name='delete_adhérent'),
    path('get_carnet/<int:adherent_id>/', views.get_carnet, name='get_carnet'),

    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    path('add_fiche/', views.fiche_journaliere_agent, name='add_fiche'),
    path('produits_agent/', views.produits_agent, name='produits_agent'),
    path('agent_adherent/', views.agent_adherent, name='agent_adherent'),
    path('agent_adherent_rapport/', views.agent_adherent_rapport, name='agent_adherent_rapport'),
    path('agent_list/', views.agent_list, name='agent_list'),
    path('compute/', views.compute, name='compute'),

    path('adherent_agent/<int:id>/', views.adherent_agent, name='adherent_agent'),
    path('add_mise/<int:id>/', views.payment, name='payment_mise'),
    path('list_fiche_payments/<int:id>/', views.list_fiche_payments, name='list_fiche_payments'),
    path('list_nouveau_client/<int:id>/', views.list_nouveau_client, name='list_nouveau_client'),


    path('list_fiche_agent/<int:id>/', views.list_fiche_agent, name='list_fiche_agent'),
    path('list_payment_carnet/<int:id>/', views.list_payment_carnet, name='list_payment_carnet'),


    path('carnet_adherent/<int:id>/', views.carnet_adherent, name='carnet_adherent'),
    path('valider_mise/<int:id>/<int:pka>', views.valider_mise, name='valider_mise'),
    path('mise_update/<int:id>/<int:pk>/', views.mise_update, name='mise_update'),

    path('update_mise/<int:id>/<int:pka>', views.update_mise, name='update_mise'),
    path('mon_carnet', views.mon_carnet, name='mon_carnet'),
    path('add_carnet/<int:id>/<int:pk>/', views.add_carnet, name='add_carnet'),

    path('list_adhérent', views.list_adhérent, name='list_adhérent'),
    path('adhérent_list', views.adhérent_list, name='adhérent_list'),

    path('list_payments_adherent', views.list_payments_adherent, name='list_payments_adherent'),
    







 



    

    


 
]
