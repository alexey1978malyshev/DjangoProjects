from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Aspernatur est, eveniet labore nisi reprehenderit repudiandae sit unde vel velit voluptates! Dolorem eligendi" \
        " enim et explicabo ipsa molestiae, nihil reprehenderit temporibus veniam? A accusamus aliquam, aliquid beatae " \
        "doloribus ducimus eligendi eos illum magnam molestias nemo non numquam odio odit officia, pariatur perferendis" \
        " praesentium quas quasi reiciendis repudiandae saepe sed sunt suscipit tempore unde ut! Ad adipisci animi " \
        "aspernatur atque beatae consequuntur distinctio eligendi eveniet explicabo fugiat harum itaque, iusto " \
        "laboriosam, laborum laudantium modi neque nihil non optio pariatur porro quia quidem quo voluptas " \
        "voluptate! Alias aliquid architecto, corporis dolores eaque eligendi est et facere fugit id impedit " \
        "inventore magnam molestias natus necessitatibus officiis quae quasi reiciendis rem repellat repellendus " \
        "rerum saepe soluta totam veniam vitae voluptates, voluptatibus. Animi, aperiam autem consectetur consequatur " \
        "cum dolorum ea et eum eveniet ex facere, iusto labore molestiae nam necessitatibus nobis numquam rem, " \
        "sed ut voluptate."


class Command(BaseCommand):
    help = "Generate fake authors and posts."


    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')


    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}',
                            email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()
