from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import random
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.

class User(AbstractUser) :
    matricule = models.CharField(max_length = 50,default = False, blank=True)
    profile = models.ImageField(upload_to='img', default = False)
    age = models.IntegerField(default = False, null = True, blank=True)
    nationnalite = models.CharField(max_length = 200,default = False, blank=True)
    GENRE_CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )
    genre = models.CharField(max_length = 20,choices=GENRE_CHOICES ,default = False, blank=True)
    CNI = models.ImageField(upload_to='img', default = False)
    telephone = models.CharField(max_length = 200,default = False, blank=True)
    handicap = models.CharField(max_length = 200,default = False, blank=True)
    is_terrain = models.BooleanField(default = False, blank=True)
    is_motoman = models.BooleanField(default = False, blank=True)
    syndicat = models.CharField(max_length = 50,default = False, blank=True)
    HEURE_CHOICES = (
        ('jours', 'Jours'),
        ('nuit', 'Nuit'),
        ('jours_nuit', 'Jours et Nuit'),
    )
    heure_Travaille = models.CharField(max_length = 20,choices=HEURE_CHOICES ,default = False, blank=True)
    photo_moto = models.ImageField(upload_to='img', default = False)
    carte_grise = models.ImageField(upload_to='img', default = False)
    recu_vente = models.ImageField(upload_to='img', default = False)
    assurance = models.ImageField(upload_to='img', default = False)

    #ici is_terrain c'est le controlleur de terrain et is_motoman c'est le motoman
    # superuser est deja reger par django et controlleur de terrain est gerer ici comme staff
    def __str__(self):
        return f'{self.username}-{self.last_name}'    
    def get_user_status(self):
        if self.is_terrain:
            return "Contrôleur de terrain"
        elif self.is_motoman:
            return "Motoman"
        elif self.is_superuser:
            return "Administrateur"
        elif self.is_staff:
            return "Controlleur de burreau"

def generate_random_matricule():
    return ''.join([str(random.randint(0, 9)) for _ in range(8)])

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    # Générer un matricule aléatoire de 8 chiffres si le matricule est vide
    if not instance.matricule:
        instance.matricule = generate_random_matricule()

class Rapport(models.Model):
    envoyeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rapports_envoyes')
    receveur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rapports_recus')
    texte = models.TextField()
    NOTE_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    note = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        choices=NOTE_CHOICES
    )
    heure = models.DateTimeField(auto_now_add=True)

class HistoriqueConnexion(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_connexion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.utilisateur.username} s\'est connecté le {self.date_connexion}'


class Position(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(default = False)  # Champ pour stocker la latitude
    longitude = models.FloatField(default = False) 
    localite = models.CharField(max_length = 200,default = False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.utilisateur.username

class mission(models.Model):
    envoyeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='misssion_envoyeur')
    receveur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mission_recus')
    texte = models.TextField()
    point = models.IntegerField()
    debut = models.DateTimeField()
    fin = models.DateTimeField()
    encours = models.BooleanField(default=True)
    terminer = models.BooleanField(default=False)
    reussie = models.BooleanField(default=True)
    echecs = models. BooleanField(default=False)

    def save(self, *args, **kwargs):
    # Formater les champs debut et fin avant de sauvegarder
        self.debut_formatted = self.debut.strftime('%d/%m/%Y %H:%M')
        self.fin_formatted = self.fin.strftime('%d/%m/%Y %H:%M')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.envoyeur.username} -- {self.receveur.username}'
    
    def get_mission_status(self):
        if self.encours:
            return "encours"
        else:
            return "terminer"
            
    def get_mission_status2(self):
        
        if self.reussie:
            return "reussie"
        else:
            return "echecs"


class message(models.Model):
    envoyeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mesage_envoyeur')
    receveur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_recus')
    texte = models.TextField()
    heure = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.envoyeur.username} -- {self.receveur.username}'
    
