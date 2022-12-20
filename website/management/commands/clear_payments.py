from website.models import Payments
from datetime import datetime, timedelta
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.cmd()

    def cmd(self):
        time_now = datetime.now()
        time_day_back = time_now - timedelta(days=1)

        payments_data = Payments.objects.filter(complete=False, create_at__lt=time_day_back)
        for p in payments_data:
            p.delete()

        print('Очистка старых платежей - выполнена!')