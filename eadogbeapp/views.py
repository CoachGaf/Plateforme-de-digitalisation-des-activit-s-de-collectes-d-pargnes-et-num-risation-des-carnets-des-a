from ast import IsNot, List
from collections import namedtuple
from operator import is_not
from .models import *
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from django.db import connection
from django.core.paginator import Paginator
from django.http import JsonResponse



# Create your views here.
def index(request):
    tmp = 0
    montant_tmp = 0
    montant_agent = 0

    
    list_finish = []
    nbr_agent = AgentTerrain.objects.all().count()
    agent = AgentTerrain.objects.all()
    paiement = Paiement_mise.objects.filter(Fiche_journalière__date__exact = datetime.date.today())
    
    for paiement in paiement:
        montant_tmp = paiement.montant + montant_tmp

    nbr_adherent  = Carnet.objects.all().count()
    nbr_carnet = Carnet.objects.all()
    for nbr in nbr_carnet:

        mise = Paiement_mise.objects.filter(num_carnet__id__exact = nbr.id)

        if mise:

            for mise in mise:
                
                tmp = int(mise.nbr_mise) + int(tmp)
            nbr = tmp
            if nbr == 372:

                list_finish.append(nbr)
                nbr_finish = len(list_finish)

    





    context = {
        'nbr_adherent': nbr_adherent,
        'nbr_finish': nbr_finish,
        'nbr_agent': nbr_agent,
        'montant_tmp': montant_tmp
    }
    return render(request, 'pages/index.html',context)

def fiche_journaliere_agent(request):
    if request.method == 'POST':
        
        form = FicheForm(request.POST, request.FILES)
        if form.is_valid():
            add_agent = form.save(commit=False)
            add_agent.agent = request.user
            add_agent.save()
            messages.success(request, f'Fiche journalière créee avec succès ')
            return redirect('Ajouter_paiements')
    else:
        form = FicheForm()

    context = {
        'form': form,    
    }
    return render(request, 'pages/add_fiche_agent.html',context)

def update_fiche(request, id):

    fiche = Fiche_journalière.objects.get(id=id)
    if request.method == 'POST':
        
        form = FicheForm(request.POST, request.FILES,instance=fiche)
        if form.is_valid():
            add_agent = form.save(commit=False)
            add_agent.agent = request.user
            add_agent.save()
            messages.success(request, f'Succès de la mise à jour ')
            return redirect('Ajouter_paiements')
    else:
        form = FicheForm(instance=fiche)

    context = {
        'form': form,    
        'fiche': fiche
    }
    return render(request, 'pages/add_fiche_agent.html',context)

def get_carnet(request, adherent_id):
    adherent = Adherent.objects.get(id=adherent_id)
    carnet = list(adherent.carnet.all().values())
    return JsonResponse(carnet, safe=False)

def historique(request):

    return render(request, 'pages/payments.html')

def list_payments(request):
    list_fiche_agent = Fiche_journalière.objects.filter(agent__username__exact = request.user.username).order_by('-id')
    
    
    context = {
      
        'list_fiche_agent': list_fiche_agent,

    }
    return render(request, 'pages/lists-payments.html',context)



def list_fiche_agent(request,id):
    agents = AgentTerrain.objects.get(id__exact = id)
    list_fiche_agent = Fiche_journalière.objects.filter(agent__username__exact = agents.user.username).order_by('-id').all()
  
    
    context = {
      
        'list_fiche_agent': list_fiche_agent,    
    }
    return render(request, 'pages/lists-fiche-agent.html',context)

