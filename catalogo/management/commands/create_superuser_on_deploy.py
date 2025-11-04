import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Crea un superusuario si no existe, usando variables de entorno"

    def handle(self, *args, **options):
        # Lee las variables de entorno
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        # Revisa que existan
        if not username or not email or not password:
            self.stdout.write(
                self.style.ERROR(
                    'Faltan variables de entorno (DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD)'
                )
            )
            return

        # Crea el usuario solo si no existe
        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f"Creando superusuario: {username}"))
            User.objects.create_superuser(username, email, password)
        else:
            self.stdout.write(
                self.style.WARNING(f"Superusuario '{username}' ya existe.")
            )
