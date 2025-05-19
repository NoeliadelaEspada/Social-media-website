from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.get_or_create(user=instance)
        #print("Se acaba de crear el usuario y su perfil enlazado") 

    
    
    """
    Este código no funciona.
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear el usuario y su perfil enlazado") 
    print('Señal registrada')
    """
    