def list_fiche_payments(request,id):
    nbr =0
    vente = 0
    total = 0
    list_mise_adherent = Paiement_mise.objects.filter(Fiche_journalière__id__exact=id)
    mise = Paiement_mise.objects.filter(Fiche_journalière__id__exact=id)

    list = Paiement_mise.objects.filter(Fiche_journalière__id__exact=id)
    
    for list_mise_adherent in list_mise_adherent:
        valeur= int(nbr) + int(list_mise_adherent.montant)
        nbr= valeur

    for list_mise in mise:
        if list_mise.achat_carte != None:
            total_vente= int(vente) + int(list_mise.achat_carte)
            vente= total_vente

    total_montant = int(nbr) + int(vente)

    context = {
      
        'list_mise_adherent': list_mise_adherent,
        'list':list,
        'nbr': nbr,
        'vente': vente,
        'total_montant': total_montant,
        'pk': id
        
    }
    return render(request, 'pages/lists_payments_mise.html',context)

def list_payment_carnet(request,id):
    nbr =0
    vente = 0
    total = 0
    list_mise_adherent = Paiement_mise.objects.filter(num_carnet__id__exact=id)
    mise = Paiement_mise.objects.filter(num_carnet__id__exact=id)

    list = Paiement_mise.objects.filter(num_carnet__id__exact=id)
    
    for list_mise_adherent in list_mise_adherent:
        valeur= int(nbr) + int(list_mise_adherent.montant)
        nbr= valeur

    for list_mise in mise:
        if list_mise.achat_carte != None:
            total_vente= int(vente) + int(list_mise.achat_carte)
            vente= total_vente

    total_montant = int(nbr) + int(vente)

    context = {
      
        'list_mise_adherent': list_mise_adherent,
        'list':list,
        'nbr': nbr,
        'vente': vente,
        'total_montant': total_montant,
        'pk': id
        
    }
    return render(request, 'pages/list_payment_carnet.html',context)

def list_nouveau_client(request,id):
    nbr =0
    vente = 0
    total = 0
    list_mise_adherent = Paiement_mise.objects.filter(Fiche_journalière__id__exact=id,nouveau__exact = True)
    mise = Paiement_mise.objects.filter(Fiche_journalière__id__exact=id,nouveau__exact = True)

    list = Paiement_mise.objects.filter(Fiche_journalière__id__exact=id, nouveau__exact = True)
    
    for list_mise_adherent in list_mise_adherent:
        valeur= int(nbr) + int(list_mise_adherent.montant)
        nbr= valeur

    for list_mise in mise:
        if list_mise.achat_carte != None:
            total_vente= int(vente) + int(list_mise.achat_carte)
            vente= total_vente

    total_montant = int(nbr) + int(vente)

    context = {
      
        'list_mise_adherent': list_mise_adherent,
        'list':list,
        'nbr': nbr,
        'vente': vente,
        'total_montant': total_montant,
        'pk': id
        
    }
    return render(request, 'pages/list_nouveau_client.html',context)

def list_payments_adherent(request):
    nbr =0
    list = Paiement_mise.objects.filter(nom_adhérent__user__username__exact=request.user.username)
    list_paiement = Paiement_mise.objects.filter(nom_adhérent__user__username__exact=request.user.username)

    
    
    for list_paiement in list_paiement:
        valeur= int(nbr) + int(list_paiement.montant)
        nbr= valeur
    context = {
      
        'list': list,
        'list_paiement':list_paiement,    
       
        'nbr': nbr
    }
    return render(request, 'pages/list_payments_adherent.html',context)

def add_carnet(request,id,pk):
  
   
    numero = Carnet.objects.filter(agentt__user__username__exact= request.user.username)
    cpt =0

    if request.method == 'POST':
        
        form = CarnetForm(request.POST, request.FILES)
        if form.is_valid():
            
           
            add_fiche = form.save(commit=False)
            if numero:
                for numero in numero:
                    cpt = int(numero.numero_carnet) + 1
            else:
                cpt = 1
            add_fiche.numero_carnet = cpt
            add_fiche.agentt = AgentTerrain(id = pk)
            add_fiche.adhérent = Adherent(id = id)
            add_fiche.save()
            messages.success(request, f'Carnet crée avec succès')
            return redirect('Ajouter_paiements')
    else:
        form = CarnetForm()

    context = {
        'form': form,
        
    }
    return render(request, 'pages/carnet.html',context)

def connexion(request):

    return render(request, 'pages/pages-login.html')



def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]





