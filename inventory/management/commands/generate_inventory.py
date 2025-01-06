from django.core.management.base import BaseCommand
from faker import Faker
from inventory.models import InventoryItem
from users.models import CustomUser
import random

class Command(BaseCommand):
    help = "Generate fake inventory data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        user = CustomUser.objects.first()  # Assuming at least one user exists
        if not user:
            self.stdout.write(self.style.ERROR("No users found! Please create a user first."))
            return

        units = ['kg', 'liters', 'pieces', 'packs']
        for _ in range(20):  # Generate 20 items
            item = InventoryItem(
                name=fake.random_element(elements=('Apple', 'Banana', 'Orange', 'Pear', 'Mango')).capitalize(),
                quantity=random.randint(1, 50),
                unit=random.choice(units),
                expiration_date=fake.date_between(start_date="today", end_date="+30d"),
                added_by=user
            )
            item.save()
            self.stdout.write(self.style.SUCCESS(f"Added {item}"))
