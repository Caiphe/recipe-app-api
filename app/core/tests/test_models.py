from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='marc@propdata.net', password="testpass"):
    """ create the sample user """
    return get_user_model().objects.create_user(email, password)

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

    def test_tag_str(self):
        """ Test the tag string representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test the ingredient string respresentation """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)