def contact_agent(request):
    
    agent = AgentTerrain.objects.order_by('-id').all()
    adherent=Adherent.objects.filter(user__username=request.user.username)
    for adherent in adherent:
        agent = AgentTerrain.objects.get(user__username = adherent.nom_agent_terrain.user.username)


    context = {
        
        'agent': agent
    }
    

    return render(request, 'pages/mon_agent.html',context)

def notification(request):

    return render(request, 'pages/notifications.html')

def agents(request):
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)

    list = AgentTerrain.objects.order_by('-id').all()

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur
    }
    return render(request, 'pages/agents.html', context)

def ajouter_produit(request):
    
    if request.method == 'POST':
        
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            fo=form.save(commit=False)

            initiateur=Initiateur.objects.filter(user__username=request.user.username)
            if initiateur:
                for lists in initiateur:
                   nametontine = lists.nom_tontine
                
            fo.nom_tontine = nametontine
            form.save()
            messages.success(request, f'Produit crée avec succès!')
            messages.success(request, f'Vous pouvez continuer avec la création de catégorie de fournisseur!')

            return redirect('ajouter_produit')
    else:
        form = ProduitForm()

    context = {
        'form': form,    
    }
    return render(request, 'pages/add-produit.html',context)

def ajouter_agents(request):
    if request.method =='POST':
        form = UserForm(request.POST, request.FILES)
        profileform = ProfileAgentForm(request.POST, request.FILES)
        if form.is_valid() and profileform.is_valid():
            user = form.save()
            profil=profileform.save(commit=False)
            profil.user = user
            profil.save()
            login(request, user)
            form.save()
            group = Group.objects.get(name='agent')
            user.groups.add(group)
            messages.success(request, "Inscription effectuée avec succès! Vous pouvez continuer l'inscription d'un autre adhérent")
            return redirect("ajouter_agents")
        messages.error(request, "Echec de l'envoie")
    else:
        form = UserForm()
        profileform= ProfileAgentForm()
        context = {
            'form' : form,
            'profilform' : profileform
        }

    return render(request, 'pages/add-agents.html', context)


def adhérents(request):
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)
    list = Adherent.objects.order_by('-id').all()

    agent = AgentTerrain.objects.filter(user__username__exact= request.user.username)
    agentterrain = AgentTerrain.objects.get(user__username__exact= request.user.username)
    for agent in agent:
        list_adherent = Adherent.objects.filter(nom_tontine__exact = agent.nom_tontine)

    list_carnet = Carnet.objects.filter(agentt__user__username = agentterrain.user.username)
    

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur,
        'list_adherent': list_adherent,
        'list_carnet' : list_carnet
        
    }
    return render(request, 'pages/adhérents.html', context) 

def adhérent_list(request):
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)
    list = Adherent.objects.order_by('-id').all()

    agent = AgentTerrain.objects.filter(user__username__exact= request.user.username)
    agentterrain = AgentTerrain.objects.get(user__username__exact= request.user.username)
    for agent in agent:
        list_adherent = Adherent.objects.filter(nom_tontine__exact = agent.nom_tontine)

    list_carnet = Carnet.objects.filter(agentt__user__username = agentterrain.user.username)
    

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur,
        'list_adherent': list_adherent,
        'list_carnet' : list_carnet
        
    }
    return render(request, 'pages/adhérent_list.html', context) 
    
def agent_adherent(request):
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)

    for list_initiateur in tontineinitiateur:
        list_agent = AgentTerrain.objects.filter(nom_tontine__exact = list_initiateur.nom_tontine)

    

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur,
        'list_agent': list_agent
    }
    


    return render(request, 'pages/agents_adherent.html', context) 

def agent_adherent_rapport(request):
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)

    for list_initiateur in tontineinitiateur:
        list_agent = AgentTerrain.objects.filter(nom_tontine__exact = list_initiateur.nom_tontine)

    

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur,
        'list_agent': list_agent
    }
    


    return render(request, 'pages/payment-report.html', context)

