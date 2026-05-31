from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='testuser@exemple.com',
            password='testpass1234',
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@exemple.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user_admin = User.objects.create_superuser(
            username='testsuperuser',
            email='testsuperuser@exemple.com',
            password='testpass1234',
        )

        self.assertEqual(user_admin.username, 'testsuperuser')
        self.assertEqual(user_admin.email, 'testsuperuser@exemple.com')
        self.assertTrue(user_admin.is_active)
        self.assertTrue(user_admin.is_staff)
        self.assertTrue(user_admin.is_superuser)


class SignUpPageTests(TestCase):

    def test_url_exist_at_correct_location_signupview(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
    
    def test_signup_form(self):
        response = self.client.post(
            reverse('signup'),
            {
                'username':'testuser',
                'email': 'testuser@exemple.com',
                'password1': 'testpass1234',
                'password2': 'testpass1234'
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@exemple.com')