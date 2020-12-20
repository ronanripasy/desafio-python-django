from django.test import TestCase
from user.serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.user = {
            "first_name": "",
            "last_name": "",
            "email": "hello@world.com",
            "password": "hunter2",
            "phones": [
                {
                    "number": 988887888,
                    "area_code": 81,
                    "country_code": "+55"
                }
            ]
        }

        self.user_missing_first_name = {
            "last_name": "",
            "email": "hello@world.com",
            "password": "hunter2",
            "phones": [
                {
                    "number": 988887888,
                    "area_code": 81,
                    "country_code": "+55"
                }
            ]
        }

    def test_success_serializer(self):
        serializer = UserSerializer(data=self.user)
        self.assertTrue(serializer.is_valid())

    def test_missing_fields_serializer(self):
        serializer = UserSerializer(data=self.user_missing_first_name)
        self.assertFalse(serializer.is_valid())
