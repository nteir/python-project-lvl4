from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UsersTestCase(TestCase):

    fixtures = ['users.json']

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user_list = [self.user1, self.user2]

    def test_users_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['users'], self.user_list)

    def test_user_create(self):
        new_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'tuser',
            'password1': 'qwerty',
            'password2': 'qwerty',
        }
        url = reverse('signup')
        response = self.client.post(url, new_data, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.filter(username='tuser').count(), 1)

    def test_user_update(self):
        user = self.user1
        self.client.force_login(user)
        url = reverse('update', kwargs={'pk': user.id})
        new_data = {
            'first_name': user.first_name,
            'last_name': 'Sidorov',
            'username': user.username,
            'password1': user.password,
            'password2': user.password,
        }
        response = self.client.post(url, new_data, follow=True)
        self.assertRedirects(response, reverse('users'))
        self.assertEquals(User.objects.filter(last_name='Sidorov').count(), 1)

    def test_user_delete(self):
        user = self.user1
        self.client.force_login(user)
        url = reverse('delete', kwargs={'pk': user.id})
        response = self.client.post(url, follow=True)
        self.assertEquals(User.objects.filter(id=self.user1.id).count(), 0)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user1.id)
        self.assertRedirects(response, reverse('users'))
