from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from user.models import HistoriqueConnexion, User
import logging

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    print(f"Utilisateur connecté : {user}")
    HistoriqueConnexion.objects.create(utilisateur=user)
