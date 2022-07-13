from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task
from django.urls import reverse

User = get_user_model()


# Create your tests here.
class TasksTestCase(TestCase):

    fixtures = [
        'tasks/tasks.json',
        'statuses/statuses.json',
        'users.json',
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=3)
        self.task_list = [self.task1, self.task2, self.task3]

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], self.task_list)

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_card', kwargs={'pk': self.task1.id}))
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(reverse('task_card', kwargs={'pk': self.task1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['task'], self.task1)

    def test_task_create(self):
        self.client.force_login(self.user)
        new_data = {
            'name': 'ttask',
            'description': 'text',
            'status': 1,
            'author': self.user.id,
            'executor': 2,
        }
        url = reverse('task_create')
        response = self.client.post(url, new_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.filter(name='ttask').count(), 1)

    def test_task_update(self):
        self.client.force_login(self.user)
        url = reverse('task_update', kwargs={'pk': self.task2.id})
        new_data = {
            'name': 'tname',
            'description': 'text',
            'status': 1,
            'executor': 2,
        }
        response = self.client.post(url, new_data, follow=True)
        self.assertRedirects(response, reverse('task_list'))
        self.assertEqual(Task.objects.filter(name='tname').count(), 1)

    def test_task_delete(self):
        self.client.force_login(self.user)
        url = reverse('task_delete', kwargs={'pk': self.task2.id})
        response = self.client.post(url, follow=True)
        self.assertEqual(Task.objects.filter(id=self.task2.id).count(), 1)
        self.assertRedirects(response, reverse('task_list'))
        url = reverse('task_delete', kwargs={'pk': self.task3.id})
        response = self.client.post(url, follow=True)
        self.assertEqual(Task.objects.filter(id=self.task3.id).count(), 0)
        self.assertRedirects(response, reverse('task_list'))
