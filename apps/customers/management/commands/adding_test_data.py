import random

import pytz
from django.core.management.base import BaseCommand
from faker import Faker
from apps.customers.models import client, organization, department

faker_ru = Faker(['ru'])
faker = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('type', type=str, default='all')

    def handle(self, *args, **options):
        if options['type'] == 'clear':
            self.clear()
        else:
            # for i in range(0, 30000):
            #     self.gen_clients()
            for i in range(0, 200):
                self.gen_organization()
                dep = self.gen_department()
                a = random.randint(7, 30000)
                b = a - random.randint(1, 6)
                dep.clients.add(*client.Client.objects.all()[b:a])
                if faker.pybool():
                    self.gen_department(dep)

    @staticmethod
    def clear():
        client.Client.objects.all().delete()
        department.Department.objects.all().delete()
        organization.Organization.objects.all().delete()

    @staticmethod
    def gen_clients() -> None:
        gender = 'man' if faker.pybool() else 'woman'
        full_name = faker_ru.name_male().split() if gender == 'man' else faker_ru.name_female().split()
        client.Client.objects.create(
            phone=faker.bothify(text='############'),
            first_name=full_name[1],
            last_name=full_name[0],
            patronymic=full_name[2],
            is_active=faker.pybool(),
            client_type=client.Client.ClientTypesEnum.choices[random.randint(0, 3)][0],
            gender=gender,
            timezone=faker.timezone()
        )

    @staticmethod
    def gen_organization() -> organization.Organization:
        name = faker_ru.company()
        short_name = ''.join([n[0] for n in name.split()])
        print(name)
        obj = organization.Organization.objects.create(
            name=name,
            short_name=short_name,
            tin=faker.bothify(text='##########'),
            ppc=faker.bothify(text='#########'),
        )
        return obj

    @staticmethod
    def gen_department(parent=None) -> department.Department:
        print(parent)
        obj = department.Department.objects.create(
            name=faker_ru.company(), parent=parent)
        return obj
