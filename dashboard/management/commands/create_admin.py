
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Creates a default admin user"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="vaishali").exists():
            User.objects.create_superuser(
                username="vaishali",
                email="vaishali.nagpure@gmail.com",
                password="NextGen@123"
            )
            self.stdout.write(self.style.SUCCESS("✅ Superuser 'vaishali' created"))
        else:
            self.stdout.write("ℹ️ Superuser already exists")
