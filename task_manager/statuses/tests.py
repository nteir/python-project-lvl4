from django.test import TestCase
from django.contrib.auth.models import User
from .models import TaskStatus
from django.urls import reverse


# Create your tests here.
class StatusesTestCase(TestCase):

    fixtures = ['statuses/statuses.json', 'users.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.status1 = TaskStatus.objects.get(pk=1)
        self.status2 = TaskStatus.objects.get(pk=2)
        self.status_list = [self.status1, self.status2]

    def test_status_list_view(self):
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['statuses'], self.status_list)

    def test_status_create(self):
        self.client.force_login(self.user)
        new_data = {
            'name': 'tstatus',
        }
        url = reverse('status_create')
        response = self.client.post(url, new_data, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(TaskStatus.objects.filter(name='tstatus').count(), 1)

    def test_user_update(self):
        self.client.force_login(self.user)
        url = reverse('status_update', kwargs={'pk': self.status2.id})
        new_data = {
            'name': 'tname',
        }
        response = self.client.post(url, new_data, follow=True)
        self.assertRedirects(response, reverse('status_list'))
        self.assertEquals(TaskStatus.objects.filter(name='tname').count(), 1)

    def test_status_delete(self):
        self.client.force_login(self.user)
        url = reverse('status_delete', kwargs={'pk': self.status2.id})
        response = self.client.post(url, follow=True)
        self.assertEquals(TaskStatus.objects.filter(id=self.status2.id).count(), 0)
        self.assertRedirects(response, reverse('status_list'))