def agent_list(request):
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)

    for list_initiateur in tontineinitiateur:
        list_agent = AgentTerrain.objects.filter(nom_tontine__exact = list_initiateur.nom_tontine)

    

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur,
        'list_agent': list_agent
    }
    


    return render(request, 'pages/payment-report.html', context)

def adherent_agent(request,id):
    agent = AgentTerrain.objects.filter(id__exact= id)
    for agent in agent:
        list_adherent = Carnet.objects.filter(agentt__user__username__exact = agent.user.username)

    

    context = {
        
        'list_adherent': list_adherent
    }
    


    return render(request, 'pages/adherent_agent.html', context) 


def deleteadhérents(request,id):
    user = Adherent.objects.get(id=id)
    user.delete()
    return redirect('index')

def ajouter_adhérents(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        profileform = ProfileAdherentForm(request.POST, request.FILES)
        if form.is_valid() and profileform.is_valid():
            user = form.save()
            profil=profileform.save(commit=False)
            profil.user = user
            tontineinitiateur=  AgentTerrain.objects.filter(user__username=request.user.username)
            if tontineinitiateur:
                for list in tontineinitiateur:
                    getnametontine = list.nom_tontine
            profil.nom_tontine= getnametontine
            profil.nom_agent_terrain = AgentTerrain.objects.get(user__username=request.user.username)
            profil.save()
            login(request, user)
            form.save()
            group = Group.objects.get(name='adherent')
            user.groups.add(group)    
            messages.success(request, "Inscription effectuée avec succès! Vous pouvez créer un carnet pour l'adhérent enrégistré précédemment ")
            return redirect("ajouter_adhérents")
        messages.error(request, "Echec de l'envoie")
    else:
        form = UserForm()
        profileform= ProfileAdherentForm()
    context = {
            'form' : form,
            'profilform' : profileform
    }
    return render(request, 'pages/add-adhérents.html', context)


def produits(request):

    initiateur = Initiateur.objects.get(user__username__exact=request.user.username)

    list_produit = Produit.objects.filter(nom_tontine__exact=initiateur.nom_tontine)


    context = {
        'list_produit': list_produit
    }
    return render(request, 'pages/produits.html',context)

def produits_agent(request):
    agent = AgentTerrain.objects.get(user__username__exact= request.user.username)
    
    list_produits = Produit.objects.filter(nom_tontine__exact=agent.nom_tontine)

    context = {
        'list' : list_produits,
        
    }
    return render(request, 'pages/produits_agent.html',context)

def rapport_paiement(request):

    return render(request, 'pages/payment-report.html')

def rapport_revenu(request):

    return render(request, 'pages/income-report.html')

def rapport_paiement(request):

    return render(request, 'pages/payment-report.html')

def reçus(request):

    return render(request, 'pages/reçus.html')

def faq(request):

    return render(request, 'pages/pages-faq.html')

def Ajouter_paiements(request):
    agent = Fiche_journalière.objects.filter(agent__username__exact = request.user.username)
    list_fiche_agent = Fiche_journalière.objects.filter(agent__username__exact = request.user.username).order_by('-id').all()
    context = {
        'list' : list_fiche_agent,
        'nom_agent' : agent
    }
    return render(request, 'pages/add-payments.html', context)


def list_tontine(request):
    list = TontineAdogbe.objects.order_by('-id').all()
    context = {
        'list' : list
    }
    

    return render(request, 'pages/list_tontine.html', context)

def details_tontine(request):

    return render(request, 'pages/details_tontine.html')

def register(request): 
    if request.method =='POST':
        form = UserForm(request.POST)
        profileform = ProfileAdherentForm(request.POST)
        if form.is_valid() and profileform.is_valid():
            user = form.save()
            profil=profileform.save(commit=False)
            profil.user = user
            profil.save()
            login(request, user)
            form.save()
            group = Group.objects.get(name='Adhérents')
            user.groups.add(group)
            messages.success(request, "Inscription effectuée avec succès")
            return redirect("connexion")
        messages.error(request, "Echec de l'envoie")
    else:
        form = UserForm()
        profileform= ProfileAdherentForm()
    context = {
        'form' : form,
        'profilform' : profileform
    }
    
    return render(request, 'pages/pages-register.html',context)

def registerAdherent(request): 
    if request.method =='POST':
        form = UserForm(request.POST)
        profileform = ProfileAdherentForm(request.POST)
        if form.is_valid() and profileform.is_valid():
            user = form.save()
            profil=profileform.save(commit=False)
            profil.user = user
            profil.save()
            login(request, user)
            form.save()
            group = Group.objects.get(name='Adhérents')
            user.groups.add(group)
            messages.success(request, "Inscription effectuée avec succès")
            return redirect("connexion")
        messages.error(request, "Echec de l'envoie")
    else:
        form = UserForm()
        profileform= ProfileAdherentForm()
    context = {
        'form' : form,
        'profilform' : profileform
    }
    
    return render(request, 'pages/add-adhérent.html',context)
@permission_required('eadogbeapp.can_mark_user_initiateur')
def profile(request):
    profil = Initiateur.objects.get(user__username__exact=request.user.username)

   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileInitiateurUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.initiateur)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre compte a été mise à jour !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileInitiateurUpdateForm(instance=request.user.initiateur)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profil': profil
    }

    return render(request, 'pages/pages-profile.html', context)
