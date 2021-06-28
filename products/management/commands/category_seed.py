from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from products.models import Category

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(30):
            cat = Category.objects.create(
                name=faker.name(),
                description=faker.name()
            )

            cat.save()
