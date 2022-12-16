from website.models import Settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.cmd()

    def cmd(self):
        Settings.objects.create()
        print('Первоначальная настройка завершена!')