@permission_required('eadogbeapp.can_mark_user_adhérent')
def profileAdherent(request):
    profil = Adherent.objects.get(user__username__exact=request.user.username)

   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileAdherentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.adherent)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre compte a été mise à jour !')
            return redirect('profileadherent')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileAdherentUpdateForm(instance=request.user.adherent)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profil': profil
    }

    return render(request, 'pages/pages-profile-adherent.html', context)

@permission_required('eadogbeapp.can_mark_user_agent')
def profileAgent(request):
    profil = AgentTerrain.objects.get(user__username__exact=request.user.username)

   
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileAgentUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.agentterrain)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre compte a été mise à jour !')
            return redirect('profileagent')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileAgentUpdateForm(instance=request.user.agentterrain)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profil': profil
    }

    return render(request, 'pages/pages-profile-agent.html', context)


def payment(request,id):
    nbr=0
    tmp = 0
    jr = 0
    list_adherent = Adherent.objects.filter(nom_agent_terrain__user__username__exact= request.user.username)
    
    liste_carnet = Carnet.objects.filter(agentt__user__username__exact= request.user.username)
   
    agent = AgentTerrain.objects.filter(user__username__exact= request.user.username)
    for agent in agent:
        produit = Produit.objects.filter(nom_tontine__exact = agent.nom_tontine)
    
    
    


    if request.method == 'POST':
        
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            
            add_fiche = form.save(commit=False)
            carnet_num = Carnet.objects.get(numero_carnet=request.POST['num_cnt'])
            prix = carnet_num.objectif.prix_mise_produit
            add_fiche.mise = prix
            add_fiche.nom_adhérent = Adherent.objects.get(id=request.POST['adh'])
            add_fiche.num_carnet = Carnet.objects.get(numero_carnet=request.POST['num_cnt'])
            num = Carnet.objects.get(numero_carnet=request.POST['num_cnt'])
            add_fiche.objectif  = Produit.objects.get(nom_produit__exact = num.objectif.nom_produit)
            add_fiche.Fiche_journalière = Fiche_journalière(id = id)
            add_fiche.montant = request.POST.get("montant")
            paiement = Paiement_mise.objects.filter(num_carnet__numero_carnet__exact = num.numero_carnet).last()
            if paiement == None:
                nbr = add_fiche.nbr_mise
                if nbr <= 31:
                    add_fiche.niveau = nbr
                    add_fiche.mois = 1
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 31 and nbr <= 62:
                    add_fiche.mois = 2
                    tmp = int(nbr) - 31 
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 62 and nbr <= 93:
                    add_fiche.mois = 3
                    tmp = int(nbr) - 62 
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 93 and nbr <= 124:
                    add_fiche.mois = 4
                    tmp = int(nbr) - 93 
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 124 and nbr <= 155:
                    add_fiche.mois = 5
                    tmp = int(nbr) - 124 
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 155 and nbr <= 186:
                    add_fiche.mois = 6
                    tmp = int(nbr) - 155 
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 186 and nbr <= 217:
                    add_fiche.mois = 7
                    tmp = int(nbr) - 186
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 217 and nbr <= 248:
                    add_fiche.mois = 8
                    tmp = int(nbr) - 217
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200

                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 248 and nbr <= 279:
                    add_fiche.mois = 9
                    tmp = int(nbr) - 248
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 279 and nbr <= 310:
                    add_fiche.mois = 10
                    tmp = int(nbr) - 279
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 310 and nbr <= 341:
                    add_fiche.mois = 11
                    tmp = int(nbr) - 310
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès ')
                    return redirect('payment_mise',id=id)

                if nbr > 341 and nbr <= 372:
                    add_fiche.mois = 12
                    tmp = int(nbr) - 341
                    add_fiche.niveau = tmp
                    add_fiche.nouveau =True
                    add_fiche.achat_carte = 200
                    add_fiche.save()
                    messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                    return redirect('payment_mise',id=id)
            
            else:
                nbr = add_fiche.nbr_mise
                if paiement.mois == 1:
                    
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 1
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 2
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 3
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 4
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 5
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 6
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 186 and tmp <= 217:
                        add_fiche.mois = 7
                        tmp = int(nbr) - 186
                        add_fiche.niveau = tmp
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 217 and tmp <= 248:
                        add_fiche.mois = 8
                        jr = int(tmp) - 217
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if nbr > 248 and nbr <= 279:
                        add_fiche.mois = 9
                        jr = int(tmp) - 248
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 279 and tmp <= 310:
                        add_fiche.mois = 10
                        jr = int(tmp) - 279
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 310 and tmp <= 341:
                        add_fiche.mois = 11
                        jr = int(tmp) - 310
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 341 and tmp <= 372:
                        add_fiche.mois = 12
                        jr = int(tmp) - 341
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)
                if paiement.mois == 2:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 2
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)
                        

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 3
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 4
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 5
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 6
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 7
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 186 and tmp <= 217:
                        add_fiche.mois = 8
                        tmp = int(nbr) - 186
                        add_fiche.niveau = tmp
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 217 and tmp <= 248:
                        add_fiche.mois = 9
                        jr = int(tmp) - 217
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if nbr > 248 and nbr <= 279:
                        add_fiche.mois = 10
                        jr = int(tmp) - 248
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 279 and tmp <= 310:
                        add_fiche.mois = 11
                        jr = int(tmp) - 279
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 310 and tmp <= 341:
                        add_fiche.mois = 12
                        jr = int(tmp) - 310
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)
                
                if paiement.mois == 3:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 3
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 4
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 5
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 6
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 7
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 8
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 186 and tmp <= 217:
                        add_fiche.mois = 9
                        tmp = int(nbr) - 186
                        add_fiche.niveau = tmp
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 217 and tmp <= 248:
                        add_fiche.mois = 10
                        jr = int(tmp) - 217
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if nbr > 248 and nbr <= 279:
                        add_fiche.mois = 11
                        jr = int(tmp) - 248
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 279 and tmp <= 310:
                        add_fiche.mois = 12
                        jr = int(tmp) - 279
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)

                if paiement.mois == 4:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 4
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)
                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 5
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 6
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 7
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 8
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 9
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 186 and tmp <= 217:
                        add_fiche.mois = 10
                        tmp = int(nbr) - 186
                        add_fiche.niveau = tmp
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 217 and tmp <= 248:
                        add_fiche.mois = 11
                        jr = int(tmp) - 217
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if nbr > 248 and nbr <= 279:
                        add_fiche.mois = 12
                        jr = int(tmp) - 248
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)

                if paiement.mois == 5:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 6
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 7
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 8
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 9
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 10
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 186 and tmp <= 217:
                        add_fiche.mois = 11
                        tmp = int(nbr) - 186
                        add_fiche.niveau = tmp
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 217 and tmp <= 248:
                        add_fiche.mois = 12
                        jr = int(tmp) - 217
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)

                if paiement.mois == 6:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 6
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 7
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 8
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 9
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 10
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 11
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 186 and tmp <= 217:
                        add_fiche.mois = 12
                        tmp = int(nbr) - 186
                        add_fiche.niveau = tmp
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)

                if paiement.mois == 7:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 7
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 8
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 9
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 10
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 11
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 155 and tmp <= 186:
                        add_fiche.mois = 12
                        jr = int(tmp) - 155
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)

                if paiement.mois == 8:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 8
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 9
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 10
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 11
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 124 and tmp <= 155:
                        add_fiche.mois = 12
                        jr = int(tmp) - 124
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)

                
                if paiement.mois == 9:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 9
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 10
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 11
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 93 and tmp <= 124:
                        add_fiche.mois = 12
                        jr = int(tmp) - 93 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')

                if paiement.mois == 10:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 10
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 11
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.objectif = Produit.objects.get(id=request.POST['produit'])
                        add_fiche.Fiche_journalière = Fiche_journalière(id = id)
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 62 and tmp <= 93:
                        add_fiche.mois = 12
                        jr = int(tmp) - 62 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès, Carte terminée ')
                        return redirect('payment_mise',id=id)
                
                if paiement.mois == 11:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 11
                        add_fiche.save()
                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

                    if tmp > 31 and tmp <= 62:
                        add_fiche.mois = 12
                        jr = int(tmp) - 31 
                        add_fiche.niveau = jr
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)
                
                if paiement.mois == 12:
                    tmp = int(paiement.niveau) + nbr
                    if tmp <=31:
                        add_fiche.niveau = tmp
                        add_fiche.mois = 12
                        add_fiche.save()
                        if jr == 31:
                            messages.info(request, f'Carte terminéé. Vous ne pouvez plus enrégistrer dans ce carnet ')

                        messages.success(request, f'Paiement éffectué avec succès ')
                        return redirect('payment_mise',id=id)

        messages.error(request, "Echec de l'envoie")
    else:
        form = PaymentForm()

    context = {
        'form': form,
        'list_adherent': list_adherent,
        'produit': produit,
        'liste_carnet': liste_carnet,
        'pk': id
    }
    return render(request, 'pages/add-mise.html',context)

