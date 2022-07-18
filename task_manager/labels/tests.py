from django.contrib.auth import get_user_model
from .models import Label
from django.urls import reverse
import task_manager.custom_test_objects as CO

User = get_user_model()


# Create your tests here.
class StatusesTestCase(CO.CustomTestCase):
    """
    List, Create and Update tests are
    inherited from CO.CustomTestCase
    """
    fixtures = ['labels/labels.json', 'users.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.model = Label
        self.object1 = self.model.objects.get(pk=1)
        self.object2 = self.model.objects.get(pk=2)
        self.object3 = self.model.objects.get(pk=3)
        self.object_list = [self.object1, self.object2, self.object3]
        self.context_name = 'objects'
        self.redirect_url = reverse('labels:obj_list')
        self.create_url = reverse('labels:obj_create')
        self.data_create = {
            'name': 'tlabel',
        }
        self.update_url = reverse('labels:obj_update', kwargs={'pk': self.object2.id})
        self.data_update = {
            'name': 'tname',
        }

    def test_label_delete(self):
        self.client.force_login(self.user)
        url = reverse('labels:obj_delete', kwargs={'pk': self.object2.id})
        response = self.client.post(url, follow=True)
        self.assertEqual(self.model.objects.filter(id=self.object2.id).count(), 0)
        self.assertRedirects(response, self.redirect_url)
