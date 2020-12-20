from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from core.exceptions import PythonDjangoException
from .models import User, Phone
from .serializers import UserSerializer


@api_view(['GET'])
@authentication_classes((JWTAuthentication,))
@permission_classes((IsAuthenticated,))
def me(request, **kwargs):
    try:
        data_user = request.user
        response = {
            'first_name': data_user.first_name,
            'last_name': data_user.last_name,
            'email': data_user.email,
            'phones': Phone.objects.values('number', 'area_code', 'country_code').filter(user_id=data_user.id),
        }
        return Response(data=response)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)


@api_view(['POST'])
def signup(request, **kwargs):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            phones = request.data.pop('phones')
            data_user = request.data
            user = User.objects.create_user(**data_user)
            for phone in phones:
                p = Phone(number=phone['number'], area_code=phone['area_code'], country_code=phone['country_code'],
                          user=user)
                p.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise PythonDjangoException(message=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)

