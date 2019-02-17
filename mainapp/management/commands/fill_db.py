from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
from basketapp.models import Basket
import random

import json, os


JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)



class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()
        
        
        products = load_from_json('products')
        
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        # django_user = ShopUser.objects.filter(username='django').first()
        # if not django_user:
        #     super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local',\
        #                                                'geekbrains', age=18)
        ShopUser.objects.all().delete()

        django = ShopUser.objects.create_superuser('django', 'django@geekshop.local', \
                                                   'geekbrains', age=18)
        user_1 = ShopUser.objects.create_user('user1', 'user1@geekshop.local', \
                                              'geekbrains', age=22)
        user_2 = ShopUser.objects.create_user('user2', 'user2@geekshop.local', \
                                              'geekbrains', age=32)
        user_3 = ShopUser.objects.create_user('user3', 'user3@geekshop.local', \
                                              'geekbrains', age=42)

        products = list(Product.objects.all())

        user_products = random.sample(products, 4)
        for product in user_products:
            Basket(user=django, product=product, quantity=int(random.random()*20) + 1).save()

        user_products = random.sample(products, 3)
        for product in user_products:
            Basket(user=user_1, product=product, quantity=int(random.random() * 15) + 1).save()

        user_products = random.sample(products, 5)
        for product in user_products:
            Basket(user=user_2, product=product, quantity=int(random.random() * 10) + 1).save()

        user_products = random.sample(products, 2)
        for product in user_products:
            Basket(user=user_3, product=product, quantity=int(random.random() * 25) + 1).save()



        

