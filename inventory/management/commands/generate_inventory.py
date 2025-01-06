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

        grocery_data = [
            {"name": "Apple", "unit": "kg"},
            {"name": "Banana", "unit": "kg"},
            {"name": "Orange", "unit": "kg"},
            {"name": "Pear", "unit": "kg"},
            {"name": "Mango", "unit": "kg"},
            {"name": "Potato", "unit": "kg"},
            {"name": "Tomato", "unit": "kg"},
            {"name": "Carrot", "unit": "kg"},
            {"name": "Milk", "unit": "liters"},
            {"name": "Cheese", "unit": "kg"},
            {"name": "Butter", "unit": "kg"},
            {"name": "Bread", "unit": "packs"},
            {"name": "Eggs", "unit": "pieces"},
            {"name": "Chicken", "unit": "kg"},
            {"name": "Fish", "unit": "kg"},
            {"name": "Rice", "unit": "kg"},
            {"name": "Flour", "unit": "kg"},
            {"name": "Coffee", "unit": "kg"},
        ]

        added_items = set()

        item = InventoryItem(
            name="Salt",
            quantity=random.randint(1, 3),
            unit= "kg",
            expiration_date=fake.date_between(start_date="today", end_date="+30d"),
            added_by=user
        )
        item.save()

        item = InventoryItem(
            name="Sugar",
            quantity=random.randint(1, 3),
            unit="kg",
            expiration_date=fake.date_between(start_date="today", end_date="+30d"),
            added_by=user
        )
        item.save()

        for _ in range(20):  # Generate up to 20 unique items
            grocery = fake.random_element(elements=grocery_data)
            if grocery["name"] in added_items:
                continue
            added_items.add(grocery["name"])
            item = InventoryItem(
                name=grocery["name"].capitalize(),
                quantity=random.randint(1, 3),
                unit=grocery["unit"],
                expiration_date=fake.date_between(start_date="today", end_date="+30d"),
                added_by=user
            )
            item.save()
            self.stdout.write(self.style.SUCCESS(f"Added {item}"))

        self.stdout.write(self.style.SUCCESS(f"Total unique items added: {len(added_items)}"))