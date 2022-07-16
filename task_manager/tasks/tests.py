from django.contrib.auth import get_user_model
from .models import Task, TaskLabelRelation
from task_manager.labels.models import Label
from django.urls import reverse
import task_manager.custom_test_objects as CO

User = get_user_model()


# Create your tests here.
class TasksTestCase(CO.CustomTestCase):
    """
    List, Create and Update tests are
    inherited from CO.CustomTestCase
    """
    fixtures = [
        'tasks/tasks.json',
        'tasks/task_label_rel.json',
        'statuses/statuses.json',
        'labels/labels.json',
        'users.json',
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.model = Task
        self.object1 = self.model.objects.get(pk=1)
        self.object2 = self.model.objects.get(pk=2)
        self.object3 = self.model.objects.get(pk=3)
        self.object_list = list(self.model.objects.all())
        self.context_name = 'tasks'
        self.redirect_url = reverse('task_list')
        self.create_url = reverse('task_create')
        self.data_create = {
            'name': 'ttask',
            'description': 'text',
            'status': 1,
            'author': self.user.id,
            'executor': 2,
            'labels': 1,
        }
        self.update_url = reverse('task_update', kwargs={'pk': self.object2.id})
        self.data_update = {
            'name': 'tname',
            'description': 'text',
            'status': 1,
            'executor': 2,
            'labels': 2,
        }
        # self.labels = Label.objects.all()
        # self.task_label_rel = TaskLabelRelation.objects.all()

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_card', kwargs={'pk': self.object1.id}))
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(reverse('task_card', kwargs={'pk': self.object1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['task'], self.object1)

    def test_task_delete(self):
        self.client.force_login(self.user)
        url = reverse('task_delete', kwargs={'pk': self.object2.id})
        response = self.client.post(url, follow=True)
        self.assertEqual(self.model.objects.filter(id=self.object2.id).count(), 1)
        self.assertRedirects(response, reverse('task_list'))
        url = reverse('task_delete', kwargs={'pk': self.object3.id})
        response = self.client.post(url, follow=True)
        self.assertEqual(self.model.objects.filter(id=self.object3.id).count(), 0)
        self.assertRedirects(response, reverse('task_list'))

    def test_status_filter(self):
        self.client.force_login(self.user)
        url = f"{reverse('task_list')}?status=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], [self.object1])

    def test_executor_filter(self):
        self.client.force_login(self.user)
        url = f"{reverse('task_list')}?executor=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], [self.object1, self.object3])

    def test_label_filter(self):
        # from .filter import TaskFilter
        # qs = Task.objects.all()
        # f = TaskFilter(data={'labels': 2}, queryset=qs)
        # result = f.qs
        # print(result)
        
        self.client.force_login(self.user)
        url = f"{reverse('task_list')}?labels=2"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], [self.object3])

    def test_get_user_tasks(self):
        self.client.force_login(self.user)
        url = f"{reverse('task_list')}?self_tasks=on"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks'], [self.object1, self.object3])
