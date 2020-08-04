from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_successfull(self):
        """ Creating the new user with an email is successful """
        email = "marcdesign1@gmail.com"
        password = "Marchall004"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normlizer(self):
        """ Test the email for a new user is normalizzd """
        email = 'marcdesign1@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Marchall004')
        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """ Test creating user with no email raisees error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Marchall004')


    def test_creat_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'marcdesign1@gmail.com',
            'Marchall004'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

