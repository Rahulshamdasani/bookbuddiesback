from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Book, Exchange

# user model
from django.contrib.auth.models import User

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        
   

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ('title', 'desc', 'url')

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        # serialize fields such that user and books are forieign keys
        fields = ('id','user', 'bookSell', 'bookBuy1', 'bookBuy2', 'bookBuy3', 'isSettled')
        
