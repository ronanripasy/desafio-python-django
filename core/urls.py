from django.contrib import admin
from django.conf.urls import include, url
from django.shortcuts import redirect
from django.urls.base import reverse
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from user import views


router = routers.DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    # url(r'^$', lambda request: redirect(reverse('api-root'))),
    url(r'^api/', include(router.urls), name='api-root'),
    url('api/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
