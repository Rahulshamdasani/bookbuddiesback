from django.shortcuts import render
from .models import Book, Exchange
from .serializers import BooksSerializer, UserSerializer, ExchangeSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response


# Import user model
from django.contrib.auth.models import User

# user viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def removeUser(self, request):
        # print("Here for pk", pk)
        user_name = request.data['username']
        print("Passed username", user_name)
        
        # filter user for this username
        user = User.objects.filter(username=user_name)
        print("Here for user", user)
        if(not user):
            return Response({'status': 'User not found!, passed '+user_name}, status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'status': 'User deleted successfully!'}, status.HTTP_200_OK)
        
    @action(detail=False, methods=['post'])
    def updateUser(self, request):
        # print("Here for pk", pk)
        user_name = request.data['username']
        print("Passed username", user_name)
        
        # filter user for this username
        user = User.objects.get(username=user_name)
        
        if(not user):
            return Response({'status': 'User not found!, passed '+user_name}, status.HTTP_404_NOT_FOUND)
        #  check if request.data has password
        if('email' in request.data):
            user.email = request.data['email']
        if('first_name' in request.data):
            user.first_name = request.data['first_name']
        if ('last_name' in request.data):
            user.last_name = request.data['last_name']
        if ('password' in request.data):
            user.set_password(request.data['password'])
        user.save()
        return Response({'status': 'User updated successfully!'}, status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def getUser(self, request):
        # print("Here for pk", pk)
        print("*****"*100,request.data)
        user_name = request.data['username']
        print("Passed username", user_name)
        
        # filter user for this username
        user = User.objects.get(username=user_name)
        print("Here for user", user)
        if(not user):
            return Response({'status': 'User not found!, passed '+user_name}, status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
    
   

# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer

    @action(detail=False, methods=['post'])
    def addExchange(self, request):
        print("Here for exchange"*100)
        username_ = request.data['username']
        print("Passed username", username_)
        userObj = User.objects.get(username=username_)
        print("got user")
        if(not userObj):
            return Response({'status': 'User not found!, passed '+username_}, status.HTTP_404_NOT_FOUND)
        
        # check if request.data has bookSell
        if('bookSell' not in request.data):
            return Response({'status': 'No bookSell passed!'}, status.HTTP_400_BAD_REQUEST)
        bookSell_ = request.data['bookSell']
        print("Passed bookSell", bookSell_)
        # get the object for book
        bookSellObj = Book.objects.filter(title=bookSell_)[0]
        if(not bookSellObj):
            return Response({'status': 'Book not found!, passed '+bookSell_}, status.HTTP_404_NOT_FOUND)
        else:
            print("Here for bookSellOBJ", bookSellObj)
        # check if request.data has bookBuy1
        bookBuy1_ = request.data['bookBuy1']
        print("Passed bookBuy1", bookBuy1_)
        bookBuy1Obj = Book.objects.filter(title=bookBuy1_)[0]
        

        # check if request.data has bookBuy2
        bookBuy2_ = request.data['bookBuy2']
        print("Passed bookBuy2", bookBuy2_)
        bookBuy2Obj = Book.objects.filter(title=bookBuy2_)[0]

        # check if request.data has bookBuy3
        bookBuy3_ = request.data['bookBuy3']
        print("Passed bookBuy3", bookBuy3_)
        bookBuy3Obj = Book.objects.filter(title=bookBuy3_)[0]

        # Create username
        usernameField = username_+"_"+bookSell_
        print("Here for username", usernameField)
        # # Create exchange
        # obj = {user:user, username:username,bookSell:bookSell, bookBuy1:bookBuy1, bookBuy2:bookBuy2, bookBuy3:bookBuy3}
        # print("Here for obj", obj)
        exchange = Exchange.objects.create(username=usernameField, bookSell=bookSellObj, bookBuy1=bookBuy1Obj, bookBuy2=bookBuy2Obj, bookBuy3=bookBuy3Obj, user=userObj)
        # print("Here for exchange", exchange)
        # exchange.bookSell.add(bookSellObj)
        # print("Booksell added")
        # exchange.bookBuy1.add(bookBuy1Obj)
        # exchange.bookBuy2.add(bookBuy2Obj)
        # exchange.bookBuy3.add(bookBuy3Obj)
        # print("Books added")
        # exchange.user.add(userObj)

        # print("Here for exchange", exchange)
        exchange.save()
        return Response({'status': 'Exchange created successfully!'}, status.HTTP_200_OK)

    # Define another function to get all exchanges
    @action(detail=False, methods=['get'])
    def getAllExchanges(self, request):
        print("Here for getallexchange"*100)
        exchanges = Exchange.objects.all()
        print("Here for exchanges", exchanges)
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # getuser exchanges
    @action(detail=False, methods=['post'])
    def getUserExchanges(self, request):
        print("Here for getuserexchange"*100)
        username_ = request.data['username']
        print("Passed username", username_)
        userObj = User.objects.get(username=username_)
        exchanges = Exchange.objects.filter(user=userObj)
        print("Here for exchanges", exchanges)
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    # Define another function to all unsettled exchanges
    @action(detail=False, methods=['get'])
    def getAllUnsettledExchanges(self, request):
        print("Here for getall unsettled exchange"*100)
        exchanges = Exchange.objects.all()
        exchanges = exchanges.filter(isSettled=False)
        print("Here for exchanges", exchanges)
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    # Define another function to all settled exchanges
    @action(detail=False, methods=['get'])
    def getAllSettledExchanges(self, request):
        print("Here for getall settled exchange"*100)
        exchanges = Exchange.objects.all()
        exchanges = exchanges.filter(isSettled=True)
        print("Here for exchanges", exchanges)
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    # Define another function settle exchange
    @action(detail=False, methods=['post'])
    def settleExchange(self, request):
        print("Here for settle exchange"*100)
        exchangeId = request.data['exchangeId']
        print("Passed exchangeId", exchangeId)
        exchangeObj = Exchange.objects.get(id=exchangeId)
        print("Here for exchange", exchangeObj)
        exchangeObj.isSettled = True
        exchangeObj.save()
        return Response({'status': 'Exchange settled successfully!'}, status.HTTP_200_OK)
    