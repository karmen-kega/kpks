from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, HistoriqueConnexion, Position, mission, message
from bootstrap_datepicker_plus.widgets import DatePickerInput


    
class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='nom',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nom de famille', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile = forms.ImageField(label='Photo', required=False)
    password1 = forms.CharField(label='mot de passe',required=False,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirmer',required=False,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    nationnalite = forms.CharField(label='nationnalite',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    CNI = forms.ImageField(label='CNI', required=False)
    telephone = forms.CharField(label='numero de telephone',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    handicap = forms.CharField(label='handicap',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(label='Admin', required=False, initial=False)
    is_staff = forms.BooleanField(label='Staff', required=False, initial=False)
    is_terrain = forms.BooleanField(label='Terrain', required=False, initial=False)
    is_motoman = forms.BooleanField(label='Motoman', required=False, initial=False, widget=forms.CheckboxInput(attrs={'id': 'id_is_motoman'}))
    activite = forms.CharField(label="zone d'activite",required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    syndicat = forms.CharField(label="syndicat",required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    Numero = forms.CharField(label="numero de la moto",required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','last_name', 'profile','password1', 'password2','age', 'nationnalite','genre',
        'CNI','telephone','handicap','is_superuser','is_staff', 'is_terrain', 'is_motoman', 
        'syndicat', 'heure_Travaille']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='nom',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nom de famille', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    nationnalite = forms.CharField(label='nationnalite',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='numero de telephone',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    handicap = forms.CharField(label='handicap',required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.BooleanField(label='Admin', required=False, initial=False)
    is_staff = forms.BooleanField(label='Staff', required=False, initial=False)
    is_terrain = forms.BooleanField(label='Terrain', required=False, initial=False)
    is_motoman = forms.BooleanField(label='Motoman', required=False, initial=False, widget=forms.CheckboxInput(attrs={'id': 'id_is_motoman'}))
    syndicat = forms.CharField(label="syndicat",required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','last_name','profile','age', 'nationnalite','genre',
        'CNI','telephone','handicap','is_superuser','is_staff', 'is_terrain', 'is_motoman',
        'syndicat', 'heure_Travaille',]



class UpdateUserPasswordForm(forms.ModelForm):

    password = forms.CharField(label = 'passowrd', required=False,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['password',]
        
        def clean_password(self):
            password = self.cleaned_data.get('password')
            if password:
                return password
            else:
                raise forms.ValidationError("Ce champ est requis.")



class filtreUserForm(forms.Form):
    matricule = forms.CharField(label='matricule', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'matricule du personnel'}))
    start_date = forms.DateField(label='Date de début', required=False, widget=DatePickerInput( attrs={'placeholder': 'Sélectionnez une date'}))
    end_date = forms.DateField(label='Date de fin', required=False, widget=DatePickerInput( attrs={'placeholder': 'Sélectionnez une date'}))
    def filter(self):
        data = self.cleaned_data
        date_connexion = HistoriqueConnexion.objects.all()
        if data['matricule']:
            date_connexion = date_connexion.filter(utilisateur__matricule__icontains=data['matricule'])
        if data['start_date']:
            date_connexion = date_connexion.filter(date_connexion__gte=data['start_date'])
        if data['end_date']:
            date_connexion = date_connexion.filter(date_connexion__lte=data['end_date'])
        
        return date_connexion


class filtreTrajectForm(forms.Form):
    matricule = forms.CharField(label='matricule', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'matricule du personnel'}))
    start_date = forms.DateField(label='début de traject', required=False, widget=DatePickerInput( attrs={'placeholder': 'Debut de traject'}))
    end_date = forms.DateField(label='fin de traject', required=False, widget=DatePickerInput( attrs={'placeholder': 'Fin de traject'}))
    def filter(self):
        data = self.cleaned_data
        position = Position.objects.all()
        if data['matricule']:
            position = position.filter(utilisateur__matricule__icontains=data['matricule'])
        if data['start_date']:
            position = position.filter(date__gte=data['start_date'])
        if data['end_date']:
            position = position.filter(date__lte=data['end_date'])
        
        return position

class filtreAllForm(forms.Form):
    matricule = forms.CharField(label='matricule', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'matricule du personnel'}))
    def filter(self):

        data = self.cleaned_data
        user = User.objects.all()
        if data['matricule']:
            user = user.filter(matricule__icontains=data['matricule'])

        return user
    
class CreateMissionForm(forms.ModelForm):
    texte = forms.CharField(label='detaille de la mission', max_length=100, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'detail de la mission'}))
    point = forms.IntegerField(label='point', required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'point'}))
    debut = forms.DateField(input_formats=['%d/%m/%Y %H:%M'],  widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input','placeholder': 'date de debut',
            'data-target': '#datetimepicker1'
        }))
    fin =  forms.DateField(input_formats=['%d/%m/%Y %H:%M'],  widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input','placeholder': 'date de fin',
            'data-target': '#datetimepicker2'
        }))
    
    class Meta : 
        model = mission
        fields = ['receveur','texte','point','debut','fin','encours','terminer','reussie','echecs']

class CreateMessageForm(forms.ModelForm):
    texte = forms.CharField(label='texte', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'detail de la mission'}))
    class Meta : 
        model = message
        fields = ['receveur','texte']

class uploadImageForm(forms.ModelForm):

    class Meta : 
        model = User
        fields = ['profile','CNI', 'photo_moto','carte_grise', 'recu_vente', 'assurance']