def compute(request):

    a = request.POST.get("a")
    
    c =  request.POST.get("c")
   

    carnet = Carnet.objects.get(numero_carnet__exact = c)

    prix = carnet.objectif.prix_mise_produit

    prix_int = int(prix)


    result = int(a) * prix_int
    return JsonResponse({"operation_result": result})



def list_adhérent(request):
   
    tontineinitiateur=Initiateur.objects.filter(user__username=request.user.username)
    list = Adherent.objects.order_by('-id').all()

    agent = AgentTerrain.objects.filter(user__username__exact= request.user.username)
    for agent in agent:
        list_adherent = Adherent.objects.filter(nom_tontine__exact = agent.nom_tontine)

  
    

    context = {
        'list' : list,
        'tontineinitiateur': tontineinitiateur,
        'list_adherent': list_adherent,
        'agent': agent
    }
    return render(request, 'pages/list_adhérent.html',context)



def add_carte_finish(request):
    list_adherent = Adherent.objects.filter(nom_agent_terrain__user__username__exact= request.user.username)
   
   
    agent = AgentTerrain.objects.filter(user__username__exact= request.user.username)
    for agent in agent:
        produit = Produit.objects.filter(nom_tontine__exact = agent.nom_tontine)

    if request.method == 'POST':
        
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            
            add_fiche = form.save(commit=False)
            add_fiche.nom_adhérent = Adherent.objects.get(id=request.POST['adh'])
            num = Adherent.objects.get(id=request.POST['adh'])
            add_fiche.num_carnet = num.code_identification_adhérent
            add_fiche.objectif = Produit.objects.get(id=request.POST['produit'])
            add_fiche.Fiche_journalière = Fiche_journalière(id = id)

            add_fiche.save()
            messages.success(request, f'Paiement éffectué avec succès ')
            return redirect('payment_mise',id=id)
    else:
        form = PaymentForm()

    context = {
        'form': form,
        'list_adherent': list_adherent,
        'produit': produit 
    }
    return render(request, 'pages/add-mise.html',context)





