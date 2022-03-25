from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import fields
from .models import *
from django.dispatch import receiver
from django.forms.widgets import DateTimeInput

class DateInput(forms.DateTimeInput):
    input_type = 'date'

from django.contrib.auth.models import User 
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget= forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password = forms.CharField (required=True,label='Password',  widget= forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    
class UserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.is_active = True
        if commit:
            user.save()
        return user

class ProfileAdherentForm(forms.ModelForm):
    date_adhésion = forms.DateTimeField(required=False, widget=DateInput)

    class Meta:
        model = Adherent
        exclude = ['user','nom_agent_terrain','code_identification_adhérent','Avoir_agent_terrain','nom_tontine']

    
    def save(self, commit=True):
        profile = super(ProfileAdherentForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile

class ProfileAgentForm(forms.ModelForm):
    class Meta:
        model = AgentTerrain
        exclude = ['user']

    
    def save(self, commit=True):
        profile = super(ProfileAgentForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        

class ProfileAdherentUpdateForm(forms.ModelForm):
    date_adhésion = forms.DateTimeField(required=False, widget=DateInput)

    class Meta:
        model = Adherent
        exclude = ['user','nom_tontine','nom_agent_terrain','nom_groupe_tontine','code_identification_adhérent','Avoir_agent_terrain',  ]

class ProfileInitiateurUpdateForm(forms.ModelForm):
    class Meta:
        model = Initiateur
        exclude = ['user','nom_tontine']


class ProfileAgentUpdateForm(forms.ModelForm):
    class Meta:
        model = AgentTerrain
        exclude = ['user','code_identification_agent','nom_tontine','terme_contrat','salaire_agent','nom_temoin_agent ','prenom_temoin_agent','adresse_temoin_agent','numero_tel_temoin_agent','adresse_mail_agent']



class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

class FicheForm(forms.ModelForm):
    date = forms.DateTimeField(required=False, widget=DateInput)
    class Meta:
        model = Fiche_journalière
        exclude = ['agent']

class PaymentForm(forms.ModelForm):
    
    class Meta:
        model = Paiement_mise
        exclude = ['Fiche_journalière','nom_adhérent','num_carnet','nouveau','achat_carte', 'niveau', 'mois','mise','montant','objectif']

class CarnetForm(forms.ModelForm):
    
    class Meta:
        model = Carnet

        exclude = ['numero_carnet','adhérent','agentt']

  






