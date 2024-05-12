from django.core.management.base import BaseCommand
from shopapp.models import Customer, P
from faker import Faker


class Command(BaseCommand):
    help = "Generate fake authors and posts."


    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=fake.name(), email=fake.email())
            author.save()
            for j in range(1, count + 1):
                post = Post(title=fake.words(), content=fake.text(max_nb_chars=150), author=author)
                post.save()
