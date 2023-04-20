from django.core.management.base import BaseCommand , CommandError 
from django.contrib.auth import get_user_model

user_model = get_user_model() 


class Command(BaseCommand):

    def handle(self,*args,**kwargs):
        admin_user = user_model.objects.filter(username='admin').first()
        if not admin_user:
            admin_user = user_model.objects.create_user(username='admin',password='admin',is_staff=True,is_superuser=True) 
            print('Created Superuser')

