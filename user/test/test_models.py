from django.test import TestCase
from django.db.utils import IntegrityError
from user.models import User


class UserModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(first_name='Hello', last_name='World', email='hello@gmail.com',
                                        password='123')

    def test_user_object(self):
        """Teste para validar se objeto de usuário é criado."""
        self.assertEqual(self.user.email, 'hello@gmail.com')

    def test_user_same_email(self):
        """Teste para validar se usuários possuem mesmo email ao cadastrar."""
        user2 = User.objects.create(first_name='Hello 2', last_name='World 2', email='hello@gmail.com',
                                    password='123123')
        # self.assertEqual(self.user.email, 'hello@gmail.com')
        with self.assertRaisesMessage(IntegrityError, 'django.db.utils.IntegrityError: UNIQUE constraint failed: user_user.email'):
            int('a')
        self.assertRaises(IntegrityError, 'django.db.utils.IntegrityError: UNIQUE constraint failed: user_user.email')
