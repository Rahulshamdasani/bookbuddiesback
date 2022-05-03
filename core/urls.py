
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from bookbuddies.views import UserViewSet, ExchangeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('exchanges', ExchangeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookbuddies.urls')),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