def carnet_adherent(request,id):
    tmp=0
    nbr = 0
    i=1
    decr_nbr =0
    cpt=0
    mise_list = []

    
    paiement = Paiement_mise.objects.filter(num_carnet__id__exact = id)



    if paiement:
        for paiement in paiement:
            tmp = int(paiement.nbr_mise) + int(tmp)
    nbr = tmp

    while i <= nbr:
        mise_list.append(i)
        i=i+1
    mise = mise_list
    niveau_mise = Niveau.objects.order_by('id').all()
    
    pka = id
    paginator = Paginator(mise, 31)
    page = request.GET.get('page')
    niveau = paginator.get_page(page)
    context = {
        'niveau': niveau, 
        'pka': pka,
        'niveau_mise': niveau_mise,
        'nbr' : nbr,
        'i': i,
        'mise_list' : mise_list,
        'paiement' : paiement
     
    }
    
    return render(request, 'pages/carnet_adherent.html',context)

def mon_carnet(request):
    
    list_carnet = Carnet.objects.filter(adhérent__user__username__exact = request.user.username)
  
  
    context = {
        'list': list_carnet, 
        
        
    }
    
    return render(request, 'pages/mon_carnet.html',context)

def mes_carnets(request):
    
    list_carnet = Carnet.objects.filter(adhérent__user__username__exact = request.user.username)
  
  
    context = {
        'list_carnet': list_carnet, 
        
        
    }
    
    return render(request, 'pages/mon_carnet.html',context)


