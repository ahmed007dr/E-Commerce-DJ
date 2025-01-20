import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from products.models import Product , Brand, Review
import random

def seed_brand(n):
    fake = Faker()
    images = ['2 (1).jpg','2 (2).jpg','2 (3).jpg','2 (4).jpg','2 (5).jpg','2 (6).jpg','2 (7).jpg','2 (8).jpg','2 (9).jpg']
    for x in range(n):
        Brand.objects.create(
            name = fake.name(),
            image=f'brand/{random.choice(images)}',  # Use random.choice for cleaner code
        )
    print(f'number of Brand {n}')


def seed_product(n):
    fake = Faker()
    flag_type = ['New', 'Sale', 'Feature']
    images = ['1 (1).jpg', '1 (2).jpg', '1 (3).jpg', '1 (4).jpg', '1 (5).jpg', '1 (6).jpg', '1 (7).jpg', 
              '1 (8).jpg', '1 (9).jpg', '1 (10).jpg', '1 (11).jpg', '1 (12).jpg', '1 (13).jpg']
    
    brands = Brand.objects.all()
    
    for x in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=random.choice(flag_type),  # Use random.choice for cleaner code
            price=round(random.uniform(20.00, 99.22), 2),
            sku=random.randrange(10, 99),
            subtitle=fake.sentence(nb_words=5),  # Example for generating a short subtitle
            description=fake.text(max_nb_chars=1000),
            tags=fake.word(),
            brand=random.choice(brands),  # Choose a random brand from the list
            image=f'product/{random.choice(images)}',  # Choose a random image from the list
        )
    
    print(f'number of products {n}')

# def seed_review(n):
#     pass



# seed_brand(20)
# seed_product(1000)