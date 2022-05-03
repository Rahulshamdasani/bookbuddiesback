from django.urls import path, include
from rest_framework import routers
from .views import BooksViewSet, UserViewSet, ExchangeViewSet

router = routers.DefaultRouter()
router.register('', BooksViewSet)
router.register('exchange', ExchangeViewSet)



urlpatterns = [
    path('', include(router.urls)),
]


