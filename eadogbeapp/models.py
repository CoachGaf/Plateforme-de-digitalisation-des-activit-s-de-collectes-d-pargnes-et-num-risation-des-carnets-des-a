from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Produit(models.Model):
    nom_produit = models.CharField(max_length=255,null=True, blank=True)
    prix_mise_produit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    nom_tontine = models.ForeignKey('TontineAdogbe', on_delete=models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return self.nom_produit

class TontineAdogbe(models.Model):
    nom_tontine =models.CharField(max_length=255,null=True, blank=True)
    sigle_tontine =models.CharField(max_length=255,null=True, blank=True)
    logo = models.ImageField(upload_to='postes_image/',null=True, blank=True)

    def __str__(self):
        return self.nom_tontine

class Adherent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_identification_adhérent = models.CharField(max_length=255,null=True, blank=True)
    nom_tontine = models.ForeignKey('TontineAdogbe', on_delete=models.SET_NULL, null=True,blank=True)
    âge_adhérent = models.IntegerField (null=True, blank=True)
    adresse_adhérent = models.CharField(max_length=255,null=True, blank=True)
    profession_adhérent = models.CharField(max_length=255,null=True, blank=True)
    numero_tel_adhérent = models.CharField(max_length=255,null=True, blank=True)
    email_de_notification = models.EmailField(max_length=255,null=True, blank=True)
    date_adhésion =models.DateField(null=True, blank=True)
    nom_agent_terrain = models.ForeignKey('AgentTerrain', on_delete=models.SET_NULL, null=True,blank=True)  
    photo_adhérent= models.ImageField(upload_to='postes_image/',null=True, blank=True)             

    class Meta:
        
        permissions = (
            ("can_mark_user_adhérent", "Set user as adhérent"),
            ("can_mark_adhérent_subscribe_échéance_jour", "Set user as adhérent_subscribe_échéance_jour"),
            ("can_mark_adhérent_subscribe_échéance_semaine", "Set user as adhérent_subscribe_échéance_semaine"),
            

        
        )
            
            
        

    def __str__(self):
        return self.user.username

class AgentTerrain(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_identification_agent = models.CharField(max_length=255,null=True, blank=True)
    nom_tontine = models.ForeignKey('TontineAdogbe', on_delete=models.SET_NULL, null=True,blank=True)
    âge_agent = models.IntegerField (null=True, blank=True)
    adresse_agent = models.CharField(max_length=255,null=True, blank=True)
    numero_tel_agent = models.CharField(max_length=255,null=True, blank=True)
    nom_temoin_agent = models.CharField(max_length=255,null=True, blank=True)
    prenom_temoin_agent = models.CharField(max_length=255,null=True, blank=True)
    âge_temoin_agent = models.CharField(max_length=255,null=True, blank=True)
    adresse_temoin_agent = models.CharField(max_length=255,null=True, blank=True)
    numero_tel_temoin_agent = models.CharField(max_length=255,null=True, blank=True)
    adresse_mail_agent = models.CharField(max_length=255,null=True, blank=True)
    email_de_notification = models.CharField(max_length=255,null=True, blank=True)
    terme_contrat = models.ImageField(upload_to='postes_image/',null=True, blank=True)     
    photo_agent= models.ImageField(upload_to='postes_image/',null=True, blank=True)     
    salaire_agent = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    class Meta:
        
        permissions = ("can_mark_user_agent", "Set user as agent"),
                       
        
                    


    def __str__(self):
        return self.user.username


class Carnet(models.Model):
    numero_carnet =models.IntegerField()
    adhérent = models.ForeignKey(Adherent,  related_name='carnet', on_delete=models.CASCADE,default=1)
    objectif = models.ForeignKey('Produit', on_delete=models.SET_NULL, null=True,blank=True)
    agentt = models.ForeignKey(AgentTerrain, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.numero_carnet}'


class Initiateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_tontine = models.ForeignKey('TontineAdogbe', on_delete=models.SET_NULL, null=True,blank=True)
    adresse_initiateur = models.CharField(max_length=255,null=True, blank=True)
    numero_tel_initiateur = models.CharField(max_length=255,null=True, blank=True)
    email_de_notification = models.EmailField(max_length=255,null=True, blank=True)
    photo_initiateur= models.ImageField(upload_to='postes_image/',null=True, blank=True)  

    class Meta:
        
        permissions = ("can_mark_user_initiateur", "Set user as initiateur"),   

    def __str__(self):
        return self.user.username

class Secretaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_tontine = models.ForeignKey('TontineAdogbe', on_delete=models.SET_NULL, null=True,blank=True)
    adresse_secretaire = models.CharField(max_length=255,null=True, blank=True)
    numero_tel_secretaire = models.CharField(max_length=255,null=True, blank=True)
    email_de_notification = models.EmailField(max_length=255,null=True, blank=True)
    photo_secretaire= models.ImageField(upload_to='postes_image/',null=True, blank=True)  

    class Meta:
        
        permissions = ("can_mark_user_secretaire", "Set user as secretaire"),   

    def __str__(self):
        return self.user.username

class Jours(models.Model):
    num_jour = models.IntegerField (null=True, blank=True)
    def __str__(self):
        return f'{self.num_jour}'
    

class Mois(models.Model):
    num_mois = models.IntegerField (null=True, blank=True)

    def __str__(self):
        return f'{self.num_mois}'

class Mois_adherent(models.Model):
    mois = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.mois}'

class Semaine (models.Model):
    num_semaine = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.num_semaine
    

class Paiement_mise(models.Model):

    num_carnet = models.ForeignKey('Carnet',  related_name='paiement_mise', on_delete=models.SET_NULL, null=True,blank=True)
    nom_adhérent = models.ForeignKey(Adherent,related_name='paiement_mise',  on_delete=models.CASCADE)
    objectif = models.ForeignKey('Produit', on_delete=models.SET_NULL, null=True,blank=True)
    mise = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    nbr_mise = models.IntegerField (null=True, blank=True)
    montant = models.IntegerField (null=True, blank=True)
    nouveau = models.BooleanField(default=False)
    achat_carte = models.IntegerField (null=True, blank=True)
    niveau = models.IntegerField (null=True, blank=True)
    mois = models.IntegerField (null=True, blank=True)
    Fiche_journalière = models.ForeignKey('Fiche_journalière', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return f'{self.num_carnet}. {self.nom_adhérent}'

class Carte_finish(models.Model):
    
    num_carnet =models.CharField(max_length=255,null=True, blank=True)
    nom_adhérent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    objectif = models.ForeignKey('Produit', on_delete=models.SET_NULL, null=True,blank=True)
    mise = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    finish = models.BooleanField(default=False)
    date_adhésion = models.DateTimeField()
    date_fin = models.DateTimeField()

    def __str__(self):
        return f'{self.num_carnet}'




class Fiche_journalière(models.Model):
    
    mois = models.ForeignKey('Mois', on_delete=models.SET_NULL, null=True,blank=True)
    semaine = models.ForeignKey('Semaine', on_delete=models.SET_NULL, null=True,blank=True)
    date = models.DateTimeField()
    agent = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f'{self.date}. {self.agent.username}'

class Suggession(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    sujet = models.CharField(max_length=255)
    message = models.TextField()

class Temoignages(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    contain = models.TextField()
    date_post = models.DateTimeField(auto_now_add=True)

class Recu(models.Model):
    reference_reçu =models.CharField(max_length=255,null=True, blank=True)
    nom_adhérent = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    date_paiement = models.DateTimeField(auto_now_add=True)
    montant_payé = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

class Niveau(models.Model):
    jours = models.ForeignKey('Jours', on_delete=models.SET_NULL, null=True,blank=True)
    mois_num = models.ForeignKey('Mois_adherent', on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
        return f'{self.jours}j {self.mois_num} mois'


class Mise_adherent(models.Model):
    niveau = models.ForeignKey('Niveau', on_delete=models.SET_NULL, null=True,blank=True)
    nom_adhérent = models.ForeignKey(Adherent, on_delete=models.CASCADE)
    nom_agent_terrain = models.ForeignKey('AgentTerrain', on_delete=models.SET_NULL, null=True,blank=True)  
    valider = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.nom_adhérent}.{self.niveau}'