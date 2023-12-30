from rest_framework import serializers
from .models import  User, Rapport, Position, mission, message
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginSerializer(serializers.Serializer):
   username = serializers.CharField(max_length=255)
   password = serializers.CharField(max_length=128, write_only=True)

   class Meta:
    model = User
    fields = ['username','password']

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Ajoutez le champ pour confirmer le mot de passe

    class Meta:
        model = User
        fields = [
        'username','last_name','password', 'password2','age', 'nationnalite','genre',
        'telephone','handicap','is_terrain', 'is_motoman',
        'syndicat', 'heure_Travaille',
        ]
    
    def validate(self, data):
        # Assurez-vous que les mots de passe correspondent
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

class RapportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rapport
        fields = ['envoyeur', 'receveur', 'texte', 'note', 'heure']

    def validate(self, data):
        # Assurez-vous que l'envoyeur est présent dans les données
        envoyeur = data.get('envoyeur')
        if envoyeur is None:
            raise serializers.ValidationError("Veuillez mentionner l'envoyeur.")

        # Assurez-vous que le receveur est présent dans les données
        receveur = data.get('receveur')
        if receveur is None:
            raise serializers.ValidationError("Veuillez mentionner le receveur.")

        # Assurez-vous que le texte est présent dans les données
        texte = data.get('texte')
        if texte is None:
            raise serializers.ValidationError("Veuillez mentionner le texte.")

        # Assurez-vous que la note est présente dans les données
        note = data.get('note')
        if note is None:
            raise serializers.ValidationError("Veuillez mentionner la note.")

        # Assurez-vous que l'heure est présente dans les données

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'matricule']

class RapportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapport
        fields = ('id', 'envoyeur', 'receveur', 'texte', 'note', 'heure')

class RapportListSerializer(serializers.ModelSerializer):
    envoyeur_nom = serializers.ReadOnlyField(source='envoyeur.username')
    receveur_nom = serializers.ReadOnlyField(source='receveur.username')

    class Meta:
        model = Rapport
        fields = ('id', 'envoyeur', 'receveur', 'envoyeur_nom', 'receveur_nom', 'texte', 'note', 'heure')

class PositionSerailize(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('utilisateur', 'latitude', 'longitude', 'localite')

class missionSerializer(serializers.ModelSerializer):
    envoyeur_nom = serializers.ReadOnlyField(source='envoyeur.username')
    receveur_nom = serializers.ReadOnlyField(source='receveur.username')
    class Meta:
        model = mission
        fields = ('id', 'envoyeur', 'receveur', 'envoyeur_nom','receveur_nom','texte', 'point', 'debut', 'fin')

class messageSerializer(serializers.ModelSerializer):
    envoyeur_nom = serializers.ReadOnlyField(source='envoyeur.username')
    receveur_nom = serializers.ReadOnlyField(source='receveur.username')
    class Meta:
        model = message
        fields = ('id', 'envoyeur', 'receveur', 'envoyeur_nom','receveur_nom','texte','fin')

class UserSerializer_image(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'profile']
