from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=255, blank=True)
    author = models.TextField(max_length=1000, blank=True)
    year = models.CharField(max_length=15 ,blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True)
    url = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Exchange(models.Model):
    # bookSell = models.ManyToManyField(Book, related_name='bookSell', blank=True)
    bookSell = models.ForeignKey(Book, related_name='bookSell', on_delete=models.CASCADE, blank=True, null=True)
    # bookBuy1 = models.ManyToManyField(Book, related_name='bookBuy1', blank=True)
    # bookBuy2 = models.ManyToManyField(Book, related_name='bookBuy2', blank=True)
    # bookBuy3 = models.ManyToManyField(Book, related_name='bookBuy3', blank=True)
    bookBuy1 = models.ForeignKey(Book, related_name='bookBuy1', on_delete=models.CASCADE, blank=True, null=True)
    bookBuy2 = models.ForeignKey(Book, related_name='bookBuy2', on_delete=models.CASCADE, blank=True, null=True)
    bookBuy3 = models.ForeignKey(Book, related_name='bookBuy3', on_delete=models.CASCADE, blank=True, null=True)
    # keep user as foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True)
    isSettled = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    
