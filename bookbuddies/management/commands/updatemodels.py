from django.core.management.base import BaseCommand
import pandas as pd
from bookbuddies.models import Book

class Command(BaseCommand):
    help = 'import books from csv file'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('bookfinal.csv')
        for index, row in df.iterrows():
            book = Book()
            book.isbn = row['ISBN']
            book.title = row['Book-Title']
            book.author = row['Book-Author']
            book.year = row['Year-Of-Publication']
            book.publisher = row['Publisher']
            book.url = row['Image-URL-L']
            book.save()
            if(index == 10000):
                break

        # delete all books
        # Book.objects.all().delete()