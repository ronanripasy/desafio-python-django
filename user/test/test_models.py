from django.test import TestCase
from user.models import User, Phone


class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(first_name='Hello', last_name='World', email='hello@gmail.com',
                                        password='123')
        self.phone = Phone.objects.create(user_id=self.user.id, number=981566541, area_code=92, country_code='+55')

    def test_user_object(self):
        """Teste para validar se objeto de usuário é criado."""
        self.assertEqual(self.user.email, 'hello@gmail.com')

    def test_phone_object(self):
        """Teste para validar se objeto de phone é criado."""
        self.assertEqual(self.phone.number, 981566541)

