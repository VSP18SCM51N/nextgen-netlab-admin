from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Creates a default admin user if it doesn't exist"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "vaishali"
        email = "vaishali.nagpure@gmail.com"
        password = "Spectrum@123"  # ⚠️ Change this later!

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write("Superuser already exists")
