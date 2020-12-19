from django.test import TestCase
from user.serializers import UserSerializer


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.usuario = {"phones": [{"number": 123, "area_code": 511, "country_code": "123"}], "password": "1233",
                        "first_name": "222",
                        "last_name": "333",
                        "email": "123333@gmail.com"}

    def test_serializer_user(self):
        serializer = UserSerializer(data=self.usuario)
        self.assertTrue(serializer.is_valid())
