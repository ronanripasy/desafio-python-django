from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

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
            'last_login': data_user.last_login,
            'created_at': data_user.created_at,
            'phones': Phone.objects.values('number', 'area_code', 'country_code').filter(user_id=data_user.id),
        }
        return Response(data=response)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
    except APIException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def signup(request, **kwargs):
    try:
        serializer = UserSerializer(data=request.data)
        response = Response()
        if serializer.is_valid():
            phones = request.data.pop('phones')
            data_user = request.data
            user = User.objects.create_user(**data_user)
            for phone in phones:
                p = Phone(number=phone['number'], area_code=phone['area_code'], country_code=phone['country_code'],
                          user=user)
                p.save()

            # Creating access token for user
            token = RefreshToken.for_user(user)
            response.data = {
                'access_token': str(token.access_token),
                'refresh_token': str(token),
            }
            return Response(data=response.data, status=status.HTTP_201_CREATED)
        else:
            raise PythonDjangoException(message=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
    except APIException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        response = Response()
        if (email is None) or (password is None):
            raise PythonDjangoException(message='email and password required', status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if user is None:
            raise PythonDjangoException(message='Email not found', status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(password):
            raise PythonDjangoException(message='Wrong password', status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken.for_user(user)
        response.data = {
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        }

        return Response(data=response.data, status=status.HTTP_200_OK)
    except PythonDjangoException as e:
        return Response(e.detail, status=e.status_code)
    except APIException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
