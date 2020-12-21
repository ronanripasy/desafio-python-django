from django.contrib import admin
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenRefreshView)
from user import views

urlpatterns = [
    url('me/', views.me),
    url('signup/', views.signup),
    url('signin/', views.signin, name='login'),
    url('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('admin/', admin.site.urls),
]
