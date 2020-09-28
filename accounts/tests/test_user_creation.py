from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserCreationTests(TestCase):

    def test_user_is_created(self):
        """ test a user can sign up with an email address and first name """

        email = "someone@test.com"
        first_name = "Bob"
        password = "testpass1234"
        user = get_user_model().objects.create_user(
            email=email,
            first_name=first_name,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertTrue(user.check_password(password))

    def test_noname_invalid(self):
        """ test a user attempting to sign up without an email raises an error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="someone@test.com",
                first_name="",
                password="testpass1234"
            )

    def test_blankname_invalid(self):
        """ tests a user cannot sign up with a blank name """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="someone@test.com",
                first_name=" ",
                password="testpass1234"
            )

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_removes_trailing_spaces(self):
        """ tests trailing spaces are removed from name and email fields"""

        user = get_user_model().objects.create_user(
            email="  someone@test.com  ",
            first_name="  Bob   ",
            password="testpass1234"
        )
        self.assertEqual(user.email, "someone@test.com")
        self.assertEqual(user.first_name, "Bob")
