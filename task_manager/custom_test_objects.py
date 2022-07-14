from django.test import TestCase


class CustomTestCase(TestCase):
    """
    setUp must have:
    self.user
    self.model
    self.object1, self.object2, self.object3
    self.object_list
    self.context_name
    self.redirect_url
    self.create_url
    self.data_create
    self.update_url
    self.data_update
    """
    def test_list_view(self):
        response = self.client.get(self.redirect_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.redirect_url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context[self.context_name], self.object_list)

    def test_create_view(self):
        self.client.force_login(self.user)
        new_data = self.data_create
        url = self.create_url
        response = self.client.post(url, new_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.model.objects.filter(**self.data_create).count(), 1)

    def test_update_view(self):
        self.client.force_login(self.user)
        new_data = self.data_update
        url = self.update_url
        response = self.client.post(url, new_data, follow=True)
        self.assertRedirects(response, self.redirect_url)
        self.assertEqual(self.model.objects.filter(**self.data_update).count(), 1)
