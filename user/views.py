from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.exceptions import PythonDjangoException
from .models import User, Phone
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['GET'])
    def me(self):
        return ''

    @action(detail=False, methods=['POST'])
    def signup(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                phones = request.data.pop('phones')
                data_user = request.data
                user = User.objects.create(**data_user)
                for phone in phones:
                    p = Phone(number=phone['number'], area_code=phone['area_code'], country_code=phone['country_code'],
                              user=user)
                    p.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PythonDjangoException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
