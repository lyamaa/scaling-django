from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from products.models import Category, Product
from random import randrange, randint

from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        faker = Faker()

        for _ in range(5000):
            price = randrange(10, 100)
            quantity = randrange(1, 5)
            cat = randint(4, 30)
            category = Category.objects.get(id=cat)
            product = Product.objects.create(
                name=faker.name(),
                category=category,
                description=faker.name(),
                price=price,
                discount=100,
                quantity=quantity,
                image="https://image.shutterstock.com/image-photo/4k-monitor-isolated-on-white-260nw-357968483.jpg")
            product.save()
