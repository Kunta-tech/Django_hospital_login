# myapp/management/commands/create_missing_profiles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from members.models import Profile

class Command(BaseCommand):
    help = 'Create missing profiles for existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            Profile.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created missing profiles'))
