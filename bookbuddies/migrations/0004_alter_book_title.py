# Generated by Django 4.0.3 on 2022-03-07 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookbuddies', '0003_remove_book_desc_book_author_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
