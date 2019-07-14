from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'teste@teste.com'
        password = 'teste@t'

        user = get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'teste@LONDOMAPP.com'
        user = get_user_model().objects.create_user(email=email,password='sdsdsds')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email=None,password='sfsfdsfs')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(email='adadada',password='adada')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

            