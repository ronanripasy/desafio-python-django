from django.contrib import admin
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from user import views

urlpatterns = [
    url('me/', views.me),
    url('signup/', views.signup),
    url('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