def valider_mise(request,id,pka):
    agent = AgentTerrain.objects.get(user__username__exact= request.user.username)
    ss_created = Mise_adherent.objects.create(niveau=Niveau(id=id), nom_adhérent = Adherent(id=pka), nom_agent_terrain = agent ,valider = True )
    ss_created.save()
    return redirect('carnet_adherent',id=pka)

def update_mise(request,id,pka):
    agent = AgentTerrain.objects.get(user__username__exact= request.user.username)
    mise = Mise_adherent.objects.filter(niveau=Niveau(id=id), nom_adhérent = Adherent(id=pka), nom_agent_terrain = agent).update(valider=False)
    
    return redirect('carnet_adherent',id=pka)

def mise_update(request, id,pk):
    mise = Paiement_mise.objects.get(id=id)
    list_adherent = Adherent.objects.filter(nom_agent_terrain__user__username__exact= request.user.username)
   
   
    agent = AgentTerrain.objects.filter(user__username__exact= request.user.username)
    for agent in agent:
        produit = Produit.objects.filter(nom_tontine__exact = agent.nom_tontine)
    if request.method == 'POST':
         form = PaymentForm(request.POST, request.FILES, instance=mise)
         if form.is_valid():
            add_fiche = form.save(commit=False)
            add_fiche.nom_adhérent = Adherent.objects.get(id=request.POST['adh'])
            num = Adherent.objects.get(id=request.POST['adh'])
            add_fiche.num_carnet = num.code_identification_adhérent
            add_fiche.objectif = Produit.objects.get(id=request.POST['produit'])
            add_fiche.Fiche_journalière = Fiche_journalière(id = pk)
            add_fiche.save()
            messages.success(request, f'Paiement éffectué avec succès ')
            return redirect('payment_mise',id=id)
    else:
        form = PaymentForm(instance=mise)

    context = {
        'form': form,
        'mise': mise,
        'list_adherent': list_adherent,
        'produit': produit 
    }
    
    return render(request, 'pages/add-mise.html', context)
    
    
